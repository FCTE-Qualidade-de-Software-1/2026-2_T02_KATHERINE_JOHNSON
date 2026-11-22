# Fase 4 — Análise e julgamento GQM

Preparação da issue #48 em 16/11/2026. Responsáveis pela análise: Pedro Henrique e Philipe. Revisor designado: Heitor.

## Situação e dependência

Os oito CSV de `dados/brutos/` contêm apenas cabeçalhos nesta revisão. As quatorze métricas e todas as questões e objetivos permanecem inconclusivos por ausência de medições. A issue #47 deve entregar os dados elegíveis, evidências anonimizadas, desvios e procedimento de cálculo reproduzível. O levantamento autenticado da Fase 3 contribui para preparar a coleta, mas ainda faltam as repetições e registros requeridos para o julgamento.

O [acompanhamento da #47](fase4-coleta.md) apresenta o cálculo automatizado e as pendências de
execução. `python3 dados/scripts/calcular.py` gera a tabela de métricas e o manifesto das
entradas; os estados sem medição não respondem às questões GQM. A interpretação e o julgamento
continuam sob responsabilidade da #48.

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
