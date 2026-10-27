# Pacote do aplicativo Android — versão 2.6.9

**Data da coleta:** 26/10/2026  
**Origem:** aplicativo instalado pela Google Play (instalador `com.android.vending`) em um aparelho Android da equipe, copiado com `adb pull`. Os arquivos foram apenas lidos; nada foi instalado, modificado ou executado.  
**Usado em:** `docs/fase1-produto.md` (Seções 1.1, 1.4 e 2) e Seção 3.2.3 do artigo.

## 1. Identificação

| Campo | Valor |
|---|---|
| Pacote | `br.com.mesotec.detrandf` |
| Versão | 2.6.9 (código de versão 244) |
| Android mínimo | API 26 (Android 8.0) |
| Android alvo | API 36 |

| Arquivo | Tamanho (bytes) | SHA-256 |
|---|---|---|
| `base.apk` | 41.391.781 | `8998141933d07c9209d75931f72417131feb467d80c6fc35f21bd4418b573282` |
| `split_config.arm64_v8a.apk` | 24.496.571 | `b94e73b99e2e6fdce7e9cca2906369f427fba3763d47e050f1249d8145bffb1a` |
| `split_config.pt.apk` | 41.369 | `8de5fd9f24c391541458f9f6f68ab6df727e45deeadb5694747d02a406b04dd2` |
| `split_config.xxhdpi.apk` | 79.985 | `ee2f9ae3df3027ee861f53dbb6f6681edbc5d997ee389423fe7065027167ba0d` |

Os pacotes não foram adicionados ao repositório, por serem software de terceiros; os hashes permitem conferir que outra cópia da mesma versão é idêntica.

## 2. Tecnologia

- **React Native:** bibliotecas nativas `libreactnative.so` e `libfbjni.so` em `lib/arm64-v8a/` (`split_config.arm64_v8a.apk`), além de módulos como `libreact_codegen_rnscreens.so` e `libreact_codegen_rnsvg.so`.
- **Motor JavaScript Hermes:** biblioteca `libhermes.so`, e o código JavaScript do aplicativo (`assets/index.android.bundle`, 10.410.272 bytes, SHA-256 `8b0e93c3e7f60f03ac576c7270613065e5b64b5d5021a50447e97b4b8b49210e`) está compilado em bytecode Hermes: o arquivo começa com a assinatura `c6 1f bc 03 c1 03 19 1f`, versão 96 do bytecode.

## 3. Rótulos de infração no código do aplicativo

Ocorrências, em `assets/index.android.bundle`, dos rótulos atribuídos ao aplicativo na Seção 1.4 de `docs/fase1-produto.md`. O Hermes guarda textos sem acento em 1 byte por caractere e textos acentuados em UTF-16LE; as duas codificações foram consideradas.

| Rótulo | Ocorrências |
|---|---|
| Placa | 21 |
| Marca/Modelo | 2 |
| Infração | 13 |
| Descrição da infração | 1 |
| Regulamento | 1 |
| Natureza | 1 |
| Auto Infração | 1 |
| Código RENAINF | 1 |
| Órgão Autuador | 1 |
| Responsável pela infração | 1 |
| Data Infração | 1 |
| Hora Infração | 1 |
| Local da Infração | 1 |
| Velocidade Permitida | 1 |
| Velocidade Aferida | 1 |
| Data da Notif. de Autuação | 1 |
| Data da Notif. de Penalidade | 1 |
| Data limite para defesa prévia | 2 |
| Identificação condutor infrator | 1 |
| Data de Vencimento | 1 |
| Data opção desconto 40% - SNE | 1 |
| Valor da Multa | 1 |
| Valor Correção | 1 |
| Valor Desconto | 1 |
| Valor Devido | 1 |
| Pontuação da Infração | 1 |
| Situação do pagamento | 1 |
| Situação Multa | 1 |
| Origem: RENAINF | 1 |

O texto "Detalhes da infração" não aparece no aplicativo, e "UF" aparece 309 vezes em contextos variados; pela tabela de textos não é possível dizer se a UF é exibida na tela de detalhes da infração, o que continua a confirmar com veículo real.

## 4. Como reproduzir

Com o aplicativo instalado pela Google Play e a depuração USB ativada:

```bash
adb shell dumpsys package br.com.mesotec.detrandf | grep -E 'versionName|versionCode|minSdk'
for f in $(adb shell pm path br.com.mesotec.detrandf | sed 's/package://' | tr -d '\r'); do adb pull "$f" .; done
sha256sum *.apk
unzip -l split_config.arm64_v8a.apk | grep -E 'libhermes|libreactnative'
unzip -p base.apk assets/index.android.bundle | head -c 8 | od -A n -t x1
```
