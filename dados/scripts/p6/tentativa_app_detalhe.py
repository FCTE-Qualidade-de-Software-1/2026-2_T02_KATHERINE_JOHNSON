"""Uma tentativa da P6 no app 2.7.0 até o detalhe da infração (S05, B01; desvio D010).

Caminho: Início (rolagem, porque no D03 o cartão fica atrás da barra de abas) → Infrações →
Histórico de infrações por veículo → veículo → Situação da Multa "Todas" → Consultar → cartão da
infração com a data informada → detalhe. Antes de salvar a captura, cobre de preto a barra de status
e todo texto que não é rótulo conhecido. Depois da captura, fecha o detalhe pelo cabeçalho do app
(nunca usa o "voltar" do sistema). Não digita credenciais nem toca em "Sair".

Uso: SESSAO=S05 BLOCO=B01 VEIC=V2 VEICULO=1 python tentativa_app_detalhe.py <repeticao> <pasta-das-capturas> <data-da-infracao>
A data (dd/mm/aaaa) é argumento: não registrá-la no repositório.
"""
import io, json, os, sys, time
from datetime import datetime, timedelta, timezone
from PIL import Image, ImageDraw
import app

LIMITE = 60
ABAS_Y = 2318          # topo da barra de abas no D03 (1200x2670)
STATUS_Y = 130         # barra de status do D03
ROTULOS = {
    'Confira o detalhamento da infração', 'Dados do Veículo', 'Placa', 'UF', 'Marca/Modelo',
    'Informações gerais', 'Situação da Multa', 'Auto da Infração', 'Código RENAINF',
    'Error', 'OK', 'Infrações', 'Histórico de infrações por veículo', 'Resultado da pesquisa',
    'Ocorreu um erro ao buscar os veículos, por favor, tente novamente mais tarde.',
    'Até o presente momento, não há registros.', 'Início', 'Credenciadas',
}


class Falha(Exception):
    """Falha do serviço (entra no denominador)."""


class Instrumento(Exception):
    """Elemento esperado não encontrado: erro do instrumento."""


def texto(n):
    return n['texto'] or n['desc']


def checar_servico(lista):
    for n in lista:
        t = texto(n)
        if t.startswith('Ocorreu um erro'):
            raise Falha(f'mensagem do app: "{t}"')
    if any(n['texto'] == 'Login' for n in lista) and any(n['texto'] == 'CPF/CNPJ' for n in lista):
        raise Falha('sessao_expirada: app voltou para a tela de login')


def esperar(pred, descricao, limite=LIMITE):
    """Espera um elemento que satisfaça pred e esteja parado em duas leituras seguidas."""
    fim, anterior = time.time() + limite, None
    while time.time() < fim:
        lista = app.nos()
        checar_servico(lista)
        n = next((x for x in lista if pred(x)), None)
        if n and anterior and n['caixa'] == anterior['caixa']:
            return n
        anterior = n
        time.sleep(0.5)
    raise TimeoutError(descricao)


def rolar():
    app.adb('shell', 'input', 'swipe', '600', '2000', '600', '900', '400')
    time.sleep(1.5)


def ir_para_inicio():
    for _ in range(3):
        aba = app.achar('Início', exato=True)
        if aba:
            app.tocar(aba)
            time.sleep(1.5)
        for _ in range(3):
            lista = app.nos()
            checar_servico(lista)
            card = next((n for n in lista if texto(n).startswith('Infrações, ')), None)
            if card and card['caixa'][3] < ABAS_Y:
                return card
            if any(texto(n).startswith('Consultar veículo') for n in lista):
                rolar()
            else:
                break
    raise Instrumento('tela inicial autenticada não encontrada')


def capturar(nome):
    png = app.adb('exec-out', 'screencap', '-p', binary=True)
    lista = app.nos()
    im = Image.open(io.BytesIO(png)).convert('RGB')
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, im.width, STATUS_Y), fill='black')
    n = 0
    for no in lista:
        t = no['texto']
        if t and t not in ROTULOS:
            d.rectangle(no['caixa'], fill='black')
            n += 1
    im.save(nome)  # PIL não copia metadados da imagem original
    return n


def main():
    rep, pasta, data = sys.argv[1], sys.argv[2], sys.argv[3]
    indice = int(os.environ.get('VEICULO', '1')) - 1
    brasilia = timezone(timedelta(hours=-3))
    inicio = datetime.now(brasilia).replace(microsecond=0)
    t0 = time.time()
    passos, resultado, motivo, detalhe = [], 'concluida', '', False
    try:
        foco = app.adb('shell', 'dumpsys', 'window').split('mCurrentFocus', 1)[-1][:200]
        if 'br.com.mesotec.detrandf' not in foco:
            raise Instrumento('app não está em primeiro plano')
        app.tocar(ir_para_inicio())
        passos.append('inicio_autenticado')
        app.tocar(esperar(lambda n: texto(n).startswith('Histórico de infrações por veículo, '), 'item do histórico'))
        passos.append('infracoes')

        def veiculos():
            fim = time.time() + LIMITE
            while time.time() < fim:
                lista = app.nos()
                checar_servico(lista)
                topo = next((n for n in lista if n['texto'] == 'Veículos atuais de minha propriedade'), None)
                base = next((n for n in lista if n['texto'] == 'Veículos de minha propriedade à época da infração'), None)
                if topo and base:
                    v = [n for n in lista if n['clicavel'] and n['classe'] == 'ViewGroup'
                         and n['caixa'][1] >= topo['caixa'][3] and n['caixa'][3] <= base['caixa'][1]]
                    if v:
                        return v
                time.sleep(1)
            raise TimeoutError('lista de veículos')
        v = veiculos()
        passos.append('historico_por_veiculo')
        if indice >= len(v):
            raise Falha(f'lista com {len(v)} veículo(s); veículo {indice + 1} ausente')
        time.sleep(1)
        v = veiculos()
        app.tocar(v[indice])
        app.tocar(esperar(lambda n: texto(n) == 'Selecionar', 'filtro Situação'))
        app.tocar(esperar(lambda n: texto(n) == 'Todas', 'opção Todas'))
        time.sleep(1)
        app.tocar(esperar(lambda n: texto(n) == 'Consultar' and n['clicavel'], 'botão Consultar'))
        passos.append('filtro')
        fim = time.time() + LIMITE
        while True:
            if time.time() > fim:
                raise TimeoutError('resultado da pesquisa')
            lista = app.nos()
            checar_servico(lista)
            if any(n['texto'] == 'Resultado da pesquisa' for n in lista):
                break
            if any(n['texto'] == 'Informação não editável' for n in lista):
                rolar()  # tela de resultado carregada: a lista fica abaixo dos dados da consulta
            else:
                time.sleep(1)
        alvo = f'Data: {data}'
        card = None
        for _ in range(6):
            lista = app.nos()
            checar_servico(lista)
            card = next((n for n in lista if n['clicavel'] and alvo in texto(n)), None)
            if not card:
                linha = next((n for n in lista if n['texto'] == alvo), None)
                if linha:
                    card = next((n for n in lista if n['clicavel'] and n['caixa'][1] <= linha['caixa'][1] <= n['caixa'][3]), None)
            if card and card['caixa'][3] < ABAS_Y:
                break
            card = None
            rolar()
        if not card:
            raise Falha('infração de referência não listada no resultado')
        passos.append('lista_infracoes')
        app.tocar(card)
        esperar(lambda n: n['texto'] == 'Confira o detalhamento da infração', 'detalhe da infração')
        detalhe = True
        passos.append('detalhe')
    except TimeoutError as e:
        resultado, motivo = 'tempo_limite', f'{LIMITE} s sem {e} após {passos[-1] if passos else "início"}'
    except Falha as e:
        if str(e).startswith('sessao_expirada'):
            resultado = 'sessao_expirada'
        else:
            resultado = 'falha'
        motivo = f'{e} (após {passos[-1] if passos else "início"})'
    except (Instrumento, Exception) as e:
        resultado, motivo = 'erro_instrumento', f'{type(e).__name__}: {e} (após {passos[-1] if passos else "início"})'
    duracao = round(time.time() - t0, 1)
    nome = (f"{os.environ.get('SESSAO', 'S05')}-{os.environ.get('BLOCO', 'B01')}-aplicativo-P6-"
            f"{os.environ.get('VEIC', 'V2')}-{rep}-{inicio.date().isoformat()}.png")
    n = capturar(os.path.join(pasta, nome))
    ok = app.achar('OK', exato=True)  # fecha aviso de erro, sem sair do app
    if ok:
        app.tocar(ok)
    if detalhe:  # fecha o detalhe pelo cabeçalho do próprio app
        app.adb('shell', 'input', 'tap', '155', '265')
        time.sleep(2)
    print(json.dumps(dict(repeticao=rep, resultado=resultado, motivo=motivo, data_hora=inicio.isoformat(),
                          duracao_s=duracao, passos=passos, tarjados=n, captura=nome), ensure_ascii=False))


main()
