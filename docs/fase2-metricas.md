# Fase 2 — Fichas das métricas GQM

Esta seção especifica as métricas externas utilizadas para responder às questões de medição definidas para a avaliação da consulta de infrações no Portal de Serviços web e no aplicativo mobile oficial do Detran-DF. Todas as métricas consideram a mesma massa de dados, contextos de acesso equivalentes quando aplicável e os contextos específicos definidos no escopo para cada canal, além do mesmo intervalo temporal de consulta, de modo a permitir a comparação entre os canais.

Os intervalos de aceitabilidade foram definidos considerando a finalidade da consulta de infrações, as necessidades do cidadão condutor e referências da literatura de interação humano-computador.

## M1.1.1 — Proporção de campos da lista de referência exibidos

- **Questão respondida:** Q1.1
- **Definição:** proporção de campos da lista de referência exibidos pelo canal para cada infração consultada.
- **Fórmula:** (número de campos exibidos / número total de campos da lista de referência) × 100.
- **Unidade:** percentual.
- **Fonte dos dados:** prints anonimizados do Portal de Serviços e do aplicativo.
- **Procedimento de coleta:** usar a lista de referência R01–R15 da Fase 1 (`docs/fase1-produto.md`, Seção 1.5), que é externa aos dois canais e se baseia no conteúdo do auto de infração (CTB, arts. 258, 259 e 280); na **tela de lista de infrações** de cada canal, registrar em planilha, para cada infração, quais dos 15 campos aparecem preenchidos; consultar o mesmo veículo nos dois canais. O denominador é 15 para toda infração.
- **Interpretação:** maior é melhor.
- **Justificativa dos níveis:** a consulta cumpre sua finalidade quando o cidadão consegue identificar e compreender a infração. Por isso, a faixa Excelente admite apenas ausência residual de campos, enquanto valores abaixo de 60% indicam que parte substancial das informações necessárias não está disponível.
- **Níveis:** Inaceitável abaixo de 60%; Mínimo aceitável de 60% a 79%; Alvo de 80% a 94%; Excelente de 95% a 100%.

## M1.1.2 — Proporção de campos detalhados acessíveis

- **Questão respondida:** Q1.1
- **Definição:** proporção de campos da lista de referência que são visíveis ou consultáveis na tela de detalhamento e estão preenchidos para a infração avaliada. A diferença em relação a M1.1.1 é a tela medida (detalhamento, e não lista), não o conjunto de campos.
- **Fórmula:** (número de campos da lista de referência visíveis ou consultáveis e preenchidos no detalhamento / número de campos da lista de referência aplicáveis à infração) × 100.
- **Unidade:** percentual.
- **Fonte dos dados:** prints anonimizados das telas de detalhes da infração.
- **Procedimento de coleta:** acessar a tela de detalhamento de cada infração nos dois canais ("Detalhes da infração" no portal; detalhamento da infração no aplicativo) e registrar se cada campo R01–R15 está visível ou consultável e preenchido. Velocidade permitida e aferida entram como campos condicionais, só nas infrações de velocidade, aumentando o denominador nesses casos. Pelo levantamento da Fase 1, os rótulos dos 15 campos existem nos dois canais; a métrica verifica se o dado está efetivamente disponível para a infração avaliada.
- **Interpretação:** maior é melhor.
- **Justificativa dos níveis:** a acessibilidade às informações detalhadas contribui para a compreensão completa da autuação. A faixa Excelente admite apenas ausência residual de campos; valores abaixo de 60% indicam que parte substancial das informações detalhadas não está disponível.
- **Níveis:** Inaceitável abaixo de 60%; Mínimo aceitável de 60% a 79%; Alvo de 80% a 94%; Excelente de 95% a 100%.

## M1.2.1 — Proporção de campos comuns consistentes

- **Questão respondida:** Q1.2
- **Definição:** proporção de campos comuns entre os canais que apresentam o mesmo valor para uma mesma infração.
- **Fórmula:** (número de campos comuns, aplicáveis e comparáveis, com valor idêntico / número total de campos comuns, aplicáveis e comparáveis) × 100.
- **Unidade:** percentual.
- **Fonte dos dados:** planilha de comparação campo a campo entre Portal e aplicativo.
- **Procedimento de coleta:** Para cada infração selecionada, consultar o Portal de Serviços e o aplicativo em intervalo temporal próximo, registrando a data e a hora de cada consulta. Em seguida, identificar, na lista de referência, os campos aplicáveis àquela infração; campos não aplicáveis devem ser excluídos do cálculo. Para cada campo aplicável, registrar na planilha o valor exibido no Portal, o valor exibido no aplicativo e uma classificação: paritário, divergente ou ausente em um dos canais. A comparação deve considerar o conteúdo informacional, e não apenas a formatação visual: diferenças de maiúsculas e minúsculas, espaços, acentuação, pontuação, símbolo monetário, separador decimal ou formato de data e hora não devem ser tratadas como divergência quando os dois canais comunicam a mesma informação. Um campo é classificado como paritário quando os dois canais exibem a mesma informação; como divergente quando exibem informações diferentes; e como ausente em um dos canais quando o campo é aplicável, mas aparece em apenas um deles. Campos compostos, como velocidade permitida e velocidade aferida, devem ser comparados separadamente. Depois, calcular a proporção de campos paritários sobre o total de campos aplicáveis à infração e multiplicar por 100. Para o resultado agregado, somar todos os campos paritários de todas as infrações e dividir pelo total de campos aplicáveis em todas as infrações, multiplicando o resultado por 100. Divergências em campos como valor devido, vencimento, desconto, prazo ou situação devem ser revisadas quando puderem ser explicadas pela diferença de horário entre as consultas.
- **Interpretação:** maior é melhor.
- **Justificativa dos níveis:** divergências de status, valores monetários, pontuação ou prazos podem levar o cidadão a tomar decisões com base em informações inconsistentes. Por isso, a faixa Excelente admite apenas divergências residuais, e valores abaixo de 60% indicam inconsistência substancial entre os canais.
- **Níveis:** Inaceitável abaixo de 60%; Mínimo aceitável de 60% a 79%; Alvo de 80% a 94%; Excelente de 95% a 100%.

## M1.2.2 — Proporção de infrações sem divergência

- **Questão respondida:** Q1.2
- **Definição:** proporção de infrações consultadas que não apresentam divergência em nenhum campo comum entre os canais.
- **Fórmula:** (número de infrações sem divergência / número total de infrações consultadas) × 100.
- **Unidade:** percentual.
- **Fonte dos dados:** resultado consolidado da comparação campo a campo.
- **Procedimento de coleta:** aplicar M1.2.1 para cada infração da massa de dados e registrar se houve alguma divergência.
- **Interpretação:** maior é melhor.
- **Justificativa dos níveis:** a ausência de divergência em uma infração indica que os canais apresentam informações consistentes para o mesmo caso. A faixa Excelente admite apenas casos residuais de divergência; valores abaixo de 60% indicam que a maior parte das infrações consultadas apresenta alguma inconsistência.
- **Níveis:** Inaceitável abaixo de 60%; Mínimo aceitável de 60% a 79%; Alvo de 80% a 94%; Excelente de 95% a 100%.

## M1.3.1 — Número de passos até a lista de infrações

- **Questão respondida:** Q1.3
- **Definição:** número de ações necessárias desde o início do fluxo até a exibição completa da lista de infrações.
- **Fórmula:** contagem direta das ações realizadas.
- **Unidade:** passos.
- **Fonte dos dados:** gravação de tela e roteiro de execução.
- **Procedimento de coleta:** executar o mesmo roteiro no Portal e no aplicativo, com o mesmo veículo anonimizado; contar cada ação necessária. O fluxo começa na tela inicial já autenticada: o login não é comparável entre canais (CPF e senha com reCAPTCHA no portal; biometria opcional no aplicativo) e é registrado à parte. Pelo levantamento da Fase 1, o caminho previsto é o mesmo nos dois canais: grupo de infrações, "Histórico de infrações por veículo", seleção do veículo e lista (`docs/fase1-produto.md`, Seção 1.3) [VERIFICAR contagem com veículo real].
- **Interpretação:** menor é melhor.
- **Justificativa dos níveis:** o número de passos mede a extensão objetiva do fluxo necessário para concluir a consulta, sem avaliar a facilidade percebida.
- **Níveis:** faixas provisionais. Excelente até 4 passos; Alvo de 5 a 6 passos; Mínimo aceitável de 7 a 8 passos; Inaceitável acima de 8 passos.

## M1.3.2 — Número de transições de tela

- **Questão respondida:** Q1.3
- **Definição:** número de telas ou páginas percorridas até a exibição da lista de infrações.
- **Fórmula:** contagem direta das transições de tela.
- **Unidade:** telas.
- **Fonte dos dados:** gravação de tela.
- **Procedimento de coleta:** executar o mesmo roteiro nos dois canais, a partir da tela inicial já autenticada, como em M1.3.1, e contar as transições.
- **Interpretação:** menor é melhor.
- **Justificativa dos níveis:** o número de transições mede a extensão do caminho percorrido até o resultado.
- **Níveis:** faixas provisionais. Excelente até 3 telas; Alvo de 4 a 5 telas; Mínimo aceitável de 6 a 7 telas; Inaceitável acima de 7 telas.

## M2.1.1 — Tempo até a exibição completa da lista de infrações

- **Questão respondida:** Q2.1
- **Definição:** intervalo entre a seleção do veículo (clique ou toque que dispara a consulta, já que nenhum dos canais tem formulário de busca) e a primeira exibição completa da lista de infrações.
- **Fórmula:** tempo final menos tempo inicial.
- **Unidade:** segundos.
- **Fonte dos dados:** gravação de tela nos dois canais, com contagem de quadros entre o toque e a lista completa; no Portal, também o Chrome DevTools. O perfilador do Android Studio não serve, porque não funciona com aplicativos de loja (não depuráveis).
- **Procedimento de coleta:** definir dispositivos, condições de rede e número de repetições; usar o mesmo veículo anonimizado nos dois canais. Os dispositivos devem respeitar os requisitos mínimos levantados na Fase 1 (aplicativo: Android 8.0 ou iOS 15.1). A medição começa depois da autenticação.
- **Interpretação:** menor é melhor.
- **Resultado reportado:** média, mediana e percentil 90.
- **Justificativa dos níveis:** os intervalos foram baseados nos limites de tempo de resposta propostos por Nielsen. Segundo o autor, respostas de até 1 segundo tendem a preservar o fluxo de pensamento do usuário, enquanto esperas de até 10 segundos ainda permitem manter a atenção na tarefa; acima desse limite, há maior risco de interrupção da interação. Considerando que a consulta envolve autenticação, processamento e exibição de dados, adotaram-se faixas provisionais intermediárias entre esses limites.
- **Níveis:** faixas provisionais. Excelente até 3 segundos; Alvo de 3,01 a 5 segundos; Mínimo aceitável de 5,01 a 8 segundos; Inaceitável acima de 8 segundos.

## M2.1.2 — Tempo até a exibição completa dos detalhes da infração

- **Questão respondida:** Q2.1
- **Definição:** intervalo entre a seleção de uma infração e a exibição completa de seus detalhes.
- **Fórmula:** tempo final menos tempo inicial.
- **Unidade:** segundos.
- **Fonte dos dados:** gravação de tela nos dois canais, com contagem de quadros; no Portal, também o Chrome DevTools.
- **Procedimento de coleta:** usar a mesma infração anonimizada nos dois canais.
- **Interpretação:** menor é melhor.
- **Resultado reportado:** média, mediana e percentil 90.
- **Justificativa dos níveis:** os intervalos seguem a mesma referência de tempo de resposta proposta por Nielsen. Como a exibição dos detalhes é uma operação posterior à consulta, adotaram-se faixas provisionais ligeiramente inferiores às da lista de infrações.
- **Níveis:** faixas provisionais. Excelente até 2 segundos; Alvo de 2,01 a 4 segundos; Mínimo aceitável de 4,01 a 6 segundos; Inaceitável acima de 6 segundos.

## M2.2.1 — Volume de dados transferidos na consulta completa

- **Questão respondida:** Q2.2
- **Definição:** volume total de dados transferidos durante a execução completa da consulta de infrações.
- **Fórmula:** soma dos bytes transferidos durante a consulta.
- **Unidade:** megabytes.
- **Fonte dos dados:** Chrome DevTools, aba Network, no Portal; no aplicativo Android, contadores de tráfego do sistema por aplicativo (`adb shell dumpsys netstats detail`, filtrado pelo UID do pacote `br.com.mesotec.detrandf`), lidos antes e depois da consulta. O iOS não oferece contador equivalente por aplicativo [VERIFICAR alternativa ou restringir a medição do aplicativo ao Android].
- **Procedimento de coleta:** definir condições de rede, dispositivo e número de repetições; medir a consulta completa nos dois canais, da abertura do grupo de infrações (já autenticado) até a lista completa, como em M1.3.1. Definir no plano se o cache é limpo antes de cada repetição, e aplicar a mesma regra aos dois canais.
- **Interpretação:** menor é melhor.
- **Justificativa dos níveis:** o volume transferido afeta o consumo de dados móveis do cidadão.
- **Níveis:** faixas provisionais. Excelente até 2 MB; Alvo de 2,01 a 5 MB; Mínimo aceitável de 5,01 a 10 MB; Inaceitável acima de 10 MB.

## M3.1.1 — Taxa de conclusão da consulta por plataforma

- **Questão respondida:** Q3.1
- **Definição:** proporção de plataformas definidas no escopo em que a consulta é concluída com sucesso.
- **Fórmula:** (número de plataformas com consulta concluída / número total de plataformas testadas) × 100.
- **Unidade:** percentual.
- **Fonte dos dados:** registro de execução por plataforma.
- **Procedimento de coleta:** definir plataformas com Heitor; executar o mesmo roteiro em cada plataforma. Pelo levantamento da Fase 1, as plataformas candidatas são o portal em navegador de desktop e de celular e o aplicativo em Android 8.0 ou superior e iOS 15.1 ou superior. Aparelhos abaixo dessas versões não instalam o aplicativo e ficam fora do escopo; não contam como falha de conclusão.
- **Interpretação:** maior é melhor.
- **Justificativa dos níveis:** a cobertura de contexto avalia se a tarefa de consulta é concluída nos ambientes definidos. A faixa Excelente representa conclusão integral ou quase integral; valores abaixo de 60% indicam que a maior parte das plataformas não permite concluir a consulta.
- **Níveis:** Inaceitável abaixo de 60%; Mínimo aceitável de 60% a 79%; Alvo de 80% a 94%; Excelente de 95% a 100%.

## M3.1.2 — Taxa de conclusão da consulta por navegador

- **Questão respondida:** Q3.1
- **Definição:** proporção de navegadores definidos no escopo em que a consulta é concluída com sucesso.
- **Fórmula:** (número de navegadores com consulta concluída / número total de navegadores testados) × 100.
- **Unidade:** percentual.
- **Fonte dos dados:** registro de execução por navegador.
- **Procedimento de coleta:** definir navegadores com Heitor; executar o mesmo roteiro em cada navegador. A métrica só se aplica ao Portal, e o portal não declara navegadores suportados (Fase 1); a escolha deve seguir os navegadores mais usados pelo público-alvo.
- **Interpretação:** maior é melhor.
- **Justificativa dos níveis:** a conclusão da consulta em diferentes navegadores indica que o serviço é utilizável nos contextos web definidos no escopo. A faixa Excelente representa conclusão integral ou quase integral; valores abaixo de 60% indicam comprometimento relevante da cobertura de contexto.
- **Níveis:** Inaceitável abaixo de 60%; Mínimo aceitável de 60% a 79%; Alvo de 80% a 94%; Excelente de 95% a 100%.

## M3.2.1 — Taxa de conclusão da consulta por condição de rede

- **Questão respondida:** Q3.2
- **Definição:** taxa de tentativas de consulta concluídas com sucesso, calculada separadamente para cada canal e condição de rede.
- **Fórmula:** (número de tentativas concluídas em um canal e condição / número total de tentativas realizadas no mesmo canal e condição) × 100.
- **Unidade:** percentual.
- **Fonte dos dados:** registro de execução por condição de rede.
- **Procedimento de coleta:** definir com Heitor os parâmetros de Wi-Fi, 4G e latência simulada; executar o mesmo roteiro em cada condição, separadamente no Portal e no aplicativo, com o mesmo veículo anonimizado e o mesmo número de tentativas por combinação de canal e condição. Reportar os resultados para Portal + Wi-Fi, Portal + 4G, Portal + latência simulada, aplicativo + Wi-Fi, aplicativo + 4G e aplicativo + latência simulada. Para aplicar a mesma condição aos dois canais, limitar a rede no ponto de acesso (por exemplo, `tc netem` num computador que compartilha a conexão com o celular), já que o perfil de rede do DevTools só afeta o navegador.
- **Interpretação:** maior é melhor.
- **Justificativa dos níveis:** a conclusão da consulta sob diferentes condições de rede indica a capacidade do serviço de manter a tarefa disponível em contextos de uso distintos. A faixa Excelente representa conclusão integral ou quase integral; valores abaixo de 60% indicam comprometimento relevante da cobertura de contexto.
- **Níveis:** Inaceitável abaixo de 60%; Mínimo aceitável de 60% a 79%; Alvo de 80% a 94%; Excelente de 95% a 100%.

## M3.2.2 — Taxa de falhas ou expiração de sessão

- **Questão respondida:** Q3.2
- **Definição:** proporção de tentativas de consulta que apresentam falha, erro, expiração de sessão ou tempo limite, calculada separadamente para cada canal e condição de rede.
- **Fórmula:** (número de tentativas com falha ou expiração em um canal e condição / número total de tentativas realizadas no mesmo canal e condição) × 100.
- **Unidade:** percentual.
- **Fonte dos dados:** gravação de tela e registro de execução.
- **Procedimento de coleta:** registrar cada tentativa como concluída ou falha, separadamente por canal e condição de rede; descrever objetivamente o tipo de falha ou expiração.
- **Interpretação:** menor é melhor.
- **Justificativa dos níveis:** falhas, erros e expirações impedem ou interrompem a conclusão da consulta. Por isso, adotou-se a faixa de 0% a 5% como Excelente e valores acima de 40% como Inaceitáveis. Os limites intermediários serão revisados conforme o número de repetições e as condições de rede testadas.
- **Níveis:** Excelente de 0% a 5%; Alvo de 6% a 20%; Mínimo aceitável de 21% a 40%; Inaceitável acima de 40%.

## M3.2.3 — Tempo de conclusão da consulta por condição de rede

- **Questão respondida:** Q3.2
- **Definição:** tempo necessário para concluir a consulta em cada condição de rede.
- **Fórmula:** tempo final menos tempo inicial.
- **Unidade:** segundos.
- **Fonte dos dados:** gravação de tela com cronômetro e ferramentas de inspeção.
- **Procedimento de coleta:** repetir a consulta em Wi-Fi, 4G e latência simulada, separadamente no Portal e no aplicativo; usar o mesmo veículo anonimizado e o mesmo número de tentativas por combinação de canal e condição.
- **Interpretação:** menor é melhor.
- **Resultado reportado:** média, mediana e percentil 90.
- **Justificativa dos níveis:** os intervalos seguem os limites de tempo de resposta propostos por Nielsen. Sob condições de rede degradada, o tempo tende a aumentar; portanto, as faixas são mais permissivas que as das métricas M2.1.1 e M2.1.2.
- **Níveis:** faixas provisionais. Excelente até 5 segundos; Alvo de 5,01 a 10 segundos; Mínimo aceitável de 10,01 a 20 segundos; Inaceitável acima de 20 segundos.

## Níveis de pontuação e critérios de julgamento

As métricas percentuais de completude, consistência e conclusão usam as faixas: Inaceitável abaixo de 60%; Mínimo aceitável de 60% a 79%; Alvo de 80% a 94%; Excelente de 95% a 100%. Para métricas de falha, a ordem é invertida: Excelente de 0% a 5%; Alvo de 6% a 20%; Mínimo aceitável de 21% a 40%; Inaceitável acima de 40%.

Para métricas em que menor é melhor, aplicam-se as seguintes faixas provisionais:

| Métrica | Excelente | Alvo | Mínimo aceitável | Inaceitável |
|---|---:|---:|---:|---:|
| M1.3.1 — passos | até 4 | 5–6 | 7–8 | acima de 8 |
| M1.3.2 — telas | até 3 | 4–5 | 6–7 | acima de 7 |
| M2.1.1 — segundos | até 3 | 3,01–5 | 5,01–8 | acima de 8 |
| M2.1.2 — segundos | até 2 | 2,01–4 | 4,01–6 | acima de 6 |
| M2.2.1 — MB | até 2 | 2,01–5 | 5,01–10 | acima de 10 |
| M3.2.3 — segundos | até 5 | 5,01–10 | 10,01–20 | acima de 20 |

Os intervalos foram definidos a partir da finalidade da consulta, das necessidades do cidadão condutor e de referências usuais de engenharia de interação para tempo de resposta. Para métricas percentuais, os limites consideram o grau de completude, consistência e conclusão da tarefa necessário à identificação e compreensão da infração.

Para as métricas de tempo M2.1.1, M2.1.2 e M3.2.3, os intervalos foram baseados nos limites de tempo de resposta propostos por Nielsen. Segundo o autor, respostas de até 1 segundo tendem a preservar o fluxo de pensamento do usuário, enquanto esperas de até 10 segundos ainda permitem manter a atenção na tarefa; acima desse limite, há maior risco de interrupção da interação. Considerando que a consulta de infrações envolve autenticação, processamento e exibição de dados, adotaram-se faixas provisionais intermediárias entre esses limites.

A prioridade atribuída à taxa de conclusão nas métricas de cobertura de contexto fundamenta-se na abordagem de Krug, segundo a qual a avaliação de um produto digital deve considerar prioritariamente a capacidade do usuário de realizar a tarefa pretendida. Assim, a conclusão da consulta é o critério principal, enquanto falhas, expirações e tempo são utilizados como medidas complementares de estabilidade e resiliência.

Uma questão é atendida quando todas as suas métricas atingem pelo menos o nível Mínimo aceitável. Um objetivo é atendido quando todas as suas questões são atendidas; consequentemente, nenhuma métrica associada pode ser classificada como Inaceitável. O canal superior é aquele que obtém nível de pontuação maior na métrica; empate de nível é registrado como paridade entre os canais.

Para Q2.1, a mediana é o critério principal, com média e percentil 90 como medidas de estabilidade. Para Q3.1 e Q3.2, a taxa de conclusão é o critério principal, e falhas ou expirações são usadas para desempate.

## Diagrama GQM

A seguir está o diagrama Objetivo–Questão–Métrica: [diagrama GQM](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/artigo/figuras/diagram.png). O código editável está disponível em [`diagram_code.mmd`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/artigo/figuras/diagram_code.mmd).

## Referência bibliográfica
KRUG, Steve. Don’t make me think, revisited: a common sense approach to web usability. 3. ed. San Francisco: New Riders, 2014.

NIELSEN, Jakob. Usability engineering. San Francisco: Morgan Kaufmann, 1994.