#!/usr/bin/env python3
"""Valida os instrumentos e calcula as 14 métricas; usa somente a biblioteca padrão."""

import argparse
import csv
import hashlib
import json
import math
import re
import statistics
import subprocess
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = {
    'ambientes': 'sessao,contexto,canal,dispositivo,modelo,cpu,ram_gb,so_build,navegador_versao,aplicativo_versao,resolucao,gravador_versao,fps,rede,configuracao_rede,download_mbps,upload_mbps,latencia_ms,data_hora,evidencia',
    'campos-por-infracao': 'sessao,contexto,canal,veiculo,infracao,tela,campo,aplicavel,presente,acao_consulta,data_hora,evidencia,revisor',
    'comparacao-canais': 'sessao,veiculo,infracao,campo,aplicavel,classificacao,portal_data_hora,aplicativo_data_hora,motivo,evidencia,revisor,elegivel',
    'desvios': 'desvio,sessao,procedimento,metrica,data_hora,motivo,efeito,decisao,responsavel,prazo,evidencia',
    'fluxo': 'sessao,bloco,contexto,canal,veiculo,repeticao,passos,transicoes,rolagens,sequencia,data_hora,evidencia,revisor',
    'tempos': 'sessao,bloco,contexto,canal,rede,veiculo,infracao,metrica,repeticao,aquecimento,quadro_inicial,quadro_final,fps,inicio_s,fim_s,tempo_s,resultado,elegivel,motivo,data_hora,evidencia,revisor',
    'tentativas': 'sessao,bloco,contexto,canal,rede,veiculo,procedimento,repeticao,aquecimento,resultado,elegivel,motivo,data_hora,evidencia,revisor',
    'volume': 'sessao,bloco,contexto,canal,rede,veiculo,repeticao,aquecimento,instrumento,bytes_iniciais,bytes_finais,bytes_transferidos,mb,elegivel,motivo,data_hora,evidencia,revisor',
}
KEYS = {
    'ambientes': 'sessao contexto rede',
    'campos-por-infracao': 'sessao contexto canal veiculo infracao tela campo',
    'comparacao-canais': 'sessao veiculo infracao campo',
    'desvios': 'desvio',
    'fluxo': 'sessao bloco repeticao',
    'tempos': 'sessao bloco repeticao metrica',
    'tentativas': 'sessao bloco repeticao',
    'volume': 'sessao bloco repeticao',
}
METRICAS = ('M1.1.1 M1.1.2 M1.2.1 M1.2.2 M1.3.1 M1.3.2 M2.1.1 '
            'M2.1.2 M2.2.1 M3.1.1 M3.1.2 M3.2.1 M3.2.2 M3.2.3').split()
LIMITES = {
    'M1.3.1': (4, 6, 8), 'M1.3.2': (3, 5, 7), 'M2.1.1': (3, 5, 8),
    'M2.1.2': (2, 4, 6), 'M2.2.1': (2, 5, 10), 'M3.2.2': (5, 20, 40),
    'M3.2.3': (5, 10, 20),
}
BASE = {f'R{i:02}' for i in range(1, 16)}
CONDICIONAIS = {'velocidade_permitida', 'velocidade_aferida'}
FALHAS = {'falha', 'sessao_expirada', 'tempo_limite'}
CONTEXTOS = {f'CT{i:02}': 'portal' if i <= 3 else 'aplicativo' for i in range(1, 7)}
OUTPUT = ('metrica,canal,veiculo,contexto,rede,n_valido,n_excluido,numerador,denominador,'
          'unidade,media,mediana,p90,valor_julgado,nivel,estado,commit_dados,'
          'procedimento_calculo,evidencia,limitacoes,sessao,bloco,infracao').split(',')
NUMEROS = set(('ram_gb fps download_mbps upload_mbps latencia_ms repeticao passos transicoes '
               'rolagens quadro_inicial quadro_final inicio_s fim_s tempo_s bytes_iniciais '
               'bytes_finais bytes_transferidos mb').split())
INTEIROS = set('repeticao passos transicoes rolagens quadro_inicial quadro_final bytes_iniciais bytes_finais bytes_transferidos'.split())


def grupos(rows, cols):
    result = defaultdict(list)
    for row in rows:
        result[tuple(row.get(c, '') for c in cols.split())].append(row)
    return result


def oficial(row):
    return row['sessao'] != 'S01'


def elegivel(row):
    return oficial(row) and row.get('elegivel', 'sim') == 'sim' and row.get('aquecimento', 'nao') == 'nao' and row.get('resultado') != 'nao_avaliado'


def numero(row, field):
    return float(row[field])


def data(value):
    result = datetime.fromisoformat(value)
    if result.utcoffset() is None:
        raise ValueError('data sem fuso')
    return result


def ler_validar(root):
    """Falha antes de escrever resultados; erros não exibem valores pessoais das linhas."""
    tables, errors = {}, []
    for name, schema in SCHEMAS.items():
        path = root / 'dados/brutos' / f'{name}.csv'
        try:
            with path.open(encoding='utf-8-sig', newline='') as handle:
                reader = csv.DictReader(handle)
                if reader.fieldnames != schema.split(','):
                    errors.append(f'{name}: cabeçalho diferente do dicionário')
                    tables[name] = []
                    continue
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f'{name}: leitura inválida ({type(exc).__name__})')
            tables[name] = []
            continue
        tables[name] = rows
        seen = set()
        for line, row in enumerate(rows, 2):
            prefix = f'{name}:{line}'
            try:
                if None in row or any(v is None for v in row.values()):
                    raise ValueError('número de colunas inválido')
                key = tuple(row[c] for c in KEYS[name].split())
                if not all(key) or key in seen:
                    raise ValueError('chave vazia ou duplicada')
                seen.add(key)
                if row['sessao'] not in {'S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S08'}:
                    raise ValueError('sessão inválida')
                if 'contexto' in row and CONTEXTOS.get(row['contexto']) != row['canal']:
                    raise ValueError('contexto incompatível com canal')
                if 'rede' in row and row['rede'] not in {'wifi', '4g', 'degradada'}:
                    raise ValueError('rede inválida')
                for c in ('veiculo', 'infracao'):
                    pattern = r'V[1-9][0-9]*' if c == 'veiculo' else r'V[1-9][0-9]*-I[1-9][0-9]*'
                    if c in row and not re.fullmatch(pattern, row[c]):
                        raise ValueError(f'{c}: usar somente código anonimizado')
                if 'infracao' in row and not row['infracao'].startswith(row['veiculo'] + '-I'):
                    raise ValueError('infração não pertence ao código do veículo')
                for c in ('aplicavel', 'presente', 'elegivel', 'aquecimento'):
                    if c in row and row[c] not in {'sim', 'nao'}:
                        raise ValueError(f'{c}: esperado sim/nao')
                for c in NUMEROS & row.keys():
                    if row[c]:
                        n = numero(row, c)
                        if not math.isfinite(n) or n < 0 or (c in INTEIROS and not n.is_integer()):
                            raise ValueError(f'{c}: número inválido')
                        if c in {'fps', 'repeticao'} and n == 0:
                            raise ValueError(f'{c}: deve ser positivo')
                for c in ('data_hora', 'portal_data_hora', 'aplicativo_data_hora'):
                    if c in row:
                        data(row[c])
                unavailable = row.get('resultado') == 'nao_avaliado'
                if 'revisor' in row and not row['revisor'].strip():
                    raise ValueError('conferência independente pendente')
                if not unavailable:
                    evidence = (root / row['evidencia']).resolve()
                    if not evidence.is_relative_to((root / 'evidencias/fase4').resolve()) or not evidence.is_file() or evidence.name in {'README.md', 'modelo-sessao.md'}:
                        raise ValueError('evidência ausente ou fora de evidencias/fase4')
                if row.get('elegivel') == 'nao' or unavailable:
                    if not row.get('motivo', '').strip():
                        raise ValueError('exclusão/contexto não avaliado exige motivo')
                if 'resultado' in row:
                    if row['resultado'] not in FALHAS | {'concluida', 'erro_instrumento', 'nao_avaliado'}:
                        raise ValueError('resultado inválido')
                    if row['resultado'] in FALHAS and row['elegivel'] != 'sim':
                        raise ValueError('falha do serviço não pode ser excluída')
                    if row['resultado'] in {'erro_instrumento', 'nao_avaliado'} and row['elegivel'] != 'nao':
                        raise ValueError('erro de instrumento/contexto não avaliado deve ser inelegível')
                if name == 'ambientes':
                    required = set(schema.split(',')) - NUMEROS
                    if any(not row[c].strip() for c in required):
                        raise ValueError('inventário incompleto')
                if name in {'campos-por-infracao', 'comparacao-canais'}:
                    if row['campo'] not in BASE | CONDICIONAIS:
                        raise ValueError('campo fora da lista de referência')
                    if row['campo'] in BASE and row['aplicavel'] != 'sim':
                        raise ValueError('R01–R15 sempre integram o denominador')
                if name == 'campos-por-infracao' and row['tela'] not in {'lista', 'detalhe'}:
                    raise ValueError('tela inválida')
                if name == 'comparacao-canais':
                    if row['classificacao'] not in {'paritario', 'divergente', 'ausente_portal', 'ausente_aplicativo', 'ausente_ambos'}:
                        raise ValueError('classificação inválida')
                    if row['elegivel'] == 'sim' and abs((data(row['portal_data_hora']) - data(row['aplicativo_data_hora'])).total_seconds()) > 600:
                        raise ValueError('par acima de dez minutos: registrar desvio e elegivel=nao')
                if name == 'fluxo':
                    if any(not row[c] for c in ('passos', 'transicoes', 'rolagens', 'sequencia')):
                        raise ValueError('contagem/roteiro incompleto')
                if name == 'tempos':
                    if row['metrica'] not in {'M2.1.1', 'M2.1.2', 'M3.2.3'}:
                        raise ValueError('métrica de tempo inválida')
                    if row['resultado'] == 'concluida' and row['elegivel'] == 'sim':
                        validar_tempo(row)
                    elif row['tempo_s']:
                        raise ValueError('tentativa não concluída/elegível deve ficar sem tempo')
                if name == 'volume' and row['elegivel'] == 'sim':
                    if not row['instrumento'] or row['contexto'] == 'CT06':
                        raise ValueError('instrumento ausente ou volume iOS sem método aprovado')
                    if not math.isclose(numero(row, 'mb'), numero(row, 'bytes_transferidos') / 1_000_000, abs_tol=1e-9):
                        raise ValueError('MB deve ser bytes/1.000.000, sem arredondamento prévio')
                    if row['canal'] == 'aplicativo' and numero(row, 'bytes_finais') - numero(row, 'bytes_iniciais') != numero(row, 'bytes_transferidos'):
                        raise ValueError('diferença dos contadores incompatível com bytes transferidos')
                if name == 'tentativas' and row['procedimento'] not in {'P6', 'P7'}:
                    raise ValueError('procedimento deve ser P6/P7')
                if name == 'desvios':
                    if row['decisao'] not in {'manter', 'excluir_erro_instrumento', 'repetir', 'pendente'} or not all(row[c] for c in ('motivo', 'efeito', 'responsavel', 'prazo')):
                        raise ValueError('desvio incompleto/decisão inválida')
            except (ValueError, KeyError, ZeroDivisionError) as exc:
                # Não reproduzir a entrada inválida no terminal.
                message = str(exc) if type(exc) is ValueError and not str(exc).startswith(('could not', 'Invalid isoformat')) else 'valor obrigatório ausente ou inválido'
                errors.append(f'{prefix}: {message}')
    if errors:
        raise ValueError('\n'.join(errors))
    validar_relacoes(tables)
    return tables


def validar_tempo(row):
    has_frames = any(row[c] for c in ('quadro_inicial', 'quadro_final'))
    has_stamps = any(row[c] for c in ('inicio_s', 'fim_s'))
    if has_frames == has_stamps:
        raise ValueError('usar quadros ou timestamps, exatamente um método')
    expected = ((numero(row, 'quadro_final') - numero(row, 'quadro_inicial')) / numero(row, 'fps')
                if has_frames else numero(row, 'fim_s') - numero(row, 'inicio_s'))
    if expected < 0 or not math.isclose(expected, numero(row, 'tempo_s'), abs_tol=2e-6):
        raise ValueError('tempo incompatível com marcações')


def validar_relacoes(tables):
    inventory = {(r['sessao'], r['contexto'], r['rede']) for r in tables['ambientes']}
    for name in ('campos-por-infracao', 'fluxo', 'tempos', 'tentativas', 'volume'):
        for row in tables[name]:
            if row.get('resultado') != 'nao_avaliado' and (row['sessao'], row['contexto'], row.get('rede', 'wifi')) not in inventory:
                raise ValueError(f'{name}: sessão/contexto/rede sem inventário')
        for rows in grupos(tables[name], 'sessao bloco').values() if name != 'campos-por-infracao' else []:
            signatures = {tuple(r.get(c, '') for c in ('contexto', 'canal', 'rede', 'veiculo', 'metrica', 'instrumento', 'procedimento', 'infracao')) for r in rows}
            if len(signatures) != 1:
                raise ValueError(f'{name}: bloco mistura contextos, veículos, métricas ou instrumentos')
    for name, cols in [('campos-por-infracao', 'sessao contexto canal veiculo infracao tela'), ('comparacao-canais', 'sessao veiculo infracao')]:
        for rows in grupos(tables[name], cols).values():
            applicable = {r['campo'] for r in rows if r['aplicavel'] == 'sim'}
            expected = BASE if rows[0].get('tela') == 'lista' else BASE | (CONDICIONAIS if applicable & CONDICIONAIS else set())
            if applicable != expected:
                raise ValueError(f'{name}: conjunto de campos incompleto (15 ou 17 obrigatórios)')
            if name == 'comparacao-canais' and len({r['elegivel'] for r in rows}) != 1:
                raise ValueError('comparacao-canais: a elegibilidade deve abranger a infração inteira')
    attempts = {(r['sessao'], r['bloco'], r['repeticao']): r for r in tables['tentativas'] if r['procedimento'] == 'P7'}
    times = {(r['sessao'], r['bloco'], r['repeticao']): r for r in tables['tempos'] if r['metrica'] == 'M3.2.3'}
    if attempts.keys() != times.keys():
        raise ValueError('P7: cada tentativa, inclusive falha/aquecimento, exige linha correspondente em tempos')
    for key, row in attempts.items():
        if any(row[c] != times[key][c] for c in ('contexto', 'canal', 'rede', 'veiculo', 'resultado', 'elegivel', 'aquecimento')):
            raise ValueError('P7: tentativa e tempo discordam')


def nivel(metrica, value):
    if metrica in LIMITES:
        return ('Excelente', 'Alvo', 'Mínimo aceitável', 'Inaceitável')[sum(value > x for x in LIMITES[metrica])]
    return ('Inaceitável', 'Mínimo aceitável', 'Alvo', 'Excelente')[sum(value >= x for x in (60, 80, 95))]


def calcular(tables):
    output = []

    def emitir(m, rows, valid=None, value=None, numerator=None, denominator=None, values=None, limitation='', **dims):
        valid = rows if valid is None else valid
        first = rows[0] if rows else {}
        row = {c: '' for c in OUTPUT}
        row.update({c: first.get(c, '') for c in ('canal', 'veiculo', 'contexto', 'rede', 'sessao', 'bloco', 'infracao')})
        row.update(dims)
        row.update(metrica=m, n_valido=len(valid), n_excluido=len(rows) - len(valid),
                   unidade='s' if m in {'M2.1.1', 'M2.1.2', 'M3.2.3'} else 'MB' if m == 'M2.2.1' else 'passos' if m == 'M1.3.1' else 'telas' if m == 'M1.3.2' else '%',
                   estado='inconclusivo', limitacoes=limitation,
                   procedimento_calculo='dados/scripts/calcular.py',
                   evidencia=';'.join(sorted({r['evidencia'] for r in rows if r['evidencia']})))
        if values:
            row.update(media=statistics.mean(values), mediana=statistics.median(values),
                       p90=sorted(values)[math.ceil(.9 * len(values)) - 1])
        if denominator:
            value = 100 * numerator / denominator
            row.update(numerador=numerator, denominador=denominator)
        if value is not None:
            row.update(valor_julgado=value, nivel=nivel(m, value), estado='calculado')
        output.append(row)

    # P1: por infração e agregado, preservando sessão/canal/contexto/veículo.
    p1 = [r for r in tables['campos-por-infracao'] if oficial(r) and r['aplicavel'] == 'sim']
    for cols, aggregate in [('sessao contexto canal veiculo tela infracao', False), ('sessao contexto canal veiculo tela', True)]:
        for rows in grupos(p1, cols).values():
            emitir('M1.1.1' if rows[0]['tela'] == 'lista' else 'M1.1.2', rows,
                   numerator=sum(r['presente'] == 'sim' for r in rows), denominator=len(rows),
                   infracao='todas' if aggregate else rows[0]['infracao'], rede='wifi')
    # P2: resultados do par; ausência em ambos permanece no denominador.
    for rows in grupos([r for r in tables['comparacao-canais'] if oficial(r) and r['aplicavel'] == 'sim'], 'sessao veiculo').values():
        valid = [r for r in rows if elegivel(r)]
        infractions = list(grupos(valid, 'infracao').values())
        limitation = 'Par de canais, sem ranking individual. n conta campos; denominador de M1.2.2 conta infrações.'
        for m, num, den in [('M1.2.1', sum(r['classificacao'] == 'paritario' for r in valid), len(valid)),
                            ('M1.2.2', sum(all(r['classificacao'] == 'paritario' for r in group) for group in infractions), len(infractions))]:
            emitir(m, rows, valid, numerator=num, denominator=den, canal='par', contexto='CT01+CT05', rede='wifi', infracao='todas', limitation=limitation)
    # P3: moda somente com três repetições e recorrência.
    for rows in grupos([r for r in tables['fluxo'] if oficial(r)], 'sessao bloco').values():
        for m, col in [('M1.3.1', 'passos'), ('M1.3.2', 'transicoes')]:
            value, count = Counter(numero(r, col) for r in rows).most_common(1)[0]
            ok = len(rows) == 3 and count >= 2
            emitir(m, rows, value=value if ok else None, rede='wifi', limitation='' if ok else 'Exige três execuções e contagem recorrente; registrar desvio.')
    # P4/P5/P7: nunca reunir blocos, aparelhos, veículos ou redes.
    for name in ('tempos', 'volume'):
        for rows in grupos([r for r in tables[name] if oficial(r)], 'sessao bloco').values():
            m = rows[0].get('metrica', 'M2.2.1')
            valid = [r for r in rows if elegivel(r) and r.get('resultado', 'concluida') == 'concluida']
            values = [numero(r, 'tempo_s' if name == 'tempos' else 'mb') for r in valid]
            measured = [r for r in rows if r['aquecimento'] == 'nao' and r.get('resultado') != 'nao_avaliado']
            limit = []
            if sum(r['aquecimento'] == 'sim' for r in rows) != 1:
                limit.append('Aquecimento único não registrado; conferir desvio.')
            if len(valid) != 10 and m != 'M3.2.3':
                limit.append('Amostra diferente de dez válidas; registrar bloqueio/desvio.')
            if m != 'M3.2.3' and len(measured) > 20:
                limit.append('Limite de vinte tentativas excedido; conferir desvio.')
            if m == 'M3.2.3':
                limit.append('Tempo apenas das concluídas; consultar taxas M3.2.1/M3.2.2 do mesmo bloco.')
            if name == 'volume':
                limit.append('Sem ranking entre instrumentos sem equivalência documentada no piloto.')
            emitir(m, rows, valid, values=values, value=statistics.median(values) if values else None, limitation=' '.join(limit))
    # P6: contextos aprovados com >=2/3; computador exige CT01 e CT02.
    p6 = [r for r in tables['tentativas'] if oficial(r) and r['procedimento'] == 'P6']
    for rows in grupos(p6, 'sessao canal veiculo rede').values():
        evaluated, incomplete = {}, []
        for (context,), group in grupos(rows, 'contexto').items():
            valid = [r for r in group if elegivel(r)]
            if len(valid) == 3:
                evaluated[context] = sum(r['resultado'] == 'concluida' for r in valid) >= 2
            elif valid:
                incomplete.append(context)
        channel = rows[0]['canal']
        planned = {c for c, ch in CONTEXTOS.items() if ch == channel}
        missing = sorted(planned - evaluated.keys())
        limits = 'Contextos não avaliados/com amostra incompleta: ' + (', '.join(missing) or 'nenhum')
        platforms = list(evaluated.values()) if channel == 'aplicativo' else []
        if channel == 'portal':
            if {'CT01', 'CT02'} <= evaluated.keys():
                platforms.append(evaluated['CT01'] and evaluated['CT02'])
            if 'CT03' in evaluated:
                platforms.append(evaluated['CT03'])
        for m, units in [('M3.1.1', platforms)] + ([('M3.1.2', list(evaluated.values()))] if channel == 'portal' else []):
            emitir(m, rows, [r for r in rows if elegivel(r)], numerator=sum(units), denominator=len(units) if not incomplete else 0,
                   contexto='+'.join(sorted(evaluated)), bloco='', limitation=limits + '. n conta tentativas; denominador conta plataformas/navegadores. ' + '; '.join(f'{c}: {"aprovado" if ok else "reprovado"}' for c, ok in sorted(evaluated.items())))
    # P7: falhas reais entram nas duas taxas complementares.
    p7 = [r for r in tables['tentativas'] if oficial(r) and r['procedimento'] == 'P7']
    for rows in grupos(p7, 'sessao bloco').values():
        valid = [r for r in rows if elegivel(r)]
        limitation = '' if len(valid) == 10 else 'Amostra diferente de dez tentativas elegíveis; registrar desvio.'
        for m, num in [('M3.2.1', sum(r['resultado'] == 'concluida' for r in valid)), ('M3.2.2', sum(r['resultado'] in FALHAS for r in valid))]:
            emitir(m, rows, valid, numerator=num, denominator=len(valid), limitation=limitation)
    for (session, channel, vehicle, context), rows in grupos(p7, 'sessao canal veiculo contexto').items():
        for network in sorted({'wifi', '4g', 'degradada'} - {r['rede'] for r in rows}):
            for m in ('M3.2.1', 'M3.2.2', 'M3.2.3'):
                emitir(m, [], sessao=session, canal=channel, veiculo=vehicle, contexto=context,
                       rede=network, limitation='Condição de rede prevista, sem execução registrada.')
    # Inventário de cobertura: ausência de dados nunca se converte em zero ou aprovação.
    for m in METRICAS:
        channels = ['par'] if m.startswith('M1.2.') else ['portal', 'aplicativo']
        for channel in channels:
            if not any(r['metrica'] == m and r['canal'] == channel for r in output):
                emitir(m, [], canal=channel, limitation='Sem medições oficiais elegíveis registradas.')
                if m == 'M3.1.2' and channel == 'aplicativo':
                    output[-1].update(estado='nao_aplicavel', limitacoes='Métrica exclusiva do portal.')
    return sorted(output, key=lambda r: tuple(str(r[c]) for c in ('metrica', 'canal', 'sessao', 'contexto', 'rede', 'veiculo', 'bloco', 'infracao')))


def executar(root, output, validate_only=False, require_data=False):
    tables = ler_validar(root)
    results = calcular(tables)
    count = sum(r['estado'] == 'calculado' for r in results)
    if require_data and count == 0:
        raise ValueError('Nenhuma métrica calculável: a estrutura vazia não comprova coleta.')
    if validate_only:
        return count
    try:
        commit = subprocess.check_output(['git', '-C', str(root), 'rev-parse', 'HEAD'], text=True, stderr=subprocess.DEVNULL).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        commit = 'sem-git'
    hashes = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((root / 'dados/brutos').glob('*.csv'))}
    hashes['dados/scripts/calcular.py'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    for row in results:
        row['commit_dados'] = commit
    output.mkdir(parents=True, exist_ok=True)
    with (output / 'resultados-metricas.csv').open('w', encoding='utf-8', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT, lineterminator='\n')
        writer.writeheader()
        writer.writerows(results)
    manifest = {'commit_base': commit, 'sha256': hashes, 'linhas_brutas': {k: len(v) for k, v in tables.items()},
                'resultados_calculados': count, 'estados': dict(Counter(r['estado'] for r in results)),
                'observacao': 'Hashes identificam os arquivos efetivamente lidos, inclusive alterações ainda não commitadas. Validação estrutural não atesta consentimento, anonimização ou revisão humana.'}
    (output / 'manifesto-calculo.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raiz', type=Path, default=ROOT)
    parser.add_argument('--saida', type=Path, help='Padrão: dados/consolidados; não altera respostas GQM/oportunidades.')
    parser.add_argument('--validar', action='store_true', help='Somente conferir, sem escrever arquivos.')
    parser.add_argument('--exigir-dados', action='store_true', help='Falhar se nenhuma métrica for calculável; não certifica completude da coleta.')
    args = parser.parse_args()
    try:
        count = executar(args.raiz.resolve(), args.saida or args.raiz / 'dados/consolidados', args.validar, args.exigir_dados)
    except ValueError as exc:
        parser.exit(1, f'Erro de validação:\n{exc}\n')
    print(f'Validação concluída; {count} resultados calculáveis.' + (' Sem dados: coleta permanece pendente.' if count == 0 else ' Conferir limitações e revisão humana.'))


if __name__ == '__main__':
    main()
