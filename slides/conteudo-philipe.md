# Conteúdo dos slides — Philipe (métricas, níveis, critérios e diagrama GQM)

Para o Pedro Henrique montar na apresentação. Fonte: `docs/fase2-metricas.md` e `artigo/figuras/fase2-gqm.svg`.

> **Rascunho preparado pelo Heitor em 19/10/2026 a partir das fichas do Philipe, para validação
> dele.** Nenhum número foi alterado em relação às fichas.

## Slide 1 — Métricas por objetivo

**Título:** Catorze métricas externas, iguais para os dois canais

| Objetivo | Questão | Métricas |
|---|---|---|
| G1 — Adequação funcional | Q1.1 Completude | M1.1.1 Campos da lista de referência exibidos na lista (%); M1.1.2 Campos acessíveis no detalhamento (%) |
| | Q1.2 Consistência | M1.2.1 Campos comuns com o mesmo valor (%); M1.2.2 Infrações sem divergência (%) |
| | Q1.3 Passos | M1.3.1 Ações até a lista; M1.3.2 Transições de tela |
| G2 — Eficiência de desempenho | Q2.1 Tempo | M2.1.1 Tempo até a lista (s); M2.1.2 Tempo até os detalhes (s) |
| | Q2.2 Rede | M2.2.1 Dados transferidos na consulta (MB) |
| G3 — Cobertura de contexto | Q3.1 Plataformas | M3.1.1 Conclusão por plataforma (%); M3.1.2 Conclusão por navegador (%) |
| | Q3.2 Rede degradada | M3.2.1 Conclusão por condição de rede (%); M3.2.2 Falhas ou expiração (%); M3.2.3 Tempo por condição de rede (s) |

Cada métrica tem ficha com definição, fórmula, unidade, fonte, procedimento de coleta, interpretação, níveis e justificativa (na GitPage, Fase 2).

**Fala (cerca de 1 min):** cada questão é respondida por pelo menos uma métrica, todas externas e aplicáveis da mesma forma ao portal e ao aplicativo. A completude usa a lista de referência de 15 campos baseada no art. 280 do CTB, externa aos dois canais, para que nenhum canal seja o padrão do outro. Memória ficou fora porque não há ferramenta equivalente para medir nos dois canais.

## Slide 2 — Níveis de pontuação, critérios de julgamento e diagrama

**Título:** Como um número vira julgamento

| Tipo de métrica | Excelente | Alvo | Mínimo aceitável | Inaceitável |
|---|---|---|---|---|
| Percentuais (completude, consistência, conclusão) | 95–100% | 80–94% | 60–79% | abaixo de 60% |
| Falhas ou expiração (M3.2.2) | 0–5% | 6–20% | 21–40% | acima de 40% |
| Tempo até a lista (M2.1.1) | até 3 s | 3,01–5 s | 5,01–8 s | acima de 8 s |
| Dados transferidos (M2.2.1) | até 2 MB | 2,01–5 MB | 5,01–10 MB | acima de 10 MB |
| Passos até a lista (M1.3.1) | até 4 | 5–6 | 7–8 | acima de 8 |

**Critérios de julgamento:**
- Uma questão é atendida quando todas as suas métricas atingem pelo menos o Mínimo aceitável.
- Um objetivo é atendido quando todas as suas questões são atendidas.
- Entre canais, é superior o que atinge nível maior; mesmo nível é paridade.
- Tempo: a mediana decide; média e percentil 90 indicam estabilidade.

Figura: diagrama GQM (`artigo/figuras/fase2-gqm.svg`), com G1–G3, Q1.1–Q3.2 e M1.1.1–M3.2.3 nos níveis conceitual, operacional e quantitativo.

**Fala (cerca de 1 min):** todas as métricas têm quatro níveis. As faixas de tempo partem dos limites de tempo de resposta de Nielsen e ainda são provisórias; queremos a opinião da professora sobre elas. A regra de julgamento é explícita: basta uma métrica inaceitável para o objetivo não ser atendido, e a comparação entre canais é feita por nível, não por diferença numérica pequena.
