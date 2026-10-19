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

## Prints pendentes

| Tela | Portal | Android | iOS |
|---|---|---|---|
| Página da loja | — | feito | feito |
| Login | feito | pendente | pendente |
| Lista de veículos | pendente | pendente | pendente |
| Lista de infrações | pendente | pendente | pendente |
| Detalhes de uma infração | pendente | pendente | pendente |

As telas pendentes exigem login do proprietário com veículo real. O procedimento está em `roteiro-levantamento.md`.
