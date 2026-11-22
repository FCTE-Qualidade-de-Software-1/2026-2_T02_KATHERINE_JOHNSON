"""Cálculos do fechamento: lacunas de esforço e declaração total sem duplicidade."""
import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('fechar', ROOT/'gestao/scripts/fechar_e2.py')
fechar = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fechar)


class FechamentoTest(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-22.json').read_text())

    def test_declaracao_total_e_lacunas(self):
        result = fechar.calcular(self.snapshot)
        self.assertEqual(result['individuais']['Hugo']['estimativa_min'], 650)
        self.assertEqual(result['individuais']['Hugo']['real_min'], 710)
        self.assertEqual(result['total_conhecido_min'], 1010)
        self.assertIsNone(result['individuais']['Philipe']['real_min'])
        self.assertFalse(result['pci_completo'])
        self.assertEqual(result['tve']['real_h'], 5)
        self.assertEqual(result['icm']['percentual'], 50)

    def test_total_individual_nao_duplica_horas_de_issue(self):
        snapshot = copy.deepcopy(self.snapshot)
        issue = next(i for i in snapshot['issues'] if i['numero']==46)
        issue.update(responsaveis=['Hugo'], real_h=1)
        # A referência passa a 11 h + 16/3 h; a declaração continua sendo total.
        result = fechar.calcular(snapshot)
        self.assertEqual(result['individuais']['Hugo']['real_min'], 1040)
        self.assertEqual(result['total_conhecido_min'], 1340)

    def test_rejeita_declaracao_duplicada(self):
        self.snapshot['declaracoes'] *= 2
        with self.assertRaisesRegex(ValueError,'duplicada'):
            fechar.calcular(self.snapshot)

    def test_bots_nao_substituem_revisao_humana(self):
        result = fechar.calcular(self.snapshot)
        self.assertIn(61,result['retrabalho']['sem_revisao'])
        self.assertIn(67,result['retrabalho']['avaliados'])


if __name__ == '__main__':
    unittest.main()
