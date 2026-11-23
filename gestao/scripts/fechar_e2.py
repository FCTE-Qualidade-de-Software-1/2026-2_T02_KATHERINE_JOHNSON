#!/usr/bin/env python3
"""Calcula o fechamento a partir de uma consulta datada, sem acesso à rede."""
import argparse
import json
import statistics
from datetime import datetime
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MEMBROS = ('Daniel', 'Heitor', 'Hugo', 'Pedro Druck', 'Pedro Henrique', 'Philipe')
NOMES = dict(zip(MEMBROS, ('Daniel de Oliveira Lira', 'Heitor Macedo Ricardo',
    'Hugo Freitas Silva', 'Pedro Druck Montalvão Reis', 'Pedro Henrique Ferreira Xavier',
    'Philipe Amâncio Reis Caetano')))
PAPEIS = dict(zip(MEMBROS, ('Gestão, metodologia, integração e revisão da coleta',
    'GitPage, acompanhamento PSM e revisão da análise',
    'Plano, preparação da coleta, instrumentos, artigo e integração documental',
    'Coleta por contexto e ação de melhoria', 'Objetivos GQM e análise comparativa',
    'Instrumentação, coleta e análise das métricas')))


def calcular(snapshot):
    issues = snapshot['issues']
    if len({i['numero'] for i in issues}) != len(issues):
        raise ValueError('Issue duplicada')
    por_numero = {i['numero']: i for i in issues}
    corte = snapshot['corte']
    planejadas = [i for i in issues if i['prazo'] <= corte]
    fechadas = [i for i in planejadas if i['fechada_em'] and i['fechada_em'][:10] <= corte]
    com_horas = [i for i in fechadas if i['real_h'] is not None]
    estimadas = sum(Fraction(str(i['estimativa_h'])) for i in com_horas)
    reais = sum(Fraction(str(i['real_h'])) for i in com_horas)
    individuais = {m: dict(estimativa_min=Fraction(0), real_min=None, completo=False) for m in MEMBROS}
    for issue in issues:
        for m in issue['responsaveis']:
            individuais[m]['estimativa_min'] += Fraction(str(issue['estimativa_h'])) * 60 / len(issue['responsaveis'])
        # Horas coletivas não são divididas como se fossem declarações individuais.
        if issue['real_h'] is not None and len(issue['responsaveis']) == 1:
            m = issue['responsaveis'][0]
            individuais[m]['real_min'] = (individuais[m]['real_min'] or 0) + Fraction(str(issue['real_h'])) * 60
    declarados = set()
    detalhes = []
    for d in snapshot['declaracoes']:
        membro = d['integrante']
        if membro in declarados:
            raise ValueError('Declaração total duplicada para integrante')
        declarados.add(membro)
        base = sum(Fraction(str(por_numero[n]['estimativa_h'])) * 60 /
                   len(por_numero[n]['responsaveis']) for n in d['issues_estimativa']
                   if membro in por_numero[n]['responsaveis'])
        if len(set(d['issues_estimativa'])) != len(d['issues_estimativa']):
            raise ValueError('Issue duplicada na declaração')
        if base != individuais[membro]['estimativa_min']:
            raise ValueError('Declaração total deve cobrir a estimativa individual da E2')
        total = base + d['acrescimo_min']
        if total < 0 or (individuais[membro]['real_min'] or 0) > total:
            raise ValueError('Total declarado incompatível com horas já registradas')
        # A declaração é um total: substitui a soma conhecida, não a acumula.
        individuais[membro].update(real_min=total, completo=d['completo'])
        detalhes.append(dict(integrante=membro, data=d['data'], fonte=d['fonte'], metodo_estimativa=d['metodo_estimativa'],
                             escopo=d['escopo'], base_min=float(base), acrescimo_min=d['acrescimo_min'], total_min=float(total)))
    total_conhecido = sum(i['real_min'] or 0 for i in individuais.values())
    pci_completo = all(i['completo'] for i in individuais.values()) and total_conhecido > 0
    for item in individuais.values():
        item['percentual_conhecido'] = (float(item['real_min'] / total_conhecido * 100)
                                       if item['real_min'] is not None and total_conhecido else None)
        item['estimativa_min'] = float(item['estimativa_min'])
        item['real_min'] = float(item['real_min']) if item['real_min'] is not None else None
    avaliados, retrabalho, sem_revisao, esperas = [], [], [], []
    revisoes_por_membro = {}
    for pr in snapshot['prs']:
        reviews = sorted([r for r in pr['revisoes'] if r['data'][:10] <= corte], key=lambda r: r['data'])
        if not reviews:
            if pr['estado'] == 'MERGED':
                sem_revisao.append(pr['numero'])
            continue
        avaliados.append(pr['numero'])
        primeira = reviews[0]['data']
        esperas.append((datetime.fromisoformat(primeira.replace('Z', '+00:00')) -
                        datetime.fromisoformat(pr['aberto_em'].replace('Z', '+00:00'))).total_seconds() / 3600)
        if any(r['estado'] == 'CHANGES_REQUESTED' for r in reviews) or any(
                primeira < c['data'] and c['data'][:10] <= corte for c in pr['commits']):
            retrabalho.append(pr['numero'])
        for review in reviews:
            revisoes_por_membro[review['autor']] = revisoes_por_membro.get(review['autor'], 0) + 1
    return dict(corte=corte,estimativa_equipe_h=sum(i['estimativa_h'] for i in issues),
                icm=dict(concluidas=len(fechadas),planejadas=len(planejadas),
                         percentual=100*len(fechadas)/len(planejadas) if planejadas else None,
                         fechadas=[i['numero'] for i in fechadas],
                         atrasadas=[i['numero'] for i in fechadas if i['fechada_em'][:10] > i['prazo']]),
                tve=dict(issues=[i['numero'] for i in com_horas],real_h=float(reais),estimativa_h=float(estimadas),
                         percentual=float((reais-estimadas)/estimadas*100) if estimadas else None,
                         completo=len(com_horas)==len(fechadas)),
                individuais=individuais,total_conhecido_min=float(total_conhecido),pci_completo=pci_completo,
                declaracoes=detalhes,
                retrabalho=dict(avaliados=avaliados,com_retrabalho=retrabalho,sem_revisao=sem_revisao,
                                percentual=100*len(retrabalho)/len(avaliados) if avaliados else None),
                revisoes_por_login=revisoes_por_membro,
                espera_mediana_h=statistics.median(esperas) if esperas else None,
                esperas_acima_48h=sum(h>48 for h in esperas))


def lista_nomes(nomes):
    nomes = list(nomes)
    if len(nomes) <= 1:
        return ''.join(nomes)
    return ', '.join(nomes[:-1]) + ' e ' + nomes[-1]


def quantidade(n):
    return {0: 'nenhum', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis'}.get(n, str(n))


def declaracoes_texto(result):
    paragrafos = []
    for d in result['declaracoes']:
        pct = d['acrescimo_min'] / d['base_min'] * 100 if d['base_min'] else 0
        sinal = '+' if d['acrescimo_min'] >= 0 else '−'
        paragrafos += [f"**{d['integrante']}** declarou, em {d['data'][8:10]}/{d['data'][5:7]}/{d['data'][:4]}, o total individual de "
                       f"**{duracao(d['total_min'])}** na E2, contra {duracao(d['base_min'])} estimadas "
                       f"(variação individual {sinal}{numero(abs(pct))}%). Fonte: {d['fonte']} "
                       f"Estimativa-base: {d['metodo_estimativa']} Escopo: {d['escopo']}", '']
    return paragrafos


def numero(value):
    return 'Não informado' if value is None else f'{value:.2f}'.replace('.', ',')


def duracao(minutes):
    if minutes is None:
        return 'Não informado'
    rounded = round(minutes)
    return f'{rounded // 60} h {rounded % 60:02d} min'


def contribuicao(result):
    """Apêndice permitido pela #49; indicadores de gestão ficam fora do artigo."""
    lines = [r'\section{Tabela de Contribuição Individual}', r'\label{sec:contribuicao}', '',
        r'A Tabela~\ref{tab:contribuicao} resume as horas conhecidas da E2 em 23/11/2026. Declararam o total individual: ' + lista_nomes(d['integrante'] for d in result['declaracoes']) + r'; os demais registros são parciais ou ausentes. A conciliação está em \texttt{docs/gestao-fechamento-e2.md}.', '',
        r'\begin{table}[htbp]', r'\centering', r'\scriptsize',
        r'\caption{Contribuição documentada da E2 (parcial; não é o percentual final).}',
        r'\label{tab:contribuicao}', r'\begin{tabular}{P{3.1cm}P{6.0cm}P{2.2cm}}',
        r'\toprule', r'\textbf{Integrante} & \textbf{Atividades registradas / atribuídas} & \textbf{Participação conhecida} \\',
        r'\midrule']
    for m, item in result['individuais'].items():
        percentual = numero(item['percentual_conhecido']) + r'\%' if item['percentual_conhecido'] is not None else 'Não apurável'
        lines.append(NOMES[m]+' & '+PAPEIS[m]+' & '+percentual+r' \\')
    lines += [r'\bottomrule', r'\end{tabular}', r'\par\smallskip',
        r'\raggedright\scriptsize Fonte: issues da E2 e declarações individuais em 23/11/2026; os percentuais somam 100\% apenas do esforço informado.',
        r'\end{table}', '']
    return '\n'.join(lines)


def relatorio(snapshot, result, fonte='gestao/dados/fechamento-e2-2026-11-22.json'):
    nomes = lista_nomes(d['integrante'] for d in result['declaracoes'])
    parciais = sum(1 for i in result['individuais'].values() if i['real_min'] is not None and not i['completo'])
    sem_horas = sum(1 for i in result['individuais'].values() if i['real_min'] is None)
    icm, tve, dp = result['icm'], result['tve'], result['retrabalho']
    lines = ['# Fechamento documental PSM/CID da Entrega 2', '',
             f"**Consulta:** {snapshot['consultado_em']}. **Corte:** {snapshot['corte']}. "
             'A coleta prevista para 21/11 foi realizada em 22/11; não foi retrodatada.', '',
             '**Estado:** fechamento apurado com as evidências disponíveis; contribuição final e esforço '
             'global incompletos por falta de declarações dos demais integrantes. Ausência de horas não é zero.', '',
             '## Indicadores e alcance', '',
             '| Indicador | Resultado | Interpretação |', '|---|---|---|',
             f"| M-CP1 | {icm['concluidas']}/{icm['planejadas']} = {numero(icm['percentual'])}% | Vermelho; "
             f"issues fechadas {icm['fechadas']}. A #46 foi fechada com critérios empíricos pendentes e um dia de atraso |",
             f"| M-RC1 | {numero(tve['real_h'])} h / {numero(tve['estimativa_h'])} h = {numero(tve['percentual'])}% | "
             f"Amarelo, somente issues fechadas com horas {tve['issues']}; não é TVE global |",
             f"| M-RC2 | {duracao(result['total_conhecido_min'])} conhecidas; PCI final não apurável | "
             f'Declaração total de {nomes} e registros parciais de {quantidade(parciais)} {"integrante" if parciais == 1 else "integrantes"}; {quantidade(sem_horas)} sem horas informadas |',
             f"| M-DP1 | {len(dp['com_retrabalho'])}/{len(dp['avaliados'])} = {numero(dp['percentual'])}% | "
             f"Conta PR com revisão humana; PRs sem revisão excluídos: {dp['sem_revisao']}; verde não comprova revisão profunda |", '',
             '*Tabela 1 — Indicadores no corte. Fonte: consulta de issues e PRs e plano PSM/CID.*', '',
             'O ICM conta fechamento formal, sem converter critérios pendentes em entregas concluídas. '
             'Até 21/11 venciam sete issues e quatro estavam fechadas (57,14%); em 22/11 a #49 entra '
             'no denominador (50,00%). As datas de fechamento são preservadas na fonte.', '',
             f"M-DP1: avaliados {dp['avaliados']}; com retrabalho {dp['com_retrabalho']}. Inclui PRs "
             'avaliados ainda abertos e PRs de conteúdo integrados na branch da Fase 3, seguindo o alcance '
             'da coleta anterior. Bots não contam como revisão humana. Retrabalho é Changes Requested '
             'ou commit posterior à primeira revisão humana, dentro do corte.', '',
             f"Espera pela primeira revisão: mediana {numero(result['espera_mediana_h'])} h; "
             f"{result['esperas_acima_48h']} PR(s) acima de 48 h. Revisões por login: "
             ', '.join(f'{k}: {v}' for k,v in sorted(result['revisoes_por_login'].items())) + '.', '',
             '## Horas e contribuição da E2', '',
             '| Integrante | Estimativa individual | Horas conhecidas | Alcance | Participação nas horas conhecidas |',
             '|---|---|---|---|---|']
    for m, item in result['individuais'].items():
        status = 'Total individual declarado' if item['completo'] else 'Parcial' if item['real_min'] is not None else 'Não informado'
        percent = numero(item['percentual_conhecido']) + '%' if item['percentual_conhecido'] is not None else 'Não apurável'
        lines.append(f"| {m} | {duracao(item['estimativa_min'])} | {duracao(item['real_min'])} | {status} | {percent} |")
    lines += ['', '*Tabela 2 — Contribuição parcial, sem imputar zero às lacunas. Fonte: mesma consulta e declarações de ' + nomes + '.*', '',
              'O denominador da última coluna contém apenas as horas conhecidas; ele não é o esforço '
              'total da equipe e os percentuais não são o PCI final. A decisão de contribuição igual '
              'da E1 não foi estendida à E2.', '',
              *declaracoes_texto(result),
              'O planejamento no corpo da #46 identifica Hugo e Philipe, embora a lista de assignees '
              'da API contenha só Hugo. Usou-se o planejamento explícito para ratear estimativas, '
              'coerente com a tabela histórica de horas. Estimativas individuais fracionárias são '
              'mantidas sem arredondamento no cálculo; a exibição em minutos arredonda apenas ao final.', '',
              '## Resposta aos desvios', '',
              '| Evidência | Encaminhamento documentado | Responsável designado | Estado |',
              '|---|---|---|---|',
              '| ICM abaixo de 70%; coleta/análise atrasadas | Priorizar conferência de S03 e registrar limitações antes da integração da análise | Equipe da #47; Heitor revisa #48 | Proposta para confirmação no PR |',
              '| Esforço individual incompleto | Registrar totais individuais e atribuição por issue, conciliando totais sem duplicidade | Cada integrante; Daniel consolida | ' + nomes + (' declarou' if len(result['declaracoes']) == 1 else ' declararam') + ' total; demais declarações pendentes |',
              '| Tabela de contribuição ainda era da E1 | Substituir pelo retrato parcial E2; publicar final somente após todas as declarações | Integrador da #49 | Atualizada nesta branch |',
              '| Relato de falha no aplicativo | Entregar proposta de processo, ficha e matriz de regressão da #36 | Revisão designada a Daniel | Artefato entregue; revisão e eficácia pendentes |',
              '| Coleta final prevista para 21/11 sem registro | Apurar em 22/11 com data real, fontes e reprodução local | Consolidação desta entrega | Realizada; sem simular reunião da equipe |', '',
              '*Tabela 3 — Tratamento dos desvios. Fonte: indicadores e issues #36, #47, #48 e #49.*', '',
              'Esses encaminhamentos são propostas documentadas nesta revisão, não deliberações '
              'de uma reunião que não ocorreu. Não foram inventadas atas nem aprovações dos demais autores.', '',
              '## Fontes e reprodução', '',
              f'- [Consulta datada e declarações individuais](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/{fonte}).',
              '- [Cálculo e testes](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/gestao/scripts).',
              '- [Planejamento e histórico](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/gestao/plano-psm.md).', '',
              '```bash', 'python3 gestao/scripts/fechar_e2.py', 'python3 -m unittest discover -s gestao/tests -v', '```', '',
              'O script não consulta a rede nem modifica issues. Recalcula JSON, este relatório e a '
              'página de fechamento da GitPage a partir da fonte datada. Novas horas exigem nova '
              'declaração identificada; não alterar a fonte histórica para simular disponibilidade anterior.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fonte', type=Path, default=ROOT/'gestao/dados/fechamento-e2-2026-11-23-v4.json')
    args = parser.parse_args()
    snapshot = json.loads(args.fonte.read_text(encoding='utf-8'))
    result = calcular(snapshot)
    (ROOT/'gestao/dados/indicadores-e2.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    report = relatorio(snapshot,result,str(args.fonte.resolve().relative_to(ROOT)))
    for path in ('gestao/relatorio-metricas-e2.md','docs/gestao-fechamento-e2.md'):
        (ROOT/path).write_text(report,encoding='utf-8')
    (ROOT/'artigo/secoes/contribuicao.tex').write_text(contribuicao(result),encoding='utf-8')
    print('Fechamento recalculado; PCI final ' + ('disponível.' if result['pci_completo'] else 'pendente de declarações individuais.'))


if __name__ == '__main__':
    main()
