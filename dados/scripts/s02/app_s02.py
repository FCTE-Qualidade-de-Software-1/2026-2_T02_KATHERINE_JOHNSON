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
SESSAO = os.environ.get('SESSAO', 'S02')
if not re.fullmatch(r'S[0-9]{2}', SESSAO):
    raise ValueError('Código de sessão inválido')
PRIV = os.path.join(RAIZ, 'dados', 'privado', SESSAO)
os.makedirs(PRIV, mode=0o700, exist_ok=True)
os.chmod(PRIV, 0o700)
PKG = 'br.com.mesotec.detrandf'
LARGURA = int(os.environ.get('TELA_LARGURA', '1200'))
ALTURA = int(os.environ.get('TELA_ALTURA', '2670'))
ABAS_Y = int(os.environ.get('ABAS_Y', str(round(2318 * ALTURA / 2670))))
STATUS_Y = round(130 * ALTURA / 2670)
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
            raise RuntimeError('mensagem_de_erro_no_aplicativo')
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
    x = str(LARGURA // 2)
    app.adb('shell', 'input', 'swipe', x, str(round(y1 * ALTURA / 2670)),
            x, str(round(y2 * ALTURA / 2670)), '400')
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


def ate_filtro(rotulos, rolagens, card_inicio=None):
    tocar(card_inicio if card_inicio is not None else inicio(rolagens), rotulos, 'Infrações')
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
    app.adb('shell', 'input', 'tap', str(round(155 * LARGURA / 1200)), str(round(265 * ALTURA / 2670))); time.sleep(1.5)  # cabeçalho do próprio app


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
            'rotulos_detalhe': [r for r, _ in detalhe], 'privado': os.path.relpath(os.path.join(PRIV, 'app-campos.json'), RAIZ)}


def gravar(nome):
    if os.path.exists(os.path.join(PRIV, f'{nome}.mp4')):
        raise FileExistsError('Gravação já existe; use repetição diferente')
    disp = f'/sdcard/katherine-{SESSAO}-{nome}.mp4'
    p = subprocess.Popen(['adb', 'shell', 'screenrecord', '--time-limit', '120', disp])
    time.sleep(1.5)
    return p, disp, time.time()


def parar(p, disp, nome):
    p.terminate(); time.sleep(1); sh('pkill', '-INT', 'screenrecord'); time.sleep(2.5)
    local = os.path.join(PRIV, f'{nome}.mp4')
    if os.path.exists(local):
        raise FileExistsError('Gravação já existe; use repetição diferente')
    subprocess.run(['adb', 'pull', disp, local], capture_output=True, check=True, timeout=30)
    os.chmod(local, 0o600)
    sh('rm', disp)
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


def tempo_detalhe_na_lista(rep, data):
    """Repete da lista ao detalhe, sem refazer a navegação inicial a cada tentativa."""
    c = cartao(data, [])
    ponto = [(c['caixa'][0] + c['caixa'][2]) // 2, (c['caixa'][1] + c['caixa'][3]) // 2]
    antes = sh('settings', 'get', 'system', 'show_touches').strip()
    sh('settings', 'put', 'system', 'show_touches', '1')
    nome = f'tempo-app-M2.1.2-{rep}'
    p = None
    try:
        p, disp, t0 = gravar(nome)
        t_toque = tocar(c)
        esperar(lambda n: n['texto'] == 'Confira o detalhamento da infração')
        t_fim = time.time()
        time.sleep(1.5)
        video = parar(p, disp, nome)
        p = None
        fechar_detalhe()
    finally:
        if p is not None:
            parar(p, disp, nome)
        sh('settings', 'put', 'system', 'show_touches', '1' if antes == '1' else '0')
    return {'metrica': 'M2.1.2', 'repeticao': rep, 'data_hora': agora(),
            'inicio_evento': 'toque na infração', 'fim_evento': 'detalhe visível e estável',
            'ponto_toque': ponto, 'dica_tempo_s': round(t_fim - t_toque, 2), 'gravacao': video,
            'observacao': 'Dica por sondagem da interface; marcar início e fim no vídeo, com segunda leitura.'}


def lista_visivel(lista):
    """Primeira infração inteira na área útil, sem barra de status nem barra de abas."""
    return next((n for n in lista if n['clicavel'] and 'Data: ' in texto(n)
                 and n['caixa'][1] > STATUS_Y and n['caixa'][3] < ABAS_Y), None)


ROLAGEM_PID = '/data/local/tmp/katherine-rolagem.pid'


def rolagem_continua():
    """Rolagens rápidas repetidas pelo próprio aparelho, na margem esquerda (fora dos cartões).

    Começam logo após o toque, sem sondagem do computador: assim que a lista existe, a rolagem
    seguinte a traz à tela. O atraso residual é o curso de uma rolagem rápida, visível no vídeo.
    """
    x = str(round(40 * LARGURA / 1080))
    y1, y2 = str(round(1900 * ALTURA / 2340)), str(round(300 * ALTURA / 2340))
    laco = f'echo $$ > {ROLAGEM_PID}; while true; do input swipe {x} {y1} {x} {y2} 60; done'
    return subprocess.Popen(['adb', 'shell', laco], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def parar_rolagem(p):
    sh('sh', '-c', f'kill $(cat {ROLAGEM_PID}) 2>/dev/null; rm -f {ROLAGEM_PID}')
    p.terminate()


def tempo_lista(metrica, rep, bloco):
    """M2.1.1/M3.2.3: toque em Consultar até a primeira infração inteira visível.

    Com ROLAGEM=continua (padrão), a rolagem rápida contínua começa logo após o toque; com
    ROLAGEM=nenhuma, exige exibição em que a lista caiba na tela. O nome do vídeo inclui o bloco
    para não colidir com gravações anteriores (B04 da S06).
    Resultado: concluida, falha, sessao_expirada, tempo_limite ou erro_instrumento.
    """
    if not re.fullmatch(r'B[0-9]{2}', bloco) or metrica not in {'M2.1.1', 'M3.2.3'}:
        raise ValueError('bloco ou métrica inválidos')
    antes = sh('settings', 'get', 'system', 'show_touches').strip()
    sh('settings', 'put', 'system', 'show_touches', '1')
    nome = f'tempo-app-{bloco}-{metrica}-{rep}'
    p = None
    try:
        consultar = ate_filtro([], [])
        ponto = [(consultar['caixa'][0] + consultar['caixa'][2]) // 2, (consultar['caixa'][1] + consultar['caixa'][3]) // 2]
        p, disp, t0 = gravar(nome)
        t_toque = tocar(consultar)
        rolagem = rolagem_continua() if os.environ.get('ROLAGEM', 'continua') == 'continua' else None
        resultado, t_fim, diagnostico, anterior = 'concluida', None, '', None
        try:
            # Margem de 5 s para a latência da leitura; o limite de 60 s é conferido no vídeo.
            while time.time() < t_toque + LIMITE + 5:
                n = lista_visivel(ler())
                if n and anterior and n['caixa'] == anterior['caixa']:
                    t_fim = time.time()
                    break
                anterior = n
                time.sleep(0.3)
            else:
                lista = app.nos()
                foco = sh('dumpsys', 'window').split('mCurrentFocus', 1)[-1][:200]
                if PKG not in foco:
                    resultado, diagnostico = 'falha', 'aplicativo fora do primeiro plano'
                elif any(x['texto'] == 'Informação não editável' for x in lista):
                    # Tela de resultado carregada sem infração visível: conferir configuração/tela.
                    resultado, diagnostico = 'erro_instrumento', 'resultado carregado sem infração visível'
                else:
                    resultado = 'tempo_limite'
        except Expirou:
            resultado = 'sessao_expirada'
        except RuntimeError as erro:
            if str(erro) != 'mensagem_de_erro_no_aplicativo':
                raise  # leitor de interface (uiautomator) falhou: erro de instrumento, tratado pelo coletor
            resultado = 'falha'
            diagnostico = ' | '.join(texto(x) for x in app.nos() if texto(x).startswith('Ocorreu um erro'))
        finally:
            if rolagem is not None:
                parar_rolagem(rolagem)
        time.sleep(1.5)
        video = parar(p, disp, nome)
        p = None
    finally:
        if p is not None:
            parar(p, disp, nome)
        sh('settings', 'put', 'system', 'show_touches', '1' if antes == '1' else '0')
    return {'metrica': metrica, 'repeticao': rep, 'data_hora': agora(), 'resultado': resultado,
            'inicio_evento': 'toque em Consultar', 'fim_evento': 'primeira infração inteira visível e estável',
            'rolagem': os.environ.get('ROLAGEM', 'continua'),
            'ponto_toque': ponto, 'dica_tempo_s': round(t_fim - t_toque, 2) if t_fim else None,
            'dica_s_desde_inicio_gravacao': {'toque': round(t_toque - t0, 2), 'fim': round(t_fim - t0, 2) if t_fim else None},
            'diagnostico_privado': diagnostico, 'gravacao': video,
            'observacao': 'Dica por sondagem da interface; marcar início e fim no vídeo, com segunda leitura.'}


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
    card_inicio = inicio(rol)
    b0 = bytes_uid(uid)
    tocar(ate_filtro([], rol, card_inicio)); ate_resultado(rol); cartao(os.environ.get('DATA', ''), rol) if os.environ.get('DATA') else None
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
        r = {'modo': modo, 'resultado': 'falha', 'motivo': type(e).__name__, 'data_hora': agora()}
        # Mensagens do serviço podem conter dados pessoais: guardar somente no privado.
        destino = os.path.join(PRIV, 'erro-' + str(time.time_ns()) + '.json')
        with open(destino, 'w') as arquivo:
            json.dump({'tipo': type(e).__name__, 'mensagem': str(e)}, arquivo, ensure_ascii=False)
        os.chmod(destino, 0o600)
    print(json.dumps(r, ensure_ascii=False))
