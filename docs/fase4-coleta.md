# Fase 4 — Coleta, pendências e cálculo

Situação conferida em **19/11/2026**. Responsáveis pela
[#47](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/47):
Hugo, Pedro Druck e Philipe; revisão da entrega por Daniel.
O prazo planejado de 18/11 venceu e os oito instrumentos brutos continuam sem medições.
O script de cálculo e os testes estão preparados; isso não conclui a coleta.

## 1. Pendências herdadas da Fase 3

O [comentário de acompanhamento da #46](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/46#issuecomment-6922711169)
identifica sete critérios ainda parciais ou pendentes. Esta página reúne seu acompanhamento
para a #47. Novas datas abaixo são **propostas**, sujeitas à disponibilidade do titular e à
confirmação de Hugo e Philipe com Pedro Henrique; não são sessões realizadas ou acordos registrados.

| Critério | Responsável | Situação verificada | Próxima ação / evidência de conclusão | Data proposta |
|---|---|---|---|---|
| Ambiente detalhado (B02) | Hugo | Parcial: modelo do Android intermediário registrado; demais versões pendentes | Preencher inventário por sessão/contexto/rede, incluindo versão instalada do app | 19/11 |
| Consentimento aplicado (B01) | Hugo | Sem comprovação registrada | Titular lê e assina o termo; guardar via privada, publicar apenas código e data | 19/11, antes do piloto |
| Sessão com veículo real (S01/S02) | Hugo; Philipe registra; Pedro Druck confere | Sem registro de execução | Confirmar infração acessível nos dois canais; executar piloto e registrar sua liberação | 19/11, após consentimento |
| Prints autenticados (B05) | Hugo e Philipe no Android; Heitor no iOS | Portal tem seis capturas; capturas dos apps pendentes | Lista de veículos, lista de infrações e detalhes; revisão das tarjas por outro integrante | 19–20/11 |
| Rótulos, campos e passos (B05) | Hugo e Philipe | Confirmação com veículo real pendente | Registrar roteiro e contagens; atualizar Fase 1 apenas com evidência | 19–20/11 |
| Registro do iPhone (B03) | Heitor | Aparelho de Heitor; modelo/iOS/app ainda não registrados | Inventário D04 e execução de CT06; declarar não avaliado se não executado | 20/11 |
| Datas das issues no Project (B08) | Hugo | Consulta de 19/11 bloqueada por falta de `read:project` | Conferir e sincronizar #47/#48 com conta autorizada; registrar data e link do quadro | Até 20/11 |

*Tabela 1 — Acompanhamento dos critérios de execução. Fonte: #46, #47 e consulta ao Project em 19/11.*

As correções sobre o iPhone estão no
[PR #66](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/66).
Heitor executa as atividades que dependem desse aparelho. A disponibilidade não comprova coleta.
O piloto também depende da validação da rede e do contador de volume por Philipe (B04).

## 2. Sequência de execução e reagendamento proposto

Manter o [método P1–P7](fase3-metodo.md), o
[inventário](fase3-ambiente.md) e o [modelo de sessão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/modelo-sessao.md).
O [cronograma original](fase3-cronograma.md) permanece como histórico; as datas desta tabela
ainda precisam ser confirmadas nas issues e no Project.

| Ordem | Sessão / atividade | Execução e registro | Conferência | Janela proposta / condição |
|---|---|---|---|---|
| 1 | S00: titular, veículo, termo e inventário | Hugo; Philipe registra | Pedro Henrique | 19/11; disponibilidade do titular |
| 2 | S01: piloto, telas e validação dos instrumentos | Hugo; Philipe registra | Pedro Druck | 19/11; após S00 |
| 3 | S02: P1–P5 nos contextos de referência | Hugo; Philipe registra | Pedro Druck | 19–20/11; piloto liberado |
| 4 | S03: P6 por plataforma/navegador | Pedro Druck; Hugo registra; Heitor executa CT06 | Philipe | 20/11; inventários confirmados |
| 5 | S04: P7 nas três redes | Philipe; Pedro Druck registra | Hugo | 20/11; redes validadas nos dois sentidos |
| 6 | S05: contingências, anonimização e cálculo | Hugo, Pedro Druck e Philipe | Daniel revisa a entrega | 20/11; antes de passar dados à #48 |

*Tabela 2 — Proposta de recuperação da coleta. Fonte: sequência do plano da Fase 3.*

A análise #48 mantém o prazo original de **20/11** e a E2, **22/11**. Coletar até 20/11 comprime
o tempo de análise: Pedro Henrique e Philipe precisam confirmar a viabilidade antes de aceitar
a proposta. Se o titular ou instrumentos não estiverem disponíveis, registrar o impedimento,
replanejar com a equipe e manter métricas sem medição inconclusivas. Não reduzir repetições
silenciosamente nem converter reservas de agenda em horas reais.

## 3. Validação e cálculo

Depois de registrar consentimento, piloto, medições e conferência:

```bash
python3 dados/scripts/calcular.py --validar
python3 dados/scripts/calcular.py --exigir-dados
```

O [script](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/scripts/calcular.py)
calcula as 14 métricas a partir dos CSV, aplica os níveis da Fase 2 antes do arredondamento e
gera resultados com sessão, bloco, evidências e manifesto SHA-256. As instruções completas,
regras de exclusão e limites da validação estão no
[dicionário](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/README.md).

No estado atual, há **zero resultados calculáveis**. A consolidação registra 25 estados
inconclusivos e um não aplicável (navegadores no aplicativo); esses registros não são medições.
Os testes automatizados usam dados sintéticos temporários, separados dos instrumentos reais.
O validador não substitui a revisão humana de consentimento, tarjas, piloto ou independência
do conferente.

## 4. Entrega para análise e registros de gestão

- [ ] Confirmar novas datas na #47 com a equipe; conferir impacto na #48.
- [ ] Preencher inventário, cadastro anonimizado e registro de liberação do piloto.
- [ ] Executar os blocos, guardar originais em local privado e publicar apenas evidências revisadas.
- [ ] Preencher os oito CSV; registrar falhas, exclusões e reposições com seus desvios.
- [ ] Executar validação/cálculo e revisar cobertura, amostras reduzidas e limitações.
- [ ] Versionar dados, evidências, resultados e manifesto no mesmo PR; Daniel revisa a entrega.
- [ ] Registrar horas efetivamente trabalhadas por integrante nas #46/#47 até 20/11.
- [ ] Conferir datas no Project 38 e registrar a sincronização; indisponibilidade de acesso não equivale a conclusão.

As horas reais ainda precisam ser informadas pelos integrantes. O quadro remoto não foi
alterado: a credencial desta execução não dispõe de `read:project`; a escrita também exige
autorização `project`. A leitura bloqueada não permite saber se os itens ou campos estão ausentes.
Depois de obter acesso, localizar as issues #47/#48, conferir os campos de início e prazo e
aplicar as datas **confirmadas pela equipe**, preservando o histórico do atraso.

Os resultados alimentam a [análise GQM](fase4-analise.md). Consentimento, coleta e revisão
continuam pendentes; o PR de implementação do cálculo não deve encerrar automaticamente a #47.
