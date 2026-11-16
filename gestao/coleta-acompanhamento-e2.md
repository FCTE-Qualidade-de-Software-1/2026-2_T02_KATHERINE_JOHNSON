# Coleta de Acompanhamento PSM/CID — Entrega 2

**Data da coleta:** 17/11/2026 (Coleta 2 da E2, Seção 4.1 do plano)  
**Dados consultados em:** 16/11/2026, às 08h40 (Brasília), no GitHub (issues, PRs, revisões e `git log` da `main`)  
**Responsável:** Heitor Macedo Ricardo  
**Plano de referência:** [`gestao/plano-psm.md`](plano-psm.md), versão 1.2  
**Coleta anterior:** [`gestao/coleta-intermediaria-e2.md`](coleta-intermediaria-e2.md)  
**Situação deste documento:** rascunho. Os valores valem para 16/11 às 08h40 e devem ser conferidos
de novo em 17/11, antes da reunião (Seção 6). As decisões da Seção 4 são propostas; passam a valer
depois que a equipe as confirmar em ata.

Esta é a segunda coleta da Entrega 2 e o primeiro cálculo de M-CP1 e M-RC1 com a E2 planejada.
Em 16/11, 4 das 8 issues da E2 estavam fechadas (#28, #46, #53 e #55). A #46 (Fase 3) foi fechada
às 08h34 de 16/11, um dia depois do prazo, com 3 de 14 critérios marcados e sem hora real. Os PRs
#61 (plano da Fase 3) e #62 (preparo da análise da Fase 4) entraram na `main` no mesmo minuto.
Restam 4 issues abertas (#36, #47, #48 e #49), com 48 h estimadas, para 6 dias até a Entrega 2
(22/11).

## 1. Métricas do plano

| Métrica | Valor em 16/11 | Situação | Interpretação |
|---|---|---|---|
| M-CP1 — Cumprimento de marcos | Data de corte 17/11: vencem 4 issues (#53, #28, #46 e #55); as 4 estão fechadas. ICM = 4 de 4 (100%). Das 8 issues da E2, 4 estão fechadas | Verde, com ressalva | O valor está na faixa Verde (85% ou mais). A ressalva: a #46 fechou 1 dia depois do prazo e com 11 de 14 critérios sem marcação (veículo real, piloto, prints com login, iPhone, rótulos confirmados). Esses critérios empíricos não têm issue que os acompanhe, e o ICM não os vê |
| M-RC1 — Variação de esforço | Issues fechadas com horas: #28 (1 h para 3 h), #53 (3 h para 4 h) e #55 (1 h para 1 h). Total: 5 h reais para 8 h estimadas (−37,5%). A #46 (11 h estimadas) fechou sem hora real e fica fora do cálculo | Amarelo (−40% a −20%) | A estimativa inclui a margem de 32% (fator 1,1 × 1,2). Contra a base de 6 h, o real de 5 h dá −17%. A amostra são 3 issues pequenas; as 4 abertas somam 48 h estimadas, sem hora real registrada, e vão decidir o resultado |
| M-RC2 — Contribuição individual | 5 h reais registradas na E2: Heitor 3 h, Daniel 1 h, Pedro Druck 1 h; Hugo, Pedro Henrique e Philipe com 0 h | Não interpretável | Só 3 dos 6 integrantes têm hora registrada. A #46 fechou com 0 h reais, e o PR #57 tem 5 commits (Hugo 3, Philipe 2). O cálculo definitivo é na coleta de 21/11 |
| M-DP1 — Retrabalho em revisão | 0 de 7 PRs com pedido de ajuste ou commit depois da revisão (#52, #54, #56, #57, #58, #59 e #62) | Verde (até 30%) | Nenhum dos 7 PRs recebeu *Changes Requested* nem commit posterior à primeira revisão. O #61 foi mesclado sem revisão registrada e fica fora do denominador. Em 6 dos 7 PRs, o merge ocorreu até 1 minuto depois da aprovação (exceto o #57): a métrica só vê o retrabalho que deixa rastro no GitHub |

*Tabela 1 — Métricas do plano em 16/11/2026. Fonte: issues #28, #36, #46 a #49, #53 e #55; PRs #52, #54, #56, #57, #58, #59, #61 e #62, no GitHub.*

Desvio de esforço por integrante nas issues fechadas com horas: Daniel −66,7% (#28), Heitor −25,0%
(#53) e Pedro Druck 0% (#55). O plano só define faixa de alerta acima de +40%; o desvio abaixo de
−40% não tem cor definida.

## 2. Ações da retrospectiva

| Ação | Métrica | Valor em 16/11 | Situação |
|---|---|---|---|
| C1 — PR revisado em até 48 h (Daniel) | Tempo até a 1ª revisão | 7 PRs com revisão: #52: 5 min; #56: 6 min; #58: 2,2 h; #62: 7,3 h; #59: 8,2 h; #54: 11,4 h; #57: 48,4 h (aberto em 13/11 às 21h47, 1ª revisão humana em 15/11 às 22h12). Mediana: 7,3 h; 1 PR acima de 48 h. O #61 foi mesclado sem revisão registrada. O #60 está em aberto desde 16/11 às 00h24 e vence em 18/11 | Amarelo (1 PR acima de 48 h) |
| C3 — Lista de bloqueios da #46 com responsável e data (Hugo) | M-CP1 | O plano da Fase 3, com 8 bloqueios (B01 a B08), cada um com responsável e prazo, está na `main` (PRs #61 e #62). A lista de pendências no corpo da #46 continua sem responsável e data. Os prazos (14 e 15/11) passaram, sem evidência de resolução no repositório | Cumprida na `main`, com 2 semanas de atraso em relação ao prazo de 30/10 |
| C3 — Repassar pendências em toda reunião (Pedro Henrique) | M-CP1 | Repassadas em 10/11 ([ata 04](../atas/ata-04-2026-11-10.md)). Sem reunião registrada na semana de 16/11 até agora | Aplicada em 10/11 |
| C5 — Revisor em rodízio (Philipe) | M-RC2 aplicada às revisões | 8 de 8 issues da E2 com revisor. Em 5 dos 6 PRs com revisor designado (#54, #56, #57, #58 e #62), o revisor foi o designado; no #59, o designado era Pedro Druck e a revisão foi de Philipe. Revisões desde 30/10 (8 no total): Pedro Henrique 3 (37,5%), Philipe 2 (25%), Heitor 2 (25%), Hugo 1 (12,5%), Daniel 0 e Pedro Druck 0 | Cumprida na designação; concentrada na execução |
| C6 — Sem commit direto na `main` (Pedro Druck) | M-DP1 e commits diretos | 4 commits diretos depois do fechamento da E1: `0c32d68` e `c29861b` (28/10) e `dced9e2` e `d7ed7a6` (11/11, sem PR associado). Nenhum depois de 11/11. O PR #61 foi mesclado sem aprovação registrada, o que a proteção da `main` permite aos administradores | Vermelho (proposto): a regra foi mantida na reunião de 10/11 e quebrada em 11/11 |
| C7 — Atas ÷ reuniões (Heitor) | Atas ÷ reuniões | 2 reuniões registradas (28/10 e 10/11), com 2 atas: 100%. A ata 03 saiu fora do prazo de 24 h, como já registrado em 10/11 | Amarelo |
| C7 — Frequência das reuniões | Semanas com reunião ÷ semanas | Semana de 26/10: 1; 02/11: 0; 09/11: 1; 16/11: 0 até agora. Resultado: 2 de 3 semanas fechadas (67%) | Vermelho |

*Tabela 2 — Ações da retrospectiva em 16/11/2026. Fonte: PRs e revisões no GitHub, `git log --first-parent` da `main`, pasta `atas/` e [`gestao/retrospectiva-e1.pdf`](retrospectiva-e1.pdf).*

A proteção da `main` exige 1 aprovação em PR, mas a opção que aplica a regra também aos
administradores (`enforce_admins`) está desativada. Por isso, quem é administrador consegue enviar
commit direto e mesclar sem aprovação. Essa é uma explicação possível para os commits de 11/11 e
para o merge do #61, mas ela não foi confirmada.

## 3. Decisões anteriores (D1 a D7)

| # | Decisão da coleta de 10/11 | Situação em 16/11 |
|---|---|---|
| D1 | Dar responsável, revisor, data e estimativa às issues da E2 | Feita em 10/11 |
| D2 | Priorizar a #46 antes do ponto de controle | Cumprida com 1 dia de atraso: a #46 foi fechada em 16/11 às 08h34, e o plano da Fase 3 está na `main`. Ficam 11 de 14 critérios sem marcação |
| D3 | Reunião da semana com ata | Feita em 10/11; falta a da semana de 16/11 |
| D4 | Completar a lista de bloqueios da #46 | Feita (13/11) e na `main` desde 16/11 |
| D5 | Conferir de novo os commits diretos na `main` | Conferido: nenhum commit direto novo depois de 11/11 |
| D6 | Registrar as horas reais da #51 | Não feita: a #51 continua com a estimativa de 3 h e sem hora real |
| D7 | Publicar o plano v1.2 | Feita em 11/11 (PR #54) |

*Tabela 3 — Situação das decisões anteriores. Fonte: [`gestao/coleta-intermediaria-e2.md`](coleta-intermediaria-e2.md), issues e PRs no GitHub.*

## 4. Decisões propostas

| # | Gatilho | Decisão proposta | Responsável | Prazo |
|---|---|---|---|---|
| D8 | M-CP1: #46 fechada com 11 de 14 critérios sem marcação | Registrar na #47 (ou em uma issue nova) os critérios empíricos que ficaram sem cumprir (veículo real e consentimento, piloto, prints com login nos dois canais, iPhone, rótulos confirmados), com responsável e data; ou reabrir a #46 | Hugo e Philipe; Pedro Henrique confirma | 17/11 |
| D9 | M-RC2: só 3 de 6 integrantes com hora registrada; a #46 fechou sem hora | Registrar as horas reais nas issues à medida que o trabalho acontece e, no máximo, até 20/11, antes da coleta de fechamento | Todos; Daniel confere | 20/11 |
| D10 | C6 reincidente e merge do #61 sem aprovação registrada | Ativar a regra para administradores na proteção da `main` e combinar que só se mescla PR com aprovação de outra pessoa | Quem tiver permissão de administrador; Pedro Druck confirma | 17/11 |
| D11 | C1: #57 acima de 48 h; #60 em espera | Avisar o revisor no grupo ao abrir o PR; o #60 vence em 18/11 | Autor de cada PR; revisor | Contínuo |
| D12 | C7: semana de 16/11 sem reunião | Marcar a reunião da semana com ata; pauta: D8 a D10, bloqueios da Fase 3 e preparo da apresentação final | Heitor (ata); Pedro Henrique (pauta) | 22/11 |
| D13 | C5: Daniel e Pedro Druck com 0 revisões; #59 revisado por quem não era o designado | Manter o rodízio já designado (Daniel revisa #47 e #36, Heitor revisa #48, Pedro Druck revisa #49) e dirigir o #60 a Daniel | Philipe | 21/11 |
| D14 | Pendências de registro | Sincronizar as datas das issues #47 e #48 no Project 38 (bloqueio B08); registrar as horas da #51; alinhar o prazo da #55 (corpo da issue: 17/11; documentos: 11/11); marcar os critérios das issues #53 e #55, fechadas com a lista sem marcação | Hugo (Project); Pedro Druck (#51 e #55); Heitor (#53) | 20/11 |
| D15 | O #59 foi mesclado na branch da issue #46 depois do #61, então as páginas `fase4.md` e `fase4-melhoria.md`, o menu, o rodapé 1.1 e o alt-text não estão na `main` | Levar essas mudanças para a `main` em um PR novo, reconciliando o menu da Fase 4 com a página de análise do #62 | Heitor | 17/11 |

*Tabela 4 — Decisões propostas. Fonte: Seções 1 a 3 deste documento.*

## 5. Riscos até a Entrega 2

| Risco | Evidência | Efeito |
|---|---|---|
| Critérios empíricos da Fase 3 sem dono | A #46 foi fechada com 3 de 14 critérios marcados; nenhuma issue aberta acompanha veículo real, piloto, prints com login e iPhone | A coleta da #47 depende deles; sem acompanhamento, ficam sem data |
| Cadeia crítica curta | #47 vence em 18/11, #48 em 20/11, #36 em 21/11 e #49 em 22/11; 48 h estimadas nas 4 issues abertas | Qualquer atraso da #47 empurra a análise, a ação de melhoria e o fechamento |
| Recursos da coleta não confirmados | Veículo com infração e consentimento dependem de terceiros (B01); o plano informa que não há confirmação nem evidência de execução. A equipe informou em 16/11 que tem um iPhone, mas modelo e versões ainda não estão registrados (B03) | Sem veículo real, as sessões da #47 não acontecem; sem o registro do iPhone, o iOS continua como contexto não avaliado |
| Esforço pouco registrado | 0 h reais nas 4 issues abertas e na #46, que fechou sem hora | PCI e TVE do fechamento ficam sem base; a tabela de contribuição do artigo depende dessas horas |
| Limite de 15 páginas do artigo | O `main.tex` na `main` já inclui `fase3-plano.tex` e `fase4-analise.tex`; o PDF versionado, de 15 páginas, é da E1 e não tem essas seções. A contagem atual não foi verificada | Risco de passar de 15 páginas (regra do projeto) quando a Fase 4 e a conclusão entrarem |
| Qualidade e rigor da revisão pouco visíveis | 6 de 7 PRs mesclados até 1 minuto depois da aprovação; o #61 foi mesclado sem revisão | M-DP1 em 0% pode esconder retrabalho que não deixa rastro |

*Tabela 5 — Riscos da E2. Fonte: Seções 1 e 2; cronograma da Fase 3; `artigo/main.tex`.*

## 6. O que atualizar em 17/11

Antes da reunião, conferir de novo e atualizar a Tabela 1 com:

- critérios empíricos da Fase 3: se foram migrados para a #47 ou se a #46 foi reaberta (D8);
- horas reais lançadas nas issues, que mudam o M-RC1 e o M-RC2;
- revisão do PR #60 (tempo até a 1ª revisão, M-DP1 e revisões por integrante) e novos PRs;
- novos commits diretos na `main` (`git log origin/main --first-parent --no-merges`) e merges sem aprovação;
- situação do PR que leva as páginas da Fase 4 para a `main` (D15);
- reunião da semana de 16/11 e ata correspondente.

## 7. Próxima coleta

A coleta de fechamento acontece em 21/11/2026, antes da Release E2 (22/11), conforme a Seção 4.1 do
plano. Ela fecha M-RC2 e a Tabela de Contribuição.
