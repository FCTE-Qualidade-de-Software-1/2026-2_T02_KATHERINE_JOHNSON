"""Confere se a página de medições da GitPage acompanha os CSV reais e aponta para as linhas certas."""

import csv
import importlib.util
import re
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('gerar_medicoes', Path(__file__).parents[1] / 'scripts/gerar_medicoes.py')
gerar = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gerar)

LINK = re.compile(r'dados/brutos/([\w-]+)\.csv\?plain=1#L(\d+)(?:-L(\d+))?')


class PaginaMedicoesTest(unittest.TestCase):
    def test_pagina_confere_com_os_csv(self):
        self.assertEqual(gerar.SAIDA.read_text(encoding='utf-8'), gerar.gerar(),
                         'executar python3 dados/scripts/gerar_medicoes.py e versionar a página')

    def test_links_apontam_para_linhas_de_dados(self):
        texto = gerar.SAIDA.read_text(encoding='utf-8')
        links = LINK.findall(texto)
        self.assertTrue(links)
        for nome, inicio, fim in links:
            with (gerar.ROOT / f'dados/brutos/{nome}.csv').open(encoding='utf-8', newline='') as f:
                total = sum(1 for _ in csv.reader(f)) + 1
            for linha in (int(inicio), int(fim or inicio)):
                self.assertGreaterEqual(linha, 2, f'{nome}.csv: link para o cabeçalho')
                self.assertLess(linha, total, f'{nome}.csv: linha {linha} não existe')

    def test_cada_resultado_calculado_aparece_na_pagina(self):
        texto = gerar.SAIDA.read_text(encoding='utf-8')
        for r in gerar.ler('resultados-metricas', 'consolidados'):
            if r['estado'] == 'calculado':
                self.assertIn(f'### {r["metrica"]} —', texto)
                self.assertIn(gerar.valor_resultado(r), texto)


if __name__ == '__main__':
    unittest.main()
