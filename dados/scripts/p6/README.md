# Scripts da P6 (S03)

Scripts usados para executar a P6 na S03 de 21/11/2026 (desvio D001). Cada tentativa parte da tela
inicial autenticada, segue o caminho até o detalhe da infração escolhida e salva uma captura já
tarjada: todo texto que não é rótulo conhecido vira bloco preto antes da captura. O login é sempre
feito pelo titular; os scripts não digitam credenciais nem tocam em "Sair".

| Arquivo | Uso |
|---|---|
| `conectar.js` | Conecta ao Chrome do computador (DevTools, porta 9222), ao Firefox (WebDriver BiDi, 9223) ou ao Chrome do Android (DevTools via `adb forward`, 9224) |
| `tentativa.js` | Uma tentativa no portal: menu Infração → Histórico de infrações por veículo → Selecionar → período 01/01/2024–31/12/2024 → Consultar → detalhe |
| `calendario.js` | Escolhe as datas pelo calendário do portal (os campos de data são somente leitura) |
| `levantamento.js` | Conta as infrações do veículo em janelas de 1 ano nos últimos 5 anos, sem guardar valores |
| `app.py` | Lê a árvore de interface do app pelo `adb` (uiautomator) e toca nos elementos |
| `tentativa_app.py` | Uma tentativa no app: Infrações → Histórico de infrações por veículo → lista; reconhece a mensagem de erro do app |
| `tentativa_app_detalhe.py` | Uma tentativa no app 2.7.0 até o detalhe: rola a tela inicial, Infrações → Histórico de infrações por veículo → veículo → Situação "Todas" → Consultar → infração da data informada → detalhe; fecha o detalhe pelo cabeçalho do app (S05, D010) |

## Preparação

```bash
npm ci
```

Abrir o navegador com controle remoto e perfil próprio, para o titular fazer o login:

```bash
google-chrome-stable --remote-debugging-port=9222 --user-data-dir=/tmp/perfil-p6 "https://portal.detran.df.gov.br/#/home"
```

Para o Chrome do Android, com a depuração USB ligada:

```bash
adb forward tcp:9224 localabstract:chrome_devtools_remote
```

## Execução

Portal no computador (CT01). O terceiro argumento é a data da infração escolhida, como aparece na
lista; não registrar essa data no repositório:

```bash
CAPTURAS=capturas node tentativa.js chrome 1 <data-da-infracao> B01
```

Portal no Chrome do Android (CT03). `TOQUE=1` aciona os elementos pelo evento de clique da página,
porque o toque sintético sai deslocado pela barra do Chrome (desvio D007):

```bash
TOQUE=1 CAPTURAS=capturas node tentativa.js android 1 <data-da-infracao> B03
```

Aplicativo no Android (CT05), com o app aberto e logado:

```bash
BLOCO=B02 python3 tentativa_app.py 1 capturas
```

Cada execução imprime uma linha JSON com resultado, motivo, início, passos e nome da captura, que
alimenta `dados/brutos/tentativas.csv`. Conferir cada captura antes de copiá-la para
`evidencias/fase4/capturas/`. A `SESSAO` padrão é S03.

Aplicativo 2.7.0 até o detalhe (S05, CT05), com o app aberto e logado. O terceiro argumento é a
data da infração como aparece no resultado; não registrá-la no repositório. `VEICULO` é a posição
do veículo na lista de veículos atuais:

```bash
SESSAO=S05 BLOCO=B01 VEIC=V2 VEICULO=1 python3 tentativa_app_detalhe.py 1 capturas <data-da-infracao>
```

No PowerShell do Windows, definir as variáveis com `$env:SESSAO='S05'` etc. e chamar `python`.
