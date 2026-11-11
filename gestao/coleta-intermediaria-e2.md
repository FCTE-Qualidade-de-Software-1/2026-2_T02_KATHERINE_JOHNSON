# Coleta Intermediária PSM/CID — Entrega 2

**Data da coleta:** 10/11/2026  
**Responsável:** Heitor Macedo Ricardo (issue #53)  
**Plano de referência:** [`gestao/plano-psm.md`](plano-psm.md), versão 1.2  
**Fontes:** issues #28, #36, #46 a #49 e #51; PRs abertos ou mesclados depois de 26/10/2026; histórico
`git log --first-parent` da `main`; [`atas/`](../atas/) e [`gestao/retrospectiva-e1.pdf`](retrospectiva-e1.pdf)

Esta é a primeira coleta da Entrega 2. Ela mede as quatro métricas do plano e as ações da
retrospectiva de 28/10 ([ata 03](../atas/ata-03-2026-10-28.md)). A coleta mostra que a E2 ainda
não tem planejamento suficiente para medir calendário e esforço. A decisão principal é planejar
as issues antes de medir de novo.

## 1. Métricas do plano

| Métrica | Valor em 10/11 | Situação | Interpretação |
|---|---|---|---|
| M-CP1 — Cumprimento de marcos | 0 de 6 issues da E2 fechadas; 0 de 6 com data planejada | Não calculável | Sem data, nenhuma issue "vence" até a data de corte, e o ICM fica sem denominador. Para o plano, isso é um bloqueio na cadeia crítica (Fase 3 → Fase 4), o critério da faixa vermelha |
| M-RC1 — Variação de esforço | 0 de 6 issues com estimativa ("a definir no planejamento da E2") | Não calculável | Sem estimativa, não há base para o desvio. O fator de correção da E1 (+10%) ainda não foi aplicado |
| M-RC2 — Contribuição individual | Nenhuma hora real registrada na E2; 0 de 6 issues com responsável | Não calculável | Sem responsável, não é possível atribuir esforço. A #51 (E1) também não tem horas reais |
| M-DP1 — Retrabalho em revisão | 0 de 1 PR com pedido de ajuste (#52) | Verde (até 30%) | Amostra de um PR. Não permite conclusão sobre o processo |

## 2. Ações da retrospectiva

| Ação | Métrica | Valor em 10/11 | Situação |
|---|---|---|---|
| C1 — PR revisado em até 48 h (Daniel) | Tempo até a 1ª revisão | #52: 5 min (aberto 04/11 15:24, revisado 15:29) | Verde; um único PR desde 30/10 |
| C3 — Lista do que pode travar a avaliação na #46, com responsável e data (Hugo, prazo 30/10) | M-CP1 | A #46 lista iPhone, veículo real e termos, mas sem responsável e sem data | Não cumprida |
| C3 — Repassar pendências em toda reunião (Pedro Henrique) | M-CP1 | Nenhuma reunião de 29/10 a 09/11; a reunião de 10/11 ([ata 04](../atas/ata-04-2026-11-10.md)) repassou as pendências e confirmou o planejamento da E2 | Retomada em 10/11 |
| C5 — Revisor em rodízio definido na criação (Philipe, prazo 30/10) | M-RC2 aplicada às revisões | 0 de 6 issues da E2 com revisor. Na única revisão da E2, o revisor foi Pedro Henrique, que tinha 0 revisões na E1 | Não cumprida |
| C6 — Sem commit direto na `main` (Pedro Druck) | M-DP1 e commits diretos | 2 commits diretos depois de 26/10: `0c32d68` e `c29861b` (28/10, registro da retrospectiva). O `2186819` (26/10) já entra nos 5 commits diretos de 26/10 do fechamento da E1 e não é contado de novo. Nenhum depois de 28/10 | Amarelo |
| C7 — Uma reunião por semana com ata (Heitor) | Atas ÷ reuniões | 2 reuniões (28/10 e 10/11), as 2 com ata: [ata 03](../atas/ata-03-2026-10-28.md), escrita só em 10/11 (fora do prazo de 24 h), e [ata 04](../atas/ata-04-2026-11-10.md). Resultado: 2 de 2 (100%) | Amarelo |
| C7 — Frequência das reuniões | Semanas com reunião ÷ semanas | Semana de 26/10: 1; semana de 02/11: 0; semana de 09/11: 1 (10/11). Resultado: 2 de 3 semanas (67%) | Vermelho |

## 3. Decisões de gestão

| # | Gatilho | Decisão | Responsável | Prazo |
|---|---|---|---|---|
| D1 | M-CP1, M-RC1 e M-RC2 não calculáveis; C5 não cumprida | Dar responsável, revisor em rodízio, data e estimativa às 6 issues da E2 (proposta na Seção 4) | Heitor aplica; equipe confirmou em 10/11 | Feito em 10/11/2026 |
| D2 | Bloqueio na cadeia crítica (regra da faixa vermelha da M-CP1) | Priorizar a #46 (Fase 3), que trava a coleta (#47) e a análise (#48) | Hugo e Philipe | Antes do ponto de controle de 16/11 |
| D3 | C7: semana de 02/11 sem reunião; C3 sem reunião de abertura da E2 | A reunião de 10/11 vale como abertura da E2 da ação C3; registrar a ata e manter uma reunião por semana | Heitor (ata); Pedro Henrique (pauta de pendências) | Feito em 10/11 ([ata 04](../atas/ata-04-2026-11-10.md)); semanal até 22/11 |
| D4 | C3 não cumprida | Completar a lista de bloqueios da #46 com responsável e data | Hugo | Próxima reunião |
| D5 | C6 em Amarelo | Manter a regra. Os 2 commits diretos de 28/10 ficam registrados como desvio; conferir de novo na próxima coleta | Pedro Druck | Próxima coleta |
| D6 | #51 sem horas reais | Registrar as horas reais da #51 para fechar o esforço da E1 | Pedro Druck | Próxima coleta |
| D7 | Plano sem calendário da E2 | Publicar o plano v1.2 com o calendário da E2 e as métricas complementares | Heitor | Esta coleta (#53) |

## 4. Proposta de planejamento das issues da E2

Estimativa = base × 1,1 (fator de correção da E1, TVE = +10%) × 1,2 (margem de segurança do
relatório da E1), arredondada para cima. O revisor segue um rodízio diferente dos pares da E1.

| Issue | Responsável | Revisor | Base | Estimativa | Prazo |
|---|---|---|---:|---:|---|
| #28 Correções do Ponto de Controle 1 | Daniel | Hugo | 2 h | 3 h | 15/11 |
| #46 Fase 3: plano de avaliação | Hugo, Philipe | Pedro Henrique | 8 h | 11 h | 15/11 |
| #47 Fase 4: coleta e dados brutos | Hugo, Pedro Druck, Philipe | Daniel | 12 h | 16 h | 18/11 |
| #48 Fase 4: análise, respostas GQM e julgamento | Pedro Henrique, Philipe | Heitor | 8 h | 11 h | 20/11 |
| #36 Ação de melhoria | Pedro Druck | Daniel | 6 h | 8 h | 21/11 |
| #49 Fechamento da E2 | Daniel, Heitor | Pedro Druck | 10 h | 13 h | 22/11 |
| #53 Coleta intermediária PSM/CID e slides | Heitor | Pedro Henrique | 3 h | 4 h | 11/11 |
| #55 Inconsistências nos registros de gestão PSM/CID | Pedro Druck | Philipe | — | 1 h | 17/11 |
| **Total** | | | **49 h** | **67 h** | |

Os prazos partem da Entrega 2 em 22/11/2026 e do ponto de controle em 16/11/2026: a Fase 3 (#46) e
as correções do PC1 (#28) fecham antes do ponto de controle. A equipe confirmou a proposta em
10/11/2026, e os prazos, responsáveis, revisores e estimativas foram aplicados nas issues no mesmo dia.

A #55 foi aberta em 11/11, depois da coleta, para corrigir as inconsistências encontradas ao
conferir os slides com o GitHub e a GitPage. A estimativa de 1 h foi definida direto, sem o fator
de correção.

## 5. Próxima coleta

A próxima coleta acontece em 17/11/2026, depois do ponto de controle, e calcula M-CP1 e M-RC1 pela
primeira vez na E2: até essa data vencem as issues #53, #28 e #46. A coleta de fechamento acontece em
21/11/2026, antes da Release E2 (22/11), conforme a Seção 4.1 do plano.

## 6. Atualização de 11/11/2026

Depois do planejamento de 10/11, as métricas voltaram a ser calculáveis. Em 11/11, duas issues
da E2 estavam fechadas: a #53 (PR #54) e a #55 (PR #56).

| Métrica | Valor em 11/11 | Situação |
|---|---|---|
| M-CP1 — Cumprimento de marcos | 8 de 8 issues com prazo. Até 11/11 vencia só a #53, fechada no prazo (1 de 1, 100%). A #55 (prazo 17/11) fechou antes do prazo | Verde, amostra de 1 |
| M-RC1 — Variação de esforço | 8 de 8 issues com estimativa (67 h). Fechadas: #53, 3 h para 4 h (−25%), e #55, 1 h para 1 h (0%). Total: 4 h para 5 h (−20%) | Verde, no limite da faixa |
| M-RC2 — Contribuição individual | 8 de 8 issues com responsável; 4 h reais na E2 (Heitor 3 h, Pedro Druck 1 h) | Cálculo no fechamento (21/11) |
| M-DP1 — Retrabalho em revisão | 0 de 3 PRs com pedido de ajuste (#52, #54 e #56) | Verde, amostra de 3 |
| C1 — Tempo até a 1ª revisão | #52 em 5 min, #54 em 11,4 h e #56 dentro de 48 h | Verde |
| C5 — Revisor em rodízio | 8 de 8 issues da E2 com revisor; as revisões da E2 foram de Pedro Henrique (#52 e #54) e Philipe (#56) | Cumprida |
