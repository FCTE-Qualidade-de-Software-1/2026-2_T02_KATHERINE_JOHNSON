# Fase 1 — Propósito, partes interessadas e escopo

*Responsável: Heitor · Versão 1.0 — revisada e integrada à `main` em 25/10/2026 ([PR #24](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/24))*

Esta página define por que a avaliação existe, para quem ela serve e até onde ela vai. Os
pontos de vista dos objetivos de medição da [Fase 2](fase2-gqm.md) derivam das partes
interessadas descritas aqui.

## 1. Propósito e uso pretendido

O Detran-DF oferece a consulta de infrações em dois canais, o **Portal de Serviços** e o
**aplicativo**, e o cidadão escolhe qual usar conforme o aparelho e a conexão de que dispõe. Os
dois canais compartilham o servidor de identidade, mas consultam serviços de backend distintos,
como mostra o levantamento do produto. Isso abre espaço para que um mesmo veículo apareça com
informações, tempos de resposta ou possibilidade de conclusão diferentes conforme o canal.

**Esta avaliação existe para verificar se os dois canais entregam a consulta com qualidade
equivalente e, quando não entregam, onde está a diferença.**

### Requisitante

O requisitante é a **Área de Governança Digital do Detran-DF**. Trata-se de um **requisitante
hipotético**, adotado para orientar as decisões da avaliação: a equipe não tem vínculo com o
órgão, e nenhum resultado será apresentado como posição oficial dele.

### Decisões que a avaliação apoia

| ID | Decisão | Quem decide | Evidência usada |
|---|---|---|---|
| D1 | Em qual canal e em qual característica investir primeiro em melhoria | Requisitante | Julgamento dos objetivos G1, G2 e G3 por canal |
| D2 | Quais divergências de dados entre os canais corrigir, e com que urgência | Equipe técnica de TI, acionada pelo requisitante | Questão Q1.2 (consistência entre canais) |
| D3 | Qual canal recomendar ao cidadão em cada contexto de uso (computador ou celular, Wi-Fi ou rede móvel) | Requisitante, com a área de atendimento ao cidadão | Objetivos G2 e G3 por contexto |
| D4 | Quais contextos (versões de sistema, navegadores e condições de rede) devem ter suporte garantido | Equipe técnica de TI | Objetivo G3 |

*Tabela 1 — Decisões apoiadas pela avaliação e seus responsáveis. Fonte: elaborada pela equipe.*

### Uso pretendido

O uso pretendido é **comparativo**. Os resultados valem como linha de base da qualidade da
consulta nos dois canais, nas versões e nos contextos avaliados, e não como certificação de
conformidade nem como avaliação do Detran-DF como um todo.

## 2. Partes interessadas

As três primeiras partes interessadas fornecem os pontos de vista dos objetivos G1, G2 e G3 da
[Fase 2](fase2-gqm.md).

| Parte interessada | Papel | Necessidade | Critério de sucesso | Influência na avaliação |
|---|---|---|---|---|
| **Requisitante:** Área de Governança Digital do Detran-DF (hipotético) | Solicita a avaliação e recebe o relatório | Saber se os canais têm paridade e onde investir | Julgamento por característica e por canal que permita ordenar as melhorias (D1) | Definiu o propósito comparativo e a regra de que toda métrica se aplica igualmente aos dois canais |
| **Cidadão/condutor** proprietário do veículo | Usuário da consulta | Ver as infrações completas e corretas para pagar, recorrer ou indicar condutor no prazo | Consulta concluída, com os campos de referência, em todos os contextos do escopo e com os mesmos dados nos dois canais | Motivou a adequação funcional e a cobertura de contexto (celular, rede móvel); ponto de vista de G1 e G3 |
| **Equipe técnica de TI e gestão de serviços digitais do Detran-DF**, incluindo o fornecedor do aplicativo | Mantém os dois canais | Saber em que canal e em que condição a consulta fica lenta, pesada ou falha | Medições reproduzíveis por canal e por condição de rede, que indiquem onde está a diferença (D2, D4) | Motivou a eficiência de desempenho; ponto de vista de G2 |
| **Área de atendimento ao cidadão** | Orienta o cidadão | Saber qual canal indicar | Recomendação por contexto de uso (D3) | Indireta: reforça a comparação por contexto em G2 e G3 |
| **Órgãos de controle e transparência** | Fiscalizam a prestação do serviço público | Evidência de que o serviço digital é equivalente nos canais | Resultados rastreáveis até os dados brutos | Indireta: reforça a rastreabilidade dos dados no repositório |
| **Equipe avaliadora** (Katherine Johnson) | Executa a avaliação | Avaliação viável em caixa-preta, no prazo da disciplina | Todas as métricas coletáveis sem acesso ao código e com consentimento dos proprietários | Restringiu o escopo e a massa de dados |

*Tabela 2 — Partes interessadas, critérios de sucesso e influência na avaliação. Fonte: elaborada pela equipe.*

## 3. Escopo, profundidade e objetos

### Dentro do escopo

O objeto é o **histórico de infrações por veículo**, na área autenticada:

- **Portal de Serviços:** <https://portal.detran.df.gov.br>, versão observada em 18/10/2026;
- **aplicativo DETRAN-DF:** versão 2.6.9, Android e iOS.

A consulta é observada **da escolha do menu de infrações, já com o usuário autenticado, até a
exibição dos detalhes de uma infração**.

### Contextos de uso especificados

São os contextos que a cobertura de contexto (objetivo G3) deve cobrir. Insumo para as métricas
M3.1.1, M3.1.2 e M3.2.1.

| Dimensão | Contextos |
|---|---|
| Portal de Serviços | Google Chrome e Mozilla Firefox em computador; Google Chrome em celular Android |
| Aplicativo | Um celular Android de entrada e um intermediário (Android 8.0 ou superior); um iPhone (iOS 15.1 ou superior), mas nenhum integrante da equipe possui iPhone: o iOS depende de um aparelho emprestado na Fase 3 e, sem ele, fica fora da avaliação (os modelos dos aparelhos são definidos na preparação do ambiente, na Fase 3) |
| Rede | Wi-Fi; rede móvel 4G; rede degradada simulada, com parâmetros definidos no plano de avaliação (Fase 3) |

*Tabela 3 — Contextos de uso especificados. Fonte: elaborada pela equipe.*

### Profundidade

**Caixa-preta.** Todas as métricas são externas, obtidas por avaliadores da equipe que seguem um
roteiro fixo, sem acesso ao código-fonte, aos servidores ou à base do Detran-DF, e sem coleta de
opinião de usuários.

### Fora do escopo

| Fora do escopo | Justificativa |
|---|---|
| Autenticação (login) | Pré-condição, não objeto: o portal exige reCAPTCHA e o aplicativo aceita biometria, o que torna tempo e passos de login incomparáveis |
| Consulta pública de débitos, sem login | Mostra só débitos pendentes, sem o detalhamento da autuação; não equivale ao histórico de infrações |
| Histórico de infrações por condutor | Existe apenas no aplicativo (a confirmar no portal com veículo real na Fase 3); não pode ser comparado entre canais |
| Pagamento, defesa, recurso e indicação de condutor | São serviços distintos da consulta e exigiriam transações financeiras ou processos administrativos reais com os veículos da massa de dados |
| Consulta de veículo de outra UF | Depende de bases de outros estados, fora do serviço do Detran-DF |
| Capacidade de interação (usabilidade) | Excluída por exigência da disciplina |
| Aparelhos abaixo de Android 8.0 ou iOS 15.1 | Não instalam o aplicativo; não contam como falha de conclusão |

*Tabela 4 — Itens fora do escopo e justificativa de cada corte. Fonte: elaborada pela equipe.*

As características de qualidade excluídas (confiabilidade, segurança, compatibilidade,
capacidade e outras) estão justificadas no modelo de qualidade adaptado da Fase 1.

### Limites de validade dos resultados

- **Amostra:** apenas veículos de integrantes e familiares que consentiram por escrito, o que
  limita a quantidade e os tipos de infração observados.
- **Versões e período:** os resultados valem para as versões avaliadas e para o período de
  coleta; uma atualização de qualquer canal pode alterá-los.
- **Tempo de resposta:** depende da carga dos servidores, que a equipe não controla.
- **Rede degradada:** é simulada, e não uma rede real com problemas.
- **Correção dos dados:** é julgada pela consistência entre os canais e com a notificação
  recebida pelo proprietário, e não contra a base oficial.
- **Aplicativo no iOS:** nenhum integrante da equipe possui iPhone. Se não houver um aparelho emprestado na Fase 3, os
  resultados do aplicativo valem apenas para o Android.
