#!/usr/bin/env python3
"""Inspeção offline dos artefatos; não executa consultas ao Detran-DF."""
import csv
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    for name in ('README.md', 'incidente.md'):
        if '14ab804210f4b1be2aaa84e1946d9e11079a9a28' not in (root / name).read_text(encoding='utf-8'):
            raise ValueError(f'{name}: fonte imutável ausente')
    with (root / 'regressao.csv').open(encoding='utf-8', newline='') as handle:
        rows = list(csv.DictReader(handle))
    if {r['caso'] for r in rows} != {'RG01', 'RG02', 'RG03', 'RG04'} or len(rows) != 4:
        raise ValueError('Exigir referência, intervenção e dois controles')
    for row in rows:
        if row['procedimento'] != 'P6' or row['repeticoes'] != '3' or row['estado'] != 'planejado':
            raise ValueError('Planejamento não pode ser apresentado como coleta')
        if not row['condicao'].strip() or not row['criterio'].strip():
            raise ValueError('Cenário sem condição ou critério de aceitação')
    print('Fonte e quatro cenários P6 conferidos. Revisão humana e eficácia pendentes.')


if __name__ == '__main__':
    main()
