#!/usr/bin/env python3
"""Verificações mecânicas da revisão final do artigo (issue de revisão e padronização).

Uso, na raiz do repositório:  python3 artigo/scripts/verificar.py

Confere, nos arquivos .tex de artigo/ e no referencias.bib:
  1. rótulos (\\label) duplicados, e referências (\\ref, \\autoref) a rótulos inexistentes;
  2. citações (\\cite) sem entrada no .bib e entradas do .bib nunca citadas;
  3. campos obrigatórios das entradas do .bib e tipos que o BibTeX do modelo SBC não reconhece;
  4. tabelas e figuras sem \\caption, sem \\label, sem linha de "Fonte" ou nunca chamadas no texto;
  5. emojis e símbolos decorativos nos .tex e nos .md de docs/;
  6. termos fora do padrão da equipe (ver gestao/revisao-final.md, Seção 2);
  7. marcas [VERIFICAR] pendentes.

Sai com código 1 se houver erro (itens 1 a 5); avisos (itens 6 e 7) não alteram o código.
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
TEX = sorted((RAIZ / "artigo").rglob("*.tex"))
MD = sorted((RAIZ / "docs").glob("*.md"))
BIB = RAIZ / "artigo" / "referencias.bib"

# Termo fora do padrão -> forma padronizada.
TERMOS = {
    r"\bPortal Web\b|\bportal web\b|\bPortal de Serviços web\b": "Portal de Serviços",
    r"\baplicativo mobile\b|\bApp mobile\b|\bapp mobile\b|\bAplicativo Mobile\b": "aplicativo",
    r"\bapp\b(?!\.|/| (?:Store|iOS))": "aplicativo (ou Aplicativo, em título)",
    r"\bconsulta de multas\b": "consulta de infrações",
    r"\beficiência\b(?! de desempenho)(?! do modelo)": "eficiência de desempenho (confirmar o sentido)",
    r"\badequação funcional do fluxo\b|\bhomologad[oa]s?\b|\bstakeholders?\b": "ver Seção 2 de gestao/revisao-final.md",
}
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B50\u2B06\u2705\u274C]")


def sem_comentarios(texto):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", linha) for linha in texto.splitlines())


def main():
    erros, avisos = [], []
    fontes = {p: sem_comentarios(p.read_text(encoding="utf-8")) for p in TEX}
    tudo = "\n".join(fontes.values())

    # 1. rótulos
    rotulos = {}
    for p, t in fontes.items():
        for m in re.finditer(r"\\label\{([^}]+)\}", t):
            rotulos.setdefault(m.group(1), []).append(p.name)
    for r, arqs in rotulos.items():
        if len(arqs) > 1:
            erros.append(f"rótulo duplicado '{r}' em {', '.join(arqs)}")
    refs = {}
    for p, t in fontes.items():
        for m in re.finditer(r"\\(?:auto|page|eq)?ref\{([^}]+)\}", t):
            refs.setdefault(m.group(1), set()).add(p.name)
    for r, arqs in refs.items():
        if r not in rotulos:
            erros.append(f"referência a rótulo inexistente '{r}' em {', '.join(sorted(arqs))}")

    # 2. citações
    bib_txt = BIB.read_text(encoding="utf-8")
    entradas = re.findall(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", bib_txt)
    chaves = {c for _, c in entradas}
    citadas = set()
    for p, t in fontes.items():
        for m in re.finditer(r"\\cite[a-z]*\{([^}]+)\}", t):
            for c in m.group(1).split(","):
                c = c.strip()
                citadas.add(c)
                if c not in chaves:
                    erros.append(f"citação sem entrada no .bib: '{c}' em {p.name}")
    for c in sorted(chaves - citadas):
        avisos.append(f".bib: '{c}' nunca é citada")

    # 3. entradas do .bib
    obrig = {
        "article": ["author", "title", "journal", "year"],
        "book": ["author", "title", "publisher", "year"],
        "incollection": ["author", "title", "booktitle", "publisher", "year"],
        "misc": ["title", "year"],
        "techreport": ["author", "title", "institution", "year"],
    }
    blocos = re.split(r"(?m)^@", bib_txt)[1:]
    for bloco in blocos:
        m = re.match(r"(\w+)\s*\{\s*([^,\s]+)\s*,", bloco)
        if not m:
            continue
        tipo, chave = m.group(1).lower(), m.group(2)
        if tipo not in obrig:
            erros.append(f".bib: '{chave}' usa @{tipo}, tipo que o BibTeX clássico do modelo SBC não reconhece")
            continue
        for campo in obrig[tipo]:
            if not re.search(rf"(?m)^\s*{campo}\s*=", bloco):
                erros.append(f".bib: '{chave}' (@{tipo}) sem o campo '{campo}'")

    # 4. tabelas e figuras
    for p, t in fontes.items():
        for m in re.finditer(r"\\begin\{(table|figure)\*?\}(.*?)\\end\{\1\*?\}", t, re.S):
            tipo, corpo = m.group(1), m.group(2)
            rot = re.search(r"\\label\{([^}]+)\}", corpo)
            nome = rot.group(1) if rot else "(sem rótulo)"
            if "\\caption" not in corpo:
                erros.append(f"{p.name}: {tipo} '{nome}' sem \\caption")
            if not rot:
                erros.append(f"{p.name}: {tipo} sem \\label")
            elif nome not in refs:
                erros.append(f"{p.name}: {tipo} '{nome}' nunca é chamada no texto")
            if not re.search(r"Fonte\s*:", corpo):
                erros.append(f"{p.name}: {tipo} '{nome}' sem linha de 'Fonte:'")

    # 5. emojis
    for p in TEX + MD:
        for i, linha in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if EMOJI.search(linha):
                erros.append(f"{p.relative_to(RAIZ)}:{i}: emoji ou símbolo decorativo")

    # 6. termos
    for p, t in fontes.items():
        if p.parent.name != "secoes":  # figuras usam nomes de nós, não texto corrido
            continue
        for padrao, padrao_ok in TERMOS.items():
            for m in re.finditer(padrao, t):
                linha = t.count("\n", 0, m.start()) + 1
                avisos.append(f"{p.name}:{linha}: '{m.group(0)}' -> {padrao_ok}")

    # 7. pendências
    for p in TEX + MD:
        n = len(re.findall(r"\[VERIFICAR", p.read_text(encoding="utf-8")))
        if n:
            avisos.append(f"{p.relative_to(RAIZ)}: {n} marca(s) [VERIFICAR]")

    for e in erros:
        print("ERRO  ", e)
    for a in avisos:
        print("AVISO ", a)
    print(f"\n{len(erros)} erro(s), {len(avisos)} aviso(s); {len(TEX)} arquivos .tex, {len(chaves)} entradas no .bib.")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
