# Fase 4 — Análise e julgamento GQM

Atualização documental em **23/11/2026**, referente à #48. Responsáveis pela análise: Pedro Henrique
e Philipe; revisor designado: Heitor. Os valores abaixo são **primeira leitura**, exceto P1 a P3 da S02,
que tiveram [segunda leitura independente](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/S02-segunda-leitura-2026-11-23.md)
(86 de 87 linhas; uma rolagem do P3 segue pendente). Nas demais, o campo `revisor` está vazio e o
validador recusa promover as linhas a dados oficiais. Por isso não há nível de pontuação.

## Situação e dependência

Os registros reúnem seis sessões, em 21 e 22/11/2026: o piloto S01, a S02 (P1 a P3), a S03 e a S05
(P6), a S06 (P4 e P5) e a S08 (P7). S01 é piloto e não entra no cálculo oficial. Os casos usam
veículos diferentes (V1, V2, V4 e V5), com aparelhos e versões distintos, e não são reunidos em uma
única mediana. O consentimento foi aplicado, conforme confirmação de Hugo em 22/11/2026, com vias
assinadas privadas; os códigos V1, V2, V4 e V5 foram conciliados com a tabela privada por Hugo (PR #84).

### P1 a P3: S02 (caso V2, Wi-Fi, portal no Chrome e aplicativo 2.7.0 no Android)

| Métrica | Portal | Aplicativo |
|---|---|---|
| M1.1.1, campos na lista (de 15) | 5 | 5 |
| M1.1.2, campos no detalhe (de 17) | 17 | 16 (sem R14) |
| M1.2.1, campos paritários (par) | 16 de 17; R14 ausente no aplicativo | |
| M1.2.2, infrações sem divergência (par) | 0 de 1, pela ausência de R14 | |
| M1.3.1, passos até a lista | 4 | 6 |
| M1.3.2, transições; rolagens | 3; 0 | 5; 2 |

*Tabela — Observações provisórias de S02. Fonte: `evidencias/fase4/S02-registro-2026-11-22.md`; segunda leitura independente concluída (86 de 87 linhas; uma rolagem do aplicativo pendente).*

Nenhum campo divergiu em valor. A regra de contagem das transições (D015) e a execução por script (D014)
estão registradas como desvios.

### P6: contextos (S03 e S05)

| Contexto | Concluídas | Resultado e limite |
|---|---|---|
| CT01: portal/Chrome | 3/3 (V1); 3/3 (V2) | Cinco erros de instrumento da S03 preservados à parte |
| CT02: portal/Firefox | 3/3 (V2) | Falha de login na S03 (D005), fora das tentativas; resolvida na S05 |
| CT03: portal/Chrome Android | 2/3 (V1) | Sessão expirada, preservada como falha |
| CT05: aplicativo 2.6.3 | 0/3 (V1) | Erro ao buscar veículos; aparelho superior ao planejado (D006) |
| CT05: aplicativo 2.7.0 | 3/3 (V2) | Outro aparelho, titular e veículo (D009) |
| CT06: aplicativo iOS 2.7.1 | 3/3 (V5) | Executor é o titular (D028); filtro de período (D030); M2.2.1 não medida no iOS (D008) |
| CT04 | Sem execução | Sem aparelho; contexto não avaliado |

*Tabela — Observações provisórias de P6. Fonte: registros S03, S05 e do CT06; conferência independente pendente.*

Versões, aparelhos, titulares e veículos diferentes impedem atribuir a diferença entre 2.6.3 e 2.7.0 a
uma causa técnica. As durações dos scripts de P6 não substituem P4, e P6 não mede as taxas por rede de P7.

As sete questões e hipóteses e os três objetivos permanecem **inconclusivos no julgamento oficial**
até a segunda leitura. O relato de falha não deve ser apagado nem convertido em aprovação, e a
ausência de dado ou de conferência não equivale a paridade nem a aprovação.

## Continuação com o caso V4 (S06 e S08)

Em 22/11/2026, a coleta prosseguiu com outro titular coberto pelo consentimento
(caso V4), no computador D06 (Chrome 157) e no Samsung SM-S731B (Aplicativo 2.7.0). Os registros
estão em `evidencias/fase4/S06-registro-2026-11-22.md` e `evidencias/fase4/S08-registro-2026-11-22.md`.
Os tempos abaixo são **propostas automáticas de primeira leitura**, pelos timestamps dos quadros,
sem aquecimentos; sem a segunda leitura independente, nenhum nível é atribuído.

| Métrica e rede | Portal (concluídas; mediana; P90) | Aplicativo (concluídas; mediana; P90) |
|---|---|---|
| M2.1.1, Wi-Fi | 10/10; 0,145 s; 0,683 s (B03) | 10/10; 0,774 s; 0,858 s (B09) |
| M2.1.2, Wi-Fi | 10/10; 0,136 s; 0,153 s (B05) | 10/10; 0,641 s; 0,816 s (B06) |
| M2.2.1, Wi-Fi | mediana 0,0107 MB, escopo do navegador (B07) | mediana 0,0649 MB, contador do UID (B08) |
| M3.2.3, Wi-Fi | 10/10; 0,083 s; 0,083 s (B10) | 10/10; 0,408 s; 0,667 s (B11) |
| M3.2.3, 4G | 10/10; 0,142 s; 0,183 s (B14) | 10/10; 0,726 s; 0,942 s (B15) |
| M3.2.3, degradada | 8/10; 0,850 s; 1,500 s (B12) | Não avaliada (D021) |

*Tabela — Observações provisórias de S06/S08. Fonte: `dados/brutos/`; conferência independente pendente.*

- Os escopos de volume diferem (bytes codificados no navegador; recebidos + enviados pelo UID): não declarar superioridade.
- No aplicativo, a lista fica abaixo da área visível. O B04 foi excluído por esperas do instrumento; o B09 usou rolagens rápidas feitas pelo aparelho desde o toque, cujo curso integra o tempo (D026).
- Na rede degradada do portal, uma falha na preparação e um tempo limite ficam no denominador (D023).
- A condição degradada não pôde ser imposta ao aplicativo: o adaptador Wi-Fi não sustentou ponto de acesso concorrente, e o app ignorou proxy e recusou VPN reversa. Tudo foi desfeito sem medições (D021). Com o computador ligado por cabo ao roteador, o Wi-Fi ficaria livre para o ponto de acesso.
- Demais limitações: execução automatizada, Wi-Fi doméstico sem controle de carga externa e tráfego do agente de automação no enlace degradado (D016–D027).

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
| Q2.1 / H2.1 | M2.1.1, M2.1.2 | H2.1 compara a mediana da lista, no mesmo veículo/rede. Detalhes complementam Q2.1 e têm julgamento próprio | Inconclusivo; amostras V4 provisórias, segunda leitura pendente |
| Q2.2 / H2.2 | M2.2.1 | Comparar médias apenas com escopo dos instrumentos equivalente e contexto pareado. Sem equivalência, hipótese inconclusiva | Inconclusivo; amostras V4 provisórias, segunda leitura pendente |
| Q3.1 / H3.1 | M3.1.1, M3.1.2 | Verificar todos os contextos previstos. Taxa de 100% no subconjunto testado não confirma cobertura dos contextos ausentes | Inconclusivo |
| Q3.2 / H3.2 | M3.2.1, M3.2.2, M3.2.3 | Verificar se a taxa degradada é menor que Wi-Fi e que 4G em pelo menos um canal. Discutir falhas e tempo junto das taxas | Inconclusivo; portal nas três redes e app em Wi-Fi/4G, provisórios; app degradado não avaliado |

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
