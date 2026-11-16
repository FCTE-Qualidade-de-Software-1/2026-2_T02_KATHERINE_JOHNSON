# Consolidação da análise — issue #48

Os modelos CSV contêm somente cabeçalhos. A entrada vem da #47 e segue `dados/README.md`. As regras de interpretação e a dependência estão em `docs/fase4-analise.md`.

`resultados-metricas.csv` recebe uma linha por métrica, canal ou par, veículo, contexto e rede. Registrar n válido, n excluído, numerador/denominador quando aplicável, unidade e estatísticas. `valor_julgado` segue a ficha da Fase 2. `nivel` admite Inaceitável, Mínimo aceitável, Alvo ou Excelente somente com resultado calculável. `estado` admite calculado, inconclusivo ou nao_aplicavel. Valores ausentes ficam vazios. Evidência e origem dos cálculos devem permitir reproduzir cada resultado.

`respostas-gqm.csv` recebe cada Q e G por canal/contexto. `estado` admite atendido, nao_atendido, inconclusivo ou nao_aplicavel. `hipotese` identifica H quando houver. `avaliacao_hipotese` admite compativel_com_amostra, contrariada ou inconclusiva. Descrever resultado, métricas e evidências na resposta e registrar limitações. Métricas do par subsidiam ambos os canais, sem eleger superioridade individual.

`oportunidades.csv` registra problemas observados e sua priorização proposta. `prioridade` é posição ordinal justificada por impacto, recorrência e abrangência. Vincular a decisão D1–D4 e a ação de melhoria quando definida. Nenhum problema foi inferido apenas pela ausência de dados.
