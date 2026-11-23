"""Uma tentativa da P6 no app: tela inicial autenticada → Infrações → Histórico de infrações por veículo
→ veículo → infração → detalhe. Antes de salvar a captura, cobre de preto todo texto que não é rótulo
conhecido e a barra de status. Uso: BLOCO=B02 python3 tentativa_app.py <repeticao> <pasta-das-capturas>"""
import io, json, os, sys, time
from datetime import datetime, timedelta, timezone
from PIL import Image, ImageDraw
import app

ROTULOS = {'Error', 'OK', 'Ocorreu um erro ao buscar os veículos, por favor, tente novamente mais tarde.', 'Infrações', 'Histórico de infrações por veículo', 'Histórico e o detalhamento de infrações',
           'Veículos atuais de minha propriedade', 'Até o presente momento, não há registros.',
           'Veículos de minha propriedade à época da infração', 'Início', 'Credenciadas'}
VAZIO = 'Até o presente momento, não há registros.'
LIMITE = 60

def capturar(nome):
    png = app.adb('exec-out', 'screencap', '-p', binary=True)
    lista = app.nos()
    im = Image.open(io.BytesIO(png)).convert('RGB')
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, im.width, 110), fill='black')  # barra de status: hora, notificações, bateria
    n = 0
    for no in lista:
        t = no['texto']
        if t and t not in ROTULOS and not t.startswith('autuadas nos veículos'):
            d.rectangle(no['caixa'], fill='black'); n += 1
    im.save(nome)  # PIL não copia metadados da imagem original
    return n

def main():
    rep = sys.argv[1]
    brasilia = timezone(timedelta(hours=-3))
    inicio = datetime.now(brasilia).replace(microsecond=0)
    t0 = time.time()
    passos, resultado, motivo = [], 'concluida', ''
    try:
        # Nunca usa "voltar" (pode fechar o app): só confere que o app está na frente e toca na aba Início.
        if 'br.com.mesotec.detrandf' not in app.adb('shell', 'dumpsys', 'window', 'displays').split('mCurrentFocus', 1)[-1][:200]:
            raise RuntimeError('app não está em primeiro plano (tela inicial autenticada não encontrada)')
        for _ in range(3):
            if app.esperar('Infrações, ', limite=10):
                break
            aba = app.achar('Início', exato=True)
            if aba:
                app.tocar(aba); time.sleep(1.5)
        else:
            raise RuntimeError('tela inicial autenticada não encontrada')
        passos.append('inicio_autenticado')
        app.tocar(app.esperar('Infrações, ', limite=LIMITE) or (_ for _ in ()).throw(RuntimeError('cartão Infrações ausente')))
        passos.append('infracoes')
        app.tocar(app.esperar('Histórico de infrações por veículo, ', limite=LIMITE) or (_ for _ in ()).throw(RuntimeError('item do histórico ausente')))
        passos.append('historico_por_veiculo')
        # Espera a lista carregar: ou aparece veículo, ou as duas seções terminam com "não há registros".
        fim = time.time() + LIMITE
        while time.time() < fim:
            lista = app.nos()
            erro = next((n['texto'] for n in lista if n['texto'].startswith('Ocorreu um erro')), None)
            if erro:
                raise RuntimeError(f'mensagem do app: "{erro}"')
            if not any(n['texto'] == 'Histórico e o detalhamento de infrações' for n in lista):
                time.sleep(1); continue  # ainda na tela anterior ou em transição
            vazios = sum(n['texto'] == VAZIO for n in lista)
            secoes = [n for n in lista if n['texto'] in ('Veículos atuais de minha propriedade', 'Veículos de minha propriedade à época da infração')]
            outros = [n for n in lista if n['clicavel'] and n['caixa'][1] > 760 and n['caixa'][3] < 2003]
            if outros:
                raise RuntimeError('lista com veículo: caminho seguinte ainda não mapeado')
            if len(secoes) == 2 and vazios == 2:
                break
            time.sleep(1)
        else:
            raise TimeoutError
        time.sleep(3)  # nova leitura depois de 3 s, para não registrar estado intermediário de carregamento
        if sum(n['texto'] == VAZIO for n in app.nos()) == 2:
            raise RuntimeError('histórico sem veículos: "Até o presente momento, não há registros." nas duas seções')
    except TimeoutError:
        resultado, motivo = 'tempo_limite', f'60 s sem lista após {passos[-1] if passos else "início"}'
    except RuntimeError as e:
        resultado = 'erro_instrumento' if 'não mapeado' in str(e) or 'não encontrada' in str(e) else 'falha'
        motivo = f'{e} (após {passos[-1] if passos else "início"})'
    nome = f"{os.environ.get('SESSAO', 'S03')}-{os.environ.get('BLOCO', 'B02')}-aplicativo-P6-V1-{rep}-{inicio.date().isoformat()}.png"
    n = capturar(f'{sys.argv[2]}/{nome}')
    ok = app.achar('OK', exato=True)  # fecha o aviso de erro depois da captura, sem sair do app
    if ok:
        app.tocar(ok)
    print(json.dumps(dict(repeticao=rep, resultado=resultado, motivo=motivo, data_hora=inicio.isoformat(),
                          duracao_s=round(time.time() - t0, 1), passos=passos, tarjados=n, captura=nome), ensure_ascii=False))

main()
