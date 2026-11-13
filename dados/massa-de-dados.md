# Massa de dados da avaliação

Responsável: Hugo Freitas Silva. Plano atualizado em 13/11/2026.

**Situação:** não há comprovação de consentimentos, veículos recrutados ou sessão autenticada no repositório. Os códigos abaixo são reservas de identificação, não dados observados.

## 1. Seleção e justificativa

Amostra intencional por disponibilidade e consentimento, sem pretensão de representar a frota do DF. Planejar até três veículos (V1–V3) e registrar todas as infrações selecionadas antes da coleta. O mínimo operacional é um veículo com pelo menos uma infração consultável nos dois canais; com esse mínimo, limitar as conclusões ao caso estudado.

Buscar variedade de situações (a vencer, vencida e paga), uma infração de outro órgão/RENAINF e uma de velocidade. São metas de diversidade, não ocorrências já confirmadas. Se ausentes, registrar a lacuna; não criar infrações nem presumir campos condicionais. Veículo sem infrações serve apenas como caso exploratório de lista vazia e não fornece denominador para completude de detalhes ou paridade.

Cada titular precisa aceitar o [termo de consentimento](consentimento.md), fazer login pessoalmente nos dois canais e estar disponível para nova autenticação. Nunca solicitar ou guardar senha. Usar a mesma seleção de veículos e infrações em ambos os canais; consultas comparadas devem ocorrer em até dez minutos, conforme P2.

## 2. Cadastro anonimizado

| Código reservado | Tipo de veículo | Nº de infrações selecionadas | Situações | Outro órgão? | Velocidade? | Consentimento (data) | Sessão |
|---|---|---|---|---|---|---|---|
| V1 | A confirmar | A confirmar | A confirmar | A confirmar | A confirmar | Não confirmado | S01, a agendar |
| V2 | A confirmar | A confirmar | A confirmar | A confirmar | A confirmar | Não confirmado | A agendar |
| V3 | A confirmar | A confirmar | A confirmar | A confirmar | A confirmar | Não confirmado | A agendar |

*Tabela 1 — Cadastro a preencher após recrutamento. Fonte: plano de avaliação.*

Atribuir V1-I1, V1-I2 etc. às infrações na tabela privada; manter os códigos estáveis entre sessões. Registrar no conjunto público apenas código, categoria necessária ao cálculo e indicadores de presença/consistência. Valores pessoais são comparados em ambiente privado, nunca transcritos no CSV público. Documentar a seleção e eventuais exclusões antes do cálculo.

## 3. Guarda e anonimização

Guardar termos assinados, correspondência código–titular, originais de vídeo/prints e HAR em `dados/privado/`, ignorado pelo Git, ou em armazenamento privado sob controle de Hugo. A pasta ignorada é uma precaução, não controle de acesso; restringir o acesso aos avaliadores e não anexar esses arquivos a issues ou PRs. Apagar os originais e a correspondência ao fim da disciplina, conforme o termo.

Publicar apenas evidências revisadas: tarjas opacas sobre CPF, placa, RENAVAM, chassi, nome, endereço, CNH, número do auto e outros identificadores; revisar também áudio, notificações e metadados. HAR pode conter cookies, tokens, URLs e corpos de resposta identificáveis: manter o original privado e publicar somente o resumo numérico necessário, sem exigir HAR público como evidência.

Se houver retirada do consentimento, interromper o uso, retirar registros/evidências vinculados e refazer as agregações. Caso dados pessoais tenham sido publicados indevidamente, tratar também cópias e histórico; apagar só o arquivo atual não remove o histórico do Git.

## 4. Checklist de recrutamento e preparação

- [ ] Hugo confirma um titular e agenda S00/S01 até 14/11/2026.
- [ ] Preencher o contato do responsável no termo e colher assinatura antes da captura.
- [ ] Registrar data do consentimento e códigos na tabela, sem assinatura ou identidade.
- [ ] Registrar as categorias disponíveis e a justificativa das lacunas da amostra.
- [ ] Executar o roteiro de `evidencias/fase1/roteiro-levantamento.md` em S01.
- [ ] Revisar e publicar as capturas anonimizadas; atualizar os itens ainda não confirmados da Fase 1.

O cronograma completo e as contingências estão em `docs/fase3-cronograma.md`; as instruções de coleta estão em `docs/fase3-metodo.md`.
