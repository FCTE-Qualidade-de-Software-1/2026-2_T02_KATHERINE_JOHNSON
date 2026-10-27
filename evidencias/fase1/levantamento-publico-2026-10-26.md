# Levantamento público dos canais — lojas e código cliente do portal

**Data da coleta:** 26/10/2026  
**Escopo:** apenas informações públicas, acessíveis sem login e sem acesso à infraestrutura do Detran-DF.  
**Usado em:** `docs/fase1-produto.md` (Seções 1.1, 1.2, 1.4 e 2) e Seção 3.2.3 do artigo.

## 1. Aplicativo nas lojas

### 1.1 App Store (iOS)

Metadados retornados pela consulta pública da Apple (`https://itunes.apple.com/lookup?id=1526746296&country=br`),
guardados em [`app-ios-app-store-metadados-2026-10-26.json`](app-ios-app-store-metadados-2026-10-26.json).

| Campo | Valor |
|---|---|
| Nome | DETRAN-DF |
| Vendedor | DEPARTAMENTO DE TRANSITO DO DISTRITO FEDERAL |
| Identificador | `id1526746296` (bundle `br.com.mesotec.detrandigital`) |
| Versão | 2.6.9, publicada em 13/10/2026 |
| Versão mínima do iOS | 15.1 |
| Tamanho | 43.521.024 bytes (43,5 MB) |

### 1.2 Google Play (Android)

Página pública `https://play.google.com/store/apps/details?id=br.com.mesotec.detrandf`, seção "Sobre este app".
Avaliações de usuários não foram registradas.

| Campo | Valor |
|---|---|
| Nome | DETRAN-DF, oferecido por DETRAN DF |
| Pacote | `br.com.mesotec.detrandf` |
| Versão | 2.6.9 |
| Atualizado em | 9 de outubro de 2026 |
| Requer Android | 8.0 ou superior |
| Downloads | 1.000.000+ |
| Lançado em | 14 de agosto de 2020 |
| Nota média | 2,3 (cerca de 16,5 mil avaliações) |
| Descrição | "Nessa versão o cidadão poderá consultar informações sobre o Veículo, Infrações, Habilitação, quitar débitos e utilizar mais de vinte serviços sem sair de casa!" |

## 2. Portal de Serviços

### 2.1 Recursos carregados pelo navegador

Página inicial (`https://portal.detran.df.gov.br/#/home`) e tela de login (`#/login`), abertas no Google Chrome; lista
obtida das entradas de recursos do navegador (`performance.getEntriesByType('resource')`).

| Domínio ou arquivo | Função |
|---|---|
| `portal.detran.df.gov.br` | Aplicação do portal (`runtime`, `polyfills` e `main` em versões es2017 e es5) |
| `ruxitagentjs_*.js`, servido pelo próprio portal | Agente de monitoramento de usuário real da Dynatrace |
| `code.jquery.com` | jQuery 3.7.1 |
| `fonts.gstatic.com` | Google Fonts |
| `www.google.com`, `www.gstatic.com` | Google reCAPTCHA, carregado na tela de login (iframe presente) |
| `www.google-analytics.com`, `www.googletagmanager.com` | Google Analytics |
| `cdn.socket.io`, `in.bot`, `cf.in.bot`, `files.in.bot`, `bot-server.s3.amazonaws.com` | Assistente virtual (chatbot) da página |

Na tela de login há o botão "Entrar com gov.br".

### 2.2 Código cliente público

| Item | Valor |
|---|---|
| Arquivo principal | `main-es2017.922e684e19a946a612c1.js` |
| Tamanho | 11.092.670 bytes |
| SHA-256 | `0939ca1e7c87131b0fa15ba7c6c873d5307b09368dd3a4fc3fb70509cff9c1d3` |

O nome do arquivo muda a cada nova versão do portal.

Ocorrências dos rótulos da tela "Detalhes da infração" no arquivo principal, depois de decodificar os caracteres
acentuados (o código guarda, por exemplo, "Auto Infração" como `Auto Infra\xe7\xe3o`):

| Rótulo | Ocorrências |
|---|---|
| Detalhes da infração | 2 |
| Placa | 341 |
| UF | 457 |
| Marca/Modelo | 24 |
| Descrição da Infração | 5 |
| Regulamento | 4 |
| Natureza | 5 |
| Auto Infração | 9 |
| Código Renainf | 4 |
| Origem: RENAINF | 4 |
| Órgão Autuador | 7 |
| Responsável pela Infração | 2 |
| Data Infração | 3 |
| Hora Infração | 3 |
| Local da Infração | 3 |
| Velocidade Permitida | 4 |
| Velocidade Aferida | 4 |
| Data da Notif. de Autuação | 4 |
| Data da Notif. de Penalidade | 1 |
| Data da Defesa Prévia | 1 |
| Identificação do Condutor Infrator | 2 |
| Data de Vencimento | 4 |
| Valor da Multa | 3 |
| Valor Correção | 1 |
| Valor Desconto | 1 |
| Valor Devido | 1 |
| Pontuação Infração/Status | 1 |
| Situação Pagamento | 2 |
| Situação Multa | 3 |
| Histórico de infrações | 2 |

"Placa" e "UF" aparecem também em outras telas do portal, por isso têm muitas ocorrências.

### 2.3 Como reproduzir

```bash
curl -s -o main.js https://portal.detran.df.gov.br/main-es2017.922e684e19a946a612c1.js
sha256sum main.js
grep -o 'Auto Infra\\xe7\\xe3o' main.js | head -1
```

Se o portal tiver sido atualizado, o nome do arquivo principal estará no código-fonte da página inicial
(`<script src="main-es2017.<hash>.js">`).
