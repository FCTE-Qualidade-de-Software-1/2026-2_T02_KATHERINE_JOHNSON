# Fase 4 — Análise e julgamento GQM

Atualização documental em **24/11/2026**, referente à #48. Responsáveis pela análise: Pedro Henrique
e Philipe; revisor designado: Heitor. As segundas leituras independentes dos procedimentos elegíveis
foram concluídas em 23/11. As divergências de tempo e a rolagem pendente da S02 foram resolvidas em
conjunto e registradas; os dados conferidos foram calculados pelo procedimento versionado.
Resultados não coletados continuam sem nível.

> **Cada número desta página pode ser conferido.** A página
> [Medições por métrica](fase4-medicoes.md) mostra todas as leituras brutas por trás de cada
> resultado, com link para a linha exata do CSV, para a captura e para a segunda leitura
> independente. Nas tabelas abaixo, o nome de cada métrica leva para essas medições.

## Situação e dependência

Os registros reúnem seis sessões, em 21 e 22/11/2026: piloto S01; S02 (P1 a P3); S03 e S05 (P6);
S06 (P4 e P5); e S08 (P7). S01 é piloto e não entra no cálculo. Os casos usam veículos V1, V2, V4
e V5, com aparelhos e versões distintos, e não são reunidos em uma única mediana. O consentimento
foi aplicado, conforme confirmação de Hugo em 22/11/2026, com vias assinadas privadas; os códigos
dos veículos foram conciliados por Hugo (PR #84).

## G1 — Adequação funcional: S02 (V2, Wi-Fi) {#resultados-s02}

P1 e P2 foram conferidos por Heitor; P3 também foi conferido e a única divergência de rolagem foi
resolvida com Pedro Druck. A tabela apresenta os valores e níveis oficiais para a amostra observada.

| Métrica | Portal | Aplicativo | Resultado do par |
|---|---|---|---|
| [M1.1.1](fase4-medicoes.md#m1-1-1), campos preenchidos na lista (n=15) | 5/15; 33,33%; **Inaceitável** | 5/15; 33,33%; **Inaceitável** | — |
| [M1.1.2](fase4-medicoes.md#m1-1-2), campos acessíveis no detalhe (n=17) | 17/17; 100%; **Excelente** | 16/17; 94,12%; **Alvo** (R14 ausente) | — |
| [M1.2.1](fase4-medicoes.md#m1-2-1), campos paritários (n=17) | — | — | 16/17; 94,12%; **Alvo** |
| [M1.2.2](fase4-medicoes.md#m1-2-2), infrações sem divergência (n=1) | — | — | 0/1; 0%; **Inaceitável** |
| [M1.3.1](fase4-medicoes.md#m1-3-1), passos até a lista (3 repetições) | 4; **Excelente** | 6; **Alvo** | — |
| [M1.3.2](fase4-medicoes.md#m1-3-2), transições (3 repetições) | 3; **Excelente** | 5; **Alvo** | — |

*Tabela 1 — Resultados G1 na S02. Fonte: registros e segunda leitura independente da S02. A rolagem do aplicativo foi conferida e resolvida; ela não integra M1.3.1 nem M1.3.2.*

Não houve divergência de valores: a ausência de R14 no aplicativo explica M1.2.1 abaixo de 100% e
M1.2.2 em 0/1. A completude da lista é baixa nos dois canais apesar da completude superior no
detalhe. As contagens de P3 são medidas objetivas do fluxo, não uma avaliação de usabilidade.

## G2 — Eficiência de desempenho: S06 (V4, Wi-Fi) {#resultados-v4}

| Métrica | Portal | Aplicativo |
|---|---|---|
| [M2.1.1](fase4-medicoes.md#m2-1-1), lista (n=10; média / mediana / P90) | 0,254 / 0,145 / 0,683 s; **Excelente** | 0,695 / 0,774 / 0,858 s; **Excelente** |
| [M2.1.2](fase4-medicoes.md#m2-1-2), detalhe (n=10; média / mediana / P90) | 0,142 / 0,136 / 0,153 s; **Excelente** | 0,687 / 0,641 / 0,816 s; **Excelente** |
| [M2.2.1](fase4-medicoes.md#m2-2-1), volume (n=10; média / mediana) | 0,0107 / 0,0107 MB; **Excelente** | 0,0660 / 0,0649 MB; **Excelente** |

*Tabela 2 — Resultados G2 na S06. Fonte: registros S06 e segunda leitura de P4/P5. Tempos em segundos; níveis aplicados antes do arredondamento.*

O portal teve medianas menores nos dois tempos desta amostra. Os volumes recebem nível
individualmente, mas **não permitem ordenar os canais**: DevTools mede bytes codificados do
navegador e o contador Android soma tráfego enviado e recebido pelo UID. A amostra de P4/P5 usa
um veículo, um aparelho por canal e uma sessão; o B04 excluído e o erro de instrumento da primeira
repetição B09 foram preservados conforme os desvios.

## P6 — cobertura de plataforma {#resultados-p6}

| Plataforma/contexto | Portal | Aplicativo |
|---|---|---|
| CT03, Chrome Android (V1) | 1/1 plataforma móvel; 100%; **Excelente** | — |
| CT01 + CT02, Chrome+Firefox desktop (V2) | 1/1 plataforma computador; 100%; **Excelente** | — |
| [M3.1.2](fase4-medicoes.md#m3-1-2), navegadores portal (V1: CT01+CT03; V2: CT01+CT02) | 2/2 em cada grupo; 100%; **Excelente** | Não aplicável |
| CT05, Android 2.6.3 (V1) | — | 0/1 plataforma; 0%; **Inaceitável** |
| CT05, Android 2.7.0 (V2) | — | 1/1 plataforma; 100%; **Excelente** |
| CT06, iOS 2.7.1 (V5) | — | 1/1 plataforma; 100%; **Excelente** |
| CT04 | — | Sem execução; inconclusivo |

*Tabela 3 — M3.1.1 e M3.1.2 por plataforma/contexto. Fonte: registros S03/S05/CT06 e segunda leitura independente de P6. M3.1.2 não se aplica ao aplicativo.*

O portal atingiu os critérios nos contextos medidos: CT03 concluiu 2/3 tentativas, o mínimo
operacional para aprovação de contexto. No aplicativo, a falha 0/3 em CT05 com 2.6.3 é um resultado
Inaceitável; CT05 com 2.7.0 e CT06 tiveram sucesso. Aparelhos, versões, veículos e titulares
diferem, portanto não se atribui a diferença a uma causa técnica. CT04 não foi executado.

## P7 — cobertura por rede no caso V4 {#resultados-p7}

| Rede (n=10) | Canal | M3.2.1 conclusão | M3.2.2 falha | M3.2.3 tempo mediano (média; P90) |
|---|---|---|---|---|
| Wi-Fi | Portal | 10/10; 100%; **Excelente** | 0%; **Excelente** | 0,083 s (0,073; 0,083); **Excelente** |
| Wi-Fi | Aplicativo | 10/10; 100%; **Excelente** | 0%; **Excelente** | 0,408 s (0,470; 0,667); **Excelente** |
| 4G | Portal | 10/10; 100%; **Excelente** | 0%; **Excelente** | 0,142 s (0,152; 0,183); **Excelente** |
| 4G | Aplicativo | 10/10; 100%; **Excelente** | 0%; **Excelente** | 0,726 s (0,661; 0,942); **Excelente** |
| Degradada | Portal | 8/10; 80%; **Alvo** | 2/10; 20%; **Alvo** | 0,850 s (0,942; 1,567); **Excelente** |
| Degradada | Aplicativo | Não avaliada; inconclusivo | Não avaliada; inconclusivo | Não avaliada; inconclusivo |

*Tabela 4 — Resultados de P7 por rede. Fonte: S08, segunda leitura independente e `resultados-metricas.csv`. O tempo inclui apenas consultas concluídas; as falhas permanecem no denominador das taxas.*

No aplicativo, a condição degradada não pôde ser imposta (D021); não há nível nem comparação
nessa condição. No portal, uma falha de preparação e um tempo limite permaneceram no denominador
(D023). A execução automatizada, a carga externa não controlada do Wi-Fi e o tráfego do agente no
enlace degradado limitam os resultados (D016–D027).

O bloqueio no aplicativo motivou a [ação de melhoria entregue](fase4-melhoria.md): proposta de
processo e templates de diagnóstico/regressão. A entrega não depende de inventar resultados;
sua eficácia e a revisão humana permanecem pendentes.

## Procedimento de análise {#procedimento-analise}

1. Registrar o commit dos dados recebidos da #47 e a versão do procedimento de cálculo em cada linha de `dados/consolidados/resultados-metricas.csv`.
2. Conferir chaves, duplicações, campos obrigatórios, revisão independente, vínculo às evidências e elegibilidade conforme `dados/README.md`. Registrar exclusões com motivo e contagem. Preservar falhas do serviço nas taxas e separar aquecimento e piloto.
3. Calcular cada métrica conforme a [Fase 2](fase2-metricas.md) e as regras da [Fase 3](fase3-metodo.md). Reportar veículo, contexto, rede, tamanho da amostra e denominador efetivo. Separar aparelhos, redes e veículos nos resumos temporais e de volume.
4. Aplicar os limites contínuos da Fase 2 antes de arredondar. Usar mediana para julgamento de tempo e volume, acompanhada de média e P90 para tempos. H2.2 compara médias de volume, ainda que o nível de M2.2.1 seja atribuído pela mediana.
5. Preencher as respostas de cada Q e G em `dados/consolidados/respostas-gqm.csv`, com valores, nível, evidências e limitações. Avaliar a hipótese separadamente do atendimento da questão. Uma hipótese pode ser contrariada mesmo quando os dois canais atingem o mínimo aceitável.
6. Julgar G1, G2 e G3 por canal e contexto. Comparar níveis por métrica, com empate de nível como paridade. M1.2.1/M1.2.2 são resultados do par de canais. M3.1.2 é exclusiva do portal. Ausência de métrica aplicável deixa a questão inconclusiva conforme a Fase 2, preservando eventuais falhas já observadas na resposta textual.

<span id="respostas-questoes"></span>As respostas explícitas às sete questões e às hipóteses estão resumidas na Tabela 5; a decomposição por canal/contexto, as evidências e as limitações estão em [`respostas-gqm.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/consolidados/respostas-gqm.csv). “Compatível com a amostra” não implica confirmação estatística nem generalização.

| Questão / hipótese | Resposta e estado por canal | Avaliação da hipótese |
|---|---|---|
| <span id="resp-q1-1"></span>[Q1.1](fase2-gqm.md#q1-1) / [H1.1](fase2-gqm.md#h1-1) | **Portal e aplicativo: não atendida.** Ambos exibiram 5/15 campos preenchidos na lista (33,33%, Inaceitável). No detalhe, o portal exibiu 17/17 (Excelente) e o aplicativo 16/17 (Alvo), sem R14. | Compatível quanto à contagem observada igual; não comprova equivalência semântica de rótulos, que M1.1.1 não mede diretamente. |
| <span id="resp-q1-2"></span>[Q1.2](fase2-gqm.md#q1-2) / [H1.2](fase2-gqm.md#h1-2) | **Par: não atendida.** 16/17 campos paritários (Alvo), mas 0/1 infração sem divergência ou ausência (Inaceitável): R14 não estava no aplicativo. | Contrariada para paridade integral; não houve divergência de valores, mas houve ausência aplicável. |
| <span id="resp-q1-3"></span>[Q1.3](fase2-gqm.md#q1-3) / [H1.3](fase2-gqm.md#h1-3) | **Portal e aplicativo: atendida.** Os níveis foram Excelente/Alvo: 4 contra 6 passos e 3 contra 5 transições. O portal exige menos ações nesta amostra. | Contrariada: as contagens não foram iguais. Não é uma conclusão sobre usabilidade. |
| <span id="resp-q2-1"></span>[Q2.1](fase2-gqm.md#q2-1) / [H2.1](fase2-gqm.md#h2-1) | **Portal e aplicativo: atendida.** As duas métricas atingiram Excelente. No V4/Wi-Fi, medianas do portal foram 0,145 s (lista) e 0,136 s (detalhe), contra 0,774 s e 0,641 s no aplicativo. | Contrariada nesta amostra: o aplicativo não teve menor mediana. |
| <span id="resp-q2-2"></span>[Q2.2](fase2-gqm.md#q2-2) / [H2.2](fase2-gqm.md#h2-2) | **Portal e aplicativo: atendida.** M2.2.1 atingiu Excelente nos dois canais (medianas de 0,0107 MB no portal e 0,0649 MB no aplicativo, contra o limite de 2 MB). | Inconclusiva: os instrumentos têm escopos diferentes (bytes codificados no navegador; tráfego enviado e recebido pelo UID no Android), então os volumes não sustentam comparação nem confirmação de menor média no aplicativo. |
| <span id="resp-q3-1"></span>[Q3.1](fase2-gqm.md#q3-1) / [H3.1](fase2-gqm.md#h3-1) | **Portal: atendida** nos contextos medidos (M3.1.1 e M3.1.2, 100%, Excelente). **Aplicativo: não atendida** no escopo observado: CT05/2.6.3 teve 0/3 (Inaceitável), apesar de CT05/2.7.0 e CT06 atingirem 3/3; CT04 não foi executado. | Contrariada pela falha observada no aplicativo; não identifica causa entre versões, aparelhos e veículos diferentes. |
| <span id="resp-q3-2"></span>[Q3.2](fase2-gqm.md#q3-2) / [H3.2](fase2-gqm.md#h3-2) | **Portal: atendida** nas três redes; na degradada, 8/10 conclusões (Alvo), 20% de falhas (Alvo) e mediana de 0,850 s (Excelente). **Aplicativo: inconclusiva** porque a rede degradada não pôde ser aplicada. | Compatível com a amostra para o portal (80% < 100% em Wi-Fi e 4G); inconclusiva para o aplicativo. |

*Tabela 5 — Respostas às questões e hipóteses GQM. Fonte: Fase 2, dados consolidados e segundas leituras independentes de S02, S03, S05, S06 e S08.*

## Julgamento por característica e propósito {#julgamento}

O julgamento segue a regra da [Fase 2](fase2-metricas.md#niveis): cada questão requer que todas as métricas aplicáveis alcancem ao menos o nível Mínimo aceitável. O objetivo é atendido somente quando todas as questões forem atendidas. A Tabela 6 vincula cada resultado às decisões e partes interessadas da [Fase 1](fase1-proposito.md).

| Objetivo | Questões | Decisão e parte interessada | Portal | Aplicativo |
|---|---|---|---|---|
| <span id="julg-g1"></span>[G1](fase2-gqm.md#g1) — Adequação funcional | Q1.1–Q1.3 | D1, investimento pelo requisitante; D2, correção de inconsistências para o cidadão pela equipe técnica | **Não atendido**: Q1.1 e Q1.2 abaixo do mínimo | **Não atendido**: Q1.1 e Q1.2 abaixo do mínimo |
| <span id="julg-g2"></span>[G2](fase2-gqm.md#g2) — Eficiência de desempenho | Q2.1–Q2.2 | D1, investimento pelo requisitante; D3, recomendação pela área de atendimento | **Atendido** no caso medido (V4, CT01, Wi-Fi): Q2.1 e Q2.2 atendidas, medianas menores que as do aplicativo | **Atendido** no caso medido (V4, CT05, Wi-Fi): Q2.1 e Q2.2 atendidas; H2.1 contrariada e H2.2 inconclusiva |
| <span id="julg-g3"></span>[G3](fase2-gqm.md#g3) — Cobertura de contexto | Q3.1–Q3.2 | D1, D3 e D4: investimento, recomendação por contexto e definição de suporte pela equipe técnica | **Atendido nos contextos medidos** | **Não atendido no escopo observado**: falha em CT05/2.6.3; CT04 e rede degradada ausentes |

*Tabela 6 — Julgamento por característica e canal, ligado ao propósito e às partes interessadas. Fonte: Fase 1, regras da Fase 2 e respostas GQM.*

Em G2, a falta de equivalência entre os instrumentos de volume afeta somente a hipótese H2.2,
que compara os canais. A questão Q2.2 é julgada pelo nível de M2.2.1 em cada canal, como definem a
[regra da Fase 2](fase2-metricas.md#niveis) e o passo 5 do procedimento acima; os dois canais
atingiram Excelente. O julgamento vale para o caso V4 em Wi-Fi e para os contextos previstos para
P4 e P5 (CT01 e CT05); M2.2.1 não tem instrumento no iOS (D008).

## Relações entre características e limites {#relacoes}

**Adequação funcional e eficiência.** A lista exibiu 5/15 campos em ambos os canais, nível Inaceitável, enquanto os tempos da lista foram Excelentes e menores no portal. Portanto, rapidez não substitui completude. No detalhe, o aplicativo omitiu R14 e a infração pareada não atingiu paridade integral. O volume numericamente menor no portal não pode ser relacionado à completude nem usado para ranking, pois os instrumentos têm escopos distintos.

**Adequação funcional e cobertura de contexto.** A falha 0/3 do aplicativo 2.6.3 em CT05 bloqueou a chegada à lista; não se atribui completude zero a uma tela não alcançada. Em outro bloco, CT05 com aplicativo 2.7.0 concluiu 3/3, mas a mudança concomitante de veículo, titular, aparelho e versão impede atribuir a diferença a uma causa. A relação permanece observada, não causal.

**Eficiência e cobertura de contexto.** No portal/V4, a rede degradada reduziu a conclusão para 8/10, com duas falhas no denominador; a mediana de 0,850 s considera somente as oito consultas concluídas. Por isso, o tempo baixo não apaga as falhas nem prova melhor resiliência. Para o aplicativo, não há par degradado. A amostra intencional, o cache, a ordem dos canais, a carga externa do Wi-Fi e os instrumentos limitam as conclusões.

## Apresentação e oportunidades de melhoria {#oportunidades}

As Tabelas 1–6 foram chamadas e interpretadas no texto; cada uma indica legenda e fonte. A consolidação integral com valores, níveis, denominadores, evidências e proveniência está em [`resultados-metricas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/consolidados/resultados-metricas.csv). Não se agregam veículos, versões ou redes diferentes. O arquivo [`oportunidades.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/consolidados/oportunidades.csv) registra a priorização proposta para revisão de Heitor:

| Prioridade | Problema observado | Evidência e impacto | Decisão apoiada |
|---:|---|---|---|
| 1 | Consulta bloqueada no aplicativo 2.6.3 (CT05) | 0/3 concluídas; a versão 2.7.0 em outro bloco teve 3/3, sem permitir atribuir causa | D4 e D1: investigar suporte por versão e regressão |
| 2 | R14 ausente no detalhe do aplicativo | 16/17 campos e 0/1 infração integralmente paritária; campo de prazo de defesa/condutor | D2 e D1: conferir e corrigir ou justificar a informação |
| 3 | Apenas 5/15 campos preenchidos na lista de ambos os canais | 33,33%, Inaceitável, na amostra V2 | D1: investigar apresentação dos campos essenciais |
| 4 | Queda de conclusão do portal na rede degradada | 8/10 sucessos e 2/10 falhas; apenas uma sessão e um veículo | D3 e D4: repetir em rede controlada antes de orientar suporte |

*Tabela 7 — Oportunidades priorizadas por impacto, recorrência e abrangência observados. Fonte: `oportunidades.csv`, S02, S03 e S08. As posições são uma proposta, não estimativa de esforço.*

## Fechamento e limitações da #48

Os resultados, níveis, respostas, julgamentos e oportunidades foram registrados com base nas
leituras conferidas. Permanecem sem medição o CT04, a condição degradada no aplicativo e a
M2.2.1 no iOS; não recebem zero nem nível. Os resultados valem somente para os veículos,
dispositivos, versões, redes e datas observados, não certificam o serviço nem representam
todos os cidadãos do Detran-DF. O PR desta entrega aguarda a revisão designada de Heitor;
aprovação e fechamento da issue não são presumidos.
