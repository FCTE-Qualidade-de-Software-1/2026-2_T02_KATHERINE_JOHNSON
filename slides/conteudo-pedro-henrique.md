# Conteúdo dos slides — Pedro Henrique (GQM, capa, agenda e próximos passos)

Fonte: `docs/fase2-gqm.md` e `artigo/secoes/fase2-objetivos.tex`.

> **Rascunho preparado pelo Heitor em 19/10/2026 a partir dos objetivos GQM do Pedro Henrique,
> para validação dele.** A sequência completa do deck está em `slides/conteudo-geral.md`.

## Capa

**Título:** Avaliação da consulta de infrações do Detran-DF: Portal de Serviços e aplicativo

**Subtítulo:** Ponto de controle 1 — Fases 1 e 2

Equipe Katherine Johnson: Daniel, Heitor, Hugo, Pedro Druck, Pedro Henrique e Philipe. FGA0315 Qualidade de Software 1, UnB/FGA, 2026/2. Profa. Cristiane Soares Ramos.

## Agenda

1. Problema, propósito, partes interessadas e escopo
2. Produto e modelo de qualidade
3. Priorização e ODS
4. Objetivos, questões e hipóteses GQM
5. Métricas, níveis e critérios de julgamento
6. Metodologia e gestão
7. Próximos passos e pontos para validar

## Slide 1 — Objetivos de medição

**Título:** Três objetivos, um por característica priorizada

Os três objetivos analisam o serviço de consulta de infrações com o propósito de compará-lo e avaliá-lo entre os canais.

| | Com respeito à | Do ponto de vista de | No contexto de |
|---|---|---|---|
| G1 | Adequação funcional: completude, correção e adequação do fluxo de consulta | Cidadão/condutor e requisitante | Consulta no portal e no aplicativo com veículos reais registrados no DF |
| G2 | Eficiência de desempenho: tempo até a lista de infrações e dados transferidos | Equipe técnica de TI do Detran-DF e requisitante | Condições controladas de conectividade, aparelhos representativos |
| G3 | Cobertura de contexto: conclusão da consulta em plataformas e redes diferentes | Cidadão/condutor com restrição de aparelho ou rede, e requisitante | Android, iOS, navegadores; Wi-Fi, 4G e rede degradada simulada |

**Rastreabilidade:** o foco de cada objetivo vem de uma característica priorizada na Fase 1, e o ponto de vista vem da tabela de partes interessadas.

**Fala (cerca de 1 min):** cada característica priorizada virou um objetivo no template GQM. O ponto de vista não foi escolhido agora: vem das partes interessadas da Fase 1. O cidadão olha completude e conclusão; a equipe técnica olha tempo e dados.

## Slide 2 — Questões e hipóteses

**Título:** Sete questões, uma hipótese para cada

| Questão | Hipótese |
|---|---|
| Q1.1 Os canais apresentam as informações necessárias para identificar e compreender a autuação? | H1.1 O portal apresenta mais campos da lista de referência que o aplicativo |
| Q1.2 Status, valores, pontuação e prazos são consistentes entre os canais? | H1.2 Não há divergência entre os canais para a mesma infração |
| Q1.3 Algum canal impõe passos desnecessários até a lista de infrações? | H1.3 O aplicativo exige menos passos e telas que o portal |
| Q2.1 Qual canal exibe a lista de infrações em menos tempo? | H2.1 O aplicativo é mais rápido nas mesmas condições de rede |
| Q2.2 Quanto tráfego de rede cada canal gera na consulta? | H2.2 O aplicativo transfere menos dados que o portal |
| Q3.1 A consulta é concluída em todos os ambientes do escopo? | H3.1 Os dois canais concluem em 100% dos ambientes |
| Q3.2 A consulta continua sendo concluída em rede degradada? | H3.2 A conclusão cai em rede degradada em pelo menos um canal |

**Fala (cerca de 1 min):** as questões perguntam sobre o comportamento dos canais, não sobre o valor de uma métrica. Cada uma tem uma hipótese verificável, que a Fase 4 vai confirmar ou refutar.

## Próximos passos

**Título:** Até a Entrega 1 (26/10) e depois

- Até 21/10: priorização, ODS e referencial SQuaRE no artigo; primeira coleta de gestão.
- Até 24/10: Introdução e Metodologia; artigo integrado; GitPage com as Fases 1 e 2.
- 25/10: revisão cruzada, revisão de português e declaração de IA consolidada.
- 26/10: release E1 e submissão no Moodle.
- Entrega 2: plano de avaliação (Fase 3), sessão com veículos reais, execução, julgamento e ação de melhoria (Fase 4).

**Pontos que queremos validar com a professora:**
1. A inclusão da cobertura de contexto, que vem do modelo de qualidade em uso (ISO/IEC 25010:2011), num trabalho de qualidade do produto.
2. As faixas provisórias dos níveis de pontuação, principalmente as de tempo.
3. O requisitante hipotético (Área de Governança Digital do Detran-DF).

**Fala (cerca de 1 min):** fechamos com o que falta até a entrega e três decisões em que a opinião da professora muda o trabalho. A principal é a cobertura de contexto, que escolhemos por ser a característica que mede justamente a diferença entre usar o serviço no computador e no celular.
