# Instrumentos da Fase 4

Os CSV em `brutos/` são modelos vazios (UTF-8, vírgula, ponto decimal). Não são evidência de execução. Preencher após consentimento e piloto. Aspas delimitam textos com vírgulas. Não publicar identificadores, credenciais, valores pessoais ou HAR original.

## Dicionário e convenções

- `sessao`: S01–S05; `contexto`: CT01–CT06; `canal`: portal ou aplicativo; `rede`: wifi, 4g ou degradada; `veiculo`/`infracao`: códigos V1/V1-I1; `procedimento`: P1–P7; `metrica`: identificador da Fase 2.
- `data_hora`, `portal_data_hora`, `aplicativo_data_hora`: ISO 8601 com fuso (ex.: AAAA-MM-DDTHH:MM:SS-03:00). `repeticao`: inteiro a partir de 1 por bloco. `bloco`: código único por sessão, procedimento, canal e rede. `aquecimento`: sim/nao; aquecimentos não entram no cálculo.
- `evidencia`: caminho relativo à raiz para arquivo anonimizado em `evidencias/fase4/`; `revisor`: integrante que conferiu, sem inventar aprovação. Usar nomes `<sessao>-<bloco>-<canal>-<metrica>-<veiculo>-<repeticao>-<AAAA-MM-DD>` para evitar sobrescrever capturas.
- `campo`: R01–R15; campos condicionais separados `velocidade_permitida` e `velocidade_aferida`. `tela`: lista/detalhe. `aplicavel`, `presente`, `elegivel`: sim/nao. Campo vazio significa informação pendente, não zero nem ausência observada.
- `classificacao`: paritario, divergente, ausente_portal, ausente_aplicativo ou ausente_ambos. Ausências não contam como paridade. Em P2 o conjunto aplicável deve ser fixado no piloto segundo a ficha da Fase 2, registrando a escolha do denominador e qualquer revisão antes da coleta.
- `passos`, `transicoes`, `rolagens`: contagens inteiras; `sequencia`: rótulos das ações, sem dados digitados do titular.
- `quadro_inicial`, `quadro_final`: índices; `fps`: taxa efetiva; `inicio_s`, `fim_s`: timestamps relativos ao vídeo; `tempo_s`: diferença de timestamps ou quadros/fps quando taxa constante. Nunca misturar os dois métodos sem registrar desvio.
- `bytes_iniciais`, `bytes_finais`: contadores Android agregados de envio/recebimento no mesmo UID, sem dupla contagem; `bytes_transferidos`: diferença válida, ou valor da ferramenta do portal; `mb`: bytes/1.000.000. `instrumento` identifica ferramenta/versão e escopo da contagem. Valores não equivalentes são reportados separadamente, sem ranking.
- `resultado`: concluida, falha, sessao_expirada, tempo_limite ou erro_instrumento. `nao_avaliado` só indica contexto não executado e não integra denominador de tentativas realizadas. `motivo`: justificativa sem dados pessoais.
- `desvio`: identificador D001 etc.; `decisao`: manter, excluir_erro_instrumento, repetir ou pendente; `responsavel`, `prazo` e `evidencia` documentam resolução. Não excluir falha do serviço para melhorar o resultado.
- Inventário: `dispositivo` é D01–D04; modelo, CPU, RAM em GB, SO/build, navegador/versão, aplicativo/versão, resolução, gravador/versão, FPS e configuração/medidas de rede são observações do equipamento usado; sem dado real, deixar pendente. Não guardar SSID, MAC ou IP público.

## Cálculo e integridade

1. P1: uma linha por campo/tela/infração/canal; denominador 15 na lista e 15 mais dois campos apenas em infrações de velocidade no detalhamento. Nenhuma infração disponível implica resultado não calculável, não 0%.
2. P2: uma linha por campo/infração com horários dos dois canais; registrar apenas classificação pública. Infrações sem divergência exigem todos os campos aplicáveis paritários; agregado conforme a Fase 2. A ficha M1.2.1 contém tensão entre “campos comuns comparáveis” e “total aplicável”: congelar o conjunto no piloto, documentando ausências, sem alterar o denominador após observar os resultados.
3. P3: três execuções por canal; contagem recorrente, ou desvio quando as três diferirem.
4. P4/P5: dez medidas válidas mais um aquecimento por bloco; registrar todas as tentativas inválidas. Limitar a vinte tentativas medidas por bloco; se não alcançar dez válidas, reportar n real e bloqueio, sem completar artificialmente a amostra.
5. P6: contexto aprovado com pelo menos duas de três tentativas concluídas. Para M3.1.1 no portal, agrupar CT01/CT02 como computador (sucesso exige aprovação dos dois) e CT03 como celular; no aplicativo usar CT04/CT05/CT06 disponíveis. Para M3.1.2, cada combinação navegador/dispositivo CT01–CT03 é uma unidade. Publicar também resultados por contexto e numerador/denominador; não extrapolar para contextos não avaliados.
6. P7: dez tentativas após aquecimento por canal/rede, sem substituir falhas do serviço. Taxas de conclusão e de falha somam 100% das tentativas elegíveis; erro de instrumento é desvio e exige reposição identificada. Tempo apenas das concluídas, reportando n e taxa de sucesso juntos.
7. Tempos: média aritmética, mediana (média dos dois valores centrais se n par) e P90 pelo posto mais próximo: ordenar e selecionar o elemento de índice teto(0,90 × n), contando a partir de 1. Sem conclusões, tempo não calculável. Julgar pela mediana conforme a Fase 2. Para volume, reportar média e mediana das medidas elegíveis e usar mediana para as faixas provisionais.
8. Preservar precisão bruta; no relatório exibir duas casas decimais e aplicar os níveis da Fase 2 ao valor reportado. Explicitar esse arredondamento para evitar lacunas nas faixas de centésimos. Em percentuais, usar limites contínuos: <60, [60,80), [80,95), >=95; falhas: <=5, (5,20], (20,40], >40.
9. Métrica não medida é inconclusiva; não atribuir nível nem declarar atendido o objetivo que depende dela. M3.1.2 é exclusiva do portal e não serve para ranking com o aplicativo.
