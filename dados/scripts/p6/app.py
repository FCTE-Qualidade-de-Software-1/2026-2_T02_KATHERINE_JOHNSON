"""Ajudante adb para o app Detran-DF: lê a árvore de UI e toca em elementos pelo texto."""
import re, subprocess, sys, time, xml.etree.ElementTree as ET

def adb(*a, binary=False):
    r = subprocess.run(['adb', *a], capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode(errors='replace')

def nos():
    for _ in range(3):
        try:
            adb('shell', 'uiautomator', 'dump', '/sdcard/ui.xml')
            raiz = ET.fromstring(adb('exec-out', 'cat', '/sdcard/ui.xml'))
            break
        except Exception:
            time.sleep(1)
    else:
        raise RuntimeError('uiautomator falhou')
    out = []
    for n in raiz.iter('node'):
        x1, y1, x2, y2 = map(int, re.findall(r'\d+', n.get('bounds')))
        if x2 - x1 < 3 or y2 - y1 < 3:
            continue
        out.append(dict(texto=(n.get('text') or '').strip(), desc=(n.get('content-desc') or '').strip(),
                        clicavel=n.get('clickable') == 'true', classe=n.get('class').split('.')[-1], caixa=(x1, y1, x2, y2)))
    return out

def achar(texto, lista=None, exato=False):
    for n in (lista or nos()):
        alvo = n['texto'] or n['desc']
        if (alvo == texto) if exato else alvo.startswith(texto):
            return n
    return None

def tocar(n):
    x1, y1, x2, y2 = n['caixa']
    adb('shell', 'input', 'tap', str((x1 + x2) // 2), str((y1 + y2) // 2))

def esperar(texto, limite=60, exato=False):
    """Devolve o elemento só quando aparece na mesma posição em duas leituras seguidas (tela parada)."""
    fim, anterior = time.time() + limite, None
    while time.time() < fim:
        n = achar(texto, exato=exato)
        if n and anterior and n['caixa'] == anterior['caixa']:
            return n
        anterior = n
        time.sleep(0.5)
    return None

def listar(lista=None):
    for n in (lista or nos()):
        t = n['texto'] or n['desc']
        if t or n['clicavel']:
            print('c' if n['clicavel'] else ' ', n['caixa'], n['classe'], t[:60].replace('\n', ' '))

if __name__ == '__main__':
    acao, *resto = sys.argv[1:]
    if acao == 'listar':
        listar()
    elif acao == 'tocar':
        n = achar(resto[0])
        if not n:
            sys.exit(f'não encontrado: {resto[0]}')
        tocar(n); time.sleep(float(resto[1]) if len(resto) > 1 else 3); listar()
