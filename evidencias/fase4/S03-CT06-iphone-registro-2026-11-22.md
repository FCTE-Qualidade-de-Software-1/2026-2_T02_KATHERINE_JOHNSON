# Registro do iPhone (D04) e do contexto CT06 — 22/11/2026

Registro do inventário do iPhone de Heitor (bloqueio B03) e do plano do bloco B04 da sessão S03.
**Nenhuma tentativa do P6 no iPhone foi executada até este registro**, e as três telas com login
no iOS ainda não foram capturadas. Este arquivo não comprova execução, consentimento nem
aprovação de piloto.

## O que está registrado em `dados/brutos/ambientes.csv`

| Campo | Valor | Origem |
|---|---|---|
| Contexto, canal, dispositivo | CT06, aplicativo, D04 | Plano da Fase 3 |
| Modelo | iPhone 16e, 128 GB | Informado por Heitor, dono do aparelho, em 22/11/2026 |
| CPU | Apple A18, CPU de 6 núcleos (2 de desempenho e 4 de eficiência) e GPU de 4 núcleos | Especificação oficial da Apple (ver fontes) |
| RAM | 8 GB | Fontes secundárias; a Apple não publica a RAM (ver fontes) |
| Tela | 1170x2532 pixels (460 ppi) | Especificação oficial da Apple |
| Sistema (`so_build`) | iOS 27.2.1 (build 24B156) | Heitor informou que o aparelho está na versão mais recente; versão e build identificados em fontes públicas em 22/11/2026, **a conferir em Ajustes > Geral > Sobre antes da sessão** (ver abaixo) |
| Aplicativo | DETRAN-DF 2.7.1; pacote `br.com.mesotec.detrandigital` | Versão informada por Heitor; nome do pacote nos metadados da App Store de 26/10/2026 (`evidencias/fase1/`) |
| Navegador | `nao_se_aplica` | Canal é aplicativo |
| Captura | Captura de tela nativa do iOS, sem vídeo; o P6 não mede tempo | Plano do P6 |
| Rede | Wi-Fi, sem limitação; velocidade não medida | Plano do P6 |

## Conferência obrigatória antes da sessão

O `so_build` foi preenchido com a versão estável mais recente do iOS em 22/11/2026, porque Heitor informou
que o iPhone está atualizado. **Antes de executar o P6, abrir Ajustes > Geral > Sobre, conferir a versão e o
build e, se forem outros, corrigir `ambientes.csv`.** Se o aparelho não estiver na versão mais recente, o
valor registrado estará errado e deve ser substituído, sem apagar o histórico do desvio.

## O que ficou em branco, de propósito

- **Número do modelo (A####):** não foi informado e não consta no campo `modelo`.
- **FPS, download, upload e latência:** o P6 não mede tempo nem volume.

## Bloco B04: P6 no iPhone (pendente)

| Item | Situação |
|---|---|
| Contexto e rede | CT06, Wi-Fi |
| Tentativas | 3, até o detalhe de V1-I1 (critério e caminho iguais ao do registro do S03 de 21/11) |
| Aprovação do contexto | Pelo menos 2 das 3 tentativas concluídas |
| Executor | Heitor |
| Titular | Presente; faz o login pessoalmente, com a captura desligada na digitação |
| Conferência independente | Pendente (quem confere não pode ter executado) |
| Linhas em `tentativas.csv` | Ainda não criadas: só entram depois da execução |

Se o titular não estiver disponível ou o aparelho não puder executar, o CT06 fica **não avaliado**,
com desvio em `desvios.csv`, e os resultados do aplicativo valem para o Android. Não substituir por
captura da App Store.

## Telas com login no iOS (pendentes)

`S01-ios-lista-veiculos.png`, `S01-ios-lista-infracoes-V1.png` e `S01-ios-detalhe-V1-I1.png`, em
`evidencias/fase4/capturas/S01/`, tarjadas antes de sair do aparelho, sem notificações e sem metadados.

## Desvio registrado

**D008:** a M2.2.1 do iOS fica **não medida**, porque o iOS não oferece contador de bytes por
aplicativo equivalente ao `adb dumpsys netstats` usado no Android (`dados/brutos/desvios.csv`).

## Fontes consultadas em 22/11/2026

- Versão e build do iOS, em fontes secundárias (a página oficial da Apple para a 27.2.1 não foi recuperada):
  [iOS 27.2.1 build map](https://iphonewired.com/firmware-update/1200337/) (build 24B156 para iPhones),
  [MacRumors, 9/11/2026](https://macrumors.com/2026/11/09/apple-releases-ios-27-2-1-with-bug-fixes) e
  [Apple Developer, iOS 27.2](https://developer.apple.com/news/releases/?id=10262026b) (build 24B119, que a 27.2.1
  substitui). A versão 27.3 ainda está em beta. O iPhone 16e é compatível com o iOS 27.

- Apple, [Especificações técnicas do iPhone 16e](https://www.apple.com/iphone-16e/specs) e
  [página de suporte do modelo](https://support.apple.com/122208): chip A18 com CPU de 6 núcleos e
  GPU de 4 núcleos; tela OLED de 6,1 polegadas com 2532 por 1170 pixels e 460 ppi.
- RAM de 8 GB, em fontes secundárias: [ficha técnica da Columbia University (dados do GSMArena)](https://www.cuit.columbia.edu/sites/default/files/content/CUIT%20Website%20Pages/Phone%20Specs/16e.pdf)
  e [guia de dispositivos da Vodafone](https://deviceguides.vodafone.co.uk/apple/iphone-16e-ios-27/specifications);
  reportagens de desmontagem também citam 8 GB. Conferir no aparelho se possível; a Apple não
  publica esse valor.
