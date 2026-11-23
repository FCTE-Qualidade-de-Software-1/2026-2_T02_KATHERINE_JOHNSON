# Fechamento documental PSM/CID da Entrega 2

**Consulta:** 2026-11-22T02:00:20-03:00. **Corte:** 2026-11-22. A coleta prevista para 21/11 foi realizada em 22/11; não foi retrodatada.

**Estado:** fechamento apurado com as evidências disponíveis; contribuição final e esforço global incompletos por falta de declarações dos demais integrantes. Ausência de horas não é zero.

## Indicadores e alcance

| Indicador | Resultado | Interpretação |
|---|---|---|
| M-CP1 | 4/8 = 50,00% | Vermelho; issues fechadas [28, 46, 53, 55]. A #46 foi fechada com critérios empíricos pendentes e um dia de atraso |
| M-RC1 | 5,00 h / 8,00 h = -37,50% | Amarelo, somente issues fechadas com horas [28, 53, 55]; não é TVE global |
| M-RC2 | 27 h 25 min conhecidas; PCI final não apurável | Declaração total de Hugo e Heitor e registros parciais de dois integrantes; dois sem horas informadas |
| M-DP1 | 0/13 = 0,00% | Conta PR com revisão humana; PRs sem revisão excluídos: [61]; verde não comprova revisão profunda |

*Tabela 1 — Indicadores no corte. Fonte: consulta de issues e PRs e plano PSM/CID.*

O ICM conta fechamento formal, sem converter critérios pendentes em entregas concluídas. Até 21/11 venciam sete issues e quatro estavam fechadas (57,14%); em 22/11 a #49 entra no denominador (50,00%). As datas de fechamento são preservadas na fonte.

M-DP1: avaliados [52, 54, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67]; com retrabalho []. Inclui PRs avaliados ainda abertos e PRs de conteúdo integrados na branch da Fase 3, seguindo o alcance da coleta anterior. Bots não contam como revisão humana. Retrabalho é Changes Requested ou commit posterior à primeira revisão humana, dentro do corte.

Daniellira540: 2Espera pela primeira revisão: mediana 8,24 h; 2 PR(s) acima de 48 h. Revisões por login: , HeitorM50: 3Espera pela primeira revisão: mediana 8,24 h; 2 PR(s) acima de 48 h. Revisões por login: , HugoFreitass: 1Espera pela primeira revisão: mediana 8,24 h; 2 PR(s) acima de 48 h. Revisões por login: , PedroGTG: 5Espera pela primeira revisão: mediana 8,24 h; 2 PR(s) acima de 48 h. Revisões por login: , Phill-Chill: 2Espera pela primeira revisão: mediana 8,24 h; 2 PR(s) acima de 48 h. Revisões por login: , pedruck: 1.

## Horas e contribuição da E2

| Integrante | Estimativa individual | Horas conhecidas | Alcance | Participação nas horas conhecidas |
|---|---|---|---|---|
| Daniel | 9 h 30 min | 1 h 00 min | Parcial | 3,65% |
| Heitor | 10 h 30 min | 11 h 00 min | Total individual declarado | 40,12% |
| Hugo | 10 h 50 min | 14 h 25 min | Total individual declarado | 52,58% |
| Pedro Druck | 14 h 20 min | 1 h 00 min | Parcial | 3,65% |
| Pedro Henrique | 5 h 30 min | Não informado | Não informado | Não apurável |
| Philipe | 16 h 20 min | Não informado | Não informado | Não apurável |

*Tabela 2 — Contribuição parcial, sem imputar zero às lacunas. Fonte: mesma consulta e declarações de Hugo e Heitor.*

O denominador da última coluna contém apenas as horas conhecidas; ele não é o esforço total da equipe e os percentuais não são o PCI final. A decisão de contribuição igual da E1 não foi estendida à E2.

**Hugo** declarou, em 23/11/2026, o total individual de **14 h 25 min** na E2, contra 10 h 50 min estimadas (variação individual +33,08%). Fonte: Declaração do próprio Hugo em 23/11/2026: total de 14 h 25 min na E2. Substitui a declaração de 22/11 (11 h 50 min). Estimativa-base: Rateio igual das estimativas coletivas pelos responsáveis do planejamento; não é rateio de horas reais. Escopo: Total individual da E2, sem distribuição declarada entre issues; substitui qualquer soma parcial das mesmas atividades, nunca adiciona duas vezes.

**Heitor** declarou, em 22/11/2026, o total individual de **11 h 00 min** na E2, contra 10 h 30 min estimadas (variação individual +4,76%). Fonte: Estimativa de Heitor, calculada com apoio de Claude Code a partir de registros datados (commits, PRs, revisões, comentários e arquivos locais), agrupados em blocos de trabalho; não é cronometragem. Composição: 3 h da #53 (10 e 11/11), cerca de 5,3 h em 16/11 e cerca de 2,9 h em 22/11 até 12:58, somando 11,2 h; declarado: 11 h. Valor conferido e aceito por Heitor em 22/11/2026. Estimativa-base: Rateio igual da estimativa coletiva da #49 entre Daniel e Heitor (13 h ÷ 2 = 6 h 30 min) mais a #53 (4 h): 10 h 30 min; não é rateio de horas reais. Escopo: Total individual da E2 até 13:15 de 22/11, sem distribuição declarada entre issues; substitui as 3 h já registradas na #53, nunca adiciona duas vezes. Trabalho posterior a esse horário não está incluído.

O planejamento no corpo da #46 identifica Hugo e Philipe, embora a lista de assignees da API contenha só Hugo. Usou-se o planejamento explícito para ratear estimativas, coerente com a tabela histórica de horas. Estimativas individuais fracionárias são mantidas sem arredondamento no cálculo; a exibição em minutos arredonda apenas ao final.

## Resposta aos desvios

| Evidência | Encaminhamento documentado | Responsável designado | Estado |
|---|---|---|---|
| ICM abaixo de 70%; coleta/análise atrasadas | Priorizar conferência de S03 e registrar limitações antes da integração da análise | Equipe da #47; Heitor revisa #48 | Proposta para confirmação no PR |
| Esforço individual incompleto | Registrar totais individuais e atribuição por issue, conciliando totais sem duplicidade | Cada integrante; Daniel consolida | Hugo e Heitor declararam total; demais declarações pendentes |
| Tabela de contribuição ainda era da E1 | Substituir pelo retrato parcial E2; publicar final somente após todas as declarações | Integrador da #49 | Atualizada nesta branch |
| Relato de falha no aplicativo | Entregar proposta de processo, ficha e matriz de regressão da #36 | Revisão designada a Daniel | Artefato entregue; revisão e eficácia pendentes |
| Coleta final prevista para 21/11 sem registro | Apurar em 22/11 com data real, fontes e reprodução local | Consolidação desta entrega | Realizada; sem simular reunião da equipe |

*Tabela 3 — Tratamento dos desvios. Fonte: indicadores e issues #36, #47, #48 e #49.*

Esses encaminhamentos são propostas documentadas nesta revisão, não deliberações de uma reunião que não ocorreu. Não foram inventadas atas nem aprovações dos demais autores.

## Fontes e reprodução

- [Consulta datada e declarações individuais](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/gestao/dados/fechamento-e2-2026-11-23-v3.json).
- [Cálculo e testes](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/gestao/scripts).
- [Planejamento e histórico](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/gestao/plano-psm.md).

```bash
python3 gestao/scripts/fechar_e2.py
python3 -m unittest discover -s gestao/tests -v
```

O script não consulta a rede nem modifica issues. Recalcula JSON, este relatório e a página de fechamento da GitPage a partir da fonte datada. Novas horas exigem nova declaração identificada; não alterar a fonte histórica para simular disponibilidade anterior.
