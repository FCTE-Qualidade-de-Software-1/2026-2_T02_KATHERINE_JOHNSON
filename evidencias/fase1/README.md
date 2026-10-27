# Evidências da Fase 1

Capturas de tela do levantamento dos canais (Portal de Serviços e aplicativo do Detran-DF). Descrição completa em `docs/fase1-produto.md`.

## Nome dos arquivos

`<canal>-<tela>-<AAAA-MM-DD>.png`, em que `<canal>` é `portal`, `app-android` ou `app-ios`. Capturas das páginas das lojas usam `<tela>` = `google-play` ou `app-store`. Exemplo: `app-android-detalhes-infracao-2026-10-20.png`.

## Regras de anonimização (LGPD)

Nenhum print entra no repositório sem passar por estas regras:

1. Cobrir com tarja opaca (retângulo preenchido, não desfoque) placa, RENAVAM, chassi, CPF, CNH, nome, endereço e número do auto de infração.
2. Usar os códigos da massa de dados no nome do arquivo e na legenda (ex.: "Veículo V1"), nunca a placa.
3. Remover metadados da imagem antes do commit (ex.: `exiftool -all= arquivo.png`).
4. Conferir o print ampliado antes do commit; outra pessoa da equipe confere no pull request.
5. Guardar o original sem tarja apenas fora do repositório, com o responsável pela massa de dados.

## Outras evidências

| Arquivo | Conteúdo |
|---|---|
| [`levantamento-publico-2026-10-26.md`](levantamento-publico-2026-10-26.md) | Metadados públicos do aplicativo nas lojas; no portal, recursos carregados pelo navegador, arquivo principal do código cliente e rótulos de "Detalhes da infração" encontrados nele |
| [`app-ios-app-store-metadados-2026-10-26.json`](app-ios-app-store-metadados-2026-10-26.json) | Resposta da consulta pública da App Store sobre o aplicativo |
| [`app-android-pacote-2026-10-26.md`](app-android-pacote-2026-10-26.md) | Pacote do aplicativo Android 2.6.9 instalado pela Google Play: versão, bibliotecas, bytecode Hermes e rótulos encontrados |
| [`roteiro-levantamento.md`](roteiro-levantamento.md) | Roteiro da sessão com veículo real |

## Prints pendentes

| Tela | Portal | Android | iOS |
|---|---|---|---|
| Página da loja | — | feito | feito |
| Tela inicial (sem login) | feito | feito | não realizado (sem iPhone) |
| Login (campos vazios) | feito | feito | não realizado (sem iPhone) |
| Lista de veículos | pendente | pendente | pendente |
| Lista de infrações | pendente | pendente | pendente |
| Detalhes de uma infração | pendente | pendente | pendente |

As telas pendentes exigem login do proprietário com veículo real. O procedimento está em `roteiro-levantamento.md`.

**Limitação: aplicativo no iOS.** Nenhum integrante da equipe possui iPhone, por isso as telas do aplicativo no iOS
não foram capturadas; do iOS há apenas a página da App Store. Para a Fase 3, a equipe tentará um aparelho emprestado;
sem ele, a avaliação do aplicativo se restringe ao Android, e o iOS fica registrado como contexto não avaliado.
