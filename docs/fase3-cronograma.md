# Fase 3 — Cronograma e bloqueios

Versão 0.2 — 13/11/2026. Datas em horário de Brasília.

Os marcos de 15/11 (#46), 18/11 (#47), 20/11 (#48) e 22/11 (Entrega 2) seguem o planejamento confirmado na ata 04 de 10/11. **As datas e janelas abaixo são propostas de agenda, ainda sujeitas à disponibilidade dos titulares.** Duração é reserva de agenda, não esforço real registrado.

| Sessão / atividade | Data / janela proposta | Reserva | Executor / responsável | Registrador; conferência independente | Saída e dependência |
|---|---|---|---|---|---|
| S00 — inventário, recrutamento e consentimento | 14/11/2026, 09h–10h | 1 h | Hugo | Philipe; Pedro Henrique | Inventário, massa autorizada e horário do titular; condição para S01 |
| S01 — piloto e levantamento com login | 15/11/2026, 09h–11h | 2 h | Hugo | Philipe; Pedro Druck | Telas anonimizadas, rótulos, validação da rede e instrumentos; exige S00 |
| Revisão do plano #46 | 15/11/2026, 14h–15h | 1 h | Hugo e Philipe | Pedro Henrique (revisor designado) | Revisão do plano e decisão documentada sobre bloqueios |
| S02 — referência, P1–P5 | 16/11/2026, 14h–16h | 2 h | Hugo | Philipe; Pedro Druck | Campos, comparação, fluxo, tempos e volume; exige piloto aprovado |
| S03 — plataformas e navegadores, P6 | 17/11/2026, 09h–10h | 1 h | Pedro Druck | Hugo; Philipe | Três tentativas por contexto disponível e contexto indisponível explícito |
| S04 — redes, P7 | 17/11/2026, 10h–12h | 2 h | Philipe | Pedro Druck; Hugo | Dez tentativas por canal/rede, após aquecimento; exige rede validada |
| S05 — contingência e revisão dos dados #47 | 18/11/2026, 14h–16h | 2 h | Hugo, Pedro Druck e Philipe | Daniel revisa entrega | Repetições justificadas, evidências conferidas e dados entregues |
| Análise GQM #48 | 19–20/11/2026 | Conforme estimativa da issue | Pedro Henrique e Philipe | Heitor | Análise apenas dos dados elegíveis; prazo 20/11 |

*Tabela 1 — Sequência proposta das sessões. Fonte: elaborada a partir dos marcos da E2.*

P4 e P5 exigem dez repetições válidas por canal no contexto de referência; P3 exige três. P6 tem quinze tentativas no mínimo (cinco contextos obrigatórios × três), mais três se houver iOS. P7 tem sessenta tentativas medidas (dois canais × três redes × dez), além de seis aquecimentos. Se houver mais veículos, ampliar a reserva; não reduzir a amostra silenciosamente para caber na sessão. O titular deve estar disponível para autenticar novamente quando necessário.

## Bloqueios e critérios de resolução

Situação documental em 13/11/2026: não há confirmação dos recursos nem evidências de execução. As datas abaixo são prazos propostos de tratamento, não declarações de conclusão.

| ID | Pendência | Responsável | Prazo | Evidência para resolver / contingência |
|---|---|---|---|---|
| B01 | Veículo com infração e consentimento | Hugo | 14/11 | Código e data na massa; termo guardado privadamente. Sem isso, adiar sessões e comunicar impacto na #47 |
| B02 | Modelos, SO e versões dos dispositivos | Hugo | 14/11 | Inventário efetivo; sem aparelho obrigatório, registrar cobertura reduzida |
| B03 | Empréstimo de iPhone | Hugo | 15/11 | Inventário e telas; sem empréstimo, CT06 não avaliado e conclusão limitada ao Android |
| B04 | Rede controlada e contador de volume | Philipe | 15/11 | Piloto documentado; métrica/cenário inviável fica não medido |
| B05 | Telas autenticadas e confirmação dos rótulos | Hugo e Philipe | 15/11 | Evidências revisadas e atualização da Fase 1 no artigo e na GitPage |
| B06 | Revisão do plano e PR | Pedro Henrique; autores abrem PR | 15/11 | PR aprovado; registrar ajustes solicitados |
| B07 | Agenda dos titulares e sessões | Hugo | 14/11 | Horários acordados e atualização das sessões/Project |
| B08 | Conferência e sincronização de datas no Project | Hugo | 15/11 | Conta com acesso ao Project 38 verifica e registra as datas da tabela abaixo |

*Tabela 2 — Bloqueios com responsável e data. Fonte: elaborada para acompanhamento da #46.*

## Sincronização e passagem para a Fase 4

Os prazos finais preservam as datas registradas no corpo das issues e na
[coleta intermediária da E2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/gestao/coleta-intermediaria-e2.md).

| Issue | Início proposto | Prazo planejado confirmado no corpo da issue | Relação com as sessões |
|---|---|---|---|
| [#46 — plano](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/46) | 13/11/2026 | 15/11/2026 | S00, S01 e revisão do plano |
| [#47 — coleta](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/47) | 16/11/2026 | 18/11/2026 | S02–S05, após liberação do piloto |
| [#48 — análise](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/48) | 19/11/2026 | 20/11/2026 | Recebimento dos dados conferidos de S05 |

*Tabela 3 — Datas para sincronização do Project. Fonte: issues #46–#48 e plano de sessões.*

**Situação da sincronização em 13/11/2026:** a leitura dos campos do
[Project 38](https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/38) foi bloqueada por
ausência do escopo `read:project` na credencial. Os campos remotos não foram conferidos nem
alterados; o critério permanece pendente. Hugo deve usar uma conta com acesso, localizar os
itens #47/#48 (adicioná-los se ausentes), conferir os nomes dos campos de início/prazo e aplicar
as datas da Tabela 3. Registrar data da conferência e link ou captura do quadro sem dados
pessoais. Não presumir que a data escrita na issue atualiza automaticamente o Project.

Se S01 atrasar, registrar a decisão e o novo prazo nas issues e no Project antes de iniciar a
coleta. Na medição PSM/CID de 17/11, relatar bloqueios e horas efetivas; não registrar a reserva
da tabela como horas trabalhadas.

Para entregar #47 à #48, conferir: arquivos sem dados pessoais, inventário preenchido, consentimentos válidos, tentativas e desvios preservados, revisão independente e indicação de métricas/contextos não medidos. A issue #46 não deve ser considerada integralmente concluída enquanto faltarem os critérios empíricos e a aprovação do PR.
