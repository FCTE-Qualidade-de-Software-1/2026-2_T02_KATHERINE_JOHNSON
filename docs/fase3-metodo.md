# Fase 3 — Método de avaliação e instruções para o avaliador

*Responsável: Pedro Druck · Versão 0.1 — rascunho em 13/11/2026 ([issue #46](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/46))*

Esta página define como cada uma das quatorze métricas da [Fase 2](fase2-metricas.md) será obtida
na Fase 4. O objetivo é que outro avaliador, seguindo apenas estas instruções, chegue às mesmas
medidas. Recursos, ambiente, massa de dados e cronograma completam o plano em páginas próprias
da Fase 3: [ambiente](fase3-ambiente.md), [massa e instrumentos](fase3-dados.md) e [cronograma](fase3-cronograma.md).

## 1. Método

**Medição externa, caixa-preta e roteirizada.** Avaliadores da equipe executam a consulta de
infrações nos dois canais seguindo um roteiro fixo e registram o que observam, com apoio de
gravação de tela, do Chrome DevTools (portal) e do `adb` (aplicativo Android). Não há acesso ao
código, aos servidores ou à base do Detran-DF, e não se coleta opinião de usuários, como definido
na profundidade da avaliação ([Fase 1](fase1-proposito.md)).

O método foi escolhido porque todas as métricas da Fase 2 são externas e observáveis na tela ou
no tráfego de rede do aparelho de teste. A repetibilidade vem de três regras:

1. **Mesmo objeto nos dois canais.** Cada medição usa o mesmo veículo (V1, V2...) e, quando
   aplicável, a mesma infração (V1-I1, V1-I2...), identificados pelos códigos da
   [massa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/massa-de-dados.md).
2. **Dois papéis por sessão.** O **executor** opera o canal; o **registrador** preenche os
   arquivos de coleta durante a sessão. O proprietário do veículo só faz o login e não opera o
   roteiro.
3. **Conferência por um segundo avaliador.** Toda medida obtida por contagem ou por marcação de
   quadro (passos, telas, campos, tempos) é refeita a partir da gravação por um integrante que não
   participou da sessão. Divergências são resolvidas em conjunto e registradas.

## 2. Parâmetros comuns

A Fase 2 deixou alguns parâmetros para o plano de avaliação. Eles valem para todas as métricas.

| Parâmetro | Decisão | Justificativa |
|---|---|---|
| Contexto de referência | Portal no Google Chrome em computador; aplicativo no celular Android intermediário; rede Wi-Fi | As métricas de G1 e G2 comparam canais, não contextos; os demais contextos da Fase 1 são usados apenas em G3 |
| Ponto de partida | Tela inicial já autenticada | O login está fora do escopo ([Fase 1](fase1-proposito.md)); é feito pelo proprietário antes de cada bloco |
| Ordem dos canais | Alterna a cada bloco: o primeiro bloco da sessão começa pelo portal, o seguinte pelo aplicativo, e assim por diante | Evita que um canal seja sempre medido depois do outro, com o servidor já "aquecido" pela consulta anterior |
| Repetições de tempo e volume | 10 válidas por canal e contexto, mais 1 de aquecimento descartada no início de cada bloco | Permite calcular mediana e percentil 90 com o mínimo de dados para isso, dentro do tempo de uma sessão |
| Cache | Não é limpo em nenhum dos canais; a sessão do usuário é mantida | Evita alterar a sessão autenticada entre repetições. O aquecimento padroniza a preparação, mas não garante estados internos equivalentes de cache; essa limitação deve acompanhar os resultados |
| Tempo limite | 60 s sem a lista completa contam como falha por tempo limite | Bem acima da faixa Inaceitável de M3.2.3 (20 s), para não confundir lentidão com falha |
| Intervalo entre canais (M1.2.x) | No máximo 10 minutos entre a consulta de uma infração no portal e no aplicativo, com hora registrada | Reduz o risco de divergência causada por atualização da infração entre as consultas, como prevê a Fase 2 |
| Taxa de quadros da gravação | 60 quadros por segundo; 30 se o aparelho não suportar, com o valor registrado | A resolução da medida de tempo é de um quadro (17 ms a 60 qps; 33 ms a 30 qps) |
| Indicação de toques | Ativar "Mostrar toques" nas opções do desenvolvedor do Android; no computador, gravar o cursor com destaque de clique | O quadro inicial das medidas de tempo é o do toque ou clique, que precisa aparecer na gravação |

*Tabela 1 — Parâmetros comuns às medições. Fonte: elaborada pela equipe.*

### Condições de rede

Para que a mesma condição valha para os dois canais, o computador do portal e o celular do
aplicativo se conectam ao mesmo ponto de acesso: um notebook com Linux que compartilha a conexão
por Wi-Fi. A condição é aplicada nesse ponto de acesso, nos dois sentidos (envio e recebimento),
e não no navegador, porque o perfil de rede do DevTools não afeta o aplicativo.

| Condição | Saída do ponto de acesso | Limitação aplicada | Uso |
|---|---|---|---|
| Wi-Fi | Rede Wi-Fi fixa do local da sessão | Nenhuma | Contexto de referência (G1, G2) e G3 |
| 4G | Celular com chip 4G ligado ao notebook por roteamento USB | Nenhuma | G3 (Q3.2) |
| Rede degradada | Rede Wi-Fi fixa | `tc netem`: atraso de 300 ms com variação de 50 ms, banda de 1 Mbit/s e perda de 1% dos pacotes | G3 (Q3.2) |

*Tabela 2 — Condições de rede. Fonte: elaborada pela equipe.*

Os valores da rede degradada definem um cenário experimental fixo, sem alegar equivalência com uma rede real. São aplicados por sentido, conforme a preparação do [ambiente](fase3-ambiente.md), e ficam fixos durante toda
a coleta. Antes de cada bloco, o registrador anota a velocidade medida no próprio ponto de
acesso, para documentar a condição real.

## 3. Procedimentos

Os procedimentos P1 a P7 agrupam as métricas que se obtêm na mesma execução. Em todos eles, o
executor começa a gravação de tela antes do primeiro passo e só a encerra depois do último
registro.

### P1 — Registro de campos (M1.1.1 e M1.1.2)

1. No contexto de referência, abrir a lista de infrações do veículo.
2. **M1.1.1:** para cada infração da lista, marcar no arquivo de coleta, campo a campo de R01 a
   R15 ([lista de referência](fase1-produto.md)), se o campo aparece **preenchido na tela de
   lista**. Campo com rótulo e sem valor conta como não exibido. O denominador é sempre 15.
3. Capturar a tela de lista (role a página e capture mais de uma tela se preciso).
4. **M1.1.2:** abrir o detalhamento de cada infração e marcar, de R01 a R15, se o campo está
   **visível ou consultável e preenchido**. "Consultável" é o campo que aparece depois de uma
   ação dentro do detalhamento (expandir uma seção, por exemplo); a ação é anotada. Velocidade
   permitida e aferida entram como dois campos a mais no denominador só nas infrações de
   velocidade.
5. Capturar a tela de detalhamento completa.
6. Repetir os passos 1 a 5 no outro canal, para as mesmas infrações.

### P2 — Comparação entre canais (M1.2.1 e M1.2.2)

Usa as telas capturadas em P1; não exige nova consulta, desde que o intervalo entre os canais
tenha respeitado o limite de 10 minutos.

1. Para cada infração, listar os campos de R01 a R15 aplicáveis a ela, mais velocidade
   permitida e aferida nas infrações de velocidade (comparadas separadamente).
2. Para cada campo aplicável, transcrever **somente no registro privado** o valor exibido no portal e no aplicativo e
   classificar como **paritário**, **divergente** ou **ausente em um canal**, seguindo as regras
   de formatação da [M1.2.1](fase2-metricas.md): diferença só de formato (maiúsculas, acentos,
   símbolo monetário, separador decimal, formato de data) não é divergência.
3. Se houver divergência em valor devido, vencimento, desconto, prazo ou situação, conferir se a
   diferença de horário entre as consultas explica o caso; anotar a conclusão na coluna de
   observação.
4. **M1.2.2:** marcar a infração como "sem divergência" quando nenhum campo foi classificado
   como divergente ou ausente em um canal.
5. Um segundo avaliador refaz a classificação a partir dos prints, sem ver a primeira.

### P3 — Contagem do fluxo (M1.3.1 e M1.3.2)

1. No contexto de referência, a partir da tela inicial autenticada, executar o caminho até a
   lista de infrações do veículo, sem atalhos e sem usar a busca do canal.
2. **M1.3.1:** conta como **passo** cada clique ou toque em elemento interativo e cada
   preenchimento ou seleção em campo. Rolagem não conta como passo; é anotada à parte.
3. **M1.3.2:** conta como **transição** cada troca do conteúdo principal da tela (nova página,
   nova rota do aplicativo ou diálogo que ocupa a tela). Menus suspensos e indicadores de
   carregamento não contam.
4. Executar o caminho três vezes em cada canal. O valor da métrica é o da contagem que se
   repetir; se as três forem diferentes, registrar como desvio e levar à discussão da equipe.
5. Anotar o rótulo exato de cada elemento acionado, para confirmar os nomes de menu da Fase 1.

### P4 — Medição de tempo (M2.1.1 e M2.1.2)

1. No contexto de referência, abrir a tela de seleção do veículo e iniciar o bloco com uma
   repetição de aquecimento, que não entra no cálculo.
2. **M2.1.1:** em cada repetição, tocar ou clicar no veículo e aguardar a lista de infrações.
   Voltar à tela de seleção e repetir até completar 10 repetições válidas.
3. **M2.1.2:** na lista, tocar ou clicar na mesma infração (V1-I1) e aguardar o detalhamento.
   Voltar à lista e repetir até completar 10 repetições válidas.
4. Na gravação, marcar o **quadro inicial** (primeiro quadro com o indicador de toque ou clique)
   e o **quadro final** (primeiro quadro em que a lista ou o detalhamento aparece completo, sem
   indicador de carregamento, e não muda nos quadros seguintes). O tempo é a diferença de quadros
   dividida pela taxa de quadros.
5. No portal, usar a aba Network do DevTools apenas como apoio diagnóstico. O evento `load` não mede necessariamente a conclusão visual de uma consulta assíncrona e não substitui a marcação na gravação.
6. O segundo avaliador marca os quadros de novo, de forma independente. Se a diferença passar
   de 3 quadros, os dois marcam juntos e a marcação final é registrada.

### P5 — Medição de volume (M2.2.1)

1. **Portal:** abrir o DevTools, aba Network, com "Preserve log" ligado e "Disable cache"
   desligado (regra de cache da Tabela 1). Limpar a lista de requisições.
2. **Aplicativo:** com o celular ligado ao computador por USB, ler o contador de bytes do
   aplicativo com `adb shell dumpsys netstats detail`, filtrado pelo UID do pacote
   `br.com.mesotec.detrandf`.
3. Executar a consulta completa: da abertura do grupo de infrações, já autenticado, até a lista
   completa (mesmo intervalo de P3).
4. **Portal:** anotar o total "transferred" exibido no rodapé da aba Network e salvar o arquivo
   HAR **apenas no armazenamento privado**, pois pode conter credenciais e dados pessoais. **Aplicativo:** ler o contador de novo; o volume é a diferença entre as duas leituras
   (recebidos mais enviados).
5. Repetir até completar 10 repetições válidas, depois da repetição de aquecimento.
6. **iOS:** não há contador equivalente por aplicativo. Se houver iPhone emprestado, a M2.2.1 do
   iOS fica registrada como não medida; o resultado do aplicativo vale para o Android.

A equivalência do escopo e a atualização dos contadores precisam ser verificadas no [piloto](fase3-ambiente.md). Sem essa verificação, não classificar um canal como superior pelo volume. Usar MB decimal (1.000.000 bytes) e registrar leituras e instrumento.

### P6 — Execução por contexto (M3.1.1 e M3.1.2)

1. Em Wi-Fi, executar a consulta completa (até o detalhamento de uma infração) em cada contexto
   especificado na [Fase 1](fase1-proposito.md):
    - portal: Chrome em computador, Firefox em computador e Chrome em celular Android;
    - aplicativo: celular Android de entrada, celular Android intermediário e, se houver aparelho
      emprestado, iPhone.
2. Fazer três tentativas por contexto. O contexto conta como **concluído** quando pelo menos duas
   das três tentativas chegam ao detalhamento sem erro.
3. **M3.1.1** usa as plataformas (computador, aprovado quando Chrome e Firefox forem aprovados, e celular Android, no portal; Android de entrada,
   Android intermediário e iOS, no aplicativo). **M3.1.2** usa os navegadores do portal (Chrome e
   Firefox em computador, Chrome em celular).
4. Registrar versão do sistema, do navegador e do aplicativo de cada contexto. Contexto sem
   aparelho disponível é registrado como **não avaliado**, e não como falha.

### P7 — Execução sob condição de rede (M3.2.1, M3.2.2 e M3.2.3)

1. No contexto de referência, para cada condição da Tabela 2, aplicar a condição no ponto de
   acesso e anotar a velocidade medida.
2. Fazer 10 tentativas por canal, depois da repetição de aquecimento. Cada tentativa vai da
   seleção do veículo até a lista completa.
3. Classificar cada tentativa como **concluída**, **falha** (mensagem de erro, tela em branco ou
   fechamento do aplicativo), **sessão expirada** (o canal pede login de novo) ou **tempo limite**
   (60 s sem a lista). Descrever a falha com as palavras exibidas na tela.
4. **M3.2.1:** tentativas concluídas sobre o total, por canal e condição. **M3.2.2:** falhas,
   sessões expiradas e tempos limite sobre o total, por canal e condição.
5. **M3.2.3:** tempo das tentativas concluídas, marcado na gravação como em P4. O intervalo é o
   mesmo da M2.1.1, para que o tempo em Wi-Fi sirva de base de comparação para as outras
   condições.
6. Se a sessão expirar, o proprietário faz o login de novo e a tentativa seguinte recomeça da
   tela inicial autenticada.

## 4. Rastreabilidade entre as Fases 2 e 3

A tabela liga cada métrica da Fase 2 ao procedimento que a obtém, aos contextos medidos, ao
instrumento e ao arquivo de dados. Os arquivos ficam em `dados/brutos/` e as evidências em
`evidencias/fase4/`, com nome `<sessao>-<bloco>-<canal>-<metrica>-<veiculo>-<repeticao>-<AAAA-MM-DD>` para evitar sobrescritas. Os modelos CSV já estão em `dados/brutos/`; o dicionário, os denominadores, as regras para falhas e os cálculos estão em `dados/README.md`.

| Questão | Métrica | Procedimento | Contextos | Instrumento | Arquivo de dados | Resultado comparado com |
|---|---|---|---|---|---|---|
| Q1.1 | M1.1.1 | P1 | Referência | Prints da lista | `campos-por-infracao.csv` | Faixas percentuais |
| Q1.1 | M1.1.2 | P1 | Referência | Prints do detalhamento | `campos-por-infracao.csv` | Faixas percentuais |
| Q1.2 | M1.2.1 | P2 | Referência | Prints dos dois canais | `comparacao-canais.csv` | Faixas percentuais |
| Q1.2 | M1.2.2 | P2 | Referência | Resultado da M1.2.1 | `comparacao-canais.csv` | Faixas percentuais |
| Q1.3 | M1.3.1 | P3 | Referência | Gravação de tela | `fluxo.csv` | Faixas de passos |
| Q1.3 | M1.3.2 | P3 | Referência | Gravação de tela | `fluxo.csv` | Faixas de telas |
| Q2.1 | M2.1.1 | P4 | Referência | Gravação de tela; DevTools no portal | `tempos.csv` | Faixas de tempo (mediana) |
| Q2.1 | M2.1.2 | P4 | Referência | Gravação de tela; DevTools no portal | `tempos.csv` | Faixas de tempo (mediana) |
| Q2.2 | M2.2.1 | P5 | Referência (Android no aplicativo) | DevTools (HAR); `adb dumpsys netstats` | `volume.csv` | Faixas de volume |
| Q3.1 | M3.1.1 | P6 | Plataformas da Fase 1 | Registro de execução | `tentativas.csv` | Faixas percentuais |
| Q3.1 | M3.1.2 | P6 | Navegadores do portal | Registro de execução | `tentativas.csv` | Faixas percentuais |
| Q3.2 | M3.2.1 | P7 | Wi-Fi, 4G, rede degradada | Registro de execução; `tc netem` | `tentativas.csv` | Faixas percentuais |
| Q3.2 | M3.2.2 | P7 | Wi-Fi, 4G, rede degradada | Gravação de tela; registro de execução | `tentativas.csv` | Faixas de falha |
| Q3.2 | M3.2.3 | P7 | Wi-Fi, 4G, rede degradada | Gravação de tela | `tempos.csv` | Faixas de tempo (mediana) |

*Tabela 3 — Rastreabilidade métrica → procedimento → dado. Fonte: elaborada pela equipe.*

Os resultados são julgados com os níveis de pontuação e as regras de agregação da
[Fase 2](fase2-metricas.md): uma questão é atendida quando todas as suas métricas atingem pelo
menos o nível Mínimo aceitável, e o canal superior é o de nível maior em cada métrica.

## 5. Registro de desvios

Qualquer mudança em relação a estas instruções durante a coleta (repetição perdida, contexto
indisponível, parâmetro alterado, falha de gravação) é registrada no arquivo de desvios da
Fase 4, com data, procedimento afetado, motivo e efeito sobre a métrica. Medidas obtidas com
desvio continuam no repositório, marcadas, e a análise da Fase 4 decide se entram no cálculo.

## 6. Regras complementares de execução

Em P4/P5, limitar cada bloco a vinte tentativas medidas para obter dez válidas; se não for possível, reportar a amostra efetiva e o bloqueio. Em P7, manter dez tentativas após aquecimento sem substituir falhas do serviço. Erros de instrumento são registrados separadamente e sua reposição deve ser vinculada ao registro original. Aquecimentos e dados do piloto não entram nos resultados.

Métrica não medida é inconclusiva, nunca zero ou aprovação. A M3.1.2 aplica-se somente ao portal. Congelar no piloto o conjunto aplicável de P2, registrando a resolução da ambiguidade do denominador da ficha M1.2.1 antes da coleta. As regras de agregação por plataforma, P90, unidades e arredondamento estão no dicionário `dados/README.md`.
