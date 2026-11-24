# S02 (P1, P2 e P3) — registro da segunda leitura independente

Registro da conferência da S02 de 22/11/2026, feita em 23/11/2026. Não contém valores pessoais:
somente presença, classificação e contagens. Os valores, as gravações e os JSON ficam em
`dados/privado/S02/`, que o Git ignora.

## 1. Identificação

| Item | Registro |
|---|---|
| Sessão conferida | S02, 22/11/2026 (registro da primeira leitura em [S02-registro-2026-11-22.md](S02-registro-2026-11-22.md)) |
| Infração de referência | V2-I1 (infração de velocidade) |
| Canais e contextos | Portal no Chrome (CT01) e aplicativo 2.7.0 no Android (CT05) |
| Rede | Wi-Fi |
| Conferente | Heitor, que não participou da execução da S02 (script supervisionado por Pedro Druck, com o titular logado nos canais) |
| Data da conferência | 23/11/2026 |
| Escopo | P1 (presença dos campos), P2 (comparação entre canais) e P3 (fluxo) |

### Como a segunda leitura foi feita

| Procedimento | Material examinado pelo conferente |
|---|---|
| P1 | `portal-campos.json`, `app-campos.json`, as capturas originais e os demais arquivos de apoio da pasta privada da S02 |
| P2 | Comparação, campo a campo, dos valores privados exibidos no portal e no aplicativo |
| P3 | As seis gravações (três do portal e três do aplicativo) |

As tabelas deste registro seguem o formato do resumo da primeira leitura, usado como modelo de
preenchimento. Os resultados foram conferidos pelo conferente nas fontes acima.

## 2. P1 — presença dos campos

### Critério

Um campo é presente quando o rótulo correspondente traz algum conteúdo. Campo vazio ou só com hífen
(`-`) é ausente. Quando há dois rótulos para o mesmo campo, basta um preenchido. As velocidades
permitida e aferida entram só no detalhe: a lista usa denominador 15 e o detalhe, 17.

### Resultado da segunda leitura

| ID | Campo | Portal / lista | App / lista | Portal / detalhe | App / detalhe |
|---|---|---:|---:|---:|---:|
| R01 | Tipificação da infração (código e descrição) | NÃO | NÃO | SIM | SIM |
| R02 | Enquadramento legal | NÃO | NÃO | SIM | SIM |
| R03 | Local da infração | NÃO | NÃO | SIM | SIM |
| R04 | Data da infração | SIM | SIM | SIM | SIM |
| R05 | Hora da infração | NÃO | NÃO | SIM | SIM |
| R06 | Placa do veículo | NÃO | NÃO | SIM | SIM |
| R07 | Marca/modelo | NÃO | NÃO | SIM | SIM |
| R08 | Órgão autuador | SIM | SIM | SIM | SIM |
| R09 | Número do auto | SIM | SIM | SIM | SIM |
| R10 | Natureza (gravidade) | NÃO | NÃO | SIM | SIM |
| R11 | Pontuação | SIM | SIM | SIM | SIM |
| R12 | Valor da multa | NÃO | NÃO | SIM | SIM |
| R13 | Data de vencimento | NÃO | NÃO | SIM | SIM |
| R14 | Prazo de defesa prévia / condutor | NÃO | NÃO | SIM | NÃO |
| R15 | Situação da infração | SIM | SIM | SIM | SIM |
| velocidade_permitida | Velocidade permitida (somente detalhe) | n/a | n/a | SIM | SIM |
| velocidade_aferida | Velocidade aferida (somente detalhe) | n/a | n/a | SIM | SIM |
| **Total** | | **5 de 15** | **5 de 15** | **17 de 17** | **16 de 17** |

### Comparação com a primeira leitura

| Contexto | Primeira leitura (script) | Segunda leitura | Resultado |
|---|---:|---:|---|
| Portal / lista | 5 de 15 | 5 de 15 | Concordância |
| App / lista | 5 de 15 | 5 de 15 | Concordância |
| Portal / detalhe | 17 de 17 | 17 de 17 | Concordância |
| App / detalhe | 16 de 17 | 16 de 17 | Concordância |

Sem divergência. Nas duas leituras o portal exibe os 17 campos aplicáveis no detalhe e o aplicativo
exibe 16: o R14 (prazo de defesa prévia / identificação do condutor infrator) está ausente no
detalhe do aplicativo.

## 3. P2 — comparação entre canais

### Critério

A comparação usa os campos do detalhe nos dois canais, com a normalização da M1.2.1: maiúsculas,
acentos, símbolo monetário, separador decimal e formato de data não contam como divergência.
Categorias: paritário, divergente, ausente no portal, ausente no aplicativo e ausente em ambos.

### Resultado da segunda leitura

| Campo | Nome | Classificação (segunda leitura) | Elegível |
|---|---|---|---|
| R01 | Tipificação da infração (código e descrição) | Paritário | Sim |
| R02 | Enquadramento legal | Paritário | Sim |
| R03 | Local da infração | Paritário | Sim |
| R04 | Data da infração | Paritário | Sim |
| R05 | Hora da infração | Paritário | Sim |
| R06 | Placa do veículo | Paritário | Sim |
| R07 | Marca/modelo | Paritário | Sim |
| R08 | Órgão autuador | Paritário | Sim |
| R09 | Número do auto | Paritário | Sim |
| R10 | Natureza (gravidade) | Paritário | Sim |
| R11 | Pontuação | Paritário | Sim |
| R12 | Valor da multa | Paritário | Sim |
| R13 | Data de vencimento | Paritário | Sim |
| R14 | Prazo de defesa prévia / condutor | Ausente no aplicativo | Sim |
| R15 | Situação da infração | Paritário | Sim |
| velocidade_permitida | Velocidade permitida | Paritário | Sim |
| velocidade_aferida | Velocidade aferida | Paritário | Sim |

### Comparação com a primeira leitura

| Classificação | Primeira leitura (script) | Segunda leitura |
|---|---:|---:|
| Paritário | 16 | 16 |
| Divergente | 0 | 0 |
| Ausente no portal | 0 | 0 |
| Ausente no aplicativo | 1 | 1 |
| Ausente em ambos | 0 | 0 |
| **Total** | **17** | **17** |

Sem divergência. Como a M1.2.2 só aceita "sem divergência" quando todos os campos aplicáveis são
paritários, a ausência do R14 impede que a V2-I1 seja classificada como paritária no par de canais.
Intervalo entre os canais: portal às 17:04:50 e aplicativo às 17:06:11 (81 segundos), dentro do
limite de dez minutos.

## 4. P3 — fluxo de navegação

### Critérios

- **Passo:** clique ou toque em elemento interativo, seleção ou preenchimento de campo.
- **Transição:** mudança do conteúdo principal da tela (nova página, nova rota ou diálogo que ocupa
  a tela).
- **Rolagem:** não conta como passo; é anotada à parte.
- Abrir um diálogo que ocupa a tela conta como transição; fechá-lo e voltar à tela anterior não
  conta (desvio D015).

### Portal — bloco B01

| Repetição | Início | Passos (script) | Passos (conferente) | Transições (script) | Transições (conferente) | Rolagens (script) | Rolagens (conferente) |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 17:17:32 | 4 | 4 | 3 | 3 | 0 | 0 |
| 2 | 17:17:52 | 4 | 4 | 3 | 3 | 0 | 0 |
| 3 | 17:18:13 | 4 | 4 | 3 | 3 | 0 | 0 |

Caminho: Infração > Histórico de infrações por veículo > Selecionar > Consultar. Sem divergência.

### Aplicativo — bloco B02

| Repetição | Início | Passos (script) | Passos (conferente) | Transições (script) | Transições (conferente) | Rolagens (script) | Rolagens (conferente) |
|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 17:10:10 | 6 | 6 | 5 | 5 | 2 | 2 |
| 2 | 17:11:17 | 6 | 6 | 5 | 5 | 2 | **1** |
| 3 | 17:12:24 | 6 | 6 | 5 | 5 | 2 | 2 |

Caminho: Infrações > Histórico de infrações por veículo > veículo > Situação da Multa: Selecionar >
Todas > Consultar.

**Divergência na repetição 2:** o conferente contou **uma** rolagem na gravação; o script registrou
**duas**. Passos e transições coincidem nas três repetições. A rolagem não entra no valor da M1.3.1
(passos) nem da M1.3.2 (transições), então o resultado dessas métricas não muda. Pelo método,
divergências são resolvidas em conjunto: a decisão final do valor da repetição 2 depende da revisão
conjunta com Pedro Druck (que supervisionou a S02) sobre a gravação. Até lá o `fluxo.csv` mantém o
valor do script (2) e a linha da repetição 2 do aplicativo permanece **sem `revisor`**.

### Resumo de P3

| Canal | Contagem | Primeira leitura (script) | Segunda leitura | Resultado |
|---|---|---|---|---|
| Portal | Passos | 4, 4, 4 | 4, 4, 4 | Concordância |
| Portal | Transições | 3, 3, 3 | 3, 3, 3 | Concordância |
| Portal | Rolagens | 0, 0, 0 | 0, 0, 0 | Concordância |
| Aplicativo | Passos | 6, 6, 6 | 6, 6, 6 | Concordância |
| Aplicativo | Transições | 5, 5, 5 | 5, 5, 5 | Concordância |
| Aplicativo | Rolagens | 2, 2, 2 | 2, 1, 2 | Divergência na repetição 2, resolvida em conjunto: 1 rolagem |

### Resolução da divergência (23/11/2026)

Heitor e Pedro Druck reviram juntos a gravação da repetição 2 do aplicativo e decidiram por **uma**
rolagem: há um único gesto efetivo de rolagem até a lista. O `fluxo.csv` passou a registrar 1 nessa
repetição, com `revisor` "Heitor e Pedro Druck". Registro em
[segunda-leitura-p4-p7-2026-11-23.md](segunda-leitura-p4-p7-2026-11-23.md), Seção 3.

## 5. Quadro consolidado

| Parte | Segunda leitura | Comparação com a primeira leitura | Situação |
|---|---|---|---|
| P1 | 5/15, 5/15, 17/17 e 16/17 | Sem divergência | Conferido |
| P2 | 16 paritários e 1 ausente no aplicativo (R14) | Sem divergência | Conferido |
| P3, portal | 4 passos, 3 transições e 0 rolagens nas três repetições | Sem divergência | Conferido |
| P3, aplicativo | 6 passos e 5 transições nas três repetições; rolagens 2, 1 e 2 | Uma divergência (rolagens, repetição 2) | Conferido; repetição 2 resolvida em conjunto (1 rolagem) |

## 6. Referências

- Primeira leitura: `dados/brutos/campos-por-infracao.csv` (64 linhas da S02),
  `dados/brutos/comparacao-canais.csv` (17 linhas) e `dados/brutos/fluxo.csv` (6 linhas).
- Método: [Método e instruções para o avaliador](../../docs/fase3-metodo.md) (P1 a P3 e regra de
  conferência por um segundo avaliador).
