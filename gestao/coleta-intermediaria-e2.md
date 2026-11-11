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
| C3 — Repassar pendências em toda reunião (Pedro Henrique) | M-CP1 | Nenhuma reunião depois de 28/10 | Não aplicada |
| C5 — Revisor em rodízio definido na criação (Philipe, prazo 30/10) | M-RC2 aplicada às revisões | 0 de 6 issues da E2 com revisor. Na única revisão da E2, o revisor foi Pedro Henrique, que tinha 0 revisões na E1 | Não cumprida |
| C6 — Sem commit direto na `main` (Pedro Druck) | M-DP1 e commits diretos | 3 commits diretos depois do fechamento da E1: `2186819` (26/10), `0c32d68` e `c29861b` (28/10, registro da retrospectiva). Nenhum depois de 28/10 | Amarelo |
| C7 — Uma reunião por semana com ata (Heitor) | Atas ÷ reuniões | 1 reunião (28/10). Ata escrita em 10/11 ([ata 03](../atas/ata-03-2026-10-28.md)): 1 de 1 (100%), mas fora do prazo de 24 h | Amarelo |
| C7 — Frequência das reuniões | Semanas com reunião ÷ semanas | Semana de 26/10: 1; semana de 02/11: 0. Resultado: 1 de 2 semanas completas (50%) | Vermelho |

## 3. Decisões de gestão

| # | Gatilho | Decisão | Responsável | Prazo |
|---|---|---|---|---|
| D1 | M-CP1, M-RC1 e M-RC2 não calculáveis; C5 não cumprida | Dar responsável, revisor em rodízio, data e estimativa às 6 issues da E2 (proposta na Seção 4) | Heitor aplica; equipe confirma na reunião | 11/11/2026 |
| D2 | Bloqueio na cadeia crítica (regra da faixa vermelha da M-CP1) | Priorizar a #46 (Fase 3), que trava a coleta (#47) e a análise (#48) | Hugo e Philipe | Antes do ponto de controle de 16/11 |
| D3 | C7: semana de 02/11 sem reunião; C3 sem reunião de abertura da E2 | Fazer a reunião desta semana com ata; ela também cumpre a reunião de abertura da E2 da ação C3 | Heitor (ata); Pedro Henrique (pauta de pendências) | Semana de 09/11 |
| D4 | C3 não cumprida | Na reunião, completar a lista de bloqueios da #46 com responsável e data | Hugo | Na reunião de D3 |
| D5 | C6 em Amarelo | Manter a regra. Os 3 commits diretos ficam registrados como desvio do fechamento da E1; conferir de novo na próxima coleta | Pedro Druck | Próxima coleta |
| D6 | #51 sem horas reais | Registrar as horas reais da #51 para fechar o esforço da E1 | Pedro Druck | Próxima coleta |
| D7 | Plano sem calendário da E2 | Publicar o plano v1.2 com o calendário da E2 e as métricas complementares | Heitor | Esta coleta (#53) |

## 4. Proposta de planejamento das issues da E2

Estimativa = base × 1,1 (fator de correção da E1, TVE = +10%) × 1,2 (margem de segurança do
relatório da E1), arredondada para cima. O revisor segue um rodízio diferente dos pares da E1.

| Issue | Responsável | Revisor | Base | Estimativa |
|---|---|---|---:|---:|
| #28 Correções do Ponto de Controle 1 | Daniel | Hugo | 2 h | 3 h |
| #46 Fase 3: plano de avaliação | Hugo, Philipe | Pedro Henrique | 8 h | 11 h |
| #47 Fase 4: coleta e dados brutos | Hugo, Pedro Druck, Philipe | Daniel | 12 h | 16 h |
| #48 Fase 4: análise, respostas GQM e julgamento | Pedro Henrique, Philipe | Heitor | 8 h | 11 h |
| #36 Ação de melhoria | Pedro Druck | Daniel | 6 h | 8 h |
| #49 Fechamento da E2 | Daniel, Heitor | Pedro Druck | 10 h | 13 h |
| #53 Coleta intermediária PSM/CID e slides | Heitor | Pedro Henrique | 3 h | 4 h |
| **Total** | | | **49 h** | **66 h** |

As datas das issues dependem da data da Entrega 2 no cronograma da disciplina. [CONFIRMAR a data
da Entrega 2 e preencher as datas de cada issue.]

## 5. Próxima coleta

A próxima coleta acontece depois que as issues tiverem data e estimativa, na semana de 16/11, e
calcula M-CP1 e M-RC1 pela primeira vez na E2. A coleta de fechamento acontece antes da Release E2,
conforme a Seção 4 do plano.
