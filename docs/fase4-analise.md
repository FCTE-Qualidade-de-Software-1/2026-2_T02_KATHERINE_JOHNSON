# Fase 4 — Análise e julgamento GQM

Atualização documental em **22/11/2026**, referente à #48. Responsáveis pela análise: Pedro Henrique
e Philipe; revisor designado: Heitor. O roteiro abaixo permanece aplicável, mas seu estado agora
distingue a `main` da coleta recente ainda não integrada.

## Situação e dependência

Na `main` (`da717f2`), os oito CSV brutos têm apenas cabeçalhos. A validação calcula zero métricas:
25 registros inconclusivos e um não aplicável (M3.1.2 no aplicativo). S01 é piloto e não entra no
cálculo oficial; seu relatório não comprova aquecimento, marcações independentes ou instrumento
de volume.

A branch `feat/pedro-s03-fase4`, no
[commit 14ab804](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/14ab804210f4b1be2aaa84e1946d9e11079a9a28),
contém o [relato S03 de 21/11](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/14ab804210f4b1be2aaa84e1946d9e11079a9a28/evidencias/fase4/S03-registro-2026-11-21.md).
Ele relata CT01 com 3/3 conclusões, CT03 com 2/3 e uma expiração, e CT05 com 0/3 e erro ao buscar
veículos. São contagens preliminares: a validação rejeita as 14 linhas por falta de conferência
independente. Consentimento e vínculo privado do veículo também estão a conferir; CT05 usa
aparelho/versão diferentes do planejamento (D006). CT02, CT04 e CT06 não foram executados no relato.

As sete questões e hipóteses e os três objetivos permanecem **inconclusivos no julgamento
oficial**. O relato de falha não deve ser apagado nem convertido em aprovação, mas ainda não
sustenta nível definitivo, ranking geral ou causa técnica. Tempos dos scripts não substituem P4;
P6 não mede taxas por rede de P7. Os arquivos dessa branch não foram copiados sobre os instrumentos
da `main`: a conferência da #47 precede sua integração como dados oficiais.

O bloqueio no aplicativo motivou a [ação de melhoria entregue](fase4-melhoria.md): proposta de
processo e templates de diagnóstico/regressão. A entrega não depende de inventar resultados;
sua eficácia e a revisão humana permanecem pendentes.

## Procedimento de análise

1. Registrar o commit dos dados recebidos da #47 e a versão do procedimento de cálculo em cada linha de `dados/consolidados/resultados-metricas.csv`.
2. Conferir chaves, duplicações, campos obrigatórios, revisão independente, vínculo às evidências e elegibilidade conforme `dados/README.md`. Registrar exclusões com motivo e contagem. Preservar falhas do serviço nas taxas e separar aquecimento e piloto.
3. Calcular cada métrica conforme a [Fase 2](fase2-metricas.md) e as regras da [Fase 3](fase3-metodo.md). Reportar veículo, contexto, rede, tamanho da amostra e denominador efetivo. Separar aparelhos, redes e veículos nos resumos temporais e de volume.
4. Aplicar os limites contínuos da Fase 2 antes de arredondar. Usar mediana para julgamento de tempo e volume, acompanhada de média e P90 para tempos. H2.2 compara médias de volume, ainda que o nível de M2.2.1 seja atribuído pela mediana.
5. Preencher as respostas da Tabela 1 com valores, nível, evidências e limitações. Avaliar a hipótese separadamente do atendimento da questão. Uma hipótese pode ser contrariada mesmo quando os dois canais atingem o mínimo aceitável.
6. Julgar G1, G2 e G3 por canal e contexto. Comparar níveis por métrica, com empate de nível como paridade. M1.2.1/M1.2.2 são resultados do par de canais. M3.1.2 é exclusiva do portal. Ausência de métrica aplicável deixa a questão inconclusiva conforme a Fase 2, preservando eventuais falhas já observadas na resposta textual.

A Tabela 1 define a interpretação a ser preenchida após a coleta. “Compatível com a amostra” não implica confirmação estatística ou generalização.

| Questão / hipótese | Métricas | Regra para interpretar a hipótese | Estado atual |
|---|---|---|---|
| Q1.1 / H1.1 | M1.1.1, M1.1.2 | Comparar completude por tela e infração nos dois canais. Distinguir rótulo existente de valor preenchido ao discutir a hipótese sobre rótulos | Inconclusivo |
| Q1.2 / H1.2 | M1.2.1, M1.2.2 | Uma divergência ou ausência em campo aplicável contraria a paridade integral. Considerar apenas pares com intervalo válido | Inconclusivo |
| Q1.3 / H1.3 | M1.3.1, M1.3.2 | Igualdade das contagens recorrentes de passos e transições sustenta paridade na amostra. Contagens diferentes a contrariam. Examinar o percurso para discutir redundância | Inconclusivo |
| Q2.1 / H2.1 | M2.1.1, M2.1.2 | H2.1 compara a mediana da lista, no mesmo veículo/rede. Detalhes complementam Q2.1 e têm julgamento próprio | Inconclusivo |
| Q2.2 / H2.2 | M2.2.1 | Comparar médias apenas com escopo dos instrumentos equivalente e contexto pareado. Sem equivalência, hipótese inconclusiva | Inconclusivo |
| Q3.1 / H3.1 | M3.1.1, M3.1.2 | Verificar todos os contextos previstos. Taxa de 100% no subconjunto testado não confirma cobertura dos contextos ausentes | Inconclusivo |
| Q3.2 / H3.2 | M3.2.1, M3.2.2, M3.2.3 | Verificar se a taxa degradada é menor que Wi-Fi e que 4G em pelo menos um canal. Discutir falhas e tempo junto das taxas | Inconclusivo |

*Tabela 1 — Roteiro de resposta às questões e hipóteses. Fonte: especificação GQM da equipe.*

## Julgamento por característica e propósito

A Tabela 2 vincula os objetivos às decisões da [Fase 1](fase1-proposito.md). Cada questão requer todas as métricas aplicáveis no mínimo aceitável e cada objetivo requer todas as questões atendidas. Registrar resultados por canal, inclusive quando a evidência é compartilhada pelo par.

| Objetivo | Questões | Decisão e parte interessada | Portal | Aplicativo |
|---|---|---|---|---|
| G1 — Adequação funcional | Q1.1–Q1.3 | D1, investimento em melhoria pelo requisitante; D2, correção de divergências pela equipe de TI para o cidadão | Inconclusivo | Inconclusivo |
| G2 — Eficiência de desempenho | Q2.1–Q2.2 | D1 e D3, investimento e recomendação de canal pelo requisitante e atendimento | Inconclusivo | Inconclusivo |
| G3 — Cobertura de contexto | Q3.1–Q3.2 | D3 e D4, recomendação por contexto e definição de suporte pela equipe de TI | Inconclusivo | Inconclusivo |

*Tabela 2 — Julgamento atual e ligação com o propósito. Fonte: questões GQM e decisões D1–D4 da equipe.*

## Relações entre características e limites

Investigar se o aumento de tempo sob rede degradada acompanha a redução da conclusão, usando M3.2.3, M3.2.1 e M3.2.2 das mesmas tentativas. O tempo só das consultas concluídas pode parecer baixo quando as lentas falham, por isso apresentar n e falhas juntos.

Cruzar completude (M1.1.x) com volume/tempo (G2) no mesmo veículo, contexto e versão. Maior volume pode acompanhar mais informação, mas a observação externa não demonstra causalidade. Um canal rápido com campos ausentes requer discussão conjunta de G1 e G2.

Examinar se contextos com falha impedem observar a completude. Não atribuir completude zero a um contexto sem tela de resultado. A amostra intencional, o cache, a ordem dos canais, atualizações entre consultas e a equivalência dos instrumentos limitam as conclusões. Sem pares suficientes, registrar a relação como inconclusiva e indicar os dados faltantes.

## Apresentação e oportunidades de melhoria

Após a #47, apresentar tabela de valores e níveis por métrica com n, contexto e evidência. Para tempos, um gráfico por métrica/rede com os pontos observados e mediana permite visualizar dispersão. Para conclusão, apresentar sucessos/total e falhas por canal/rede. Toda tabela e figura deve ter legenda, fonte com commit dos dados e chamada no texto. Os gráficos aguardam medições.

Preencher `dados/consolidados/oportunidades.csv` apenas com problemas observados. Como proposta de priorização para revisão de Heitor, ordenar por impacto documentado sobre a consulta, recorrência na amostra e abrangência de contextos. Em empate, usar a prioridade da Fase 1 (adequação funcional, cobertura de contexto, eficiência de desempenho) e registrar o esforço estimado para escolher a ação da #36. Indicar métrica afetada, evidência, decisão D1–D4, benefício esperado e como reavaliar. A priorização definitiva depende da análise dos resultados.

## Pendências para concluir a #48

- Receber da #47 dados brutos, desvios, evidências e cálculo reproduzível.
- Preencher resultados das quatorze métricas e respectivos níveis.
- Responder às sete questões e hipóteses e julgar os três objetivos por canal.
- Gerar tabelas finais e gráficos, interpretar relações entre características e priorizar melhorias com evidências.
- Atualizar a síntese do artigo e conferir compilação e limite de páginas.
- Submeter PR à revisão de Heitor e registrar esforço real.
