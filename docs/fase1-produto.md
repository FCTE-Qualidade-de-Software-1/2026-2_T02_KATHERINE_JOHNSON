# Fase 1 — Descrição do Produto e Modelo de Qualidade

**Projeto Final FGA0315 Qualidade de Software 1 (UnB/FGA, 2026/2)**  
*Avaliação da consulta de infrações do Detran-DF: Portal de Serviços × aplicativo*  
*Responsável: Hugo Freitas Silva*  
*Data do levantamento: 18/10/2026*

---

## 1. Levantamento dos canais

### 1.1 Método do levantamento

O levantamento usou apenas informações acessíveis a qualquer cidadão, sem credenciais e sem acesso à infraestrutura do Detran-DF:

1. **Acesso público ao Portal de Serviços** em navegador desktop (Google Chrome, Linux), em 18/10/2026, com captura das telas públicas (ver Seção 1.6).
2. **Páginas oficiais do aplicativo** na Google Play e na App Store, com capturas da parte superior das páginas, e consulta aos metadados públicos das duas lojas (iTunes Lookup e dados da página da Google Play), em 18/10/2026. Registro dos metadados: [`evidencias/fase1/levantamento-publico-2026-10-26.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/levantamento-publico-2026-10-26.md) (Seção 1) e [`evidencias/fase1/app-ios-app-store-metadados-2026-10-26.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/app-ios-app-store-metadados-2026-10-26.json).
3. **Inspeção do código cliente público do portal**, isto é, os arquivos que o próprio navegador baixa ao abrir a página e que qualquer usuário pode ver nas ferramentas de desenvolvedor. Essa inspeção não dá acesso ao código do servidor e serviu só para identificar rótulos de tela, rotas e serviços externos. Registro dos recursos carregados e dos rótulos encontrados no código: [`evidencias/fase1/levantamento-publico-2026-10-26.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/levantamento-publico-2026-10-26.md) (Seção 2).
4. **Inspeção do pacote público do aplicativo Android**, versão 2.6.9 (código de versão 244, o mesmo publicado na Google Play), obtido no espelho público APKPure em 18/10/2026. Foram lidos apenas o manifesto, a lista de bibliotecas e a tabela de textos do pacote, com o mesmo objetivo do item 3. A versão iOS não foi inspecionada; presume-se o mesmo código-base, a confirmar no aparelho iOS. Registro do pacote instalado pela Google Play (versão, bibliotecas, assinatura do bytecode Hermes e rótulos encontrados): [`evidencias/fase1/app-android-pacote-2026-10-26.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/app-android-pacote-2026-10-26.md).

Os itens que dependem de login com um veículo real (rótulos exatos das telas logadas, contagem de passos e campos efetivamente exibidos) serão confirmados na sessão de levantamento descrita em `evidencias/fase1/roteiro-levantamento.md`.

### 1.2 Identificação dos canais

| Item | Portal de Serviços | Aplicativo |
|---|---|---|
| Nome oficial | "Detran Digital", apresentado como "Portal de Serviços do Departamento de Trânsito do Distrito Federal (Detran/DF)" | "DETRAN-DF" nas duas lojas; a descrição na Google Play o chama de "DETRAN DIGITAL" |
| Endereço / identificador | <https://portal.detran.df.gov.br> | Android: `br.com.mesotec.detrandf` · iOS: `id1526746296` |
| Publicador | Detran-DF | App Store: "Departamento de Trânsito do Distrito Federal". Google Play: "DETRAN DF", com contato `appdetran@detran.df.gov.br` |
| Versão avaliada | Não há número de versão público; o pacote principal carregado em 26/10/2026 é `main-es2017.922e684e19a946a612c1.js` | 2.6.9 no iOS (publicada em 13/10/2026) e na Google Play (atualizada em 09/10/2026) |
| Primeira publicação | — | App Store: 17/08/2020 · Google Play: 14/08/2020 |
| Plataformas | Navegador em desktop e em celular | Android e iOS |
| Requisito mínimo | Não declarado | iOS 15.1 ou superior · Android 8.0 ou superior |
| Tamanho do pacote | — | 43,5 MB no iOS |
| Instalações | — | Mais de 1 milhão na Google Play |
| Autenticação | CPF/CNPJ e senha, com reCAPTCHA, ou botão "Entrar com gov.br" | CPF/CNPJ e senha, ou "Entrar com" gov.br; depois do primeiro acesso, login por biometria opcional. Mesma conta do portal (mesmo servidor de identidade) |
| A consulta exige login? | Sim. As telas de infrações do veículo ficam na área logada e listam só os veículos vinculados ao CPF do usuário ("Veículos atuais de minha propriedade"). Há também a opção "Consultar veículo de outra UF". | Sim, pela mesma lógica: a opção "Histórico de infrações por veículo" fica na área logada. A tela inicial oferece "Serviços abertos" sem login (ver nota abaixo) |

**Nota sobre consulta sem login.** Os dois canais têm uma consulta pública de **débitos** do veículo (serviço `acesso-publico/debitos`), que inclui débitos de infrações a pagar. Ela não substitui o histórico de infrações: mostra só o que está pendente de pagamento, sem o detalhamento da autuação. Por isso o objeto da avaliação continua sendo o histórico de infrações por veículo, na área logada. Cabe ao Heitor registrar esse corte no escopo.

### 1.3 Passos da consulta

Sequência provável nos dois canais, deduzida das telas públicas, das telas de divulgação nas lojas e dos nomes de menu e de tela presentes no código cliente. A contagem definitiva de telas e ações será feita com veículo real (ver `evidencias/fase1/roteiro-levantamento.md`).

| # | Portal de Serviços | Aplicativo |
|---|---|---|
| 1 | Abrir <https://portal.detran.df.gov.br> | Abrir o aplicativo |
| 2 | "Fazer login" e autenticar (CPF/CNPJ + senha + reCAPTCHA, ou gov.br) | "Entrar" e autenticar (CPF/CNPJ + senha, gov.br ou biometria) |
| 3 | Na área de serviços, abrir o grupo de consultas de infração | Na tela inicial, abrir "Infrações" ("Transferência de pontuação e mais") |
| 4 | Escolher "Histórico de infrações por veículo" | Escolher "Histórico de infrações por veículo" |
| 5 | Selecionar o veículo na lista "Veículos atuais de minha propriedade" | Selecionar o veículo |
| 6 | Ver a lista de infrações e escolher uma ("Selecione a multa desejada") | Ver a "Lista de infrações" e escolher uma |
| 7 | Ver a tela "Detalhes da infração" | Ver o detalhamento ("Confira o detalhamento da infração") |

O menu "Infração" do cabeçalho público do portal leva a outros serviços ("Identificação de infrator" e "Notificação de penalidade"), não ao histórico.

### 1.4 Campos exibidos por infração

Rótulos previstos nos dois canais, extraídos do código cliente do portal (tela "Detalhes da infração") e da tabela de textos do aplicativo. No aplicativo os textos não estão ligados a uma tela específica, então a coluna indica que o rótulo existe no pacote, não que aparece no detalhamento. Em ambos os casos, um rótulo previsto não garante que o dado apareça preenchido; a presença efetiva será conferida com veículo real.

| Grupo | Portal de Serviços | Aplicativo |
|---|---|---|
| Veículo | Placa · UF · Marca/Modelo | Placa · Marca/Modelo |
| Identificação da infração | Infração · Descrição da Infração · Regulamento · Natureza · Auto Infração · Código Renainf · Órgão Autuador · Responsável pela Infração | Infração · Descrição da infração · Regulamento · Natureza · Auto Infração · Código RENAINF · Órgão Autuador · Responsável pela infração |
| Ocorrência | Data Infração · Hora Infração · Local da Infração · Velocidade Permitida · Velocidade Aferida | Data Infração · Hora Infração · Local da Infração · Velocidade Permitida · Velocidade Aferida |
| Prazos | Data da Notif. de Autuação · Data da Notif. de Penalidade · Data da Defesa Prévia · Identificação do Condutor Infrator · Data de Vencimento | Data da Notif. de Autuação · Data da Notif. de Penalidade · Data limite para defesa prévia · Identificação condutor infrator · Data de Vencimento · Data opção desconto 40% - SNE |
| Valores | Valor da Multa · Valor Correção · Valor Desconto · Valor Devido | Valor da Multa · Valor Correção · Valor Desconto · Valor Devido |
| Situação | Pontuação Infração/Status · Situação Pagamento · Situação Multa | Pontuação da Infração · Situação do pagamento · Situação Multa |

Diferenças previstas, a confirmar com veículo real: o aplicativo não tem um rótulo "UF" isolado e tem um rótulo a mais, "Data opção desconto 40% - SNE", ligado ao Sistema de Notificação Eletrônica.

Nos dois canais, o campo "Código Renainf" traz a dica "Origem: RENAINF", o que indica que parte dos dados vem do Registro Nacional de Infrações de Trânsito, e não só da base do Detran-DF.

### 1.5 Lista de referência de campos (insumo para a questão Q1.1)

Para julgar a completude funcional sem depender de um dos canais como padrão, propõe-se uma lista de referência externa. Ela parte do conteúdo obrigatório do auto de infração (art. 280 do Código de Trânsito Brasileiro, Lei nº 9.503/1997) e acrescenta as informações de que o cidadão precisa para decidir o que fazer com a multa (pagar, recorrer, indicar condutor). Os textos legais foram conferidos no Planalto em 18/10/2026.

| ID | Campo de referência | Fundamento | Rótulo no portal | Rótulo no aplicativo |
|---|---|---|---|---|
| R01 | Tipificação da infração (código e descrição) | CTB, art. 280, I | Infração · Descrição da Infração | Infração · Descrição da infração |
| R02 | Enquadramento legal | Complementa o art. 280, I | Regulamento | Regulamento |
| R03 | Local da infração | CTB, art. 280, II | Local da Infração | Local da Infração |
| R04 | Data da infração | CTB, art. 280, II | Data Infração | Data Infração |
| R05 | Hora da infração | CTB, art. 280, II | Hora Infração | Hora Infração |
| R06 | Placa do veículo | CTB, art. 280, III | Placa | Placa |
| R07 | Marca/modelo do veículo | CTB, art. 280, III | Marca/Modelo | Marca/Modelo |
| R08 | Órgão autuador | CTB, art. 280, V | Órgão Autuador | Órgão Autuador |
| R09 | Número do auto de infração | Identifica a autuação em pagamento, defesa e recurso | Auto Infração | Auto Infração |
| R10 | Natureza (gravidade) | CTB, art. 258 | Natureza | Natureza |
| R11 | Pontuação | CTB, art. 259 | Pontuação Infração/Status | Pontuação da Infração |
| R12 | Valor da multa | CTB, art. 258 | Valor da Multa · Valor Devido | Valor da Multa · Valor Devido |
| R13 | Data de vencimento | Necessária para pagar no prazo | Data de Vencimento | Data de Vencimento |
| R14 | Prazo de defesa prévia ou de indicação do condutor | Necessário para exercer a defesa | Data da Defesa Prévia · Identificação do Condutor Infrator | Data limite para defesa prévia · Identificação condutor infrator |
| R15 | Situação da infração | Indica se ainda há algo a fazer | Situação Pagamento · Situação Multa | Situação do pagamento · Situação Multa |

Ficam fora da lista os incisos IV (prontuário do condutor) e VI (assinatura do infrator) do art. 280, porque são dados pessoais que não fazem parte da consulta pelo proprietário. Velocidade permitida e aferida só se aplicam a infrações de velocidade e entram como campos condicionais, não na contagem geral. A lista é usada nas métricas M1.1.1 (tela de lista) e M1.1.2 (tela de detalhamento), e os campos comuns da Seção 1.4 na métrica M1.2.1, definidas pelo Philipe em `docs/fase2-metricas.md`.

### 1.6 Evidências

| Arquivo | Conteúdo | Dados pessoais |
|---|---|---|
| [`evidencias/fase1/portal-pagina-inicial-2026-10-18.png`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/portal-pagina-inicial-2026-10-18.png) | Página inicial pública do Portal de Serviços, com o nome oficial e o menu "Infração" | Nenhum (imagem ilustrativa do próprio portal) |
| [`evidencias/fase1/portal-login-2026-10-18.png`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/portal-login-2026-10-18.png) | Tela de login: CPF/CNPJ, senha, reCAPTCHA e "Entrar com gov.br" | Nenhum (campos vazios) |
| [`evidencias/fase1/app-android-google-play-2026-10-18.png`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/app-android-google-play-2026-10-18.png) | Página do aplicativo na Google Play: nome, desenvolvedor, instalações e telas de divulgação | Nenhum (avaliações de usuários fora do recorte) |
| [`evidencias/fase1/app-ios-app-store-2026-10-18.png`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/app-ios-app-store-2026-10-18.png) | Página do aplicativo na App Store: publicador, categoria, tamanho e telas de divulgação | Primeiro nome exibido numa tela de divulgação coberto com tarja |
| [`evidencias/fase1/app-android-abertura-2026-10-26.png`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/app-android-abertura-2026-10-26.png) | Tela inicial do aplicativo no Android, sem login: "Bem-vindo ao Detran/DF Digital!", botões "Opções de cadastro", "Entrar" e "Entrar com gov.br" e os serviços abertos "Transferência de veículo de outra UF", "Empresas credenciadas" e "Administrativo Detran-DF" | Nenhum |
| [`evidencias/fase1/app-android-login-2026-10-26.png`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/app-android-login-2026-10-26.png) | Tela de login do aplicativo no Android: campos CPF/CNPJ e Senha, "Esqueceu?" e "Cadastre-se" | Nenhum (campos vazios) |
| [`evidencias/fase1/levantamento-publico-2026-10-26.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/levantamento-publico-2026-10-26.md) | Metadados públicos das lojas (versão, requisitos, datas) e, no portal, recursos carregados pelo navegador, nome e hash do arquivo principal e ocorrências dos rótulos de "Detalhes da infração" no código cliente | Nenhum |
| [`evidencias/fase1/app-ios-app-store-metadados-2026-10-26.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/app-ios-app-store-metadados-2026-10-26.json) | Resposta da consulta pública da App Store sobre o aplicativo | Nenhum |
| [`evidencias/fase1/app-android-pacote-2026-10-26.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/app-android-pacote-2026-10-26.md) | Pacote do aplicativo Android 2.6.9 instalado pela Google Play: hashes dos arquivos, bibliotecas do React Native e do Hermes e ocorrências dos rótulos de infração no código | Nenhum |

Os prints do aplicativo no Android foram capturados em 26/10/2026. No iOS, nenhum integrante da equipe possui iPhone, então as telas do aplicativo não foram capturadas; do iOS há apenas a página da App Store. As telas com login seguem pendentes. Prints pendentes, a fazer com veículo real e com tarja em placa, RENAVAM, CPF, nome, endereço e número do auto antes de entrar no repositório: lista de veículos, lista de infrações e detalhes de uma infração, nos dois canais. As regras de anonimização estão em [`evidencias/fase1/README.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/README.md).

**Capturas do levantamento**

![Página inicial pública do Portal de Serviços do Detran-DF, com o menu Infração](https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/main/evidencias/fase1/portal-pagina-inicial-2026-10-18.png){ width="420" loading=lazy }
![Tela de login do Portal de Serviços com campos de CPF ou CNPJ, senha, reCAPTCHA e botão Entrar com gov.br](https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/main/evidencias/fase1/portal-login-2026-10-18.png){ width="420" loading=lazy }
![Página do aplicativo do Detran-DF na Google Play, com nome, desenvolvedor e telas de divulgação](https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/main/evidencias/fase1/app-android-google-play-2026-10-18.png){ width="420" loading=lazy }
![Página do aplicativo do Detran-DF na App Store, com publicador, categoria e telas de divulgação](https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/main/evidencias/fase1/app-ios-app-store-2026-10-18.png){ width="420" loading=lazy }
![Tela inicial do aplicativo Detran/DF Digital no Android, com os botões Opções de cadastro, Entrar e Entrar com gov.br e os serviços abertos](https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/main/evidencias/fase1/app-android-abertura-2026-10-26.png){ width="220" loading=lazy }
![Tela de login do aplicativo Detran/DF Digital no Android, com os campos CPF/CNPJ e Senha vazios e o botão Entrar desabilitado](https://raw.githubusercontent.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/main/evidencias/fase1/app-android-login-2026-10-26.png){ width="220" loading=lazy }

---

## 2. Tipo de produto e descrição estruturada

### 2.1 Classificação

A consulta de infrações é um **serviço digital governamental ao cidadão**, oferecido por um sistema de informação do Detran-DF com dois clientes:

- **Portal de Serviços:** aplicação web de página única (SPA) feita em Angular 12 com Angular Material, executada no navegador;
- **aplicativo:** cliente móvel multiplataforma feito em React Native, com o motor JavaScript Hermes (o pacote Android traz `index.android.bundle` em bytecode Hermes e as bibliotecas `libhermes.so` e `libreactnative.so`). As telas são componentes nativos, não uma página web embutida.

Os dois clientes não guardam as infrações: consultam serviços de backend do Detran-DF, que por sua vez reúnem dados próprios e de bases nacionais, como o RENAINF.

### 2.2 Descrição lado a lado

| Aspecto | Portal de Serviços | Aplicativo |
|---|---|---|
| Módulos usados na consulta | Autenticação; módulo "Infração" (histórico por veículo, detalhes, débitos e emissão de boleto/PIX) | Autenticação; menu "Infrações" (histórico por veículo e por condutor, detalhamento, indicação de condutor, boleto) |
| Interface com o usuário | Navegador, layout responsivo para desktop e celular | Telas do aplicativo |
| Interface com o backend | API HTTPS em `api5.detran.df.gov.br` (ex.: serviço `portal/infracoes`) | Mesma família de APIs (`api5`, `api4` e `api.detran.df.gov.br`), mas com serviço próprio para infrações (`app/verifica-multa`, rota `veiculo/lista-infracao`) |
| Identidade | Servidor OpenID Connect do Detran-DF (`acesso.detran.df.gov.br`) e gov.br (`sso.acesso.gov.br`) | O mesmo servidor OpenID Connect (mesmo domínio de autenticação, `detran-portal`) e gov.br |
| Dependências externas no carregamento | Google reCAPTCHA; Google Fonts; jQuery servido por `code.jquery.com`; agente de monitoramento Dynatrace | Firebase (notificações e relatórios de falha) e agente de monitoramento Dynatrace |
| Origem dos dados | Base do Detran-DF e RENAINF (dica "Origem: RENAINF") | A mesma: o aplicativo traz a mesma dica "Origem: RENAINF" |
| Plataformas | Qualquer navegador moderno, em desktop ou celular | Android 8.0 ou superior e iOS 15.1 ou superior |
| Restrições | Login obrigatório; reCAPTCHA no login com CPF; conexão permanente | Login obrigatório, sem reCAPTCHA; instalação e atualização pela loja; conexão permanente para a consulta (há aviso "Sem conexão com a internet") |

### 2.3 Diagrama de contexto

```mermaid
flowchart LR
    cidadao(["Cidadão / condutor<br/>(proprietário do veículo)"])

    subgraph clientes["Canais avaliados (caixa-preta)"]
        portal["Portal de Serviços<br/>SPA Angular no navegador"]
        app["Aplicativo DETRAN-DF<br/>React Native, Android e iOS"]
    end

    subgraph detran["Detran-DF (fora do alcance da avaliação)"]
        idp["Servidor de identidade<br/>acesso.detran.df.gov.br"]
        api["Serviços de backend<br/>api*.detran.df.gov.br"]
        base[("Base de infrações<br/>do Detran-DF")]
    end

    subgraph externos["Serviços externos"]
        govbr["gov.br<br/>(login federado)"]
        renainf[("RENAINF<br/>(SENATRAN)")]
        terceiros["reCAPTCHA, CDN, Firebase<br/>e monitoramento"]
    end

    cidadao -->|consulta| portal
    cidadao -->|consulta| app
    portal -->|autenticação| idp
    app -->|autenticação| idp
    portal -->|HTTPS| api
    app -->|HTTPS| api
    portal --> terceiros
    app --> terceiros
    idp --> govbr
    api --> base
    api --> renainf
```

*Figura — Diagrama de contexto da consulta de infrações. Fonte: elaborado pela equipe a partir do levantamento de 18/10/2026.*

### 2.4 Implicações para a avaliação

Como a avaliação é caixa-preta, só se mede o que chega ao avaliador pelo canal. O diagrama separa o que está ao alcance (os dois clientes e o que trafega entre eles e a rede) do que não está (servidores e bases).

| Dá para medir | Como | Não dá para medir | Por quê |
|---|---|---|---|
| Campos exibidos e sua consistência entre canais | Comparar as telas dos dois canais para o mesmo veículo, no mesmo dia | Correção absoluta dos dados | Não há acesso à base oficial. A referência possível é o outro canal e a notificação recebida pelo proprietário |
| Passos até a lista de infrações | Contar telas e ações em roteiro fixo | Causa de um passo a mais | Exigiria conhecer o projeto interno |
| Tempo percebido até a lista aparecer | Gravação de tela e cronometragem; no portal, também DevTools | Tempo de processamento no servidor e na base | Só se vê o tempo de ponta a ponta |
| Dados transferidos | Portal: aba Rede do DevTools. Aplicativo: contador de dados por aplicativo do Android ou `adb shell dumpsys netstats` | Memória do servidor e capacidade | Exigiria teste de carga, não autorizado |
| Conclusão da consulta em cada contexto (dispositivo, sistema, navegador, rede) | Roteiro repetido em cada contexto, com rede limitada por perfil do DevTools ou do Android | Disponibilidade ao longo do tempo | Exigiria monitoramento contínuo por semanas |

Três consequências práticas para as Fases 2 e 3:

1. **Login obrigatório.** A consulta só lista veículos do CPF logado, então quem faz login é o proprietário que consentiu, no aparelho de teste. A equipe não guarda senhas (ver `dados/consentimento.md`).
2. **reCAPTCHA no login do portal.** O aplicativo não usa reCAPTCHA e permite biometria, então o tempo de login não é comparável entre canais; a medição de tempo deve começar depois da autenticação, a partir da escolha do menu de infrações.
3. **Ferramentas diferentes por canal.** O perfilador do Android Studio não funciona com aplicativos de loja (não depuráveis). Por isso a utilização de recursos fica restrita a dados transferidos, que têm medição equivalente nos dois canais; memória fica fora da comparação.

---

## 3. Modelo de qualidade adaptado

### 3.1 Ponto de partida

O modelo combina duas fontes da família SQuaRE:

- **modelo de qualidade do produto da ISO/IEC 25010:2023**, de onde vêm adequação funcional e eficiência de desempenho;
- **modelo de qualidade em uso da ISO/IEC 25010:2011**, de onde vem a cobertura de contexto, com medidas na ISO/IEC 25022:2016.

A segunda fonte é uma edição anterior por um motivo explícito: a ISO/IEC 25019:2023, que substituiu o modelo de qualidade em uso de 2011, removeu a cobertura de contexto. O prefácio da norma diz: "context coverage which was shown as quality characteristics in the quality-in-use model of the previous version is removed" (ISO/IEC 25019:2023, Foreword). As medidas de completude de contexto continuam na ISO/IEC 25022:2016, ainda vigente, e a própria ISO/IEC 25019:2023 prevê comparar a qualidade entre contextos de uso para encontrar lacunas (Introduction). Por isso a equipe mantém a característica, com a origem declarada.

Partes interessadas usadas nas justificativas (a tabela completa é a do Heitor, na seção de propósito e stakeholders):

- **Cidadão/condutor:** precisa ver todas as infrações, com dados corretos, em qualquer aparelho e rede;
- **Equipe técnica de TI e gestão de serviços digitais do Detran-DF:** precisa saber em que canal e em que condição o serviço fica lento ou pesado;
- **Requisitante (área de governança digital do Detran-DF):** precisa de paridade entre os canais para decidir onde investir.

### 3.2 Seleção das subcaracterísticas

| Característica (origem) | Subcaracterística | Decisão | Justificativa |
|---|---|---|---|
| Adequação funcional (25010:2023) | Completude funcional | Incluída | O cidadão precisa de todas as informações da autuação para pagar, recorrer ou indicar condutor. Medida contra a lista de referência da Seção 1.5, externa aos dois canais |
| | Correção funcional | Incluída, adaptada | Divergência entre canais leva a pagamento errado ou perda de prazo. Sem acesso à base oficial, é medida como consistência entre os canais e com a notificação recebida pelo proprietário |
| | Adequação (apropriação) funcional | Incluída, adaptada | A norma exemplifica com "the necessary and sufficient steps to complete a task, excluding any unnecessary steps" (25010:2023, 3.1.3). Mede-se a contagem objetiva de passos, sem opinião sobre facilidade |
| Eficiência de desempenho (25010:2023) | Comportamento temporal | Incluída | A equipe técnica precisa comparar tempos entre canais; o cidadão em rede móvel sente o atraso |
| | Utilização de recursos | Incluída, restrita | Só dados transferidos, que pesam no plano de dados do cidadão e têm medição equivalente nos dois canais. Memória fica fora porque não há ferramenta equivalente para o portal e para um aplicativo de loja |
| | Capacidade | Excluída | Exige teste de carga sobre a infraestrutura do Detran-DF, não autorizado e fora do alcance caixa-preta |
| Cobertura de contexto (25010:2011, qualidade em uso) | Completude de contexto | Incluída, adaptada | É o que diferencia os canais: computador × celular, Wi-Fi × 4G. A norma de 2011 define com "effectiveness, efficiency, freedom from risk and satisfaction"; a equipe usa só eficácia (consulta concluída) e tempo, porque satisfação é usabilidade, proibida neste trabalho |
| | Flexibilidade | Incluída | Contextos além dos especificados, como rede degradada e versões antigas de sistema. Não confundir com a característica "flexibilidade" do modelo de produto de 2023, que trata de adaptabilidade e instalação |
| Capacidade de interação (25010:2023) | Todas | Excluída | Corresponde à antiga usabilidade, proibida pela professora |
| Compatibilidade (25010:2023) | Coexistência, interoperabilidade | Excluída | A troca de dados com o gov.br e o RENAINF acontece no servidor, fora do que se observa |
| Confiabilidade (25010:2023) | Todas | Excluída | Disponibilidade exige monitoramento contínuo por semanas. Falhas pontuais aparecem como consulta não concluída na cobertura de contexto |
| Segurança (25010:2023) | Todas | Excluída | Testar proteção de dados exigiria autorização formal do Detran-DF; o cuidado com dados pessoais fica no procedimento da equipe (LGPD) |
| Manutenibilidade e flexibilidade (25010:2023) | Todas | Excluídas | Dependem de código-fonte ou de processo de implantação, inacessíveis |
| Segurança operacional (25010:2023) | Todas | Excluída | A consulta não controla equipamentos nem expõe pessoas a dano físico |
| Qualidade em uso (25010:2011) | Eficácia, eficiência, satisfação, ausência de risco | Excluídas como características | Satisfação é opinião de usuário. Eficácia e tempo entram só como parte da completude de contexto |

### 3.3 Adaptações em relação ao modelo de referência

1. **Origem mista.** Duas características vêm do modelo de produto de 2023 e uma do modelo de qualidade em uso de 2011, porque a comparação entre canais depende do contexto em que cada um é usado.
2. **Completude de contexto sem satisfação.** A definição de 2011 inclui satisfação; aqui ela é medida só pela conclusão da consulta e pelo tempo.
3. **Correção como consistência.** Sem a base oficial, a correção é julgada pela concordância entre os canais e com a notificação em papel ou eletrônica que o proprietário recebeu.
4. **Apropriação funcional como contagem de passos.** Segue o exemplo da própria norma e evita qualquer juízo sobre facilidade de uso.
5. **Utilização de recursos só pela rede.** É o único recurso com medição equivalente nos dois canais.

### 3.4 Diagrama do modelo

```mermaid
flowchart TB
    raiz["Qualidade da consulta de infrações<br/>Portal de Serviços × aplicativo"]

    subgraph produto["Modelo de qualidade do produto — ISO/IEC 25010:2023"]
        af["Adequação funcional"]
        af1["Completude funcional"]
        af2["Correção funcional*"]
        af3["Apropriação funcional*"]
        ed["Eficiência de desempenho"]
        ed1["Comportamento temporal"]
        ed2["Utilização de recursos*"]
    end

    subgraph uso["Modelo de qualidade em uso — ISO/IEC 25010:2011 (medidas: ISO/IEC 25022:2016)"]
        cc["Cobertura de contexto"]
        cc1["Completude de contexto*"]
        cc2["Flexibilidade"]
    end

    raiz --> af
    raiz --> ed
    raiz --> cc
    af --> af1
    af --> af2
    af --> af3
    ed --> ed1
    ed --> ed2
    cc --> cc1
    cc --> cc2
```

*Figura — Modelo de qualidade adaptado. Asterisco: subcaracterística adaptada (ver Seção 3.3). Características excluídas estão na tabela da Seção 3.2. Fonte: elaborado pela equipe com base na ISO/IEC 25010:2023 e na ISO/IEC 25010:2011.*

---

*Repositório do projeto:* [GitHub - 2026-2_T02_KATHERINE_JOHNSON](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON)  
*Versão 1.0 — revisada e integrada à `main` pelos [PR #13](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/13), [PR #14](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/14) e [PR #20](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/20).*
