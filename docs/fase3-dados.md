# Fase 3 — Massa e instrumentos de coleta

A [massa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/46-e2-fase-3-plano-de-avaliacao-metodo-ambiente-massa-de-dados-e-cronograma/dados/massa-de-dados.md) prevê até três veículos consentidos, com mínimo de um veículo com infração nos dois canais. A diversidade de situações, órgãos e infrações de velocidade é desejada, mas ainda não confirmada. A amostra é intencional e não permite generalização estatística para a frota.

O titular assina o termo em `dados/consentimento.md` antes da coleta e faz o login sem compartilhar a senha. Somente código do veículo e data do consentimento são públicos. Originais, termos e correspondências ficam privados; prints e vídeos só são publicados após anonimização e revisão independente.

## Instrumentos entregues

Os arquivos em `dados/brutos/` contêm apenas cabeçalhos, sem dados fictícios. O dicionário e as regras de cálculo estão em `dados/README.md`.

| Arquivo | Finalidade / procedimento |
|---|---|
| `ambientes.csv` | Inventário por sessão/contexto |
| `campos-por-infracao.csv` | Presença dos campos, P1 |
| `comparacao-canais.csv` | Classificação por campo, P2; valores identificáveis permanecem privados |
| `fluxo.csv` | Passos e transições, P3 |
| `tempos.csv` | Quadros, timestamps e tempos, P4/P7 |
| `volume.csv` | Leituras, unidade e elegibilidade, P5 |
| `tentativas.csv` | Resultado de cada tentativa, P6/P7 |
| `desvios.csv` | Bloqueios, mudanças e decisão de inclusão |

*Tabela 1 — Instrumentos preparados para a coleta. Fonte: elaborada para o plano.*

Cada linha liga sessão, contexto, veículo e evidência. Não preencher células ausentes com zero. Falhas do serviço devem permanecer registradas; falhas do instrumento recebem justificativa de exclusão e eventual repetição. Os [procedimentos](fase3-metodo.md), o [ambiente](fase3-ambiente.md) e o [cronograma](fase3-cronograma.md) formam o plano completo.
