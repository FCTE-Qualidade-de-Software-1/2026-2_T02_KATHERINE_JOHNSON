"""Testes de recusa e recuperação; todos os comandos de rede são simulados."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

SPEC = importlib.util.spec_from_file_location('rede_p7', Path(__file__).parents[1] / 'scripts/p7/rede.py')
rede = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(rede)


class RedeP7Test(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.privado = Path(self.temp.name)
        self.estado = {'uplink': 'interface-sintetica', 'ap': True, 'conexao': True}
        (self.privado / 'estado.json').write_text(json.dumps(self.estado))

    def executar(self, cmd):
        with mock.patch.object(rede, 'PRIV', self.privado), \
             mock.patch('sys.argv', ['rede.py', 'degradar']), \
             mock.patch.object(rede.os, 'geteuid', return_value=0), \
             mock.patch.object(rede.os, 'chown'), \
             mock.patch.object(rede, 'comando', side_effect=cmd):
            rede.main()

    def test_nao_sobrescreve_fila_personalizada(self):
        chamadas = []
        def comando(*args, **kwargs):
            chamadas.append(args)
            return json.dumps([{'kind': 'htb'}])
        with self.assertRaises(SystemExit):
            self.executar(comando)
        self.assertEqual(len(chamadas), 1)
        self.assertEqual(chamadas[0][:3], ('tc', '-j', 'qdisc'))

    def test_falha_parcial_remove_somente_ifb_criada(self):
        chamadas = []
        def comando(*args, **kwargs):
            chamadas.append(args)
            if args[:3] == ('tc', '-j', 'qdisc'):
                return json.dumps([{'kind': 'noqueue'}])
            if args[:3] == ('tc', 'qdisc', 'replace'):
                raise RuntimeError('falha sintética')
            return ''
        with self.assertRaises(RuntimeError):
            self.executar(comando)
        self.assertIn(('ip', 'link', 'del', rede.IFB), chamadas)
        estado = json.loads((self.privado / 'estado.json').read_text())
        self.assertFalse(estado.get('ifb'))
        self.assertFalse(estado.get('egress', False))
        self.assertTrue(estado['ap'])

    def test_falha_ao_restaurar_nao_declara_rede_restaurada(self):
        estado = {'uplink': 'interface-sintetica', 'egress': True}
        with mock.patch.object(rede, 'comando', side_effect=RuntimeError('falha sintética')):
            with self.assertRaises(RuntimeError):
                rede.normal(estado)
        self.assertTrue(estado['egress'])


if __name__ == '__main__':
    unittest.main()
