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
| Tela inicial (sem login) | feito | feito | pendente (iPhone de Heitor) |
| Login (campos vazios) | feito | feito | pendente (iPhone de Heitor) |
| Lista de veículos | [captura disponível](../../docs/img/passoApassoConsulta/pageConsultaDeInfrções.png) | pendente | pendente |
| Lista de infrações | [captura disponível](../../docs/img/passoApassoConsulta/pageConsultaDeInfraçõesDefinindoData.png) | pendente | pendente |
| Detalhes de uma infração | [captura disponível](../../docs/img/passoApassoConsulta/pageDetalhesDaInfração.png) | pendente | pendente |

As telas pendentes exigem login do proprietário com veículo real. O procedimento está em `roteiro-levantamento.md`.

**Conferência documental em 20/11/2026:** as capturas do portal já estavam em
`docs/img/passoApassoConsulta/`, incorporadas pelo commit `aa9d3bb` em 15/11. Sua inclusão
reconhece os arquivos disponíveis, mas não certifica consentimento, executor, revisão independente
ou liberação do piloto. **Atualização em 22/11/2026:** Hugo confirmou a aplicação dos termos;
as vias assinadas permanecem privadas. O [acompanhamento de S00/S01](../../docs/fase4-coleta.md) descreve os
limites e registros ainda necessários.

**Aplicativo no iOS.** As telas do aplicativo no iOS não foram capturadas na Entrega 1; do iOS há
apenas a página da App Store. O iPhone é de Heitor e será usado para as capturas e medições na
Fase 3. Sem o inventário e as evidências da sessão, CT06 permanece não avaliado; as conclusões do
aplicativo ficam restritas aos contextos Android efetivamente avaliados.
