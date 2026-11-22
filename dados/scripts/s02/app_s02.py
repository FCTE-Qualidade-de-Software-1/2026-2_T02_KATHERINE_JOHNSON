"""S02 no aplicativo (CT05, app 2.7.0 no D03): apoio a P1/P2 (campos), P3 (fluxo), P4 (tempo) e P5 (volume).
Valores pessoais, gravações e saídas completas do adb vão só para dados/privado/S02/ (fora do Git); a saída
padrão traz apenas presença, contagens, horários e bytes. Nunca usa o "voltar" do sistema nem toca em "Sair".

Uso (app aberto e logado; adb com um único aparelho):
  VEICULO_HASH=<sha256 da placa> python3 app_s02.py campos <data-da-infracao>
  VEICULO_HASH=... python3 app_s02.py fluxo <repeticao>
  VEICULO_HASH=... python3 app_s02.py tempo M2.1.1|M2.1.2 <repeticao> <data-da-infracao>
  VEICULO_HASH=... python3 app_s02.py volume <repeticao>
"""
import hashlib, io, json, os, re, subprocess, sys, time
from datetime import datetime, timedelta, timezone
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'p6'))
import app  # noqa: E402
from campos import presenca  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
PRIV = os.path.join(RAIZ, 'dados', 'privado', 'S02')
os.makedirs(PRIV, exist_ok=True)
PKG = 'br.com.mesotec.detrandf'
ABAS_Y = 2318      # topo da barra de abas no D03 (1200x2670)
STATUS_Y = 130
LIMITE = 60
PLACA = re.compile(r'^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$')
agora = lambda: datetime.now(timezone(timedelta(hours=-3))).replace(microsecond=0).isoformat()
texto = lambda n: n['texto'] or n['desc']
sh = lambda *a: subprocess.run(['adb', 'shell', *a], capture_output=True, text=True).stdout


class Expirou(Exception):
    pass


def ler():
    lista = app.nos()
    if any(n['texto'] == 'Login' for n in lista) and any(n['texto'] == 'CPF/CNPJ' for n in lista):
        raise Expirou('sessao_expirada')
    for n in lista:
        if texto(n).startswith('Ocorreu um erro'):
            raise RuntimeError(f'mensagem do app: "{texto(n)}"')
    return lista


def esperar(pred, limite=LIMITE):
    fim, anterior = time.time() + limite, None
    while time.time() < fim:
        n = next((x for x in ler() if pred(x)), None)
        if n and anterior and n['caixa'] == anterior['caixa']:
            return n
        anterior = n
        time.sleep(0.4)
    raise TimeoutError


def rolar(y1=2000, y2=900):
    app.adb('shell', 'input', 'swipe', '600', str(y1), '600', str(y2), '400')
    time.sleep(1.2)


def tocar(n, rotulos=None, rotulo=None):
    app.tocar(n)
    if rotulos is not None:
        rotulos.append(rotulo or texto(n).split(',')[0])
    return time.time()


def inicio(rolagens):
    if PKG not in sh('dumpsys', 'window').split('mCurrentFocus', 1)[-1][:200]:
        raise RuntimeError('app não está em primeiro plano')
    aba = app.achar('Início', exato=True)
    if aba:
        app.tocar(aba); time.sleep(1.5)
    for _ in range(3):
        card = next((n for n in ler() if texto(n).startswith('Infrações, ')), None)
        if card and card['caixa'][3] < ABAS_Y:
            return card
        rolar(1700, 1000); rolagens.append('tela inicial')
    raise RuntimeError('cartão Infrações não encontrado')


def veiculo(lista):
    topo = next(n for n in lista if n['texto'] == 'Veículos atuais de minha propriedade')
    base = next((n for n in lista if n['texto'].startswith('Veículos de minha propriedade à')), None)
    grupos = [n for n in lista if n['clicavel'] and n['classe'] == 'ViewGroup' and n['caixa'][1] >= topo['caixa'][3]
              and (not base or n['caixa'][3] <= base['caixa'][1])]
    h = os.environ.get('VEICULO_HASH')
    if not h:
        return grupos[int(os.environ.get('VEICULO', '1')) - 1]
    for g in grupos:
        for n in lista:
            x1, y1, x2, y2 = n['caixa']
            dentro = g['caixa'][0] <= x1 and x2 <= g['caixa'][2] and g['caixa'][1] <= y1 and y2 <= g['caixa'][3]
            if dentro and PLACA.match(n['texto']) and hashlib.sha256(n['texto'].encode()).hexdigest() == h:
                return g
    raise RuntimeError('veículo não encontrado na lista')


def ate_filtro(rotulos, rolagens):
    tocar(inicio(rolagens), rotulos, 'Infrações')
    tocar(esperar(lambda n: texto(n).startswith('Histórico de infrações por veículo, ')), rotulos, 'Histórico de infrações por veículo')
    esperar(lambda n: n['texto'] == 'Veículos atuais de minha propriedade'); time.sleep(1.5)
    tocar(veiculo(ler()), rotulos, 'veículo')
    tocar(esperar(lambda n: texto(n) == 'Selecionar'), rotulos, 'Situação da Multa: Selecionar')
    tocar(esperar(lambda n: texto(n) == 'Todas'), rotulos, 'Todas')
    time.sleep(0.8)
    return esperar(lambda n: texto(n) == 'Consultar' and n['clicavel'])


def ate_resultado(rolagens):
    """Rola a tela de resultado até 'Resultado da pesquisa'; devolve o horário em que a tela carregou."""
    fim, carregou = time.time() + LIMITE, None
    while time.time() < fim:
        lista = ler()
        if any(n['texto'] == 'Informação não editável' for n in lista) and carregou is None:
            carregou = time.time()
        if any(n['texto'] == 'Resultado da pesquisa' for n in lista):
            return carregou or time.time()
        if carregou:
            rolar(); rolagens.append('resultado')
        else:
            time.sleep(0.3)
    raise TimeoutError


def cartao(data, rolagens):
    for _ in range(6):
        c = next((n for n in ler() if n['clicavel'] and f'Data: {data}' in texto(n) and n['caixa'][3] < ABAS_Y), None)
        if c:
            return c
        rolar(2000, 1200); rolagens.append('resultado')
    raise RuntimeError('infração de referência não listada')


def capturar(arquivo, rotulos_ok):
    png = app.adb('exec-out', 'screencap', '-p', binary=True); lista = app.nos()
    im = Image.open(io.BytesIO(png)).convert('RGB'); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, im.width, STATUS_Y), fill='black')
    for n in lista:
        if n['texto'] and n['texto'] not in rotulos_ok:
            d.rectangle(n['caixa'], fill='black')
    im.save(arquivo)


ROTULOS_TELA = {'Infrações', 'Resultado da pesquisa', 'Informação não editável', 'Confira o detalhamento da infração',
                'Dados do Veículo', 'Informações gerais', 'Dados da Infração', 'Penalidade aplicada', 'Início', 'Credenciadas',
                'Avaliar Serviço', 'CPF', 'Placa', 'Data início', 'Data final', 'Situação', 'Pontuação'}


def pares_detalhe():
    """Lê os pares rótulo/valor do detalhe, rolando até não aparecer rótulo novo."""
    vistos, ordem = {}, []
    for _ in range(12):
        novos = 0
        for n in ler():
            if n['classe'] == 'ViewGroup' and ', ' in n['desc'] and not n['clicavel']:
                r, v = n['desc'].split(', ', 1)
                if r not in vistos:
                    vistos[r] = v; ordem.append(r); novos += 1
        if not novos and ordem:
            break
        rolar(2200, 900)
    for _ in range(12):  # volta ao topo do detalhe
        app.adb('shell', 'input', 'swipe', '600', '900', '600', '2200', '300')
        if any(n['texto'] == 'Confira o detalhamento da infração' for n in app.nos()):
            break
    return [[r, vistos[r]] for r in ordem]


def fechar_detalhe():
    app.adb('shell', 'input', 'tap', '155', '265'); time.sleep(1.5)  # cabeçalho do próprio app


def campos(data):
    rot, rol = [], []
    tocar(ate_filtro(rot, rol)); ate_resultado(rol)
    c = cartao(data, rol); h_lista = agora()
    linhas = [l for l in texto(c).split(', ') if ': ' in l]
    lista = [l.split(': ', 1) for l in linhas]
    nomes = {r for r, _ in lista}
    capturar(os.path.join(PRIV, 'S02-android-lista-infracoes-V2.png'), ROTULOS_TELA)
    tocar(c); esperar(lambda n: n['texto'] == 'Confira o detalhamento da infração'); time.sleep(1.5)
    h_det = agora()
    detalhe = pares_detalhe()
    capturar(os.path.join(PRIV, 'S02-android-detalhe-V2-I1.png'), ROTULOS_TELA | {r for r, _ in detalhe})
    fechar_detalhe()
    json.dump({'data_hora_lista': h_lista, 'data_hora_detalhe': h_det, 'lista': lista, 'detalhe': detalhe},
              open(os.path.join(PRIV, 'app-campos.json'), 'w'), ensure_ascii=False, indent=1)
    return {'data_hora_lista': h_lista, 'data_hora_detalhe': h_det, 'rotulos_lista': sorted(nomes),
            'rotulos_detalhe': [r for r, _ in detalhe], 'privado': 'dados/privado/S02/app-campos.json'}


def gravar(nome):
    disp = f'/sdcard/{nome}.mp4'
    p = subprocess.Popen(['adb', 'shell', 'screenrecord', '--time-limit', '120', disp])
    time.sleep(1.5)
    return p, disp, time.time()


def parar(p, disp, nome):
    p.terminate(); time.sleep(1); sh('pkill', '-INT', 'screenrecord'); time.sleep(2.5)
    local = os.path.join(PRIV, f'{nome}.mp4')
    subprocess.run(['adb', 'pull', disp, local], capture_output=True); sh('rm', disp)
    return os.path.relpath(local, RAIZ)


def fluxo(rep):
    toques_antes = sh('settings', 'get', 'system', 'show_touches').strip()
    sh('settings', 'put', 'system', 'show_touches', '1')
    rot, rol = [], []
    nome = f'fluxo-app-{rep}'
    try:
        p, disp, t0 = gravar(nome)
        tocar(ate_filtro(rot, rol), rot, 'Consultar'); ate_resultado(rol); cartao(os.environ.get('DATA', ''), rol) if os.environ.get('DATA') else None
        time.sleep(1.5)
        video = parar(p, disp, nome)
    finally:
        sh('settings', 'put', 'system', 'show_touches', '1' if toques_antes == '1' else '0')
    return {'repeticao': rep, 'data_hora': agora(), 'passos': len(rot), 'sequencia': ' > '.join(rot),
            'rolagens': len(rol), 'gravacao': video,
            'observacao': 'transições: contar na gravação (troca do conteúdo principal)'}


def tempo(metrica, rep, data):
    toques_antes = sh('settings', 'get', 'system', 'show_touches').strip()
    sh('settings', 'put', 'system', 'show_touches', '1')
    rol = []
    nome = f'tempo-app-{metrica}-{rep}'
    try:
        consultar = ate_filtro([], rol)
        if metrica == 'M2.1.1':
            p, disp, t0 = gravar(nome)
            t_toque = tocar(consultar); t_fim = ate_resultado(rol); time.sleep(1.5)
            evento = ('toque em Consultar', 'tela de resultado carregada')
        else:
            tocar(consultar); ate_resultado(rol); c = cartao(data, rol)
            p, disp, t0 = gravar(nome)
            t_toque = tocar(c); esperar(lambda n: n['texto'] == 'Confira o detalhamento da infração'); t_fim = time.time(); time.sleep(1.5)
            evento = ('toque na infração', '"Confira o detalhamento da infração" visível')
        video = parar(p, disp, nome)
        if metrica == 'M2.1.2':
            fechar_detalhe()
    finally:
        sh('settings', 'put', 'system', 'show_touches', '1' if toques_antes == '1' else '0')
    return {'metrica': metrica, 'repeticao': rep, 'data_hora': agora(), 'inicio_evento': evento[0], 'fim_evento': evento[1],
            'dica_s_desde_inicio_gravacao': {'toque': round(t_toque - t0, 2), 'fim': round(t_fim - t0, 2)},
            'dica_tempo_s': round(t_fim - t_toque, 2), 'gravacao': video,
            'observacao': 'quadros inicial e final marcados na gravação (indicador de toque e tela completa); a dica é só apoio'}


def bytes_uid(uid):
    sh('dumpsys', 'netstats', '--poll'); time.sleep(1)
    tot, dentro = 0, False
    for l in sh('dumpsys', 'netstats', 'detail').splitlines():
        if 'uid=' in l and 'set=' in l:
            dentro = f'uid={uid} ' in l and 'tag=0x0' in l
        elif dentro:
            m = re.search(r'rb=(\d+).*tb=(\d+)', l)
            if m:
                tot += int(m.group(1)) + int(m.group(2))
    return tot


def volume(rep):
    uid = re.search(r'uid:(\d+)', subprocess.run(['adb', 'shell', 'pm', 'list', 'packages', '-U', PKG], capture_output=True, text=True).stdout).group(1)
    rol = []
    inicio(rol)
    b0 = bytes_uid(uid)
    tocar(ate_filtro([], rol)); ate_resultado(rol); cartao(os.environ.get('DATA', ''), rol) if os.environ.get('DATA') else None
    time.sleep(3)
    b1 = bytes_uid(uid)
    return {'repeticao': rep, 'data_hora': agora(), 'instrumento': 'adb dumpsys netstats detail (UID do pacote, tag 0x0)',
            'bytes_iniciais': b0, 'bytes_finais': b1, 'bytes_transferidos': b1 - b0,
            'escopo': 'da abertura do grupo Infrações até a lista completa (mesmo intervalo do P3)'}


if __name__ == '__main__':
    modo, *args = sys.argv[1:]
    try:
        r = {'campos': lambda: campos(*args), 'fluxo': lambda: fluxo(*args), 'tempo': lambda: tempo(*args),
             'volume': lambda: volume(*args)}[modo]()
        r['resultado'] = 'concluida'
    except Expirou:
        r = {'modo': modo, 'resultado': 'sessao_expirada', 'data_hora': agora()}
    except TimeoutError:
        r = {'modo': modo, 'resultado': 'tempo_limite', 'data_hora': agora()}
    except Exception as e:  # noqa: BLE001
        r = {'modo': modo, 'resultado': 'falha', 'motivo': str(e), 'data_hora': agora()}
    print(json.dumps(r, ensure_ascii=False))
