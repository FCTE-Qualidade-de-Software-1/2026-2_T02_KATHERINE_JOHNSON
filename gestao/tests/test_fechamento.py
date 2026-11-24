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
        # 865 (Hugo) + 930 (Heitor) + 860 (Philipe) + 750 (Pedro Henrique) + 60 (Daniel) + 60 (Pedro Druck).
        self.assertEqual(result['total_conhecido_min'], 3525)
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
        self.assertIn('26,38', fechar.contribuicao(result).replace('\\%', ''))



class DeclaracaoAtualizadaHugoTest(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-23-v3.json').read_text())

    def test_nova_declaracao_substitui_a_anterior(self):
        result = fechar.calcular(self.snapshot)
        hugo = result['individuais']['Hugo']
        self.assertEqual(hugo['estimativa_min'], 650)
        self.assertEqual(hugo['real_min'], 865)
        self.assertTrue(hugo['completo'])
        # 865 (Hugo) + 660 (Heitor) + 60 (Daniel) + 60 (Pedro Druck); a declaração de 22/11 não é somada.
        self.assertEqual(result['total_conhecido_min'], 1645)

    def test_fonte_v2_permanece_historica(self):
        v2 = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-22-v2.json').read_text())
        self.assertEqual(fechar.calcular(v2)['individuais']['Hugo']['real_min'], 710)

class DeclaracoesV5Test(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-23-v5.json').read_text())

    def test_daniel_declara_o_total_e_a_estimativa_base_nao_muda(self):
        ind = fechar.calcular(self.snapshot)['individuais']
        self.assertEqual(ind['Daniel']['estimativa_min'], 570)
        self.assertEqual(ind['Daniel']['real_min'], 560)
        self.assertTrue(ind['Daniel']['completo'])
        self.assertFalse(ind['Pedro Druck']['completo'])

    def test_total_conhecido_com_cinco_declaracoes(self):
        result = fechar.calcular(self.snapshot)
        # 865 (Hugo) + 930 (Heitor) + 860 (Philipe) + 750 (Pedro Henrique) + 560 (Daniel) + 60 (Pedro Druck).
        self.assertEqual(result['total_conhecido_min'], 4025)
        self.assertFalse(result['pci_completo'])
        self.assertIn('13,91', fechar.contribuicao(result).replace('\\%', ''))

    def test_v4_permanece_como_historico(self):
        v4 = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-23-v4.json').read_text())
        self.assertEqual(fechar.calcular(v4)['total_conhecido_min'], 3525)


class DeclaracoesV6Test(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-23-v6.json').read_text())

    def test_pedro_druck_declara_13h_sem_somar_a_55_de_novo(self):
        druck = fechar.calcular(self.snapshot)['individuais']['Pedro Druck']
        self.assertEqual(druck['estimativa_min'], 860)
        self.assertEqual(druck['real_min'], 780)
        self.assertTrue(druck['completo'])

    def test_seis_declaracoes_completam_a_contribuicao(self):
        result = fechar.calcular(self.snapshot)
        # 865 (Hugo) + 930 (Heitor) + 860 (Philipe) + 750 (Pedro Henrique) + 560 (Daniel) + 780 (Pedro Druck).
        self.assertEqual(result['total_conhecido_min'], 4745)
        self.assertTrue(result['pci_completo'])
        tabela = fechar.contribuicao(result)
        self.assertIn('16,44', tabela.replace('\\%', ''))
        self.assertNotIn('parcial', tabela)

    def test_v5_permanece_como_historico(self):
        v5 = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-23-v5.json').read_text())
        self.assertEqual(fechar.calcular(v5)['total_conhecido_min'], 4025)



class DeclaracoesV7Test(unittest.TestCase):
    def setUp(self):
        self.snapshot = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-23-v7.json').read_text())

    def test_segunda_leitura_da_47_soma_5h(self):
        result = fechar.calcular(self.snapshot)
        ind = result['individuais']
        self.assertEqual(ind['Heitor']['real_min'], 1110)
        self.assertEqual(ind['Hugo']['real_min'], 925)
        self.assertEqual(ind['Philipe']['real_min'], 920)
        # 4745 da v6 + 180 (Heitor) + 60 (Hugo) + 60 (Philipe).
        self.assertEqual(result['total_conhecido_min'], 5045)
        self.assertTrue(result['pci_completo'])

    def test_v6_permanece_como_historico(self):
        v6 = json.loads((ROOT/'gestao/dados/fechamento-e2-2026-11-23-v6.json').read_text())
        self.assertEqual(fechar.calcular(v6)['total_conhecido_min'], 4745)


if __name__ == '__main__':
    unittest.main()
