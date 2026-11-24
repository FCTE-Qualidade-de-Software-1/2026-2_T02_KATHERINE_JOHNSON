# Consolidação da análise — issue #48

`resultados-metricas.csv` é gerado pelo script da #47 a partir dos dados conferidos; registra
valores, níveis e proveniência por métrica, canal/par, veículo, contexto e rede. `respostas-gqm.csv`
e `oportunidades.csv` contêm as respostas e prioridades documentadas para a #48. A entrada segue
`dados/README.md`; as regras de interpretação e os limites estão em `docs/fase4-analise.md`.

`resultados-metricas.csv` recebe uma linha por métrica, canal ou par, veículo, contexto e rede. Registrar n válido, n excluído, numerador/denominador quando aplicável, unidade e estatísticas. `valor_julgado` segue a ficha da Fase 2. `nivel` admite Inaceitável, Mínimo aceitável, Alvo ou Excelente somente com resultado calculável. `estado` admite calculado, inconclusivo ou nao_aplicavel. Valores ausentes ficam vazios. Evidência e origem dos cálculos devem permitir reproduzir cada resultado.

`respostas-gqm.csv` registra cada Q e G por canal/contexto. `estado` admite atendido, nao_atendido,
inconclusivo ou nao_aplicavel. `hipotese` identifica H quando houver. `avaliacao_hipotese` admite
compativel_com_amostra, contrariada ou inconclusiva. Cada resposta traz métricas, evidências e
limitações; métricas do par subsidiam ambos os canais, sem eleger superioridade individual.

`oportunidades.csv` registra problemas observados e sua priorização proposta. `prioridade` é
posição ordinal justificada por impacto, recorrência e abrangência. Vincular a decisão D1–D4 e a
ação de melhoria quando definida. Não inferir problema apenas da ausência de dados.

## Saída automatizada e rastreabilidade

Executar `python3 dados/scripts/calcular.py` na raiz após conferir os CSV. O script gera somente
`resultados-metricas.csv` e `manifesto-calculo.json`. Versionar ambos junto aos dados usados.

- `sessao`, `bloco` e `infracao` foram acrescentados ao resultado para distinguir execuções.
  P1 reporta cada infração e o agregado `todas`; P2 reporta o agregado por veículo e sessão.
- `n_valido` e `n_excluido` contam linhas da origem; em tempos, falhas ficam fora do resumo
  temporal, mas permanecem no denominador das taxas de P7. Em P1/P2, n conta campos; o
  denominador de M1.2.2 conta infrações. Em P6, n conta tentativas e o denominador conta
  plataformas/navegadores. Piloto S01 não entra nas linhas de resultado.
- `contexto` de P6 lista os contextos com três tentativas elegíveis; `limitacoes` registra
  aprovação/reprovação por contexto e cobertura ausente. Computador só é avaliado como
  plataforma com CT01 e CT02 completos, e só é aprovado quando ambos são aprovados.
- `media`, `mediana` e `p90` mantêm precisão para reprodução. O nível é aplicado antes de
  qualquer arredondamento de apresentação. P90 usa o posto mais próximo.
- `commit_dados` identifica a base de trabalho; o SHA-256 no manifesto identifica o conteúdo
  exato lido, mesmo quando ainda não commitado. Não usar apenas o commit como garantia de
  identidade das entradas. Uma regeneração em outro commit muda esse campo de proveniência.
- Resultados com amostra reduzida não dispensam o desvio nem a discussão de limites na #48.
  O programa não escolhe uma melhoria, responde GQM ou certifica a coleta automaticamente.
