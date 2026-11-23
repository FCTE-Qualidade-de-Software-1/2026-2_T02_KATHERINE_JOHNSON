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


class DeclaracaoHeitorTest(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-22-v2.json').read_text())

    def test_duas_declaracoes_totais_sem_duplicar_a_53(self):
        result = fechar.calcular(self.snapshot)
        heitor = result['individuais']['Heitor']
        self.assertEqual(heitor['estimativa_min'], 630)
        self.assertEqual(heitor['real_min'], 660)
        self.assertTrue(heitor['completo'])
        # 710 (Hugo) + 660 (Heitor) + 60 (Daniel) + 60 (Pedro Druck); as 180 min da #53 são substituídas.
        self.assertEqual(result['total_conhecido_min'], 1490)
        self.assertFalse(result['pci_completo'])

    def test_historico_da_primeira_consulta_nao_muda(self):
        original = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-22.json').read_text())
        self.assertEqual([d['integrante'] for d in original['declaracoes']], ['Hugo'])
        self.assertEqual(fechar.calcular(original)['total_conhecido_min'], 1010)

    def test_rejeita_total_abaixo_das_horas_ja_registradas(self):
        self.snapshot['declaracoes'][-1]['acrescimo_min'] = -500
        with self.assertRaisesRegex(ValueError, 'incompatível'):
            fechar.calcular(self.snapshot)

    def test_relatorio_cita_as_duas_declaracoes(self):
        result = fechar.calcular(self.snapshot)
        texto = fechar.relatorio(self.snapshot, result, 'gestao/dados/fechamento-e2-2026-11-22-v2.json')
        self.assertIn('Hugo e Heitor declararam total', texto)
        self.assertIn('estimativa calculada', texto.replace('Estimativa de Heitor, calculada', 'estimativa calculada'))
        self.assertIn('Hugo e Heitor', fechar.contribuicao(result))


class DeclaracoesV4Test(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-23-v4.json').read_text())

    def test_total_de_15h30_substitui_a_declaracao_de_11h(self):
        result = fechar.calcular(self.snapshot)
        heitor = result['individuais']['Heitor']
        self.assertEqual(heitor['estimativa_min'], 630)
        self.assertEqual(heitor['real_min'], 930)
        self.assertTrue(heitor['completo'])
        # 710 (Hugo) + 930 (Heitor) + 860 (Philipe) + 750 (Pedro Henrique) + 60 (Daniel) + 60 (Pedro Druck).
        self.assertEqual(result['total_conhecido_min'], 3370)
        self.assertFalse(result['pci_completo'])

    def test_philipe_e_pedro_henrique_declararam_o_total(self):
        ind = fechar.calcular(self.snapshot)['individuais']
        self.assertEqual(ind['Philipe']['estimativa_min'], 980)
        self.assertEqual(ind['Philipe']['real_min'], 860)
        self.assertEqual(ind['Pedro Henrique']['estimativa_min'], 330)
        self.assertEqual(ind['Pedro Henrique']['real_min'], 750)
        self.assertTrue(ind['Philipe']['completo'] and ind['Pedro Henrique']['completo'])
        self.assertFalse(ind['Daniel']['completo'] or ind['Pedro Druck']['completo'])

    def test_versao_anterior_permanece_como_historico(self):
        anterior = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-22-v2.json').read_text())
        self.assertEqual(fechar.calcular(anterior)['individuais']['Heitor']['real_min'], 660)

    def test_contribuicao_soma_100_do_informado(self):
        result = fechar.calcular(self.snapshot)
        self.assertIn('27,60', fechar.contribuicao(result).replace('\\%', ''))


if __name__ == '__main__':
    unittest.main()
