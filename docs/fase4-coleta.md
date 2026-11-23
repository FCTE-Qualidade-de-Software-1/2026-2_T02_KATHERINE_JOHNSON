# Fase 4 — Coleta, pendências e cálculo

**Continuação S06/V4 em 22/11:** novo titular coberto pelo consentimento aplicado, com outro
veículo, Samsung SM-S731B e computador 750XGK. Os registros brutos estão nesta branch;
consulte `evidencias/fase4/S06-registro-2026-11-22.md` e `evidencias/fase4/S08-registro-2026-11-22.md`.
P4 tem gravações provisórias; o bloco da lista no Android foi excluído por esperas artificiais
de rolagem, e a M2.1.1 do aplicativo permanece inconclusiva. P5 foi concluído nos dois canais
(10 leituras válidas cada). P7 foi executado só no portal, em Wi-Fi, rede degradada e 4G (S08);
o P7 do aplicativo não foi avaliado. Os tempos são propostas automáticas pendentes de
marcação visual e segunda leitura independente. Nenhum resultado dessa continuação foi promovido
a julgamento oficial, e nenhum original identificável é público.

**Consentimento concluído:** Hugo confirmou em 22/11/2026 a aplicação dos termos aos participantes
da coleta. As vias assinadas e datas individuais permanecem privadas, sem publicação na GitPage.

**Atualização documental em 22/11:** o PR #67 foi aprovado por Daniel em 21/11 antes do merge.
A branch `feat/pedro-s03-fase4` registra tentativas P6 em CT01/CT03/CT05 de 21/11, ainda sem
conferência independente; a [análise](fase4-analise.md) referencia a fonte imutável e suas
limitações. Os quadros datados de 20/11 abaixo preservam a situação daquela revisão.

Situação documental conferida em **20/11/2026**. Responsáveis pela
[#47](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/47):
Hugo, Pedro Druck e Philipe; revisão da entrega por Daniel.
O prazo planejado de 18/11 venceu. O relatório recebido registra observações do piloto no portal
e dez valores informados para tempo/transferência; S01 não entra nos resultados oficiais. O script
de cálculo e os instrumentos estão preparados; isso não conclui a coleta.

## Atualização dos bloqueios em 20/11

Foi comunicada a concordância de três integrantes para usar suas próprias contas na avaliação.
O [registro da concordância](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/consentimento.md)
foi atualizado; as vias individuais e a declaração nominal permanecem privadas. A correspondência
com veículos ainda precisa ser conciliada. **Atualização em 22/11:** Hugo confirmou a aplicação
dos termos; as vias assinadas permanecem privadas e não são publicadas na GitPage.

| Item do acompanhamento | Situação verificada agora | Próximo passo |
|---|---|---|
| B01 — titular, veículo e consentimento | Termos aplicados, conforme confirmação de Hugo em 22/11; vias assinadas privadas | Conciliar códigos e confirmar veículo com infração acessível nos dois canais |
| B02 — aparelhos | D03 tem caracterização parcial; computador Linux candidato a D01 foi inspecionado | Confirmar o computador inspecionado como D01; completar D02/D03 e instrumentos por sessão |
| B03 — iPhone | PR #66 continua aberto; aparelho sob responsabilidade de Heitor | Heitor registra modelo, iOS e versão do app |
| B05 — telas e rótulos | Seis capturas do portal disponíveis; levantamento autenticado dos apps sem registro | Titulares fazem login pessoalmente; executar e conferir as capturas dos apps |
| B08 — Project 38 | Nova consulta de 20/11 ainda sem escopo `read:project` | Conta autorizada sincroniza as datas confirmadas |
| S01 — piloto | Não há registro de liberação nem sessão executada; aba do portal localizada, mas a leitura da interface expirou | Restabelecer leitura suportada, conectar Android, validar instrumentos e só então registrar execução/conferência |
| Script e branch da #47 | Entregues no PR #67 | Revisar o código e usar o cálculo após as medições |
| Aprovação da entrega | Checks automáticos aprovados no commit a90f6fe; nenhuma revisão humana registrada no PR #67 | Daniel realiza a revisão designada; conferentes registram somente leituras que executarem |

*Quadro de situação — Declaração recebida, inspeção local e consultas ao GitHub em 20/11/2026.*

O [registro de preparação do computador](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/preparacao-ambiente-2026-11-20.json)
documenta sistema e versões dos navegadores, sem a configuração detalhada do equipamento. Na
inspeção técnica inicial nenhum navegador estava conectado; depois a aba do portal foi localizada,
mas a leitura da interface expirou. Nenhum Android foi identificado por USB. Não foram coletadas
senhas, capturadas telas de autenticação ou executadas operações sobre infrações.

## S00 e S01: evidências e critérios de conclusão

| Etapa | Estado documental | Evidência disponível | Condição para concluir |
|---|---|---|---|
| **S00 — preparação** | **Parcial** | Concordância informada para três integrantes, vias individuais preparadas, computador candidato a D01 inspecionado e D03 parcialmente caracterizado | Consentimentos concluídos (confirmação em 22/11); conferir códigos da massa, disponibilidade dos titulares e inventário efetivo por sessão |
| **S01 — piloto** | **Parcial, sem liberação registrada** | Relatório do portal registra presença de campos, três percursos, três acessos ao detalhe e duas capturas anonimizadas; dez valores de tempo/volume foram informados em tabela separada | Conferir instrumento, aquecimento e evidências; completar captura da lista de infrações e registrar liberação por procedimento |

O [roteiro de medições e capturas](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/roteiro-medicoes-e-capturas.md) consolida
as repetições, os oito CSV, o estado factual da preparação e os nomes/destinos exatos das imagens
que devem ser produzidas e revisadas antes de entrarem no repositório.

O responsável informou que os dez tempos foram medidos com cronômetro digital. Essa informação
foi acrescentada ao relatório S01; ela identifica o instrumento, mas não muda o status de piloto
nem comprova aquecimento ou conferência independente. A origem e a unidade do volume também
precisam ser identificadas antes de seu uso oficial.

O [relatório recebido da sessão S01 no portal para PC](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/relatorio-s01-portal-2026-11-20.md)
registra a contagem de campos, três percursos, três acessos ao detalhe, duas capturas anonimizadas
e os dez valores de tempo/volume enviados na tabela. Esses dados são do piloto, não entram no
cálculo oficial e ainda não têm evidência suficiente do aquecimento/método de timing/instrumento
de transferência para validação. A cronologia de 21:38–21:41 BRT é compatível com a revisão feita
às 21:54 BRT em 20/11.

**A revisão documental está concluída; as sessões continuam sem comprovação de conclusão.**
As capturas demonstram telas acessadas no portal, mas não identificam por si só executor,
registrador, horário da sessão ou consentimento aplicado. Também não demonstram as repetições
exigidas para as métricas. A data desta revisão não é uma data de coleta.

### Percurso do portal já documentado

As imagens abaixo foram incorporadas no
[commit aa9d3bb](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/commit/aa9d3bb38b0b905219004a005edffb9691daadee),
de 15/11/2026, cujo autor no Git é Philipe Caetano. Essa informação identifica a inclusão dos
arquivos, sem atribuir a execução da sessão a um integrante. Os nomes originais foram preservados;
a descrição desta tabela segue o conteúdo visível de cada imagem.

| Evidência | O que a captura permite conferir |
|---|---|
| [Menu de infrações](img/passoApassoConsulta/dropDownInfrações.png) | Acesso à opção de histórico por veículo |
| [Lista de veículos](img/passoApassoConsulta/pageConsultaDeInfrções.png) | Seleção de veículo na área autenticada |
| [Filtro de período](img/passoApassoConsulta/pageSeleçãoDeUmDosVeículos.png) | Campos de início/fim e ação Consultar |
| [Resultado da consulta](img/passoApassoConsulta/pageConsultaDeInfraçõesDefinindoData.png) | Lista com infração e acesso ao detalhamento |
| [Detalhamento](img/passoApassoConsulta/pageDetalhesDaInfração.png) | Rótulos e campos exibidos para a infração consultada |
| [Limite temporal](img/passoApassoConsulta/pageSeleçãoDeUmDosVeículosLimite5Anos.png) | Mensagem de erro para período anterior ao limite informado |

*Quadro de evidências — Inspeção documental das seis imagens versionadas, em 20/11/2026.*

### O que falta registrar para encerrar as sessões

| Registro | Quem providencia | Evidência mínima |
|---|---|---|
| Massa de dados (consentimento concluído) | Hugo | Aplicação confirmada em 22/11; conciliar códigos com a tabela privada. Vias assinadas, datas individuais e identidades permanecem privadas |
| Inventário efetivo | Hugo (D01–D03); Heitor (D04) | Aparelhos, versões instaladas e instrumentos usados em cada sessão/contexto/rede |
| Levantamento dos aplicativos | Hugo e Philipe (Android); Heitor (iOS) | Lista de veículos, lista de infrações e detalhes, com capturas revisadas e correspondência com a massa |
| Validação técnica do piloto | Philipe, com os executores | Rede comum, perfis nos dois sentidos, contador de volume e método de marcação de tempo verificados |
| Conferência e liberação | Hugo e Philipe registram; conferente independente identificado | Registro de sessão preenchido, duas leituras e decisão por procedimento: liberado, parcial ou bloqueado |

Usar o [modelo de sessão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/modelo-sessao.md)
para registrar fatos observados. A ausência de registro não determina se a atividade ocorreu
fora do repositório; até sua comprovação, o critério permanece pendente. O campo de revisor e a
liberação devem ser preenchidos somente depois da conferência efetiva.

## 1. Pendências herdadas da Fase 3

O [comentário de acompanhamento da #46](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/46#issuecomment-6922711169)
identifica sete critérios ainda parciais ou pendentes. Esta página reúne seu acompanhamento
para a #47. As datas abaixo preservam a **proposta de 19/11**, sujeita à disponibilidade do titular e à
confirmação de Hugo e Philipe com Pedro Henrique; não são sessões realizadas ou acordos registrados.
Na conferência de 20/11, não foi localizado registro de confirmação dessa agenda.

| Critério | Responsável | Situação verificada | Próxima ação / evidência de conclusão | Data proposta |
|---|---|---|---|---|
| Ambiente detalhado (B02) | Hugo | Parcial: modelo do Android intermediário registrado; demais versões pendentes | Preencher inventário por sessão/contexto/rede, incluindo versão instalada do app | 19/11 |
| Consentimento aplicado (B01) | Hugo | **Concluído:** aplicação dos termos confirmada por Hugo em 22/11/2026 | Vias assinadas e datas individuais mantidas privadas; nenhuma publicação das assinaturas na GitPage | Confirmação em 22/11; não representa a data de aplicação |
| Sessão com veículo real (S01/S02) | Hugo; Philipe registra; Pedro Druck confere | Sem registro de execução | Confirmar infração acessível nos dois canais; executar piloto e registrar sua liberação | 19/11, após consentimento |
| Prints autenticados (B05) | Hugo e Philipe no Android; Heitor no iOS | Portal tem seis capturas; capturas dos apps pendentes | Lista de veículos, lista de infrações e detalhes; revisão das tarjas por outro integrante | 19–20/11 |
| Rótulos, campos e passos (B05) | Hugo e Philipe | Confirmação com veículo real pendente | Registrar roteiro e contagens; atualizar Fase 1 apenas com evidência | 19–20/11 |
| Registro do iPhone (B03) | Heitor | Aparelho de Heitor; modelo/iOS/app ainda não registrados | Inventário D04 e execução de CT06; declarar não avaliado se não executado | 20/11 |
| Datas das issues no Project (B08) | Hugo | Consultas de 19 e 20/11 bloqueadas por falta de `read:project` | Conferir e sincronizar #47/#48 com conta autorizada; registrar data e link do quadro | Até 20/11 |

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

Com os consentimentos aplicados, depois de registrar piloto, medições e conferência:

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

Os resultados alimentam a [análise GQM](fase4-analise.md). O consentimento está concluído,
conforme confirmação de Hugo em 22/11; coleta e revisão continuam pendentes; o PR de implementação do cálculo não deve encerrar automaticamente a #47.
