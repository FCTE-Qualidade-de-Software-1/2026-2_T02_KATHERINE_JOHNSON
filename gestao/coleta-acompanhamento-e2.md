# Coleta de Acompanhamento PSM/CID — Entrega 2

**Data da coleta:** 17/11/2026 (Coleta 2 da E2, Seção 4.1 do plano)  
**Dados consultados em:** 16/11/2026, no GitHub (issues, PRs, revisões e `git log` da `main`)  
**Responsável:** Heitor Macedo Ricardo  
**Plano de referência:** [`gestao/plano-psm.md`](plano-psm.md), versão 1.2  
**Coleta anterior:** [`gestao/coleta-intermediaria-e2.md`](coleta-intermediaria-e2.md)  
**Situação deste documento:** rascunho. Os valores valem para 16/11 e devem ser conferidos de novo
em 17/11, antes da reunião (Seção 6). As decisões da Seção 4 são propostas; passam a valer depois
que a equipe as confirmar em ata.

Esta é a segunda coleta da Entrega 2 e o primeiro cálculo de M-CP1 e M-RC1 com a E2 planejada.
Em 16/11, 3 das 8 issues da E2 estavam fechadas. A #46 (Fase 3), que trava a coleta (#47) e a
análise (#48), venceu em 15/11 e continua aberta. Restam 5 issues abertas, com 59 h estimadas,
para 6 dias até a Entrega 2 (22/11).

## 1. Métricas do plano

| Métrica | Valor em 16/11 | Situação | Interpretação |
|---|---|---|---|
| M-CP1 — Cumprimento de marcos | Data de corte 17/11: vencem 4 issues (#53, #28, #46 e #55); 3 concluídas no prazo (#53, #28 e #55). ICM = 3 de 4 (75%). Das 8 issues da E2, 3 estão fechadas | Amarelo; passa a Vermelho em 17/11 se a #46 continuar aberta | O valor cai na faixa Amarelo (70% a 85%). A #46 tem 1 dia de atraso em tarefa com dependência (Amarelo) e, com 2 dias, vira bloqueio na cadeia crítica (Vermelho), porque trava a #47. Sem a #55, que vence em 17/11, o ICM de 16/11 seria 2 de 3 (67%) |
| M-RC1 — Variação de esforço | Issues fechadas com horas: #28 (1 h para 3 h), #53 (3 h para 4 h) e #55 (1 h para 1 h). Total: 5 h reais para 8 h estimadas (−37,5%) | Amarelo (−40% a −20%) | A estimativa inclui a margem de 32% (fator 1,1 × 1,2). Contra a base de 6 h, o real de 5 h dá −17%. A amostra são 3 issues pequenas; as 5 abertas somam 59 h estimadas, sem hora real registrada, e vão decidir o resultado |
| M-RC2 — Contribuição individual | 5 h reais registradas na E2: Heitor 3 h, Daniel 1 h, Pedro Druck 1 h; Hugo, Pedro Henrique e Philipe com 0 h | Não interpretável | Só 3 dos 6 integrantes têm hora registrada. A #46 tem 5 commits no PR #57 (Hugo 3, Philipe 2) e 0 h reais na issue. O cálculo definitivo é na coleta de 21/11 |
| M-DP1 — Retrabalho em revisão | 0 de 5 PRs com pedido de ajuste ou commit depois da revisão (#52, #54, #56, #57 e #58) | Verde (até 30%) | Nenhum dos 5 PRs recebeu *Changes Requested* nem commit posterior à primeira revisão. Em 3 dos 5 (#52, #54 e #56), a aprovação saiu no minuto do merge; a métrica só vê o retrabalho que deixa rastro no GitHub. O #57 foi aprovado em 15/11 e mesclado em 16/11, sem commit depois da aprovação |

*Tabela 1 — Métricas do plano em 16/11/2026. Fonte: issues #28, #36, #46 a #49, #53 e #55; PRs #52, #54, #56, #57 e #58, no GitHub.*

Desvio de esforço por integrante nas issues fechadas: Daniel −66,7% (#28), Heitor −25,0% (#53) e
Pedro Druck 0% (#55). O plano só define faixa de alerta acima de +40%; o desvio abaixo de −40% não
tem cor definida.

## 2. Ações da retrospectiva

| Ação | Métrica | Valor em 16/11 | Situação |
|---|---|---|---|
| C1 — PR revisado em até 48 h (Daniel) | Tempo até a 1ª revisão | #52: 5 min; #54: 11,4 h; #56: 6 min; #58: 2,2 h; #57: 48,4 h (aberto em 13/11 às 21h47, 1ª revisão humana em 15/11 às 22h12). Mediana: 2,2 h; 1 PR acima de 48 h. O #59 está em aberto desde 16/11 e vence em 18/11 | Amarelo (1 PR acima de 48 h) |
| C3 — Lista de bloqueios da #46 com responsável e data (Hugo) | M-CP1 | O PR #57 traz 8 bloqueios (B01 a B08), cada um com responsável e prazo, na página de cronograma. O PR foi mesclado em 16/11 na branch da issue #46, e não na `main`; a lista de pendências no corpo da #46 continua sem responsável e data. Os prazos (14 e 15/11) já passaram, sem evidência de resolução no repositório | Cumprida na branch da issue #46, com 2 semanas de atraso em relação ao prazo de 30/10; falta chegar à `main` |
| C3 — Repassar pendências em toda reunião (Pedro Henrique) | M-CP1 | Repassadas em 10/11 ([ata 04](../atas/ata-04-2026-11-10.md)). Sem reunião registrada na semana de 16/11 até agora | Aplicada em 10/11 |
| C5 — Revisor em rodízio (Philipe) | M-RC2 aplicada às revisões | 8 de 8 issues da E2 com revisor. Nos 4 PRs da E2 com revisor designado (#54, #56, #57 e #58), o revisor foi o designado. Revisões desde 30/10 (6 no total): Pedro Henrique 3 (50%), Philipe 1 (16,7%), Hugo 1 (16,7%), Heitor 1 (16,7%, a do #57 em 16/11), Daniel 0 e Pedro Druck 0 | Cumprida na designação; concentrada na execução |
| C6 — Sem commit direto na `main` (Pedro Druck) | M-DP1 e commits diretos | 4 commits diretos depois do fechamento da E1: `0c32d68` e `c29861b` (28/10) e, **novos**, `dced9e2` e `d7ed7a6` (11/11, sem PR associado) | Vermelho (proposto): a regra foi mantida na reunião de 10/11 e quebrada em 11/11 |
| C7 — Atas ÷ reuniões (Heitor) | Atas ÷ reuniões | 2 reuniões registradas (28/10 e 10/11), com 2 atas: 100%. A ata 03 saiu fora do prazo de 24 h, como já registrado em 10/11 | Amarelo |
| C7 — Frequência das reuniões | Semanas com reunião ÷ semanas | Semana de 26/10: 1; 02/11: 0; 09/11: 1; 16/11: 0 até agora. Resultado: 2 de 3 semanas fechadas (67%) | Vermelho |

*Tabela 2 — Ações da retrospectiva em 16/11/2026. Fonte: PRs e revisões no GitHub, `git log --first-parent` da `main`, pasta `atas/` e [`gestao/retrospectiva-e1.pdf`](retrospectiva-e1.pdf).*

A proteção da `main` exige 1 aprovação em PR, mas a opção que aplica a regra também aos
administradores (`enforce_admins`) está desativada. Por isso, quem é administrador consegue enviar
commit direto. Essa é uma explicação possível para os commits de 11/11, mas ela não foi confirmada.

## 3. Decisões anteriores (D1 a D7)

| # | Decisão da coleta de 10/11 | Situação em 16/11 |
|---|---|---|
| D1 | Dar responsável, revisor, data e estimativa às issues da E2 | Feita em 10/11 |
| D2 | Priorizar a #46 antes do ponto de controle | Parcial: o PR #57 foi aprovado em 15/11 e mesclado em 16/11, mas na branch da issue #46 e não na `main`; a #46 tem 3 de 14 critérios marcados |
| D3 | Reunião da semana com ata | Feita em 10/11; falta a da semana de 16/11 |
| D4 | Completar a lista de bloqueios da #46 | Feita no PR #57 (13/11), mesclado em 16/11 na branch da issue; falta chegar à `main` |
| D5 | Conferir de novo os commits diretos na `main` | Conferido nesta coleta: 2 commits novos em 11/11 |
| D6 | Registrar as horas reais da #51 | Não feita: a #51 continua com a estimativa de 3 h e sem hora real |
| D7 | Publicar o plano v1.2 | Feita em 11/11 (PR #54) |

*Tabela 3 — Situação das decisões anteriores. Fonte: [`gestao/coleta-intermediaria-e2.md`](coleta-intermediaria-e2.md), issues e PRs no GitHub.*

## 4. Decisões propostas

| # | Gatilho | Decisão proposta | Responsável | Prazo |
|---|---|---|---|---|
| D8 | M-CP1: #46 vencida e travando a #47 | Abrir o PR da branch da issue #46 para a `main` (o #57, mesclado em 16/11, só chegou a essa branch) e decidir na reunião se os critérios empíricos da #46 (veículo real, prints com login, iPhone) migram para a #47 ou se a #46 fica aberta com novo prazo; registrar na issue | Hugo e Philipe; Pedro Henrique confirma | 17/11 |
| D9 | M-RC2: só 3 de 6 integrantes com hora registrada | Registrar as horas reais nas issues à medida que o trabalho acontece e, no máximo, até 20/11, antes da coleta de fechamento | Todos; Daniel confere | 20/11 |
| D10 | C6 reincidente | Ativar a regra para administradores na proteção da `main` e combinar que também os administradores abrem PR | Quem tiver permissão de administrador; Pedro Druck confirma | 17/11 |
| D11 | C1: #57 acima de 48 h | Avisar o revisor no grupo ao abrir o PR; o #59 vence em 18/11 | Autor de cada PR; revisor | Contínuo |
| D12 | C7: semana de 16/11 sem reunião | Marcar a reunião da semana com ata; pauta: D8 a D10, bloqueios da Fase 3 e preparo da apresentação final | Heitor (ata); Pedro Henrique (pauta) | 22/11 |
| D13 | C5: Daniel, Heitor e Pedro Druck com 0 revisões | Manter o rodízio já designado (Daniel revisa #47 e #36, Heitor revisa #48, Pedro Druck revisa #49) e conferir no fechamento | Philipe | 21/11 |
| D14 | Pendências de registro | Sincronizar as datas das issues #47 e #48 no Project 38 (bloqueio B08); registrar as horas da #51; alinhar o prazo da #55 (corpo da issue: 17/11; documentos: 11/11); marcar os critérios das issues #53 e #55, fechadas com a lista sem marcação | Hugo (Project); Pedro Druck (#51 e #55); Heitor (#53) | 20/11 |

*Tabela 4 — Decisões propostas. Fonte: Seções 1 a 3 deste documento.*

## 5. Riscos até a Entrega 2

| Risco | Evidência | Efeito |
|---|---|---|
| Cadeia crítica comprimida | #46 vencida; #47 vence em 18/11, #48 em 20/11, #36 em 21/11 e #49 em 22/11; 59 h estimadas nas 5 issues abertas | Qualquer atraso da #46 ou da #47 empurra a análise, a ação de melhoria e o fechamento |
| Recursos da coleta não confirmados | Veículo com infração e consentimento dependem de terceiros (B01); o PR #57 informa que não há confirmação nem evidência de execução. A equipe informou em 16/11 que tem um iPhone, mas modelo e versões ainda não estão registrados (B03) | Sem veículo real, as sessões da #47 não acontecem; sem o registro do iPhone, o iOS continua como contexto não avaliado |
| Fase 3 fora da `main` | O #57 foi mesclado na branch da issue #46, e não há PR dessa branch para a `main`; a GitPage só publica a partir da `main` | Até o PR final, a GitPage e o artigo oficial não trazem a Fase 3 |
| Esforço pouco registrado | 0 h reais nas 5 issues abertas, que concentram o trabalho da E2 | PCI e TVE do fechamento ficam sem base; a tabela de contribuição do artigo depende dessas horas |
| Qualidade da revisão pouco visível | 3 de 5 PRs aprovados no minuto do merge | M-DP1 em 0% pode esconder retrabalho que não deixa rastro |

*Tabela 5 — Riscos da E2. Fonte: Seções 1 e 2; cronograma da Fase 3 no PR #57.*

## 6. O que atualizar em 17/11

Antes da reunião, conferir de novo e atualizar a Tabela 1 com:

- situação da #46 e do PR da branch da issue para a `main` (aberto, mesclado, critérios marcados), que muda o M-CP1;
- horas reais lançadas nas issues, que mudam o M-RC1 e o M-RC2;
- revisão dos PRs #59 e #60 (tempo até a 1ª revisão, M-DP1 e revisões por integrante);
- novos commits diretos na `main` (`git log origin/main --first-parent --no-merges`);
- reunião da semana de 16/11 e ata correspondente.

## 7. Próxima coleta

A coleta de fechamento acontece em 21/11/2026, antes da Release E2 (22/11), conforme a Seção 4.1 do
plano. Ela fecha M-RC2 e a Tabela de Contribuição.
