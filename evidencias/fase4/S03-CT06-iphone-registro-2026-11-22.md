# Registro do iPhone (D04) e do bloco B04 (CT06) — 22/11/2026

Registro do inventário do iPhone (bloqueio B03) e da execução do P6 no contexto CT06, bloco B04 da
sessão S03. A execução foi manual, em 22/11/2026, das 12:06:20 às 12:10:45 (Brasília). **A
conferência independente está pendente**, e este registro não comprova consentimento nem
aprovação de piloto.

## Identificação da sessão

| Item | Registro |
|---|---|
| Sessão, bloco, data, início e fim (Brasília) | S03, B04, 22/11/2026, das 12:06:20 às 12:10:45 |
| Executor / registrador / conferente independente | Heitor (executor); sem registrador (D028); conferente indicado: Philipe (pendente) |
| Veículo e infração (somente códigos) | V5 (código novo, titular Heitor; Hugo confirma o vínculo na tabela privada) e V5-I1 (D029) |
| Titular | O executor é também o titular e fez o login pessoalmente; os dados do titular ficam só no registro privado (D028) |
| Contexto e rede | CT06 (iPhone D04, aplicativo 2.7.1), Wi-Fi sem limitação; linha `S03,CT06,...,wifi` em `ambientes.csv` |
| Versão e build do iOS | Heitor informou ter conferido em Ajustes > Geral > Sobre antes da sessão e não pediu correção do valor registrado |
| Versão do plano (commit) | Branch do S03 após o PR #69 |

## Inventário registrado em `dados/brutos/ambientes.csv`

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

## Caminho executado em cada tentativa

Tela inicial autenticada, Infrações, Histórico de infrações por veículo, escolha do veículo V5,
período ajustado para incluir a infração, dentro do limite de 5 anos do aplicativo, com "Todas" as situações, Consultar, escolha da infração V5-I1 e
detalhe (folha "Confira o detalhamento da infração"). Critério de conclusão: o detalhe exibe o rótulo
"Descrição da Infração", como nas demais tentativas do P6.

## Tentativas

| Repetição | Início (Brasília) | Duração | Resultado | Observação |
|---:|---|---|---|---|
| 1 | 12:06:20 | 2 min 15 s | concluida | Detalhe com "Descrição da Infração", conforme Heitor |
| 2 | 12:08:35 | 1 min 20 s | concluida | Idem |
| 3 | 12:09:55 | 50 s | concluida | Idem |

As durações foram informadas por Heitor; as três somam 4 min 25 s, igual à janela da sessão. Os
inícios das tentativas 2 e 3 foram **calculados** pela soma das durações a partir de 12:06:20, sem
intervalo entre elas. A duração inclui a operação manual e não é medida de tempo da Fase 2. O CT06 fica
com **3 de 3** tentativas concluídas, pendente de conferência.

Observações: a tela do aplicativo iOS informa que o período máximo de busca é de 5 anos (D030).
Na lista de veículos, a seção "Veículos de minha propriedade à época da infração" mostrou "Até o
presente momento, não há registros", e a seção de veículos atuais listava dois veículos da conta.

## Evidências

Capturas feitas durante a primeira passagem pelo caminho (12:06 a 12:09, conforme os metadados dos
originais). Antes de entrar no repositório, foram cobertos com tarja opaca: a barra de status, o nome do
usuário, os modelos e as placas dos veículos, o nome e o número do auto, a data da infração,
o valor da placa e do modelo no detalhe e as datas do filtro de período. As cópias não têm metadados. Os originais, sem tarja, ficam
em `dados/privado/`, ignorado pelo Git.

| Arquivo | Conteúdo |
|---|---|
| `capturas/S01/S01-ios-lista-veiculos.png` | Histórico de infrações por veículo: lista de veículos |
| `capturas/S01/S01-ios-lista-infracoes-V5.png` | Resultado da pesquisa: lista de infrações |
| `capturas/S01/S01-ios-detalhe-V5-I1.png` | Detalhe da infração |
| `capturas/S03/S03-B04-aplicativo-P6-V5-resultado-2026-11-22.png` | Resultado do contexto CT06 (mesma tela do detalhe) |
| `capturas/S03/S03-B04-aplicativo-P6-V5-periodo-2026-11-22.png` | Formulário de período (D030) |

**Limite da evidência:** as capturas não são uma por tentativa e não mostram o rótulo "Descrição da
Infração": o detalhe aparece só na parte superior. A conclusão das 3 tentativas e a presença desse
rótulo foram informadas por Heitor. A regra do P6 pede uma captura do resultado por contexto e os três
resultados em `tentativas.csv`, o que foi feito.

## Desvios registrados

- **D008:** M2.2.1 não medida no iOS (sem contador de bytes por aplicativo).
- **D028:** executor e titular são a mesma pessoa, sem registrador.
- **D029:** CT06 usou o V5 (código novo), e não o V1 do S03; infrações diferentes.
- **D030:** o app iOS tem filtro de período, e o do Android não tinha.

## Conferência independente

| Chave do registro | Primeira leitura | Segunda leitura | Decisão final | Conferente |
|---|---|---|---|---|
| `tentativas.csv`, S03, B04, repetições 1 a 3 | concluida, concluida, concluida | | | Philipe (pendente) |

Quem confere não pode ter executado a sessão. Só depois da conferência entra o `revisor` no CSV.

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
