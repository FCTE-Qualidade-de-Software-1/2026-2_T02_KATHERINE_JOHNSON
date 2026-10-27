# Avaliação Comparativa de Qualidade em Serviços Digitais de Governo: Portal Web × Aplicativo Móvel na Consulta de Infrações do Detran-DF

Projeto final da disciplina **FGA0315 Qualidade de Software 1** (Engenharia de Software,
UnB/FCTE, semestre 2026/2), turma T02, professora Cristiane Soares Ramos. Equipe **Katherine
Johnson**.

O projeto avalia a qualidade da consulta de infrações de trânsito do Detran-DF em dois canais, o
Portal de Serviços (navegador) e o aplicativo oficial (Android e iOS), com medições externas
(caixa-preta) aplicadas igualmente aos dois. As características avaliadas são **adequação
funcional**, **eficiência de desempenho** e **cobertura de contexto**, segundo a família
ISO/IEC 25000 (SQuaRE).

## Links

| | |
|---|---|
| GitPage do projeto | <https://fcte-qualidade-de-software-1.github.io/2026-2_T02_KATHERINE_JOHNSON/> |
| Quadro do backlog (GitHub Project, acesso restrito aos membros da organização) | <https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/38> |
| Releases (versões entregues, com o PDF do artigo) | <https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/releases> |
| Issues e milestones | [Issues](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues) · [Milestones](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/milestones) |

## Método

A avaliação segue o processo de avaliação de produto da ISO/IEC 25040, em quatro fases:

| Fase | Conteúdo | Entrega |
|---|---|---|
| 1. Requisitos da avaliação | Propósito, partes interessadas, escopo, descrição do produto, modelo de qualidade, priorização e ODS | E1 |
| 2. Especificação da avaliação | Objetivos, questões e hipóteses (GQM), métricas, níveis de pontuação e critérios de julgamento | E1 |
| 3. Projeto da avaliação | Método, instruções, ambiente, massa de dados e cronograma | E2 |
| 4. Execução e julgamento | Coleta, cálculo das métricas, respostas ao GQM, julgamento e ação de melhoria | E2 |

A execução do próprio projeto é acompanhada com métricas PSM/CID (desempenho dos processos,
calendário e progresso, recursos e custos), descritas em [`gestao/plano-psm.md`](gestao/plano-psm.md).

## Estrutura do repositório

| Pasta | Conteúdo |
|---|---|
| [`artigo/`](artigo) | Artigo em LaTeX no modelo da SBC: `main.tex`, seções em `secoes/`, figuras em `figuras/` e referências em `referencias.bib` |
| [`artigo/scripts/`](artigo/scripts) | `verificar.py`, checagem mecânica de citações, rótulos, legendas e termos do artigo |
| [`docs/`](docs) | Páginas da GitPage (MkDocs Material), publicadas automaticamente a cada merge na `main` |
| [`gestao/`](gestao) | Plano de medição PSM/CID e registros de gestão |
| [`atas/`](atas) | Atas das reuniões da equipe e modelo de ata |
| [`dados/`](dados) | Massa de dados da avaliação e termo de consentimento |
| [`evidencias/`](evidencias) | Capturas de tela e roteiros de coleta, anonimizados conforme a LGPD |
| [`slides/`](slides) | Slides apresentados (PDF do Ponto de Controle 1) e o conteúdo de cada integrante |

Dados pessoais de condutores e veículos não são publicados. As regras de anonimização estão em
[`evidencias/fase1/README.md`](evidencias/fase1/README.md).

## Como trabalhamos

1. Toda tarefa é uma **issue** com responsável, critérios de aceitação e estimativa de horas. O
   título leva o prefixo da entrega: `[E1]` ou `[E2]`.
2. O trabalho é feito em uma **branch** própria (`feat/<nome>-<tema>`, `docs/<nome>-<tema>` ou
   `fix/<nome>-<tema>`).
3. A integração na `main` é feita por **pull request** revisado e aprovado por outro integrante.
4. Pendências e retrabalho de uma tarefa viram sub-issue ou item de checklist da issue original,
   e não uma issue nova.
5. Cada integrante registra as horas gastas em suas issues na página
   [Registro de horas por issue](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_KATHERINE_JOHNSON/gestao-horas/)
   da GitPage.

## Como gerar os artefatos

**Artigo (PDF):**

```bash
cd artigo
latexmk -pdf main.tex          # ou: tectonic main.tex
python3 scripts/verificar.py   # checagens mecânicas de citações, rótulos e termos
```

**GitPage (pré-visualização local):**

```bash
pip install -r requirements-docs.txt
mkdocs serve                   # http://127.0.0.1:8000
```

## Equipe

| Integrante | GitHub |
|---|---|
| Daniel de Oliveira Lira | [@Daniellira540](https://github.com/Daniellira540) |
| Heitor Macedo Ricardo | [@HeitorM50](https://github.com/HeitorM50) |
| Hugo Freitas Silva | [@HugoFreitass](https://github.com/HugoFreitass) |
| Pedro Druck Montalvão Reis | [@pedruck](https://github.com/pedruck) |
| Pedro Henrique Ferreira Xavier | [@PedroGTG](https://github.com/PedroGTG) |
| Philipe Amâncio Reis Caetano | [@Phill-Chill](https://github.com/Phill-Chill) |

As responsabilidades de cada integrante estão na página
[Equipe](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_KATHERINE_JOHNSON/equipe/) da
GitPage, e a contribuição quantificada está no apêndice do artigo.
