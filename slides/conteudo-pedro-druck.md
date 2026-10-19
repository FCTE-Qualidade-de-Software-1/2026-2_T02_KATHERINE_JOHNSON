# Conteúdo dos slides — Pedro Druck (priorização e ODS)

Para o Pedro Henrique montar na apresentação.

> **Rascunho preparado pelo Heitor em 19/10/2026 para validação do Pedro Druck.** A seção do
> artigo ainda não existe no repositório (issue #7). Notas e pesos abaixo são uma proposta
> derivada do modelo de qualidade do Hugo (`docs/fase1-produto.md`, Seção 3.2) e das partes
> interessadas (`docs/fase1-proposito.md`); ajuste o que discordar. Textos de ODS marcados com
> [VERIFICAR] precisam ser conferidos no portal oficial (odsbrasil.gov.br).

## Slide 1 — Priorização das características

**Título:** Como chegamos às três características

**Método:** matriz de pontuação ponderada, seguida de classificação MoSCoW. Cada característica candidata recebe nota de 1 a 5 em quatro critérios; a nota final é a soma ponderada (máximo 45). Capacidade de interação (usabilidade) foi excluída antes da pontuação, por exigência da disciplina.

| Critério | Peso | Por que esse peso |
|---|---|---|
| Impacto para o cidadão | 3 | É o usuário da consulta e o principal ponto de vista (G1, G3) |
| Relação com o propósito comparativo | 3 | A avaliação existe para comparar os canais (D1 a D4) |
| Viabilidade de medir em caixa-preta | 2 | Sem acesso a código, servidores ou base do Detran-DF |
| Esforço de coleta (5 = baixo) | 1 | Prazo da disciplina; pesa menos que o valor da informação |

| Característica | Impacto | Propósito | Viabilidade | Esforço | Total | MoSCoW |
|---|---:|---:|---:|---:|---:|---|
| Adequação funcional | 5 | 5 | 5 | 4 | **44** | Must |
| Cobertura de contexto | 4 | 5 | 4 | 2 | **37** | Must |
| Eficiência de desempenho | 4 | 4 | 4 | 3 | **35** | Must |
| Confiabilidade | 4 | 2 | 1 | 1 | 21 | Could (falhas entram em M3.2.2) |
| Segurança | 5 | 1 | 1 | 1 | 21 | Won't |
| Compatibilidade | 2 | 2 | 1 | 3 | 17 | Won't |

**Trade-offs:**
- Deixar segurança fora reduz o esforço e evita testes sem autorização do Detran-DF, mas a avaliação não diz nada sobre a proteção dos dados pessoais exibidos.
- Confiabilidade sai como característica, mas falhas pontuais aparecem como consulta não concluída em G3.
- Cobertura de contexto é a mais cara (vários aparelhos e redes), e entra mesmo assim porque é o que diferencia os canais.

**Fala (cerca de 1 min):** usamos uma matriz ponderada com quatro critérios. Impacto para o cidadão e relação com o propósito pesam mais, porque a avaliação existe para comparar os canais do ponto de vista de quem consulta. As três características escolhidas ficaram bem acima das demais. Segurança tem impacto alto, mas não dá para testar sem autorização do órgão; esse é o principal trade-off.

## Slide 2 — ODS, metas e indicadores

**Título:** Onde a consulta de infrações toca os ODS

| ODS | Meta | Indicador | Pertinência ao software |
|---|---|---|---|
| ODS 16 — Paz, justiça e instituições eficazes | 16.6 — Desenvolver instituições eficazes, responsáveis e transparentes em todos os níveis [VERIFICAR] | 16.6.2 — Proporção da população satisfeita com a última experiência com serviços públicos [VERIFICAR] | A consulta é o serviço público em si. Uma avaliação que mostra divergência de dados, lentidão ou falha por canal aponta onde o serviço deixa de ser eficaz e transparente para o cidadão |
| ODS 9 — Indústria, inovação e infraestrutura | 9.c — Aumentar significativamente o acesso às tecnologias de informação e comunicação [VERIFICAR] | 9.c.1 — Proporção da população coberta por rede móvel, por tecnologia [VERIFICAR] | Ter cobertura de rede móvel não basta se o serviço não conclui em rede 4G ou degradada; a cobertura de contexto (G3) mede exatamente isso |

**Considerado e descartado:** ODS 3, meta 3.6 (mortes e lesões no trânsito). A relação é com a fiscalização de trânsito em geral, não com a qualidade do software de consulta.

**Fala (cerca de 1 min):** o vínculo principal é com a meta 16.6, porque o objeto avaliado é um serviço público digital. Não medimos satisfação, que é o indicador 16.6.2; nossa avaliação produz evidências sobre causas objetivas que afetam essa experiência. O ODS 9 entra pela meta 9.c: acesso a rede móvel só vira acesso ao serviço se a consulta funciona nessa rede. Descartamos o ODS 3 porque o vínculo seria com a fiscalização, não com o software.
