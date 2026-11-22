"""Proteções dos instrumentos: dados sintéticos e nenhum acesso a aparelho real."""
import contextlib
import io
import json
from pathlib import Path
import runpy
import shutil
import sys
import tempfile
import types
import unittest
from unittest import mock


class PrivacidadeInstrumentoTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        origem = Path(__file__).parents[1] / 'scripts'
        for pasta, nomes in [('s02', ['app_s02.py', 'campos.py']), ('p6', ['app.py'])]:
            destino = root / 'dados/scripts' / pasta
            destino.mkdir(parents=True)
            for nome in nomes:
                shutil.copyfile(origem / pasta / nome, destino / nome)
        self.script = root / 'dados/scripts/s02/app_s02.py'
        self.root = root
        self.pil = types.ModuleType('PIL')
        self.pil.Image = mock.Mock()
        self.pil.ImageDraw = mock.Mock()

    def test_erro_com_dado_pessoal_fica_so_no_privado(self):
        dado = 'IDENTIFICADOR_PESSOAL_SINTETICO_NAO_PUBLICAR'
        saida = io.StringIO()
        with mock.patch.object(sys, 'argv', [str(self.script), 'volume', '1']), \
             mock.patch.object(sys, 'path', [str(self.script.parent), *sys.path]), \
             mock.patch('subprocess.run', side_effect=RuntimeError(dado)), \
             mock.patch.dict(sys.modules, {'PIL': self.pil}), \
             contextlib.redirect_stdout(saida):
            runpy.run_path(str(self.script), run_name='__main__')
        publico = json.loads(saida.getvalue())
        self.assertEqual(publico['motivo'], 'RuntimeError')
        self.assertNotIn(dado, saida.getvalue())
        arquivos = list((self.root / 'dados/privado/S02').glob('erro-*.json'))
        self.assertEqual(len(arquivos), 1)
        self.assertEqual(json.loads(arquivos[0].read_text())['mensagem'], dado)
        self.assertEqual(arquivos[0].stat().st_mode & 0o777, 0o600)

    def test_gravacao_existente_nao_e_sobrescrita(self):
        with mock.patch.object(sys, 'path', [str(self.script.parent), *sys.path]), \
             mock.patch.dict(sys.modules, {'PIL': self.pil}):
            ns = runpy.run_path(str(self.script))
        privado = Path(ns['PRIV'])
        existente = privado / 'repeticao.mp4'
        existente.write_bytes(b'gravacao sintetica preservada')
        with mock.patch('subprocess.Popen') as iniciar:
            with self.assertRaises(FileExistsError):
                ns['gravar']('repeticao')
            iniciar.assert_not_called()
        self.assertEqual(existente.read_bytes(), b'gravacao sintetica preservada')


if __name__ == '__main__':
    unittest.main()
