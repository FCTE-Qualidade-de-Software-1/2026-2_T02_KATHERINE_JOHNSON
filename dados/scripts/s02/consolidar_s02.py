"""Gera as linhas propostas de P1 (campos-por-infracao.csv) e P2 (comparacao-canais.csv) da S02 a partir dos
registros privados (dados/privado/S02/portal-campos.json e app-campos.json). Imprime só presença e
classificação; os valores ficam no arquivo privado. As linhas saem para revisão, com `revisor` vazio, e
só entram em dados/brutos/ depois da conferência.

Uso: REGISTRO=<registro da S02> python3 consolidar_s02.py campos|paridade [--velocidade]
"""
import json, os, sys
from campos import CAMPOS, CONDICIONAIS, normalizar_valor, presenca, preenchido

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
PRIV = os.path.join(RAIZ, 'dados', 'privado', 'S02')
CANAIS = {'portal': ('CT01', 'portal-campos.json', 'S02-portal'), 'aplicativo': ('CT05', 'app-campos.json', 'S02-android')}
velocidade = '--velocidade' in sys.argv
aplicaveis = CAMPOS + (CONDICIONAIS if velocidade else [])


def carregar(canal):
    return json.load(open(os.path.join(PRIV, CANAIS[canal][1]), encoding='utf-8'))


def campos():
    print('sessao,contexto,canal,veiculo,infracao,tela,campo,aplicavel,presente,acao_consulta,data_hora,evidencia,revisor')
    for canal, (ct, _, prefixo) in CANAIS.items():
        d = carregar(canal)
        for tela, chave in (('lista', 'lista'), ('detalhe', 'detalhe')):
            p = presenca(d[chave])
            hora = d[f'data_hora_{tela}']
            ev = f'evidencias/fase4/capturas/S02/{prefixo}-{"lista-infracoes-V2" if tela == "lista" else "detalhe-V2-I1"}.png'
            for c in (CAMPOS + (CONDICIONAIS if velocidade and tela == 'detalhe' else [])):
                print(f'S02,{ct},{canal},V2,V2-I1,{tela},{c},sim,{"sim" if p.get(c, (False,))[0] else "nao"},,{hora},{ev},')


def paridade():
    pt, ap = presenca(carregar('portal')['detalhe']), presenca(carregar('aplicativo')['detalhe'])
    hp, ha = carregar('portal')['data_hora_detalhe'], carregar('aplicativo')['data_hora_detalhe']
    print('sessao,veiculo,infracao,campo,aplicavel,classificacao,portal_data_hora,aplicativo_data_hora,motivo,evidencia,revisor,elegivel')
    for c in aplicaveis:
        vp = [v for v in pt.get(c, (False, []))[1] if preenchido(v)]
        va = [v for v in ap.get(c, (False, []))[1] if preenchido(v)]
        if not vp and not va:
            cl = 'ausente_ambos'
        elif not vp:
            cl = 'ausente_portal'
        elif not va:
            cl = 'ausente_aplicativo'
        else:
            # paritário se algum valor exibido num canal coincide, após normalização, com algum do outro
            cl = 'paritario' if {normalizar_valor(v) for v in vp} & {normalizar_valor(v) for v in va} else 'divergente'
        print(f'S02,V2,V2-I1,{c},sim,{cl},{hp},{ha},,{os.environ.get("REGISTRO", "evidencias/fase4/S02-registro.md")},,sim')


if __name__ == '__main__':
    {'campos': campos, 'paridade': paridade}[sys.argv[1]]()
