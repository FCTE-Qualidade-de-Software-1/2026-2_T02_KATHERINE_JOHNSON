# Fase 3 — Massa e instrumentos de coleta

A [massa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/massa-de-dados.md) previa até três veículos consentidos (na coleta foram usados quatro códigos: V1, V2, V4 e V5), com mínimo de um veículo com infração nos dois canais. A diversidade de situações, órgãos e infrações de velocidade é desejada, mas ainda não confirmada. A amostra é intencional e não permite generalização estatística para a frota.

**Atualização em 22/11:** a S03 usou o V1 (infração de referência V1-I1) e a S05 usou o V2 (V2-I1, infração de velocidade autuada por outro órgão). Os códigos V1, V2, V4 e V5 foram conciliados com a tabela privada por Hugo (PR #84). O V2-I1 atende às metas de diversidade "outro órgão" e "velocidade"; as metas de situação (a vencer, vencida e paga) ainda não foram conferidas. A S06 e a S08 usaram o V4 (V4-I1), de outro titular coberto pelo consentimento, com a correspondência mantida na tabela privada.

Os termos foram aplicados aos participantes da coleta, conforme confirmação de Hugo em 22/11/2026. As vias assinadas permanecem privadas; a GitPage registra a conclusão, sem publicar os documentos preenchidos. Para novos participantes, o titular assina o [termo](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/consentimento.md) antes da coleta e faz o login sem compartilhar a senha. O registro público informa a aplicação e sua confirmação; datas individuais e correspondências ficam no armazenamento privado. Originais, termos e correspondências ficam privados; prints e vídeos só são publicados após anonimização e revisão independente.

## Instrumentos entregues

Os arquivos em `dados/brutos/` foram entregues apenas com cabeçalhos, sem dados fictícios. Desde 21/11 recebem os registros reais: P6 (S03, S05 e CT06), P1 a P3 (S02), P4 e P5 (S06) e P7 (S08). Os valores são de primeira leitura até o preenchimento do campo `revisor`. O
[dicionário e as regras de cálculo](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/README.md)
definem chaves, denominadores e exclusões. O
[modelo de sessão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/modelo-sessao.md)
registra liberação do piloto, blocos, conferência independente e encerramento.

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
