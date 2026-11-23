# Roteiro de medições e capturas

Este roteiro deixa a coleta pronta para execução e conferência. Os CSV permanecem sem linhas de
medição até haver observações reais. Não preencher com zero, estimativa, simulação ou valor de
exemplo. `não executado` e `não avaliado` são estados documentais, não resultados de métrica.

## Estado da preparação e atualização posterior

Os itens abaixo descrevem a preparação feita antes do recebimento do relatório de sessão. As
observações posteriores de S01 e as dez repetições de tempo/transferência estão transcritas em
[relatorio-s01-portal-2026-11-20.md](relatorio-s01-portal-2026-11-20.md); S01 continua sendo piloto,
fora dos resultados oficiais.

### Preparação anterior ao relatório

- S00: foi comunicada a concordância de três integrantes para usar as próprias contas. As vias
  individuais foram preparadas, mas não há comprovação de apresentação/leitura e assinatura dos
  termos, associação a veículos ou disponibilidade de infração elegível. Nenhuma identidade ou
  assinatura entra nesta pasta. **Atualização em 22/11/2026:** Hugo confirmou que os termos foram
  aplicados; a pendência de consentimento está concluída, com vias assinadas privadas. A associação
  dos códigos aos veículos continua sendo uma verificação separada.
- S01: o usuário informou que está autenticado no portal e a aba “Detran Digital” foi localizada
  no Chrome. As chamadas suportadas para ler a interface expiraram; não foi possível verificar a
  autenticação na página nem coletar uma tela. Nenhum dado da conta foi extraído.
- Aparelhos: o computador Linux de 64 bits foi inspecionado como candidato a D01, sujeito a
  confirmação. Não foi identificado Android via USB nesta execução. O detalhamento de hardware
  foi omitido dos registros públicos para reduzir a identificabilidade do equipamento.
- Medições nesta interação de preparação: não executadas. Nenhuma sessão foi liberada pelo agente
  do navegador. O relatório posterior documenta observações comunicadas pelo executor, sem alterar
  a limitação desta preparação nem promover S01 a resultado oficial.

## Valores que cada procedimento exige

| Procedimento | Execução real exigida | Quantidade mínima / regra | Registrar em |
|---|---|---|---|
| P1 — campos | Para cada veículo e infração selecionados, verificar R01–R15 na lista e no detalhe de cada canal; marcar presença sem copiar valores pessoais | Uma observação por campo/tela/canal; velocidade permitida e aferida acrescentam dois campos só em infração de velocidade | `dados/brutos/campos-por-infracao.csv` |
| P2 — paridade | Comparar a mesma infração nos dois canais, campo a campo, preservando valores pessoais só na conferência privada | 15 campos (17 para velocidade); consultas no intervalo máximo de 10 min; segundo avaliador independente | `dados/brutos/comparacao-canais.csv` |
| P3 — fluxo | Repetir o caminho inicial autenticado até a lista; contar cliques/toques e transições; registrar rótulos acionados, sem dados digitados | 3 execuções por canal; usar o valor recorrente; divergência entre as três vira desvio | `dados/brutos/fluxo.csv` |
| P4 — tempo | Medir seleção do veículo até lista completa e seleção da mesma infração até detalhe completo | 1 aquecimento + 10 válidas por métrica/canal; no máximo 20 tentativas medidas; segunda leitura independente e resolução se diferença >3 quadros | `dados/brutos/tempos.csv` |
| P5 — volume | Medir a consulta completa; no portal, total transferido no DevTools; no Android, diferença dos bytes recebidos+enviados do UID antes/depois | 1 aquecimento + 10 válidas por canal; registrar instrumento e escopo; validar equivalência no piloto; HAR fica privado | `dados/brutos/volume.csv` |
| P6 — contexto | Executar consulta até detalhe por plataforma/navegador/dispositivo disponível | 3 tentativas por contexto; aprovado com pelo menos 2 concluídas; contexto sem aparelho fica `não_avaliado`, com motivo real | `dados/brutos/tentativas.csv` |
| P7 — rede | Para cada rede (Wi-Fi, 4G e degradada), medir seleção do veículo até lista, por canal | 1 aquecimento + 10 tentativas por canal/rede; 60 s sem lista = tempo limite; falhas do serviço permanecem no denominador | `dados/brutos/tentativas.csv` e `dados/brutos/tempos.csv` |
| Ambiente | Registrar cada combinação sessão/contexto/rede usada, incluindo versões do software e instrumentos | Uma linha por sessão/contexto/rede realmente executada; não registrar SSID, MAC, IP público, IMEI ou número de série | `dados/brutos/ambientes.csv` |
| Desvios | Registrar perda de repetição, indisponibilidade, mudança de parâmetro, falha de instrumento ou reposição | Uma linha por ocorrência; vincular sessão/procedimento/métrica e explicar efeito sem identificar titular | `dados/brutos/desvios.csv` |

As regras completas de agregação, os campos R01–R15, a lista de contextos e os formatos estão em
[`docs/fase3-metodo.md`](../../docs/fase3-metodo.md), [`docs/fase1-produto.md`](../../docs/fase1-produto.md)
e [`dados/README.md`](../../dados/README.md). Os campos vazios dos CSV significam “sem observação”;
não significam ausência no portal/aplicativo nem valor zero.

## Capturas que Hugo deve enviar primeiro — piloto S01

Faça capturas no aparelho/tela em que a consulta realmente ocorreu. Se o portal ou o app não
mostrar uma tela, não a substitua por imagem de outra sessão; anote a indisponibilidade em
`modelo-sessao.md`.

| Arquivo a enviar | De onde tirar |
|---|---|
| `S01-portal-lista-veiculos.png` | Portal autenticado, tela com a lista de veículos; tarjar placa, nome, CPF, RENAVAM e qualquer identificador antes de enviar |
| `S01-portal-lista-infracoes-V1.png` | Portal, lista de infrações do veículo escolhido; manter rótulos, datas/status necessários à análise e ocultar placa, nome e número do auto |
| `S01-portal-detalhe-V1-I1.png` | Portal, detalhe da infração escolhida; manter rótulos e indicação de campo presente/ausente, tarjar todos os valores pessoais e identificadores |
| `S01-android-lista-veiculos.png` | Aplicativo Android autenticado, lista de veículos; mesma regra de tarja |
| `S01-android-lista-infracoes-V1.png` | Aplicativo Android, infrações do mesmo veículo usado no portal; tarjar identificadores |
| `S01-android-detalhe-V1-I1.png` | Aplicativo Android, detalhe da mesma infração comparada no portal; tarjar valores pessoais |
| `S01-ios-lista-veiculos.png`, `S01-ios-lista-infracoes-V1.png`, `S01-ios-detalhe-V1-I1.png` | Somente se Heitor executar de fato no iPhone; caso contrário, registrar contexto iOS como não avaliado, sem substituir por captura da App Store |

O código `V1`/`V1-I1` só é atribuído depois da seleção real; a tabela privada que liga código a
titular/veículo nunca é enviada. Não capture login, senha, OTP, tela de consentimento assinado,
notificações ou documentos. A captura precisa ser tarjada antes do envio, não depois de entrar no
repositório. Envie somente as cópias já revisadas; não envie HAR, gravação original ou imagem com
CPF, placa, RENAVAM, nome, endereço, CNH, número do auto, QR code ou assinatura.

## Evidência adicional para as métricas

As seis capturas acima cobrem o levantamento do S01, não substituem as repetições oficiais S02–S05.
Para a coleta, criar subpastas por sessão em `evidencias/fase4/capturas/` e usar nomes que liguem
cada imagem a sessão, procedimento, canal, tela, códigos e data. Nunca inserir a placa ou número do
auto no nome do arquivo.

- **P1/P2:** uma captura anonimizada da lista e do detalhe para cada canal/infração. Registrar no
  CSV presença e classificação, nunca os valores textuais dos dados pessoais. A revisão independente
  usa as mesmas cópias anonimizadas e deixa a decisão em `modelo-sessao.md`.
- **P3:** três execuções por canal. Guardar o original da gravação em local privado; enviar somente
  quadros anonimizados que ilustrem o fluxo. Os números de passos, transições e rolagens vão em
  `fluxo.csv`.
- **P4/P7:** usar gravação local para marcar os quadros/timestamps de início e fim; não enviar o
  vídeo original. Enviar quadros inicial/final já tarjados com os códigos de repetição no nome. Os
  valores de tempo, resultado e leitura independente vão em `tempos.csv`.
- **P5:** portal: captura da aba Network com apenas total transferred visível e sem URLs, cabeçalhos,
  payloads ou tokens. Android: capturas do contador antes/depois com apenas o nome do app e bytes,
  sem identificadores do aparelho. Registrar números e ferramenta em `volume.csv`; HAR e saídas
  completas do `adb` permanecem privadas.
- **P6:** captura anonimizada do resultado de cada contexto executado; versões exatas e 3 resultados
  por contexto em `ambientes.csv`/`tentativas.csv`. Dispositivo indisponível é registrado como não
  avaliado com motivo, não como falha.
- **Rede:** capture a condição ativa (Wi-Fi, 4G ou degradada) e a velocidade configurada/medida,
  sem SSID, MAC, IP, telefone ou credenciais. As tentativas e resultados entram em `tentativas.csv`.

### Destino dos arquivos

Depois de revisar a tarja, colocar as imagens S01 em
`evidencias/fase4/capturas/S01/` e as demais em
`evidencias/fase4/capturas/<sessao>/`. Este PR inclui o roteiro e a pasta pode ser criada no
repositório quando as primeiras cópias anonimizadas forem adicionadas. Consentimentos assinados,
correspondência código–titular, gravações originais, HAR e tabelas com valores pessoais ficam em
armazenamento privado, nunca no Git ou na issue.
