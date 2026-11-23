"""Publica só campos permitidos do caso V4 (S06–S08); mantém a revisão humana pendente."""
import csv
import importlib.util
import json
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
PRIV = RAIZ / 'dados/privado/S02/V4'
EVIDENCIA = 'evidencias/fase4/S06-registro-2026-11-22.md'
# S08: P7 do portal (Wi-Fi, rede degradada e 4G). Os blocos do app no P7 só entram se executados.
EVIDENCIAS = {'S06': EVIDENCIA, 'S08': 'evidencias/fase4/S08-registro-2026-11-22.md'}
# B09 refaz a lista do app com rolagem rápida contínua iniciada no toque (sem sondagem antes de rolar).
TEMPO_APP = [('S06', 'B04', 'M2.1.1'), ('S06', 'B06', 'M2.1.2'), ('S06', 'B09', 'M2.1.1')]
# B04: lista abaixo da tela e esperas do instrumento para rolar; as gravações ficam preservadas.
EXCLUIDOS = {('S06', 'B04')}
P7 = [('B10', 'portal', 'wifi'), ('B11', 'aplicativo', 'wifi'), ('B12', 'portal', 'degradada'),
      ('B13', 'aplicativo', 'degradada'), ('B14', 'portal', '4g'), ('B15', 'aplicativo', '4g')]
SERVICO = {'concluida', 'falha', 'sessao_expirada', 'tempo_limite'}
SPEC = importlib.util.spec_from_file_location('calcular_v4', RAIZ / 'dados/scripts/calcular.py')
calc = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(calc)


def ler(path):
    return json.loads(path.read_text())


def base(nome, **valores):
    row = {k: '' for k in calc.SCHEMAS[nome].split(',')}
    row.update(sessao='S06', rede='wifi', veiculo='V4', evidencia=EVIDENCIA)
    row.update(valores)
    row['evidencia'] = EVIDENCIAS[row['sessao']]
    if 'revisor' in row:
        row['revisor'] = ''
    return {k: str(v) for k, v in row.items() if k in calc.SCHEMAS[nome].split(',')}


def gravar(nome, novos):
    path = RAIZ / 'dados/brutos' / (nome + '.csv')
    with path.open(newline='') as arquivo:
        anteriores = list(csv.DictReader(arquivo))
    if any(r.get('sessao') in EVIDENCIAS and r.get('revisor') for r in anteriores):
        raise ValueError('Há conferência humana registrada; não sobrescrever')
    manter = [r for r in anteriores if r.get('sessao') not in EVIDENCIAS]
    with path.open('w', newline='') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=calc.SCHEMAS[nome].split(','), lineterminator='\n')
        writer.writeheader()
        writer.writerows(manter + novos)


def main():
    volumes, tempos, tentativas = [], [], []
    for p in sorted(PRIV.glob('P5-portal-[0-9][0-9].json')):
        r = ler(p)
        volumes.append(base('volume', bloco='B07', contexto='CT01', canal='portal',
            repeticao=int(p.stem[-2:]), aquecimento='sim' if r['aquecimento'] else 'nao',
            instrumento='CDP Network.loadingFinished encodedDataLength',
            bytes_transferidos=r['bytes_transferidos'], mb=r['bytes_transferidos']/1_000_000,
            elegivel='sim', motivo='Leitura automática; conferência independente pendente', data_hora=r['data_hora']))
    for p in sorted(PRIV.glob('B08-[0-9][0-9].json')):
        r = ler(p)
        if r.get('resultado') != 'concluida':
            continue
        volumes.append(base('volume', bloco='B08', contexto='CT05', canal='aplicativo',
            repeticao=r['repeticao'], aquecimento='sim' if r['aquecimento'] else 'nao',
            instrumento='adb dumpsys netstats detail por UID; recebidos + enviados',
            bytes_iniciais=r['bytes_iniciais'], bytes_finais=r['bytes_finais'],
            bytes_transferidos=r['bytes_transferidos'], mb=r['bytes_transferidos']/1_000_000,
            elegivel='sim', motivo='Escopo difere do portal; conferência independente pendente', data_hora=r['data_hora']))
    for metrica, prefixo, bloco in [('M2.1.1','P4-portal-lista','B03'), ('M2.1.2','P4-portal-detalhe','B05')]:
        for p in sorted(PRIV.glob(prefixo + '-[0-9][0-9].json')):
            r = ler(p)
            proposta = p.with_name(p.stem + '-marcacao-proposta.json')
            if not proposta.exists():
                continue
            m = ler(proposta)
            tempos.append(base('tempos', bloco=bloco, contexto='CT01', canal='portal',
                infracao='V4-I1', metrica=metrica, repeticao=int(p.stem[-2:]),
                aquecimento='sim' if r['aquecimento'] else 'nao', inicio_s=m['inicio_s_proposto'],
                fim_s=m['fim_s_proposto'], tempo_s=m['tempo_s_proposto'], resultado='concluida',
                elegivel='sim', motivo='Marcação automática provisória; conferir vídeo e segunda leitura', data_hora=r['data_hora']))
    for sessao, bloco, metrica in TEMPO_APP:
        for p in sorted(PRIV.glob(bloco + '-[0-9][0-9].json')):
            r = ler(p)
            if r.get('resultado') != 'concluida':
                tempos.append(base('tempos', sessao=sessao, bloco=bloco, contexto='CT05', canal='aplicativo',
                    infracao='V4-I1', metrica=metrica, repeticao=r['repeticao'], aquecimento='nao',
                    resultado='erro_instrumento', elegivel='nao',
                    motivo='Instrumento interrompido durante preparação; preservado, com reposição em novo número',
                    data_hora=r['inicio_execucao']))
                continue
            video = RAIZ / r['gravacao']
            proposta = video.with_suffix('.marcacao-proposta.json')
            if not proposta.exists():
                if sessao != 'S06':
                    raise ValueError('proposta de marcação ausente para ' + p.name)
                continue
            m = ler(proposta)
            tempos.append(base('tempos', sessao=sessao, bloco=bloco, contexto='CT05', canal='aplicativo',
                infracao='V4-I1', metrica=metrica, repeticao=r['repeticao'],
                aquecimento='sim' if r['aquecimento'] else 'nao', inicio_s=m['inicio_s_proposto'],
                fim_s=m['fim_s_proposto'], tempo_s=m['tempo_s_proposto'], resultado='concluida',
                elegivel='sim', motivo='Proposta automática pendente de marcação visual'
                + ('; rolagem rápida contínua desde o toque, fim inclui o curso de uma rolagem' if r.get('rolagem') == 'continua' else ''),
                data_hora=r['data_hora']))
    for row in tempos:
        if (row['sessao'], row['bloco']) in EXCLUIDOS and row['resultado'] == 'concluida':
            row.update(elegivel='nao', inicio_s='', fim_s='', tempo_s='',
                       motivo='Intervalo não validado: lista fora da tela e esperas do instrumento para rolar; não usar como tempo de resposta')
    for bloco, canal, rede in P7:
        contexto = 'CT01' if canal == 'portal' else 'CT05'
        for p in sorted(PRIV.glob(bloco + '-[0-9][0-9].json')):
            r = ler(p)
            resultado = r.get('resultado')
            comum = dict(sessao='S08', bloco=bloco, contexto=contexto, canal=canal, rede=rede,
                         repeticao=int(p.stem[-2:]), aquecimento='sim' if r.get('aquecimento') else 'nao',
                         data_hora=r.get('data_hora') or r['inicio_execucao'])
            tempo = dict(infracao='V4-I1', metrica='M3.2.3')
            if resultado not in SERVICO:
                comum['aquecimento'] = 'nao'  # o aquecimento é a primeira tentativa que conta
                motivo = 'Erro de instrumento preservado; reposição em novo número'
                tentativas.append(base('tentativas', **comum, procedimento='P7', resultado='erro_instrumento', elegivel='nao', motivo=motivo))
                tempos.append(base('tempos', **comum, **tempo, resultado='erro_instrumento', elegivel='nao', motivo=motivo))
                continue
            marcas = {}
            if resultado == 'concluida':
                proposta = (p.with_name(p.stem + '-marcacao-proposta.json') if canal == 'portal'
                            else (RAIZ / r['gravacao']).with_suffix('.marcacao-proposta.json'))
                if not proposta.exists():
                    raise ValueError('proposta de marcação ausente para ' + p.name)
                m = ler(proposta)
                if m['tempo_s_proposto'] > 60:
                    resultado = 'tempo_limite'
                else:
                    marcas = dict(inicio_s=m['inicio_s_proposto'], fim_s=m['fim_s_proposto'], tempo_s=m['tempo_s_proposto'])
            motivo = {'concluida': 'Marcação automática provisória; conferir vídeo e segunda leitura'
                      + ('; rolagem rápida contínua desde o toque' if r.get('rolagem') == 'continua' else ''),
                      'falha': 'Falha do serviço' + (' na preparação, antes de Consultar' if r.get('etapa') == 'preparacao' else '')
                               + '; mensagem no registro privado; mantida no denominador',
                      'sessao_expirada': 'Sessão expirada; mantida no denominador',
                      'tempo_limite': 'Lista não exibida em 60 s após Consultar; mantida no denominador'}[resultado]
            tentativas.append(base('tentativas', **comum, procedimento='P7', resultado=resultado, elegivel='sim', motivo=motivo))
            tempos.append(base('tempos', **comum, **tempo, **marcas, resultado=resultado, elegivel='sim', motivo=motivo))
    ambientes = []
    portal = ler(PRIV / 'ambiente-portal.json')
    viewport = ler(PRIV / 'viewport-portal.json')
    app = ler(PRIV / 'ambiente-app.json')
    data_portal = datetime.fromtimestamp((PRIV / 'ambiente-portal.json').stat().st_mtime).astimezone().isoformat(timespec='seconds')
    data_app = datetime.fromtimestamp((PRIV / 'ambiente-app.json').stat().st_mtime).astimezone().isoformat(timespec='seconds')
    ambientes.append(base('ambientes', contexto='CT01', canal='portal', dispositivo='D06',
        modelo=portal['modelo'], cpu=portal['cpu'], ram_gb=portal['ram_gb'],
        so_build=portal['so'] + '; kernel ' + portal['kernel'], navegador_versao=portal['navegador'],
        aplicativo_versao='nao_se_aplica',
        resolucao=f"{viewport['largura']}x{viewport['altura']} CSS; DPR {viewport['dpr']}",
        gravador_versao='puppeteer-core 24.43.1; CDP screencast com timestamps; taxa variável',
        configuracao_rede='Wi-Fi corrente sem limitação; carga externa não controlada; velocidade não aferida',
        data_hora=data_portal))
    ambientes.append(base('ambientes', contexto='CT05', canal='aplicativo', dispositivo='D05',
        modelo=app['modelo'], cpu=app['cpu'], ram_gb=app['ram_gb'],
        so_build='Android ' + app['so'] + '; ' + app['build'], navegador_versao='nao_se_aplica',
        aplicativo_versao='br.com.mesotec.detrandf ' + app['versao_app'], resolucao=app['resolucao'],
        gravador_versao='adb 37.0.1; screenrecord com Mostrar toques; timestamps por quadro (taxa variável)',
        configuracao_rede='Wi-Fi corrente sem limitação; carga externa não controlada; velocidade não aferida',
        data_hora=data_app))
    # Configurações novas (S08) partem do inventário da S06 e trocam só os campos permitidos.
    for extra in sorted(PRIV.glob('ambiente-extra-*.json')):
        r = ler(extra)
        modelo_linha = ambientes[0] if r['canal'] == 'portal' else ambientes[1]
        linha = dict(modelo_linha)
        linha.update({k: str(v) for k, v in r.items() if k in calc.SCHEMAS['ambientes'].split(',')})
        linha['evidencia'] = EVIDENCIAS[linha['sessao']]
        ambientes.append(linha)
    gravar('ambientes', ambientes)
    # A lista explícita de campos impede copiar nomes, placas, datas de infração ou URLs.
    gravar('volume', volumes)
    gravar('tempos', tempos)
    gravar('tentativas', tentativas)
    print(json.dumps({'sessao':'S06','caso':'V4','linhas_volume':len(volumes),'linhas_tempos':len(tempos),'linhas_tentativas':len(tentativas),
                      'estado':'primeira_leitura_automatica_conferencia_humana_pendente'}))


if __name__ == '__main__':
    main()
