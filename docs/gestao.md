# Gestão do projeto (PSM/CID)

A execução do projeto é acompanhada com métricas baseadas no PSM/CID, em três categorias:

- **Desempenho dos processos** — por exemplo, retrabalho e revisões aprovadas de primeira;
- **Calendário e progresso** — por exemplo, issues fechadas em relação às planejadas;
- **Recursos e custos** — por exemplo, horas dedicadas por integrante.

Cada tarefa é registrada como uma issue, desenvolvida em uma branch própria e integrada por
pull request revisado por outro integrante. Esses registros são a fonte das medições.

- [Plano de métricas PSM/CID](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/gestao/plano-psm.md)
- [Issues do projeto](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues)
- [Pull requests](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pulls)
- [Milestones](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/milestones)
- [Quadro do backlog (GitHub Project)](https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/38)

O tempo gasto em cada issue é registrado pelos próprios integrantes em
[Registro de horas por issue](gestao-horas.md).

## Medições da Entrega 1

As métricas seguem as definições do [plano PSM/CID](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/gestao/plano-psm.md). Os
valores abaixo foram obtidos do histórico de issues e pull requests do repositório. O consolidado da
E1 está no [relatório de métricas da Release E1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/gestao/relatorio-metricas-e1.md).

| Data da coleta | Métrica | Valor medido | Situação | Interpretação | Decisão de gestão |
|---|---|---|---|---|---|
| 21/10/2026 | M-CP1 (cumprimento de marcos) | 3 de 12 issues fechadas | — | Produção adiantada, mas o fechamento formal dependia das revisões dos PRs abertos ([ata 02](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/atas/ata-02-2026-10-21.md)) | Priorizar a revisão e o merge dos PRs #18, #19 e #21 |
| 21/10/2026 | M-RC1 e M-RC2 (esforço) | Não calculável | — | Campo de horas reais em branco em todas as issues | Todos preenchem as horas reais nas suas issues |
| 26/10/2026 (fechamento) | M-DP1 (retrabalho em revisão) | 0 de 14 PRs (0%) | Verde (≤ 30%) | Nenhum PR integrado à `main` na E1 recebeu pedido de ajustes ou commits após a revisão. A métrica não capta a espera pela revisão: os PRs #18, #19, #21, #23 e #24 aguardaram de 2 a 7 dias pela aprovação | Manter a revisão por pares e acompanhar o tempo de revisão na Entrega 2 |
| 26/10/2026 (fechamento) | M-CP1 (cumprimento de marcos) | 15 de 15 issues da E1 concluídas (100%) | Verde | A #27 foi fechada como duplicada da #2 e não entra na conta. Parte das issues foi fechada em 25/10 por decisão do grupo (registro abaixo) | Consolidar o backlog da E2 em issues por artefato, com sub-issues para retrabalho |
| 26/10/2026 (fechamento) | M-RC1 (variação de esforço) | 55 h reais / 50 h estimadas (+10%) | Verde | Desvios individuais: Daniel e Heitor +24,5% (Amarelo), concentrados na configuração do repositório e na seção de propósito e GitPage | Aplicar o fator de correção observado nas estimativas da Entrega 2 |
| 26/10/2026 (fechamento) | M-RC2 (contribuição individual) | Pelas horas: mín. 13,0% (Hugo) / máx. 18,5% (Daniel, Heitor e Pedro Druck) | Amarelo | As horas não captam a revisão do trabalho dos colegas, o retorno dado a cada entrega e a organização da equipe | Contribuição final de 16,67% para cada integrante, por decisão da equipe, publicada no apêndice do artigo |

## Registro de fechamento de issues da Entrega 1

Em 25/10/2026, as issues abaixo foram fechadas por Pedro Druck, por decisão do grupo. Os
responsáveis (Heitor, Hugo e Philipe) entregaram o trabalho previsto nas suas issues, conforme as
evidências da tabela, mas não conseguiram fechá-las por estarem fora do país, em viagem
internacional. As issues do próprio Pedro Druck também foram fechadas nesta data. As horas reais
de cada issue continuam sendo registradas pelos respectivos responsáveis.

| Issue | Responsável | Evidência da entrega | Pendência remanescente |
|---|---|---|---|
| [#3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/3) Propósito, stakeholders, escopo e introdução | Heitor Macedo Ricardo | [PR #16](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/16) e [PR #24](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/24) (resgate para a `main`) | Introdução do artigo, tratada nos ajustes pedidos pela professora |
| [#4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/4) Configuração e alimentação da GitPage | Heitor Macedo Ricardo | [PR #15](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/15) | Seções das Fases 3 e 4 seguem em [#37](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/37) |
| [#5](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/5) Levantamento e descrição dos canais | Hugo Freitas Silva | [PR #13](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/13), [PR #14](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/14) e [PR #20](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/20) | Sessão com login de proprietário real, prevista em [#30](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/30) e [#32](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/32) |
| [#7](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/7) Priorização, ODS e referencial SQuaRE | Pedro Druck | [PR #18](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/18) | — |
| [#8](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/8) Revisão de português e padronização | Pedro Druck | [PR #19](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/19) | — |
| [#11](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/11) Fichas de métricas e níveis de pontuação | Philipe Amâncio Reis Caetano | [PR #14](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/14) e [PR #21](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/21) | — |
| [#12](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/12) Critérios de julgamento e diagrama GQM | Philipe Amâncio Reis Caetano | [PR #14](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/14) e [PR #21](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/21) | Regenerar o diagrama GQM em maior legibilidade (ata 02) |

Permanecem abertas as issues de Daniel ([#2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/2) e [#27](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/27), esta compartilhada com Pedro Druck) e as
que ainda não têm entrega registrada: [#25](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/25) (linhas individuais da declaração de uso de IA) e
[#26](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/26) (revisão da hipótese H1.1 e das Tabelas 3 e 5).

*Atualização de 26/10/2026:* a #2 foi concluída com o [PR #50](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/50), que também entregou
as sub-issues #25, #26 e #45; a #27 foi fechada como duplicada da #2. Todas as issues da Entrega 1
estão fechadas.