# Preparação da continuação de P4/P5 — 22/11/2026

Preparação técnica, sem medições oficiais. A branch `feat/hugo-coleta-e2` preserva o registro
de consentimentos e recebe os instrumentos da branch `feat/pedro-s03-fase4`, commit `c305ad9`.

## Ambiente observado

- Android conectado: Samsung SM-S731B, Android 17, aplicativo `br.com.mesotec.detrandf` 2.7.0.
- Resolução física: 1080 × 2340. A depuração USB foi autorizada no próprio aparelho.
- Aplicativo em primeiro plano; grupo Infrações aberto e opção de histórico por veículo disponível.
- O aparelho difere do Motorola edge 60 neo da S02 anterior. Uma execução futura exige inventário
  por bloco e registro dessa mudança; os resultados não devem substituir os do aparelho anterior.
- Portal no Chrome: tela de login na verificação de preparação; nenhuma autenticação executada
  pelo agente, nem credencial lida ou gravada.

## Condições antes da medição

- Confirmar o caso de referência, sem publicar identidade ou placa; conciliar seu código no privado.
- Confirmar o início da M2.1.1: o plano usa a seleção do veículo e a proposta da S02 usa Consultar.
  Aplicar a mesma definição aos dois canais e documentar a decisão antes do primeiro bloco.
- Fazer ensaio dos modos de tempo e volume, depois os aquecimentos e as repetições válidas.
- P7 depende da montagem e validação das três condições de rede nos dois canais.

## Proteção dos dados

Nenhum print público foi produzido nesta preparação. A árvore de interface foi guardada somente
em `dados/privado/`, ignorado pelo Git, com acesso restrito. Identificadores USB, nomes, CPF,
placas, dados de infrações, credenciais e gravações originais não integram este registro.
Os erros públicos do instrumento Android expõem somente a classe da exceção; mensagens completas
ficam no privado. As gravações recusam sobrescrita de uma repetição já existente.

## Verificações técnicas

Sintaxe Python e JavaScript verificadas. Navegação de preparação validada no grupo Infrações,
com gesto adaptado à tela do Samsung. Isso não comprova o ensaio dos modos de medição, marcação
visual de tempos, equivalência de contadores ou conferência independente.

## Continuação autorizada após autenticação

- O responsável confirmou que se trata de outro titular e veículo e que o consentimento já
  aplicado cobre esse participante. Código reservado para este caso: V4; a seleção é mantida
  na correspondência privada, sem publicar placa ou identificação.
- Início em Consultar confirmado antes da primeira medição; P4/M2.1.1 e P7/M3.2.3 usam esse
  marco nos dois canais. A seleção e os filtros ficam fora do intervalo cronometrado.
- Chrome de medição aberto em perfil separado, privado, por autorização explícita do responsável;
  o titular autenticou pessoalmente. A conexão integrada havia falhado na leitura de tela.
- A consulta de ensaio no aplicativo retornou infrações; o portal carregou a lista de veículos.
  Esses passos são preparação e não entram nos denominadores das medições.
