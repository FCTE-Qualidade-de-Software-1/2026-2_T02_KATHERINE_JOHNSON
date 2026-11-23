# Scripts da S02 (P1–P5, contexto de referência)

Apoio à execução da S02 no contexto de referência: portal no Google Chrome do D01 (CT01) e
aplicativo no D03 (CT05), Wi-Fi, veículo V2 e infração V2-I1. O titular faz o login; os scripts não
digitam credenciais nem tocam em "Sair", e no app nunca usam o "voltar" do sistema.

**Privacidade:** valores dos campos, gravações, listas de requisições e saídas completas do `adb`
vão só para `dados/privado/S02/`, que o Git ignora. A saída padrão traz apenas presença, contagens,
horários e bytes. As capturas de P1 saem tarjadas e também ficam em `dados/privado/S02/` até a
revisão; só depois vão para `evidencias/fase4/capturas/S02/`.

| Arquivo | Uso |
|---|---|
| `campos.py` | Mapa dos rótulos de cada canal para R01–R15 e as velocidades (lista de referência da Fase 1) e normalização de valores da M1.2.1 |
| `portal_s02.js` | Portal: `campos`, `fluxo`, `tempo` e `volume` |
| `app_s02.py` | Aplicativo: `campos`, `fluxo`, `tempo` e `volume` |
| `consolidar_s02.py` | Gera as linhas propostas de `campos-por-infracao.csv` (P1) e `comparacao-canais.csv` (P2) a partir dos registros privados |

## Execução

`VEICULO_HASH` é o SHA-256 da placa do veículo de referência, calculado na página ou na tela; a
placa não é gravada. No app, `DATA=<data-da-infracao>` faz `fluxo` e `volume` irem até o cartão da
infração.

```bash
# P1/P2: lista e detalhe nos dois canais, com até 10 min entre eles
node portal_s02.js campos <data-da-infracao>
python3 app_s02.py campos <data-da-infracao>
python3 consolidar_s02.py campos --velocidade
python3 consolidar_s02.py paridade --velocidade

# P3: 3 execuções por canal (transições contadas na gravação)
node portal_s02.js fluxo 1
python3 app_s02.py fluxo 1

# P4: 1 aquecimento + 10 válidas por métrica e canal
node portal_s02.js tempo M2.1.1 1 <data-da-infracao>
python3 app_s02.py tempo M2.1.2 1 <data-da-infracao>

# P5: 1 aquecimento + 10 válidas por canal
node portal_s02.js volume 1
python3 app_s02.py volume 1
```

## Limites

- **P1/P2:** a presença vem do rótulo com valor preenchido (hífen conta como vazio). A comparação
  aplica a normalização da M1.2.1 (maiúsculas, acentos, símbolo monetário, separador decimal e
  formato de data); a segunda classificação independente continua obrigatória.
- **P3:** o script conta os cliques e as rolagens e grava o percurso; as transições são contadas na
  gravação.
- **P4:** o portal grava pelo screencast do Chrome (horário por quadro, marcação de clique) e propõe
  os quadros inicial e final; o app grava com `adb screenrecord` e "Mostrar toques", e dá só uma dica
  de tempo. A marcação final é feita na gravação, com segunda leitura independente. Início da
  M2.1.1 nos dois canais: toque ou clique em "Consultar", porque os dois canais exigem o filtro antes
  da lista; essa definição foi confirmada por Hugo em 22/11/2026 para o novo caso V4, antes da coleta.
- **P5:** portal pela soma de `encodedDataLength` do DevTools; app pela diferença do contador do UID.
  Os escopos diferem (piloto S01): os valores ficam separados, sem declarar um canal superior.
- Os scripts não foram executados contra o serviço; fazer um ensaio não contado de cada modo no
  início da S02.

## Continuação da coleta por Hugo

Instrumentos trazidos de `feat/pedro-s03-fase4`, commit `c305ad9`, para a branch
`feat/hugo-coleta-e2`, preservando o registro de consentimentos. A disponibilidade dos scripts
não comprova execução. Não preencher resultados nem `revisor` antes das leituras correspondentes.

As saídas públicas de erro do Android contêm somente a classe da exceção. O diagnóstico
completo fica no armazenamento privado, com acesso restrito. Não publicar árvore de interface,
contadores completos, identificadores USB, nomes, CPF, placas, números de auto ou gravações
originais. Para P4/P5, os resultados numéricos e a referência ao registro privado bastam para
a rastreabilidade; novas capturas públicas só entram após anonimização e revisão humana.

No Android, `SESSAO` seleciona o diretório privado (`S02` por padrão). `TELA_LARGURA`,
`TELA_ALTURA` e `ABAS_Y` permitem adaptar os gestos e o limite da barra de abas ao aparelho
observado. Conferir o roteiro visualmente antes de medir; a parametrização não confirma
compatibilidade nem torna aparelhos diferentes equivalentes.

## S06 / V4

A continuação com outro titular, veículo e aparelhos usa a sessão S06. Os instrumentos mantêm
os originais em `dados/privado/S02/V4/`; essa pasta operacional não altera a identidade pública
da sessão. `coletar_app.py` executa blocos, preserva interrupções e usa novo número nas reposições.
Instalar as dependências de análise com `pip install -r dados/scripts/s02/requirements.txt`.

`propor_marcacoes.py` e `propor_marcacoes_app.py` geram propostas privadas, sem substituir
a marcação visual nem a segunda leitura. O B04 da S06 foi excluído do cálculo por latência
artificial de rolagem. `consolidar_v4.py` publica somente campos permitidos dos CSV, sem
identificadores, datas de infração, URLs ou mensagens completas; `revisor` permanece vazio.
Não sobrescreve linhas que já tenham revisor. As propostas numéricas não são julgamento oficial.

O inventário registra D05 (Samsung) e D06 (computador 750XGK), distintos dos aparelhos do plano
anterior. Para validar a sessão sem ambiguidade, conferir também os desvios D016–D020 e o
registro público `evidencias/fase4/S06-registro-2026-11-22.md`.

## S08 / P7 no portal

`coletar_portal.js` executa blocos de tempo da lista no portal (`--modo lista` para P4 ou
`--modo p7` para M3.2.3), um registro privado por tentativa e vídeos nomeados com o bloco
(`tempo-portal-<bloco>-<métrica>-<rep>`), sem sobrescrever. No P7, concluída, falha, sessão
expirada e tempo limite entram no denominador; só erro de instrumento ganha novo número.
Uma página que não carrega em 60 s na preparação conta como falha do serviço.

```bash
CASO=V4 node coletar_portal.js --bloco B10 --modo p7 --sessao S08 --rede wifi
python3 propor_marcacoes.py ../../privado/S02/V4/B10-02.json
```

O Chrome de medição precisa estar visível ou iniciado com `--disable-backgrounding-occluded-windows`
e `--disable-renderer-backgrounding`: com a janela encoberta, o clique sintético e o screencast param.

`coletar_app.py --modo lista|p7` e `app_s02.tempo_lista` medem a lista do aplicativo **sem
rolagem**, com o ponto de toque registrado e o bloco no nome do vídeo. Exigem exibição em que a
primeira infração caiba na tela; na escala original do Samsung isso não ocorre, e esses modos
não foram executados (desvios D020 e D021).
