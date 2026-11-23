# Massa de dados da avaliação

Responsável: integrante designado. Situação documental atualizada em 22/11/2026.

**Situação atualizada em 22/11/2026:** Hugo confirmou que os termos de consentimento foram
aplicados aos participantes da coleta. O [registro de aplicação](consentimento.md#9-aplicação-confirmada-em-22112026)
documenta a conclusão. As vias assinadas, datas de aplicação e correspondências permanecem
em armazenamento privado. A conciliação dos códigos dos veículos e a disponibilidade de
infrações nos dois canais são verificações separadas; não constituem pendência de consentimento.
Os códigos abaixo continuam como reservas, sem atribuição automática aos participantes.
Há capturas preexistentes do portal, indexadas no [acompanhamento da coleta](../docs/fase4-coleta.md),
mas elas não estabelecem correspondência com os novos participantes nem comprovam conclusão de S01.

## 1. Seleção e justificativa

Amostra intencional por disponibilidade e consentimento, sem pretensão de representar a frota do DF. Planejar até três veículos (V1–V3) e registrar todas as infrações selecionadas antes da coleta. O mínimo operacional é um veículo com pelo menos uma infração consultável nos dois canais; com esse mínimo, limitar as conclusões ao caso estudado.

Buscar variedade de situações (a vencer, vencida e paga), uma infração de outro órgão/RENAINF e uma de velocidade. São metas de diversidade, não ocorrências já confirmadas. Se ausentes, registrar a lacuna; não criar infrações nem presumir campos condicionais. Veículo sem infrações serve apenas como caso exploratório de lista vazia e não fornece denominador para completude de detalhes ou paridade.

Cada titular precisa aceitar o [termo de consentimento](consentimento.md), fazer login pessoalmente nos dois canais e estar disponível para nova autenticação. Nunca solicitar ou guardar senha. Usar a mesma seleção de veículos e infrações em ambos os canais; consultas comparadas devem ocorrer em até dez minutos, conforme P2.

## 2. Cadastro anonimizado

| Código reservado | Tipo de veículo | Nº de infrações selecionadas | Situações | Outro órgão? | Velocidade? | Consentimento (registro privado) | Sessão |
|---|---|---|---|---|---|---|---|
| V1 | A confirmar | A confirmar | A confirmar | A confirmar | A confirmar | Ver registro de aplicação; código reservado | S01, a agendar |
| V2 | Automóvel | 1 (V2-I1) | A ser lançada; multa com autuação notificada | Sim | Sim | Termo aplicado (ver registro de aplicação); via privada | S01 (piloto, 22/11) |
| V3 | A confirmar | A confirmar | A confirmar | A confirmar | A confirmar | Ver registro de aplicação; código reservado | A agendar |
| V4 | A confirmar | 1 (V4-I1, referência) | A confirmar | A confirmar | A confirmar | Termo aplicado (ver registro de aplicação); via privada | S06 e S08 (22–23/11) |

*Tabela 1 — Cadastro a preencher após recrutamento. Fonte: plano de avaliação.*

Atribuir V1-I1, V1-I2 etc. às infrações na tabela privada; manter os códigos estáveis entre sessões. Registrar no conjunto público apenas código, categoria necessária ao cálculo e indicadores de presença/consistência. Valores pessoais são comparados em ambiente privado, nunca transcritos no CSV público. Documentar a seleção e eventuais exclusões antes do cálculo.

### Seleção por procedimento

- P1/P2: usar todas as infrações selecionadas e cadastradas antes da sessão, nos dois canais.
  Se o titular disponibilizar muitas, escolher previamente até três por veículo, priorizando
  as categorias distintas acima; registrar quantidade disponível, quantidade selecionada e
  motivo da seleção no registro de sessão. Não excluir uma infração porque expôs divergência.
- P3–P7: escolher antes do piloto um veículo de referência e uma de suas infrações para o
  detalhamento; manter ambos em todas as repetições e contextos. Os dez registros de tempo
  são repetições do mesmo caso, não dez veículos nem dez participantes independentes.
- Veículos adicionais ampliam a verificação de campos e consistência; blocos adicionais de
  desempenho, se realizados, são analisados separadamente, com o tamanho da lista registrado.
- Se o vínculo, a infração ou sua situação mudar entre sessões, preservar o registro anterior,
  documentar a mudança e refazer o par afetado. Ausência de veículo elegível bloqueia a coleta;
  ausência de uma categoria apenas limita a cobertura da amostra.

## 3. Guarda e anonimização

Guardar termos assinados, correspondência código–titular, originais de vídeo/prints e HAR em `dados/privado/`, ignorado pelo Git, ou em armazenamento privado sob controle de Hugo. A pasta ignorada é uma precaução, não controle de acesso; restringir o acesso aos avaliadores e não anexar esses arquivos a issues ou PRs. Apagar os originais e a correspondência ao fim da disciplina, conforme o termo.

Publicar apenas evidências revisadas: tarjas opacas sobre CPF, placa, RENAVAM, chassi, nome, endereço, CNH, número do auto e outros identificadores; revisar também áudio, notificações e metadados. HAR pode conter cookies, tokens, URLs e corpos de resposta identificáveis: manter o original privado e publicar somente o resumo numérico necessário, sem exigir HAR público como evidência.

Se houver retirada do consentimento, interromper o uso, retirar registros/evidências vinculados e refazer as agregações. Caso dados pessoais tenham sido publicados indevidamente, tratar também cópias e histórico; apagar só o arquivo atual não remove o histórico do Git.

## 4. Checklist de recrutamento e preparação

- [x] Registrar o recebimento, em 20/11, da concordância informada para três integrantes; vias individuais preparadas e guardadas privadamente.
- [ ] Hugo confirma um titular e agenda S00/S01 até 14/11/2026.
- [x] Aplicar os termos aos participantes da coleta; conclusão confirmada por Hugo em 22/11/2026. Vias assinadas mantidas privadas.
- [x] Registrar publicamente a aplicação dos termos, sem publicar assinaturas ou identidades; datas de aplicação mantidas nas vias privadas.
- [ ] Conciliar os códigos reservados com a tabela privada, incluindo a ambiguidade de V2 entre sessões.
- [ ] Registrar as categorias disponíveis e a justificativa das lacunas da amostra.
- [ ] Executar o roteiro de `evidencias/fase1/roteiro-levantamento.md` em S01.
- [ ] Revisar e publicar as capturas anonimizadas; atualizar os itens ainda não confirmados da Fase 1.

O cronograma completo e as contingências estão em `docs/fase3-cronograma.md`; as instruções de coleta estão em `docs/fase3-metodo.md`.
