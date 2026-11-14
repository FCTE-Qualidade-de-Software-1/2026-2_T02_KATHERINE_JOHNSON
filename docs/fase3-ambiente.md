# Fase 3 — Recursos, ambiente e preparação

Versão 0.2 — 13/11/2026. Responsáveis: Hugo e Philipe. Plano proposto para revisão de Pedro Henrique.

Este plano complementa os [procedimentos P1–P7](fase3-metodo.md). **Os equipamentos, versões atuais e consentimentos ainda não foram confirmados.** As linhas abaixo são requisitos de preparação, não registros de testes executados. As versões levantadas na Fase 1 não substituem a leitura da versão instalada no dia da coleta.

## 1. Inventário e contextos

| ID | Canal e ambiente planejado | Rede / procedimento | Confirmação antes do piloto |
|---|---|---|---|
| CT01 | Portal; computador D01; Chrome | Wi-Fi: P1–P6; Wi-Fi, 4G e degradada: P7 | Modelo, processador, RAM, SO/build e versão do Chrome |
| CT02 | Portal; mesmo D01; Firefox | Wi-Fi: P6 | Versão do Firefox |
| CT03 | Portal; Android intermediário D03; Chrome | Wi-Fi: P6 | Modelo, RAM, Android/build e versão do Chrome |
| CT04 | Aplicativo; Android de entrada D02 | Wi-Fi: P6 | Modelo, RAM, Android/build, pacote e versão instalada |
| CT05 | Aplicativo; Android intermediário D03 | Wi-Fi: P1–P6; Wi-Fi, 4G e degradada: P7 | Mesmos dados de D02; usar o mesmo D03 de CT03 |
| CT06 | Aplicativo; iPhone D04, se emprestado | Wi-Fi: P6 | Modelo, iOS/build e versão instalada; indisponível até confirmação |

*Tabela 1 — Contextos planejados. Fonte: elaborada para o plano de avaliação.*

D02 e D03 devem ser aparelhos distintos; a equipe justifica a classificação entrada/intermediário pelas especificações registradas, sem presumir modelos disponíveis. Respeitar os mínimos levantados na Fase 1 (Android 8.0 e iOS 15.1), verificando a compatibilidade da versão instalada. Sem D04, CT06 é **não avaliado**, não falha, e os resultados do aplicativo ficam restritos ao Android. Sem outro recurso obrigatório, registrar bloqueio; não substituir silenciosamente o contexto.

Registrar o inventário efetivo em `dados/brutos/ambientes.csv`: uma linha por contexto e sessão, incluindo resolução, taxa efetiva da gravação, versões das ferramentas e perfil de rede. Mudança de versão ou aparelho exige nova linha e registro em `desvios.csv`. Não atualizar o aplicativo durante um bloco.

No portal, registrar URL de entrada e data/hora; se a interface não informar versão, anotar
`não informada pelo serviço`, sem atribuir uma versão presumida. No aplicativo, conferir
versão instalada e build nas informações do aparelho, além do identificador do pacote.
Guardar esses detalhes no registro de sessão quando não houver coluna específica no CSV.
O notebook que compartilha a rede é um recurso adicional a D01; confirmar sua placa/adaptador
Wi-Fi, modo de compartilhamento, distribuição Linux, kernel e versão do `tc` no mesmo registro.

Os avaliadores são integrantes da equipe que ensaiaram P1–P7 no piloto; não representam uma
amostra de usuários finais. O executor precisa conhecer o fluxo e o registrador, as regras de
contagem e os instrumentos. O conferente não participa da execução que revisa. Registrar os
papéis por sessão; o titular autentica, mas não recebe tarefa de julgamento ou questionário.

## 2. Recursos e responsabilidades

| Recurso | Finalidade | Responsável por disponibilizar/verificar |
|---|---|---|
| D01, D02, D03 e empréstimo D04 | Contextos da Tabela 1 | Hugo |
| Notebook Linux, adaptador Wi-Fi com modo ponto de acesso e acesso à internet | Condição comum aos dois canais | Philipe |
| Celular com chip e roteamento USB | Saída 4G do ponto de acesso | Philipe |
| Cabo USB, ADB, DevTools e gravador de tela | P1–P7 | Philipe |
| Veículo, titular presente e termo assinado | Mesma massa nos dois canais | Hugo |
| Armazenamento privado e editor para tarjas | Originais e anonimização | Hugo |
| Modelos CSV e revisão independente | Rastreabilidade e conferência | Philipe; revisor conforme cronograma |

*Tabela 2 — Recursos necessários, ainda sujeitos à confirmação. Fonte: elaborada para o plano.*

## 3. Preparação reproduzível da rede

1. Identificar as interfaces de entrada e saída do notebook e verificar que os dois dispositivos de referência navegam pelo mesmo ponto de acesso. Não usar o computador que compartilha a rede como cliente do portal sem demonstrar que o tráfego dele passa pela mesma limitação.
2. Registrar interface, meio de acesso, ferramenta/versão, horário e medidas de download, upload e latência antes de cada bloco. Medir fora do intervalo da consulta.
3. Para Wi-Fi, usar a conexão fixa sem limitação. Para 4G, usar o roteamento USB como saída e confirmar que não há saída simultânea pela conexão fixa.
4. Para rede degradada, aplicar o perfil do método nos dois sentidos: atraso de 300 ms com variação de 50 ms, banda de 1 Mbit/s e perda de 1% **por sentido**. Esse é um cenário experimental fixo, não uma medição de uma rede real. Não interpretar 300 ms como latência de ida e volta.
5. Philipe deve registrar os comandos efetivamente usados, interfaces e saída de inspeção das filas do `tc` em `dados/privado/`, e publicar uma cópia sem identificadores de rede em `evidencias/fase4/`. O comando depende da topologia; a configuração ainda precisa ser validada no piloto. Não basta limitar apenas o navegador ou apenas o tráfego de saída.
6. Verificar tráfego e limitação em ambos os clientes; guardar evidência da verificação. Restaurar o perfil sem limitação após o bloco e confirmar a restauração. Se não for possível validar os dois sentidos, marcar o cenário como não avaliado e registrar o bloqueio.

## 4. Piloto e liberação da coleta

Executar antes das sessões oficiais, sem misturar seus dados com resultados:

- Confirmar consentimento, vínculo do veículo ao titular e pelo menos uma infração acessível nos dois canais.
- Executar o [roteiro de levantamento autenticado](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase1/roteiro-levantamento.md); confirmar rótulos e caminho real, capturando as três telas pendentes por canal disponível.
- Preencher inventário e versões; testar gravação com indicação de toque/clique e conferir taxa de quadros. Preferir taxa constante; se variável, usar os timestamps dos quadros e registrar essa adaptação.
- Validar o contador por UID do Android: a leitura deve mudar após transferência conhecida e estabilizar sem consulta. Contadores atrasados, indisponíveis ou agregados de modo ambíguo impedem medir P5; zero sem validação não significa ausência de tráfego.
- Confirmar o que cada instrumento de P5 inclui. DevTools e contadores do sistema podem medir camadas diferentes; sem equivalência demonstrada, reportar valores separados, com limitação, sem declarar um canal superior em M2.2.1. Uma troca de instrumento exige revisar a ficha da Fase 2 antes da coleta.
- Testar os perfis de rede e o preenchimento dos CSV; revisar uma captura anonimizada e uma medida de tempo com avaliador independente.

Hugo e Philipe preenchem data, resultado, evidências e liberação por procedimento no
[modelo de sessão](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/modelo-sessao.md);
somente bloqueios e mudanças vão para `desvios.csv`. Pedro Henrique revisa o plano.
Consentimento ou veículo ausentes bloqueiam a coleta. Falha de um instrumento bloqueia sua
métrica, sem transformar ausência de medida em zero. O [cronograma](fase3-cronograma.md)
identifica responsáveis e prazos de resolução.
