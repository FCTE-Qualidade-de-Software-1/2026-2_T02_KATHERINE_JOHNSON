# Massa de Dados da Avaliação

**Responsável:** Hugo Freitas Silva  
**Situação em 18/10/2026:** levantamento de veículos em andamento; nenhum consentimento colhido ainda.

## 1. Requisitos da massa

A consulta de infrações só exibe veículos vinculados ao CPF que fez login (ver `docs/fase1-produto.md`, Seção 1.2). Por isso cada veículo precisa de:

1. pelo menos uma infração registrada (de preferência em situações diferentes: a vencer, vencida, paga);
2. proprietário que aceite fazer login nos dois canais durante a sessão de teste;
3. termo de consentimento assinado (`dados/consentimento.md`).

Para cobrir a comparação entre canais, o ideal é ter ao menos uma infração aplicada por órgão diferente do Detran-DF (vinda do RENAINF) e uma infração de velocidade, que exibe campos condicionais.

## 2. Tabela anonimizada

Esta é a única tabela da massa de dados que entra no repositório. Ela não contém placa, RENAVAM, CPF, nome nem número de auto.

| Código | Tipo de veículo | Nº de infrações | Situações presentes | Infração de outro órgão? | Infração de velocidade? | Consentimento (data) | Sessão de teste |
|---|---|---|---|---|---|---|---|
| V1 | | | | | | | |
| V2 | | | | | | | |
| V3 | | | | | | | |

## 3. Tabela de correspondência (fora do repositório)

A tabela que liga cada código (V1, V2...) à placa e ao titular fica em `dados/privado/`, pasta ignorada pelo Git (ver `.gitignore`), e não deve ser enviada ao GitHub por nenhum meio. O responsável mantém a cópia e a apaga ao fim da disciplina.

## 4. Pendências

- [ ] Perguntar na reunião de 19/10 quais integrantes ou familiares têm veículos com infrações.
- [ ] Colher os termos assinados até 21/10.
- [ ] Preencher a tabela anonimizada.
- [ ] Agendar a sessão de levantamento com login para confirmar os itens [VERIFICAR] de `docs/fase1-produto.md`.
