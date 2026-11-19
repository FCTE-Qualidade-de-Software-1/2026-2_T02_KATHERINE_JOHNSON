"""Cenários sintéticos, criados somente em diretórios temporários; nunca são medições."""

import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('calcular', Path(__file__).parents[1] / 'scripts/calcular.py')
calc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(calc)


class ColetaTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'dados/brutos').mkdir(parents=True)
        evidence = self.root / 'evidencias/fase4/fixture-sintetica.txt'
        evidence.parent.mkdir(parents=True)
        evidence.write_text('DADO SINTÉTICO: não comprova coleta.')
        self.tables = {k: [] for k in calc.SCHEMAS}

    def row(self, name, **kwargs):
        row = {k: '' for k in calc.SCHEMAS[name].split(',')}
        defaults = dict(sessao='S02', bloco='B01', contexto='CT01', canal='portal', veiculo='V1',
                        infracao='V1-I1', rede='wifi', repeticao='1', aquecimento='nao', elegivel='sim',
                        resultado='concluida', metrica='M2.1.1', procedimento='P7', aplicavel='sim',
                        presente='sim', classificacao='paritario', tela='lista',
                        data_hora='2026-11-19T10:00:00-03:00', portal_data_hora='2026-11-19T10:00:00-03:00',
                        aplicativo_data_hora='2026-11-19T10:10:00-03:00',
                        evidencia='evidencias/fase4/fixture-sintetica.txt', revisor='Conferente sintético')
        row.update({k: v for k, v in defaults.items() if k in row})
        row.update({k: str(v) for k, v in kwargs.items()})
        self.tables[name].append(row)
        return row

    def ambiente(self, contexto='CT01', rede='wifi', sessao='S02'):
        row = {k: 'fixture' for k in calc.SCHEMAS['ambientes'].split(',')}
        row.update({k: '1' for k in calc.NUMEROS if k in row})
        row.update(contexto=contexto, canal=calc.CONTEXTOS[contexto], sessao=sessao, rede=rede,
                   data_hora='2026-11-19T10:00:00-03:00', evidencia='evidencias/fase4/fixture-sintetica.txt')
        self.tables['ambientes'].append(row)

    def run_calc(self):
        for name, rows in self.tables.items():
            with (self.root / 'dados/brutos' / f'{name}.csv').open('w', newline='') as handle:
                writer = csv.DictWriter(handle, fieldnames=calc.SCHEMAS[name].split(','))
                writer.writeheader()
                writer.writerows(rows)
        tables = calc.ler_validar(self.root)
        return calc.calcular(tables)

    def result(self, rows, metrica, **dims):
        return next(r for r in rows if r['metrica'] == metrica and all(r[k] == v for k, v in dims.items()))

    def test_vazio_inconclusivo_e_manifesto(self):
        rows = self.run_calc()
        self.assertEqual(len(rows), 26)
        self.assertEqual(sum(r['estado'] == 'inconclusivo' for r in rows), 25)
        self.assertTrue(all(r['valor_julgado'] == '' and r['nivel'] == '' for r in rows))
        output = self.root / 'saida'
        calc.executar(self.root, output)
        manifest = json.loads((output / 'manifesto-calculo.json').read_text())
        self.assertEqual(manifest['resultados_calculados'], 0)
        self.assertEqual(len(manifest['sha256']), 9)
        with self.assertRaisesRegex(ValueError, 'Nenhuma métrica'):
            calc.executar(self.root, output, require_data=True)

    def test_limites_sem_arredondar(self):
        for m in ('M1.1.1', 'M1.2.1', 'M3.1.1', 'M3.2.1'):
            for value, expected in [(59.999, 'Inaceitável'), (60, 'Mínimo aceitável'), (80, 'Alvo'), (95, 'Excelente')]:
                self.assertEqual(calc.nivel(m, value), expected)
        for m, limits in calc.LIMITES.items():
            for i, boundary in enumerate(limits):
                levels = ['Excelente', 'Alvo', 'Mínimo aceitável', 'Inaceitável']
                self.assertEqual(calc.nivel(m, boundary), levels[i])
                self.assertEqual(calc.nivel(m, boundary + .0001), levels[i + 1])

    def test_p1_denominador_15_17_e_agregado(self):
        self.ambiente()
        for infringement, fields in [('V1-I1', calc.BASE), ('V1-I2', calc.BASE | calc.CONDICIONAIS)]:
            for field in sorted(fields):
                self.row('campos-por-infracao', campo=field, infracao=infringement, tela='detalhe', presente='nao' if field == 'R01' else 'sim')
        rows = self.run_calc()
        result = self.result(rows, 'M1.1.2', infracao='todas')
        self.assertEqual(result['denominador'], 32)
        self.assertEqual(result['numerador'], 30)
        self.assertEqual(result['valor_julgado'], 93.75)
        self.tables['campos-por-infracao'].pop()
        with self.assertRaisesRegex(ValueError, 'conjunto de campos incompleto'):
            self.run_calc()

    def test_p2_ausencia_nao_e_paridade_e_janela(self):
        for field in sorted(calc.BASE):
            self.row('comparacao-canais', campo=field, classificacao='ausente_ambos' if field == 'R01' else 'paritario')
        rows = self.run_calc()
        self.assertAlmostEqual(self.result(rows, 'M1.2.1')['valor_julgado'], 100 * 14 / 15)
        self.assertEqual(self.result(rows, 'M1.2.2')['valor_julgado'], 0)
        self.tables['comparacao-canais'][0]['aplicativo_data_hora'] = '2026-11-19T10:10:01-03:00'
        with self.assertRaisesRegex(ValueError, 'dez minutos'):
            self.run_calc()
        for row in self.tables['comparacao-canais']:
            row.update(elegivel='nao', motivo='Par fora da janela; D001.')
        rows = self.run_calc()
        self.assertEqual(self.result(rows, 'M1.2.1')['estado'], 'inconclusivo')

    def test_p3_recorrencia_e_desvio(self):
        self.ambiente()
        for i, steps in enumerate([4, 4, 5], 1):
            self.row('fluxo', repeticao=i, passos=steps, transicoes=i, rolagens=0, sequencia='Fluxo sintético')
        rows = self.run_calc()
        self.assertEqual(self.result(rows, 'M1.3.1', canal='portal')['valor_julgado'], 4)
        self.assertEqual(self.result(rows, 'M1.3.2', canal='portal')['estado'], 'inconclusivo')

    def test_p4_aquecimento_piloto_p90_e_redes_separadas(self):
        for session, network, offset in [('S01', 'wifi', 100), ('S02', 'wifi', 0), ('S02', '4g', 10)]:
            self.ambiente(rede=network, sessao=session)
            for i in range(11):
                value = 100 if i == 0 else i + offset
                self.row('tempos', sessao=session, rede=network, bloco=network, repeticao=i + 1,
                         aquecimento='sim' if i == 0 else 'nao', inicio_s=0, fim_s=value, tempo_s=value)
        rows = self.run_calc()
        wifi = self.result(rows, 'M2.1.1', canal='portal', rede='wifi')
        self.assertEqual((wifi['n_valido'], wifi['media'], wifi['mediana'], wifi['p90']), (10, 5.5, 5.5, 9))
        self.assertEqual(wifi['n_excluido'], 1)
        self.assertEqual(self.result(rows, 'M2.1.1', canal='portal', rede='4g')['mediana'], 15.5)
        self.assertFalse(any(r['sessao'] == 'S01' for r in rows))

    def test_tempo_quadros_e_inconsistencia(self):
        self.ambiente()
        row = self.row('tempos', quadro_inicial=30, quadro_final=120, fps=30, tempo_s=3, metrica='M2.1.2')
        rows = self.run_calc()
        self.assertEqual(self.result(rows, 'M2.1.2', canal='portal')['mediana'], 3)
        row['tempo_s'] = '2.9'
        with self.assertRaisesRegex(ValueError, 'tempo incompatível'):
            self.run_calc()

    def test_p5_mb_decimal_e_contador(self):
        self.ambiente('CT05')
        row = self.row('volume', canal='aplicativo', contexto='CT05', instrumento='Contador sintético',
                       bytes_iniciais=500, bytes_finais=2000500, bytes_transferidos=2000000, mb=2)
        result = self.result(self.run_calc(), 'M2.2.1', canal='aplicativo')
        self.assertEqual((result['mediana'], result['nivel']), (2, 'Excelente'))
        row['bytes_finais'] = '2000400'
        with self.assertRaisesRegex(ValueError, 'contadores'):
            self.run_calc()

    def test_p6_computador_exige_dois_navegadores(self):
        for context in ['CT01', 'CT02', 'CT03', 'CT04', 'CT05']:
            self.ambiente(context)
            for i in range(3):
                self.row('tentativas', contexto=context, canal=calc.CONTEXTOS[context], bloco=context,
                         procedimento='P6', repeticao=i + 1,
                         resultado='falha' if context == 'CT02' and i < 2 else 'concluida')
        rows = self.run_calc()
        portal = self.result(rows, 'M3.1.1', canal='portal')
        self.assertEqual((portal['numerador'], portal['denominador'], portal['valor_julgado']), (1, 2, 50))
        browsers = self.result(rows, 'M3.1.2', canal='portal')
        self.assertAlmostEqual(browsers['valor_julgado'], 100 * 2 / 3)
        app = self.result(rows, 'M3.1.1', canal='aplicativo')
        self.assertEqual(app['denominador'], 2)
        self.assertIn('CT06', app['limitacoes'])
        self.tables['tentativas'].pop()
        self.assertEqual(self.result(self.run_calc(), 'M3.1.1', canal='aplicativo')['estado'], 'inconclusivo')

    def p7(self, outcomes):
        self.ambiente()
        for i, outcome in enumerate(outcomes, 1):
            self.row('tentativas', repeticao=i, resultado=outcome)
            values = dict(inicio_s=0, fim_s=i, tempo_s=i) if outcome == 'concluida' else {}
            self.row('tempos', repeticao=i, resultado=outcome, metrica='M3.2.3', **values)

    def test_p7_preserva_falhas_e_sem_tempos(self):
        self.p7(['concluida'] * 7 + ['falha', 'sessao_expirada', 'tempo_limite'])
        rows = self.run_calc()
        self.assertEqual(self.result(rows, 'M3.2.1', canal='portal', rede='wifi')['valor_julgado'], 70)
        self.assertEqual(self.result(rows, 'M3.2.2', canal='portal', rede='wifi')['valor_julgado'], 30)
        self.assertEqual(self.result(rows, 'M3.2.3', canal='portal', rede='wifi')['n_valido'], 7)
        for row in self.tables['tempos']:
            row.update(resultado='falha', inicio_s='', fim_s='', tempo_s='')
        for row in self.tables['tentativas']:
            row['resultado'] = 'falha'
        rows = self.run_calc()
        self.assertEqual(self.result(rows, 'M3.2.2', canal='portal', rede='wifi')['valor_julgado'], 100)
        self.assertEqual(self.result(rows, 'M3.2.3', canal='portal', rede='wifi')['estado'], 'inconclusivo')

    def test_p7_redes_ausentes_permanecem_inconclusivas(self):
        self.p7(['concluida'])
        rows = self.run_calc()
        for network in ('4g', 'degradada'):
            for metrica in ('M3.2.1', 'M3.2.2', 'M3.2.3'):
                result = self.result(rows, metrica, canal='portal', rede=network)
                self.assertEqual(result['estado'], 'inconclusivo')
                self.assertEqual(result['valor_julgado'], '')

    def test_p7_correspondencia_e_proibicao_de_excluir_falha(self):
        self.p7(['falha'])
        self.tables['tempos'].clear()
        with self.assertRaisesRegex(ValueError, 'cada tentativa'):
            self.run_calc()
        self.tables['tentativas'][0].update(elegivel='nao', motivo='Exclusão indevida')
        with self.assertRaisesRegex(ValueError, 'falha do serviço'):
            self.run_calc()

    def test_erro_instrumento_nao_altera_denominador_p7(self):
        self.p7(['concluida', 'falha'])
        self.row('tentativas', repeticao=3, resultado='erro_instrumento', elegivel='nao', motivo='D001')
        self.row('tempos', repeticao=3, resultado='erro_instrumento', elegivel='nao', motivo='D001', metrica='M3.2.3')
        result = self.result(self.run_calc(), 'M3.2.1', canal='portal', rede='wifi')
        self.assertEqual((result['denominador'], result['valor_julgado'], result['n_excluido']), (2, 50, 1))

    def test_integridade_evidencia_inventario_duplicata_e_nan(self):
        self.ambiente()
        row = self.row('tempos', inicio_s=0, fim_s=3, tempo_s=3)
        self.run_calc()
        for field, value, message in [('tempo_s', 'NaN', 'número inválido'), ('evidencia', 'dados/privado/segredo.txt', 'evidência'),
                                       ('revisor', '', 'conferência'), ('data_hora', '2026-11-19T10:00:00', 'data sem fuso')]:
            with self.subTest(field=field):
                old = row[field]
                row[field] = value
                with self.assertRaisesRegex(ValueError, message):
                    self.run_calc()
                row[field] = old
        self.tables['tempos'].append(dict(row))
        with self.assertRaisesRegex(ValueError, 'duplicada'):
            self.run_calc()
        self.tables['tempos'].pop()
        self.tables['ambientes'].clear()
        with self.assertRaisesRegex(ValueError, 'sem inventário'):
            self.run_calc()

    def test_bloco_nao_mistura_veiculos(self):
        self.ambiente()
        self.row('tempos', inicio_s=0, fim_s=3, tempo_s=3)
        self.row('tempos', inicio_s=0, fim_s=9, tempo_s=9, repeticao=2, veiculo='V2', infracao='V2-I1')
        with self.assertRaisesRegex(ValueError, 'bloco mistura'):
            self.run_calc()


if __name__ == '__main__':
    unittest.main()
