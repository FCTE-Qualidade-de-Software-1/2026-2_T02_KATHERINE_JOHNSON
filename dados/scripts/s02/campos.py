"""Mapa dos rótulos exibidos para os campos R01–R15 e as velocidades (fase1-produto.md, Tabela da lista
de referência), comum ao portal e ao aplicativo. Usado pelos scripts da S02 para P1 e P2."""
import re
import unicodedata

CAMPOS = [f'R{i:02}' for i in range(1, 16)]
CONDICIONAIS = ['velocidade_permitida', 'velocidade_aferida']

# Cada padrão é testado no rótulo normalizado (minúsculas, sem acento, sem "(km/h)" e sem dois-pontos).
PADROES = [
    ('R01', r'^descricao( da infracao)?$'),
    ('R02', r'^regulamento$'),
    ('R03', r'^local( da infracao)?$'),
    ('R04', r'^data( da)?( infracao)?$'),
    ('R05', r'^hora( da)?( infracao)?$'),
    ('R06', r'^placa$'),
    ('R07', r'^marca/modelo$'),
    ('R08', r'^orgao autuador$'),
    ('R09', r'^auto( da)?( infracao)?$'),
    ('R10', r'^natureza$'),
    ('R11', r'^pontuacao'),
    ('R12', r'^valor (da multa|devido)$'),
    ('R13', r'^(data de )?vencimento$'),
    ('R14', r'(defesa previa|condutor infrator)'),
    ('R15', r'^situacao (pagamento|multa|da multa|do pagamento)$'),
    ('velocidade_permitida', r'^velocidade permitida$'),
    ('velocidade_aferida', r'^velocidade aferida$'),
]


def normalizar(texto):
    t = unicodedata.normalize('NFKD', texto or '').encode('ascii', 'ignore').decode().lower()
    t = re.sub(r'\(km/h\)', '', t).replace(':', ' ')
    return re.sub(r'\s+', ' ', t).strip()


def campo_do_rotulo(rotulo):
    r = normalizar(rotulo)
    for campo, padrao in PADROES:
        if re.search(padrao, r):
            return campo
    return None


def preenchido(valor):
    """Campo com rótulo e sem valor conta como não exibido (P1). Hífen sozinho também."""
    v = (valor or '').strip()
    return bool(v) and v not in {'-', '--', '—'}


def presenca(pares):
    """pares: lista (rótulo, valor). Devolve {campo: (presente, valores)}; vários rótulos podem mapear no
    mesmo campo (ex.: R12 = Valor da Multa ou Valor Devido) e basta um preenchido."""
    out = {}
    for rotulo, valor in pares:
        c = campo_do_rotulo(rotulo)
        if not c:
            continue
        p, vs = out.get(c, (False, []))
        out[c] = (p or preenchido(valor), vs + [valor])
    return out


def normalizar_valor(v):
    """Normalização da M1.2.1: maiúsculas, acentos, símbolo monetário, separador decimal e formato de data
    não contam como divergência."""
    t = normalizar(v).replace('r$', '').replace(' ', '')
    if re.fullmatch(r'\d{1,3}(\.\d{3})*,\d+', t):   # 1.234,56 (formato brasileiro)
        t = t.replace('.', '').replace(',', '.')
    elif re.fullmatch(r'\d+,\d+', t):                # 130,16
        t = t.replace(',', '.')
    m = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2})', t)
    if m:
        t = f'{m.group(3)}/{m.group(2)}/{m.group(1)}'
    t = re.sub(r'^(\d{2})(\d{2})$', r'\1:\2', t)  # hora 1458 -> 14:58
    return t.lstrip('0') or t
