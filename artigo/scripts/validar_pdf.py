#!/usr/bin/env python3
"""Verifica PDF compilado com Poppler: seções, referências e limite de páginas."""
import argparse
import re
import subprocess
import unicodedata
from pathlib import Path


def verificar(path):
    info = subprocess.check_output(['pdfinfo', str(path)], text=True)
    total = int(re.search(r'^Pages:\s+(\d+)', info, re.M).group(1))
    text = subprocess.check_output(['pdftotext', '-layout', str(path), '-'], text=True)
    text = unicodedata.normalize('NFKC', text)
    pages = text.split('\f')[:total]
    appendix = next((i for i, page in enumerate(pages)
                     if re.search(r'^\s*A\.\s+Tabela de Contribuição Individual', page, re.M)), None)
    if appendix is None:
        raise ValueError('Apêndice de contribuição não encontrado')
    if appendix > 15:
        raise ValueError(f'{appendix} páginas antes da contribuição; máximo de 15')
    if total - appendix != 1:
        raise ValueError('A tabela de contribuição deve ocupar uma página separada')
    if '??' in text:
        raise ValueError('Referência indefinida (??) no PDF')
    for required in ('Fase 4:', 'Considerações Finais', 'Ação de Melhoria Entregue', 'Referências'):
        if required not in text:
            raise ValueError(f'Seção obrigatória ausente no PDF: {required}')
    print(f'PDF validado: {appendix} páginas de artigo e referências + 1 de contribuição; '
          f'{total} páginas no total; seções finais presentes, sem referências indefinidas.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path, nargs='?', default=Path(__file__).resolve().parents[1]/'main.pdf')
    args = parser.parse_args()
    verificar(args.pdf)
