#!/usr/bin/env python3
"""Gera docs/fase4-medicoes.md a partir dos CSV de dados/; usa somente a biblioteca padrão.

A página mostra, para cada métrica, o resultado oficial de dados/consolidados/ e cada
observação de dados/brutos/ com o link para a linha exata do CSV no GitHub. Nenhum valor
é digitado à mão: para mudar a página, mudar os dados e executar este script de novo.
"""

import argparse
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SAIDA = ROOT / 'docs/fase4-medicoes.md'
REPO = 'https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON'
RAW = 'https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/main'
REF = 'main'

OBJETIVOS = {
    'G1': ('Adequação funcional', 'D1 e D2', 'Q1.1 Q1.2 Q1.3'),
    'G2': ('Eficiência de desempenho', 'D1 e D3', 'Q2.1 Q2.2'),
    'G3': ('Cobertura de contexto', 'D1, D3 e D4', 'Q3.1 Q3.2'),
}
QUESTOES = {
    'Q1.1': 'Completude funcional', 'Q1.2': 'Correção e consistência funcional',
    'Q1.3': 'Adequação das operações', 'Q2.1': 'Comportamento temporal',
    'Q2.2': 'Utilização de recursos de rede', 'Q3.1': 'Completude de contexto tecnológico',
    'Q3.2': 'Flexibilidade em rede degradada',
}
# métrica: (nome, questão, procedimento, arquivo bruto, contextos)
METRICAS = {
    'M1.1.1': ('Campos da lista de referência exibidos', 'Q1.1', 'P1', 'campos-por-infracao', 'CT01 CT05'),
    'M1.1.2': ('Campos detalhados acessíveis', 'Q1.1', 'P1', 'campos-por-infracao', 'CT01 CT05'),
    'M1.2.1': ('Campos comuns consistentes', 'Q1.2', 'P2', 'comparacao-canais', 'CT01 CT05'),
    'M1.2.2': ('Infrações sem divergência', 'Q1.2', 'P2', 'comparacao-canais', 'CT01 CT05'),
    'M1.3.1': ('Passos até a lista de infrações', 'Q1.3', 'P3', 'fluxo', 'CT01 CT05'),
    'M1.3.2': ('Transições de tela', 'Q1.3', 'P3', 'fluxo', 'CT01 CT05'),
    'M2.1.1': ('Tempo até a lista completa', 'Q2.1', 'P4', 'tempos', 'CT01 CT05'),
    'M2.1.2': ('Tempo até os detalhes', 'Q2.1', 'P4', 'tempos', 'CT01 CT05'),
    'M2.2.1': ('Volume de dados transferidos', 'Q2.2', 'P5', 'volume', 'CT01 CT05'),
    'M3.1.1': ('Conclusão por plataforma', 'Q3.1', 'P6', 'tentativas', 'CT01 CT02 CT03 CT04 CT05 CT06'),
    'M3.1.2': ('Conclusão por navegador (só portal)', 'Q3.1', 'P6', 'tentativas', 'CT01 CT02 CT03'),
    'M3.2.1': ('Conclusão por condição de rede', 'Q3.2', 'P7', 'tentativas', 'CT01 CT05'),
    'M3.2.2': ('Falhas ou expiração de sessão', 'Q3.2', 'P7', 'tentativas', 'CT01 CT05'),
    'M3.2.3': ('Tempo de conclusão por rede', 'Q3.2', 'P7', 'tempos', 'CT01 CT05'),
}
# Limite superior de cada nível das métricas de tempo (Excelente, Alvo, Mínimo), da Fase 2.
LIMITES_TEMPO = {'M2.1.1': (3, 5, 8), 'M2.1.2': (2, 4, 6), 'M3.2.3': (5, 10, 20)}
CAMPOS = {
    'R01': 'Tipificação da infração', 'R02': 'Enquadramento legal', 'R03': 'Local',
    'R04': 'Data', 'R05': 'Hora', 'R06': 'Placa', 'R07': 'Marca/modelo',
    'R08': 'Órgão autuador', 'R09': 'Número do auto', 'R10': 'Natureza',
    'R11': 'Pontuação', 'R12': 'Valor da multa', 'R13': 'Vencimento',
    'R14': 'Prazo de defesa ou indicação do condutor', 'R15': 'Situação',
    'velocidade_permitida': 'Velocidade permitida (condicional)',
    'velocidade_aferida': 'Velocidade aferida (condicional)',
}
SESSOES = {
    'S02': ('22/11/2026', 'P1, P2 e P3', 'V2', 'evidencias/fase4/S02-registro-2026-11-22.md',
            'evidencias/fase4/S02-segunda-leitura-2026-11-23.md', 'evidencias/fase4/capturas/S02'),
    'S03': ('21/11/2026 (B04 em 22/11)', 'P6 em CT01, CT03, CT05 e CT06', 'V1 e V5',
            'evidencias/fase4/S03-registro-2026-11-21.md',
            'evidencias/fase4/segunda-leitura-p4-p7-2026-11-23.md', 'evidencias/fase4/capturas/S03'),
    'S05': ('22/11/2026', 'P6 em CT05, CT02 e CT01', 'V2', 'evidencias/fase4/S05-registro-2026-11-22.md',
            'evidencias/fase4/segunda-leitura-p4-p7-2026-11-23.md', 'evidencias/fase4/capturas/S05'),
    'S06': ('22/11/2026', 'P4 e P5', 'V4', 'evidencias/fase4/S06-registro-2026-11-22.md',
            'evidencias/fase4/segunda-leitura-p4-p7-2026-11-23.md', ''),
    'S08': ('22/11/2026', 'P7 em Wi-Fi, 4G e rede degradada', 'V4', 'evidencias/fase4/S08-registro-2026-11-22.md',
            'evidencias/fase4/segunda-leitura-p4-p7-2026-11-23.md', ''),
}
REDES = {'wifi': 'Wi-Fi', '4g': '4G', 'degradada': 'degradada'}
CANAIS = {'portal': 'Portal', 'aplicativo': 'Aplicativo', 'par': 'Par de canais'}
NIVEIS = {'Excelente': 'excelente', 'Alvo': 'alvo', 'Mínimo aceitável': 'minimo', 'Inaceitável': 'inaceitavel'}
RESULTADOS = {
    'concluida': 'concluída', 'falha': 'falha', 'sessao_expirada': 'sessão expirada',
    'tempo_limite': 'tempo limite', 'erro_instrumento': 'erro do instrumento',
}
NOTAS = {
    'M3.1.1': '[CT04](fase3-ambiente.md#ct04), o aplicativo em Android de entrada, não foi executado por '
              'falta de aparelho: fica sem nível, nunca zero. O denominador conta plataformas; o computador '
              'só entra como plataforma quando CT01 e CT02 foram executados com o mesmo veículo.',
    'M3.2.1': 'O aplicativo não foi medido na rede degradada: a condição não pôde ser imposta ao aparelho (D021).',
}
ESTADOS_GQM = {
    'atendido': ('excelente', 'Atendida'), 'nao_atendido': ('inaceitavel', 'Não atendida'),
    'inconclusivo': ('inconclusivo', 'Inconclusiva'),
}


def ancora(metrica):
    return metrica.lower().replace('.', '-')


def slug_github(titulo):
    """Reproduz o identificador que o GitHub gera para um título Markdown."""
    titulo = re.sub(r'[`*_]', '', titulo.strip().lower())
    titulo = re.sub(r'[^\w\- ]', '', titulo)
    return titulo.replace(' ', '-')


def secao(arquivo, *termos):
    """Link para o primeiro título do arquivo que contém todos os termos (ou para o arquivo)."""
    url = f'{REPO}/blob/{REF}/{arquivo}'
    for linha in (ROOT / arquivo).read_text(encoding='utf-8').splitlines():
        if linha.startswith('#') and all(t in linha for t in termos):
            return f'{url}#{slug_github(linha.lstrip("#"))}'
    return url


def ler(nome, pasta='brutos'):
    """Lê o CSV e guarda, em cada linha, o número da linha no arquivo."""
    with (ROOT / f'dados/{pasta}/{nome}.csv').open(encoding='utf-8', newline='') as f:
        leitor = csv.DictReader(f)
        linhas = []
        for row in leitor:
            row['_linha'] = leitor.line_num
            linhas.append(row)
    return linhas


def intervalos(numeros):
    numeros = sorted(numeros)
    blocos = []
    for n in numeros:
        if blocos and n == blocos[-1][1] + 1:
            blocos[-1][1] = n
        else:
            blocos.append([n, n])
    return blocos


def link_linhas(arquivo, rows, rotulo=None):
    """Um link por faixa contínua de linhas, aberto no GitHub com as linhas destacadas."""
    partes = []
    for ini, fim in intervalos(r['_linha'] for r in rows):
        faixa = f'L{ini}' if ini == fim else f'L{ini}-L{fim}'
        texto = rotulo or (f'linha {ini}' if ini == fim else f'linhas {ini}–{fim}')
        partes.append(f'[{texto}]({REPO}/blob/{REF}/dados/brutos/{arquivo}.csv?plain=1#{faixa})')
    return ', '.join(partes)


def arquivo_repo(caminho, texto=None):
    tipo = 'tree' if not Path(caminho).suffix else 'blob'
    return f'[{texto or Path(caminho).name}]({REPO}/{tipo}/{REF}/{caminho})'


def num(valor, casas=3):
    return f'{float(valor):.{casas}f}'.replace('.', ',')


def pct(valor):
    return f'{float(valor):.2f}'.replace('.', ',').replace(',00', '') + '%'


def nivel(texto):
    if texto in NIVEIS:
        return f'<span class="kj-nivel kj-nivel--{NIVEIS[texto]}">{texto}</span>'
    if texto == 'nao_aplicavel':
        return '<span class="kj-nivel kj-nivel--na">Não se aplica</span>'
    return '<span class="kj-nivel kj-nivel--inconclusivo">Inconclusivo</span>'


def estado_gqm(estado):
    classe, texto = ESTADOS_GQM[estado]
    return f'<span class="kj-nivel kj-nivel--{classe}">{texto}</span>'


def valor_resultado(r):
    if r['estado'] != 'calculado':
        return '—'
    unidade = r['unidade']
    if unidade == '%':
        texto = pct(r['valor_julgado'])
        if r['numerador']:
            texto = f'{r["numerador"]}/{r["denominador"]} ({texto})'
        return texto
    if unidade == 's':
        return f'mediana **{num(r["mediana"])} s** (média {num(r["media"])}; P90 {num(r["p90"])})'
    if unidade == 'MB':
        return f'mediana **{num(r["mediana"], 4)} MB** (média {num(r["media"], 4)})'
    return f'**{int(float(r["valor_julgado"]))}** {unidade}'


VERSOES = {}


def versao(r):
    """Versão do aplicativo usada no caso, lida de ambientes.csv."""
    if r['canal'] != 'aplicativo':
        return ''
    texto = VERSOES.get((r['sessao'], r['contexto']), '')
    achado = re.search(r'\d+\.\d+\.\d+', texto)
    return achado.group(0) if achado else ''


def caso(r):
    contexto = r['contexto'].replace('+', ' + ') or '—'
    if versao(r):
        contexto += f' (aplicativo {versao(r)})'
    partes = [r['veiculo'] or '—', contexto]
    if r['rede']:
        partes.append(REDES.get(r['rede'], r['rede']))
    return ', '.join(partes)


def filtro_bruto(metrica, r, dados):
    """Linhas brutas que originaram um resultado consolidado."""
    _, _, proc, arquivo, _ = METRICAS[metrica]
    linhas = dados[arquivo]
    if arquivo == 'campos-por-infracao':
        tela = 'lista' if metrica == 'M1.1.1' else 'detalhe'
        return [x for x in linhas if x['sessao'] == r['sessao'] and x['canal'] == r['canal'] and x['tela'] == tela]
    if arquivo == 'comparacao-canais':
        return [x for x in linhas if x['sessao'] == r['sessao'] and x['veiculo'] == r['veiculo']]
    if arquivo == 'fluxo':
        return [x for x in linhas if x['sessao'] == r['sessao'] and x['bloco'] == r['bloco']]
    if arquivo == 'tempos':
        return [x for x in linhas if x['sessao'] == r['sessao'] and x['bloco'] == r['bloco']
                and x['metrica'] == metrica]
    if arquivo == 'volume':
        return [x for x in linhas if x['sessao'] == r['sessao'] and x['bloco'] == r['bloco']]
    if proc == 'P6':
        contextos = set(r['contexto'].split('+'))
        return [x for x in linhas if x['sessao'] == r['sessao'] and x['procedimento'] == 'P6'
                and x['contexto'] in contextos and x['veiculo'] == r['veiculo']]
    return [x for x in linhas if x['sessao'] == r['sessao'] and x['bloco'] == r['bloco']]


def segunda_leitura(metrica, r):
    proc = METRICAS[metrica][2]
    if r['sessao'] == 'S02':
        arquivo = SESSOES['S02'][4]
        return f'[segunda leitura de {proc}]({secao(arquivo, proc + " —")})'
    arquivo = SESSOES[r['sessao']][4]
    if proc in ('P4', 'P7') and r['bloco']:
        return f'[segunda leitura do {r["bloco"]}]({secao(arquivo, r["sessao"] + " " + r["bloco"])})'
    return f'[segunda leitura de {proc}]({secao(arquivo, proc + " —")})'


def resultados_da_metrica(metrica, resultados):
    linhas = [r for r in resultados if r['metrica'] == metrica]
    # Em P1 o agregado "todas" repete a única infração da amostra; mostra uma linha só.
    por_infracao = {(r['canal'], r['sessao']) for r in linhas if r['infracao'] not in ('', 'todas')}
    if metrica.startswith('M1.1'):
        linhas = [r for r in linhas if r['infracao'] != 'todas' or (r['canal'], r['sessao']) not in por_infracao]
    ordem = {'portal': 0, 'aplicativo': 1, 'par': 2}
    rede = {'wifi': 0, '4g': 1, 'degradada': 2, '': 3}
    return sorted(linhas, key=lambda r: (ordem[r['canal']], rede[r['rede']], r['sessao'], r['veiculo']))


def tabela_resultados(metrica, linhas, dados):
    arquivo = METRICAS[metrica][3]
    out = ['| Canal | Caso e sessão | n válido (excluídos) | Valor julgado | Nível | Verificar |',
           '|---|---|---|---|---|---|']
    for r in linhas:
        if r['estado'] == 'nao_aplicavel':
            out.append(f'| {CANAIS[r["canal"]]} | — | — | — | {nivel("nao_aplicavel")} | {r["limitacoes"]} |')
            continue
        brutas = filtro_bruto(metrica, r, dados) if r['sessao'] else []
        verificar = []
        if brutas:
            verificar.append(link_linhas(arquivo, brutas) + f' de {arquivo}.csv')
        if r['sessao'] in SESSOES and r['estado'] == 'calculado':
            verificar.append(segunda_leitura(metrica, r))
        if METRICAS[metrica][2] == 'P6' and 'plataformas/navegadores. ' in r['limitacoes']:
            verificar.append(r['limitacoes'].split('plataformas/navegadores. ', 1)[1])
        if substituido(r, linhas):
            verificar.append('bloco excluído e reposto (leituras nas observações)')
        elif r['estado'] != 'calculado':
            verificar.append(r['limitacoes'])
        sessao = ' '.join(x for x in (r['sessao'], r['bloco']) if x) or '—'
        n = f'{r["n_valido"]} ({r["n_excluido"]})' if r['estado'] == 'calculado' else '—'
        out.append(f'| {CANAIS[r["canal"]]} | {caso(r)}; {sessao} | {n} | {valor_resultado(r)} | '
                   f'{nivel(r["nivel"] or r["estado"])} | {"; ".join(verificar)} |')
    return out


def tabela_campos(metrica, dados):
    tela = 'lista' if metrica == 'M1.1.1' else 'detalhe'
    linhas = [x for x in dados['campos-por-infracao'] if x['tela'] == tela]
    por = {(x['canal'], x['campo']): x for x in linhas}
    campos = [c for c in CAMPOS if any(k[1] == c for k in por)]
    out = ['| Campo de referência (Fase 1) | Portal | Aplicativo |', '|---|---|---|']
    for c in campos:
        celulas = []
        for canal in ('portal', 'aplicativo'):
            x = por.get((canal, c))
            if not x:
                celulas.append('—')
                continue
            marca = 'presente' if x['presente'] == 'sim' else '**ausente**'
            celulas.append(f'{marca} ({link_linhas("campos-por-infracao", [x], "linha " + str(x["_linha"]))})')
        out.append(f'| {c}, {CAMPOS[c]} | {celulas[0]} | {celulas[1]} |')
    return out


def tabela_comparacao(dados):
    out = ['| Campo de referência (Fase 1) | Classificação no par | Linha |', '|---|---|---|']
    for x in dados['comparacao-canais']:
        classe = x['classificacao'].replace('_', ' ')
        if x['classificacao'] != 'paritario':
            classe = f'**{classe}**'
        out.append(f'| {x["campo"]}, {CAMPOS.get(x["campo"], x["campo"])} | {classe} | '
                   f'{link_linhas("comparacao-canais", [x], "linha " + str(x["_linha"]))} |')
    return out


def tabela_observacoes(arquivo, linhas, colunas):
    cab = ' | '.join(nome for nome, _ in colunas)
    out = [f'| {cab} | Linha |', '|' + '---|' * (len(colunas) + 1)]
    for x in linhas:
        valores = ' | '.join(f(x) for _, f in colunas)
        out.append(f'| {valores} | {link_linhas(arquivo, [x], str(x["_linha"]))} |')
    return out


def sim_nao(valor):
    return 'sim' if valor == 'sim' else 'não'


def detalhes(titulo, linhas):
    return ['', f'<details class="kj-obs" markdown="1">', f'<summary>{titulo}</summary>', '', *linhas, '', '</details>']


def grafico_tempos(metrica, linhas_res, dados):
    """Pontos de cada leitura válida, mediana e limite do nível Excelente, em SVG."""
    limite = LIMITES_TEMPO[metrica][0]
    grupos = []
    for r in linhas_res:
        if substituido(r, linhas_res):
            continue
        rotulo = CANAIS[r['canal']] + (f', {REDES[r["rede"]]}' if metrica == 'M3.2.3' else '')
        if r['estado'] != 'calculado':
            grupos.append((rotulo, r['canal'], [], None, 'não medido'))
            continue
        brutas = filtro_bruto(metrica, r, dados)
        validas = [x for x in brutas if x['elegivel'] == 'sim' and x['aquecimento'] == 'nao' and x['tempo_s']]
        sem_tempo = [x for x in brutas if x['elegivel'] == 'sim' and x['aquecimento'] == 'nao' and not x['tempo_s']]
        nota = f'mediana {num(r["mediana"])} s · n={len(validas)}'
        if sem_tempo:
            nota += f' · +{len(sem_tempo)} falhas'
        grupos.append((rotulo, r['canal'], validas, float(r['mediana']), nota))
    larg, esq, dir_, alt_linha, topo = 660, 150, 190, 34, 18
    plot = larg - esq - dir_
    altura = topo + alt_linha * len(grupos) + 34
    x = lambda v: esq + plot * min(v, limite) / limite
    partes = [f'<figure class="kj-grafico" id="grafico-{ancora(metrica)}">',
              f'<svg viewBox="0 0 {larg} {altura}" role="img" aria-labelledby="gt-{ancora(metrica)}">',
              f'<title id="gt-{ancora(metrica)}">{metrica}: cada leitura válida em segundos, com a mediana e o limite do nível Excelente ({limite} s)</title>']
    passo = 0.5 if limite <= 3 else 1
    t = 0.0
    while t <= limite + 1e-9:
        partes.append(f'<line class="kj-g-grade" x1="{x(t):.1f}" x2="{x(t):.1f}" y1="{topo - 6}" y2="{altura - 28}"/>'
                      f'<text class="kj-g-eixo" x="{x(t):.1f}" y="{altura - 12}" text-anchor="middle">{num(t, 1)}</text>')
        t += passo
    partes.append(f'<line class="kj-g-limite" x1="{x(limite):.1f}" x2="{x(limite):.1f}" y1="{topo - 10}" y2="{altura - 28}"/>'
                  f'<text class="kj-g-eixo" x="{x(limite) + 6:.1f}" y="{topo - 2}">limite Excelente: {limite} s</text>')
    arquivo = METRICAS[metrica][3]
    for i, (rotulo, canal, validas, mediana, nota) in enumerate(grupos):
        y = topo + alt_linha * i + alt_linha / 2
        partes.append(f'<text class="kj-g-rotulo" x="{esq - 12}" y="{y + 4:.1f}" text-anchor="end">{rotulo}</text>')
        partes.append(f'<line class="kj-g-base" x1="{esq}" x2="{esq + plot}" y1="{y:.1f}" y2="{y:.1f}"/>')
        for k, obs in enumerate(validas):
            v = float(obs['tempo_s'])
            dy = (k % 3 - 1) * 5
            url = f'{REPO}/blob/{REF}/dados/brutos/{arquivo}.csv?plain=1#L{obs["_linha"]}'
            partes.append(f'<a href="{url}"><circle class="kj-g-ponto kj-g-{canal}" cx="{x(v):.1f}" cy="{y + dy:.1f}" r="4.5">'
                          f'<title>{rotulo}, repetição {obs["repeticao"]}: {num(v)} s (linha {obs["_linha"]} de {arquivo}.csv)</title></circle></a>')
        if mediana is not None:
            partes.append(f'<line class="kj-g-mediana" x1="{x(mediana):.1f}" x2="{x(mediana):.1f}" y1="{y - 12:.1f}" y2="{y + 12:.1f}"/>')
        partes.append(f'<text class="kj-g-nota" x="{esq + plot + 12}" y="{y + 4:.1f}">{nota}</text>')
    partes.append('</svg>')
    partes.append(f'<figcaption>{metrica} — cada ponto é uma leitura válida (sem aquecimento); o traço vertical '
                  f'é a mediana usada no julgamento e a linha tracejada é o limite do nível Excelente. '
                  f'Clique em um ponto para abrir a linha correspondente de <code>{arquivo}.csv</code>.</figcaption>')
    partes.append('</figure>')
    return [''.join(partes)]


def observacoes(metrica, linhas_res, dados):
    arquivo = METRICAS[metrica][3]
    if metrica in ('M1.1.1', 'M1.1.2'):
        return detalhes('Campo a campo, com a linha de cada registro', tabela_campos(metrica, dados))
    if metrica in ('M1.2.1', 'M1.2.2'):
        return detalhes('Comparação campo a campo entre os canais', tabela_comparacao(dados))
    if metrica in ('M1.3.1', 'M1.3.2'):
        cols = [('Canal', lambda x: CANAIS[x['canal']]), ('Bloco', lambda x: x['bloco']),
                ('Repetição', lambda x: x['repeticao']), ('Passos', lambda x: x['passos']),
                ('Transições', lambda x: x['transicoes']), ('Rolagens', lambda x: x['rolagens']),
                ('Sequência', lambda x: x['sequencia']), ('Revisor', lambda x: x['revisor'])]
        return detalhes('As três repetições de cada canal', tabela_observacoes(arquivo, dados['fluxo'], cols))
    linhas = []
    for r in linhas_res:
        if r['estado'] == 'calculado':
            linhas += filtro_bruto(metrica, r, dados)
    if arquivo == 'tempos':
        excl = [x for x in dados['tempos'] if x['metrica'] == metrica and x['elegivel'] == 'nao']
        linhas += [x for x in excl if x not in linhas]
        cols = [('Bloco', lambda x: x['bloco']), ('Canal', lambda x: CANAIS[x['canal']]),
                ('Rede', lambda x: REDES[x['rede']]), ('Rep.', lambda x: x['repeticao']),
                ('Aquecimento', lambda x: sim_nao(x['aquecimento'])),
                ('Tempo (s)', lambda x: num(x['tempo_s']) if x['tempo_s'] else '—'),
                ('Resultado', lambda x: RESULTADOS[x['resultado']]), ('Entra no cálculo', lambda x: sim_nao(x['elegivel'])),
                ('Motivo da exclusão', lambda x: x['motivo'] if x['elegivel'] == 'nao' else ''),
                ('Revisor', lambda x: x['revisor'])]
        linhas.sort(key=lambda x: x['_linha'])
        return detalhes(f'Todas as {len(linhas)} leituras, inclusive aquecimentos e blocos excluídos',
                        tabela_observacoes(arquivo, linhas, cols))
    if arquivo == 'volume':
        cols = [('Bloco', lambda x: x['bloco']), ('Canal', lambda x: CANAIS[x['canal']]),
                ('Rep.', lambda x: x['repeticao']), ('Aquecimento', lambda x: sim_nao(x['aquecimento'])),
                ('Bytes', lambda x: x['bytes_transferidos']), ('MB', lambda x: num(x['mb'], 4)),
                ('Instrumento', lambda x: x['instrumento']), ('Revisor', lambda x: x['revisor'])]
        return detalhes(f'Todas as {len(linhas)} leituras de volume', tabela_observacoes(arquivo, linhas, cols))
    if metrica.startswith('M3.1'):
        brutas = [x for x in dados['tentativas'] if x['procedimento'] == 'P6']
        if metrica == 'M3.1.2':
            brutas = [x for x in brutas if x['canal'] == 'portal']
        return detalhes('Tentativas por contexto, com imagem e linha de cada uma', tabela_p6(brutas))
    brutas = [x for x in dados['tentativas'] if x['procedimento'] == 'P7']
    cols = [('Bloco', lambda x: x['bloco']), ('Canal', lambda x: CANAIS[x['canal']]),
            ('Rede', lambda x: REDES[x['rede']]), ('Rep.', lambda x: x['repeticao']),
            ('Aquecimento', lambda x: sim_nao(x['aquecimento'])), ('Resultado', lambda x: RESULTADOS[x['resultado']]),
            ('Motivo', lambda x: x['motivo']), ('Revisor', lambda x: x['revisor'])]
    return detalhes(f'Todas as {len(brutas)} tentativas de P7', tabela_observacoes('tentativas', brutas, cols))


def tabela_p6(brutas):
    capturas = {p.name: p for p in (ROOT / 'evidencias/fase4/capturas').glob('S0*/*.png')}
    out = ['| Sessão e bloco | Contexto | Canal | Veículo | Rep. | Resultado | Entra no cálculo | Captura | Linha |',
           '|---|---|---|---|---|---|---|---|---|']
    for x in brutas:
        prefixo = f'{x["sessao"]}-{x["bloco"]}-{x["canal"]}-P6-{x["veiculo"]}-{x["repeticao"]}-'
        img = next((p for n, p in sorted(capturas.items()) if n.startswith(prefixo)), None)
        if not img and x['contexto'] == 'CT06':
            img = next((p for n, p in sorted(capturas.items()) if n.startswith(f'{x["sessao"]}-{x["bloco"]}-') and 'resultado' in n), None)
        captura = arquivo_repo(img.relative_to(ROOT).as_posix(), 'imagem') if img else '—'
        out.append(f'| {x["sessao"]} {x["bloco"]} | [{x["contexto"]}](fase3-ambiente.md#{x["contexto"].lower()}) | '
                   f'{CANAIS[x["canal"]]} | {x["veiculo"]} | {x["repeticao"]} | {RESULTADOS[x["resultado"]]} | '
                   f'{sim_nao(x["elegivel"])} | {captura} | {link_linhas("tentativas", [x], str(x["_linha"]))} |')
    return out


def desvios_da_metrica(metrica, dados):
    ds = [d for d in dados['desvios'] if metrica in d['metrica'].split(';') and d['sessao'] != 'S01']
    if not ds:
        return []
    itens = [f'[{d["desvio"]}]({REPO}/blob/{REF}/dados/brutos/desvios.csv?plain=1#L{d["_linha"]})' for d in ds]
    return ['', f'**Desvios que afetam esta métrica:** {", ".join(itens)}. Cada um registra motivo, efeito e decisão.']


def capturas_s02(metrica):
    if metrica not in ('M1.1.1', 'M1.1.2'):
        return []
    tela = 'lista-infracoes-V2' if metrica == 'M1.1.1' else 'detalhe-V2-I1'
    figs = []
    for canal, nome in (('portal', 'Portal'), ('android', 'Aplicativo')):
        caminho = f'evidencias/fase4/capturas/S02/S02-{canal}-{tela}.png'
        figs.append(f'<a class="kj-miniatura" href="{REPO}/blob/{REF}/{caminho}">'
                    f'<img src="{RAW}/{caminho}" alt="Captura anonimizada da S02: {nome}, '
                    f'{"lista de infrações" if metrica == "M1.1.1" else "detalhe da infração"} do V2" loading="lazy">'
                    f'<span>{nome}: {"lista" if metrica == "M1.1.1" else "detalhe"} (S02)</span></a>')
    return ['', '<div class="kj-miniaturas">' + ''.join(figs) + '</div>']


def cadeia(metrica):
    nome, q, proc, arquivo, contextos = METRICAS[metrica]
    g = 'G' + metrica[1]
    carac, decisoes, _ = OBJETIVOS[g]
    a = ancora(metrica)
    ctx = ', '.join(f'[{c}](fase3-ambiente.md#{c.lower()})' for c in contextos.split())
    return ['<div class="kj-fases" markdown="1">', '',
            f'- <span class="kj-fase kj-fase--f1">Fase 1</span> [{carac}](fase1-priorizacao.md#resultado-priorizacao) · '
            f'[decisões {decisoes}](fase1-proposito.md#decisoes)',
            f'- <span class="kj-fase kj-fase--f2">Fase 2</span> [{g}](fase2-gqm.md#{g.lower()}) → '
            f'[{q}](fase2-gqm.md#{ancora(q)}) e [H{q[1:]}](fase2-gqm.md#h{ancora(q)[1:]}) → '
            f'[ficha e níveis de {metrica}](fase2-metricas.md#{a})',
            f'- <span class="kj-fase kj-fase--f3">Fase 3</span> [procedimento {proc}](fase3-metodo.md#{proc.lower()}) · '
            f'{ctx} · {arquivo_repo(f"dados/brutos/{arquivo}.csv", arquivo + ".csv")}',
            f'- <span class="kj-fase kj-fase--f4">Fase 4</span> [resposta à {q}](fase4-analise.md#resp-{ancora(q)}) → '
            f'[julgamento de {g}](fase4-analise.md#julg-{g.lower()}) · [linha na rastreabilidade](rastreabilidade.md#rt-{a})',
            '', '</div>']


def substituido(r, linhas):
    """Bloco excluído e reposto por outro bloco do mesmo caso (ex.: B04 substituído pelo B09)."""
    return r['estado'] == 'inconclusivo' and r['n_excluido'] != '0' and any(
        o is not r and o['estado'] == 'calculado' and
        (o['canal'], o['veiculo'], o['contexto'], o['rede']) == (r['canal'], r['veiculo'], r['contexto'], r['rede'])
        for o in linhas)


def painel(resultados, respostas):
    out = ['| Métrica | Portal | Aplicativo | Par de canais |', '|---|---|---|---|']
    for m, (nome, *_rest) in METRICAS.items():
        celulas = []
        for canal in ('portal', 'aplicativo', 'par'):
            todas = resultados_da_metrica(m, resultados)
            rs = [r for r in todas if r['canal'] == canal and not substituido(r, todas)]
            if not rs:
                celulas.append('')
                continue
            niveis = []
            for r in rs:
                rotulo = nivel(r['nivel'] or r['estado'])
                if len(rs) > 1:
                    detalhe = REDES.get(r['rede'], '') if m.startswith('M3.2') else r['contexto'].replace('+', ' + ')
                    if versao(r) and m.startswith('M3.1'):
                        detalhe += f' · {versao(r)}'

                    rotulo += f' <small>{detalhe}</small>'
                niveis.append(rotulo)
            celulas.append('<br>'.join(niveis))
        out.append(f'| [**{m}**, {nome}](#{ancora(m)}) | {" | ".join(celulas)} |')
    return out


def painel_questoes(respostas):
    por = defaultdict(dict)
    for r in respostas:
        por[r['id'].split('-')[0]][r['canal']] = r
    out = ['| Questão ou objetivo | Portal | Aplicativo |', '|---|---|---|']
    for g, (carac, _decisoes, qs) in OBJETIVOS.items():
        for q in qs.split():
            linhas = por[q]
            if 'par' in linhas:
                cel = [estado_gqm(linhas['par']['estado']) + ' <small>(par)</small>'] * 2
            else:
                cel = [estado_gqm(linhas[c]['estado']) if c in linhas else '—' for c in ('portal', 'aplicativo')]
            out.append(f'| [{q}, {QUESTOES[q]}](fase4-analise.md#resp-{ancora(q)}) | {cel[0]} | {cel[1]} |')
        cel = [estado_gqm(por[g][c]['estado']).replace('Atendida', 'Atendido').replace('Não atendida', 'Não atendido')
               .replace('Inconclusiva', 'Inconclusivo') for c in ('portal', 'aplicativo')]
        out.append(f'| **[{g}, {carac}](fase4-analise.md#julg-{g.lower()})** | **{cel[0]}** | **{cel[1]}** |')
    return out


def sessoes(dados, resultados):
    out = ['| Sessão | Data | Procedimentos e caso | Métricas produzidas | Ambiente | Registro e conferência |',
           '|---|---|---|---|---|---|']
    for s, (data, procs, veic, registro, leitura, capturas) in SESSOES.items():
        ms = sorted({r['metrica'] for r in resultados if r['sessao'] == s and r['estado'] == 'calculado'})
        links = ', '.join(f'[{m}](#{ancora(m)})' for m in ms)
        amb = [a for a in dados['ambientes'] if a['sessao'] == s]
        ambiente = link_linhas('ambientes', amb, f'{len(amb)} linhas de ambientes.csv' if len(amb) > 1 else '1 linha de ambientes.csv')
        reg = [arquivo_repo(registro, 'registro da sessão'), arquivo_repo(leitura, 'segunda leitura')]
        if capturas:
            reg.append(arquivo_repo(capturas, 'capturas'))
        out.append(f'| <span id="sessao-{s.lower()}"></span>**{s}** | {data} | {procs}; {veic} | {links} | {ambiente} | {", ".join(reg)} |')
    return out


def gerar():
    dados = {n: ler(n) for n in ('campos-por-infracao', 'comparacao-canais', 'fluxo', 'tempos',
                                 'volume', 'tentativas', 'desvios', 'ambientes')}
    resultados = ler('resultados-metricas', 'consolidados')
    respostas = ler('respostas-gqm', 'consolidados')
    VERSOES.update({(a['sessao'], a['contexto']): a['aplicativo_versao'] for a in dados['ambientes']})
    calculados = sum(r['estado'] == 'calculado' for r in resultados)
    linhas = [
        '<!-- Gerado por dados/scripts/gerar_medicoes.py; não editar à mão. -->',
        '# Fase 4 — Medições por métrica',
        '',
        'Esta página mostra **cada medição real** por trás das quatorze métricas. Para cada métrica há o',
        'caminho desde a Fase 1, o resultado oficial com o nível da Fase 2 e a lista das observações',
        'brutas. Cada observação tem link para a **linha exata** do CSV no GitHub e, quando existe, para',
        'a captura anonimizada e a segunda leitura independente. Os valores não são digitados: a página',
        'é gerada por [`gerar_medicoes.py`](' + REPO + '/blob/main/dados/scripts/gerar_medicoes.py) a partir',
        'de `dados/brutos/` e de [`resultados-metricas.csv`](' + REPO + '/blob/main/dados/consolidados/resultados-metricas.csv).',
        '',
        '<div class="kj-passos" markdown="1">',
        '',
        '**Como conferir um resultado em três cliques**',
        '',
        '1. No [painel](#painel), clique na métrica.',
        '2. Na seção dela, a coluna **Verificar** abre as linhas do CSV que geraram o valor e a segunda leitura.',
        '3. Em **observações**, cada linha do CSV aparece com captura, revisor e motivo de exclusão, quando houver.',
        '',
        f'Para refazer o cálculo: `python3 dados/scripts/calcular.py`. Ele lê os mesmos CSV, gera os {calculados}',
        'resultados calculados e registra o SHA-256 de cada entrada em',
        f'[`manifesto-calculo.json`]({REPO}/blob/main/dados/consolidados/manifesto-calculo.json).',
        '',
        '</div>',
        '',
        '## Painel de resultados {#painel}',
        '',
        'A Tabela 1 traz o nível de cada métrica por canal. Cada nome leva à seção com as medições.',
        'Quando um canal tem mais de um caso (contextos ou redes), cada caso aparece em uma linha da célula.',
        '',
        *painel(resultados, respostas),
        '',
        '*Tabela 1 — Nível de cada métrica por canal. Fonte: [`resultados-metricas.csv`]('
        + REPO + '/blob/main/dados/consolidados/resultados-metricas.csv); níveis da [Fase 2](fase2-metricas.md#niveis).*',
        '',
        'A Tabela 2 aplica a regra da [Fase 2](fase2-metricas.md#niveis): a questão é atendida quando todas',
        'as métricas aplicáveis atingem ao menos o nível Mínimo aceitável; o objetivo, quando todas as',
        'questões são atendidas. As justificativas estão na [análise](fase4-analise.md#respostas-questoes).',
        '',
        *painel_questoes(respostas),
        '',
        '*Tabela 2 — Respostas às questões e julgamento dos objetivos por canal. Fonte: [`respostas-gqm.csv`]('
        + REPO + '/blob/main/dados/consolidados/respostas-gqm.csv).*',
        '',
        '<ul class="kj-legenda" aria-label="Níveis de pontuação">',
        '<li>' + nivel('Excelente') + '</li><li>' + nivel('Alvo') + '</li><li>' + nivel('Mínimo aceitável') + '</li>',
        '<li>' + nivel('Inaceitável') + '</li><li>' + nivel('inconclusivo') + ' sem medição, nunca zero</li>',
        '<li>' + nivel('nao_aplicavel') + '</li>',
        '</ul>',
    ]
    for g, (carac, decisoes, qs) in OBJETIVOS.items():
        linhas += ['', f'## {g} — {carac} {{#{g.lower()}}}', '',
                   f'Questões {", ".join(f"[{q}](fase2-gqm.md#{ancora(q)})" for q in qs.split())} da '
                   f'[Fase 2](fase2-gqm.md#{g.lower()}); julgamento na [análise](fase4-analise.md#julg-{g.lower()}).']
        for m, (nome, q, *_r) in METRICAS.items():
            if m[1] != g[1]:
                continue
            res = resultados_da_metrica(m, resultados)
            linhas += ['', f'### {m} — {nome} {{#{ancora(m)}}}', '', *cadeia(m), '',
                       *tabela_resultados(m, res, dados), '',
                       f'*Resultado oficial de {m}. Fonte: `resultados-metricas.csv`, gerado por `calcular.py`.*']
            if m in NOTAS:
                linhas += ['', NOTAS[m]]
            if m in LIMITES_TEMPO:
                linhas += ['', *grafico_tempos(m, res, dados)]
            linhas += capturas_s02(m)
            linhas += observacoes(m, res, dados)
            linhas += desvios_da_metrica(m, dados)
    linhas += ['', '## Sessões de coleta {#sessoes}', '',
               'A Tabela 3 liga cada sessão às métricas que ela produziu. O piloto S01 não entra no cálculo.',
               'O cronograma planejado está em [Cronograma e bloqueios](fase3-cronograma.md).', '',
               *sessoes(dados, resultados), '',
               '*Tabela 3 — Sessões, métricas produzidas e registros. Fonte: `evidencias/fase4/` e `dados/brutos/`.*', '',
               'Originais sem tarja, vídeos e termos assinados ficam em armazenamento privado, com acesso',
               'restrito aos avaliadores; o repositório público guarda só o que foi anonimizado.', '']
    return '\n'.join(linhas)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--verificar', action='store_true', help='Falhar se a página estiver desatualizada.')
    args = parser.parse_args()
    texto = gerar()
    if args.verificar:
        if not SAIDA.exists() or SAIDA.read_text(encoding='utf-8') != texto:
            print(f'{SAIDA.relative_to(ROOT)} desatualizada: executar dados/scripts/gerar_medicoes.py', file=sys.stderr)
            return 1
        print(f'{SAIDA.relative_to(ROOT)} confere com os CSV.')
        return 0
    SAIDA.write_text(texto, encoding='utf-8')
    print(f'Gerado {SAIDA.relative_to(ROOT)}.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
