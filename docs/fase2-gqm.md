# Fase 2 — Especificação da Avaliação: Objetivos, Questões e Hipóteses (GQM)

**Projeto Final FGA0315 Qualidade de Software 1 (UnB/FGA, 2026/2)**  
*Avaliação da consulta de infrações do Detran-DF: Portal de Serviços × aplicativo*  
*Responsável pela especificação conceitual e operacional: Pedro Henrique*

---

## 1. Visão Geral e Rastreabilidade (Fase 1 → Fase 2)

A presente etapa do processo de avaliação da qualidade, orientada pela norma **ISO/IEC 25040:2011**, formaliza os objetivos de medição a partir da abordagem **Goal Question Metric (GQM)** (Basili et al., 1994).

A fundamentação da Fase 2 preserva estrita rastreabilidade com as decisões tomadas na Fase 1 do projeto:
- **Focos de Qualidade:** Derivados das características selecionadas e priorizadas pela equipe, sendo duas originárias do modelo de qualidade de produto da **ISO/IEC 25010:2023** (*Adequação Funcional* e *Eficiência de Desempenho*) e uma proveniente do modelo de qualidade em uso da **ISO/IEC 25010:2011** (*Cobertura de Contexto*). Conforme estipulado no regulamento da disciplina, aspectos de usabilidade e capacidade de interação foram terminantemente excluídos da modelagem.
- **Pontos de vista:** Derivados da matriz de partes interessadas da Fase 1, incorporando as perspectivas centrais do **Cidadão/Condutor**, da **Equipe Técnica de TI e Gestão de Serviços Digitais do Detran-DF** e do **Requisitante Institucional (Detran-DF)**.

### Matriz de Rastreabilidade {#matriz-f1-f2}

| Característica (Fase 1) | Subcaracterísticas Consideradas | Foco de Qualidade (GQM) | Ponto de vista (parte interessada) | Objetivo GQM |
|---|---|---|---|---|
| **Adequação funcional** (ISO/IEC 25010:2023) | Completude funcional, correção funcional, adequação funcional | Completude, correção e adequação do fluxo de consulta | Cidadão / Condutor e Requisitante Institucional | **G1** |
| **Eficiência de desempenho** (ISO/IEC 25010:2023) | Comportamento temporal, utilização de recursos | Tempo até a exibição completa da lista de infrações e volume de dados transferidos via rede | Equipe Técnica de TI e Gestão de Serviços Digitais do Detran-DF e Requisitante Institucional | **G2** |
| **Cobertura de contexto** (Qualidade em Uso) | Completude de contexto, flexibilidade de contexto | Sucesso da tarefa em condições diversas de hardware e conectividade | Cidadão / Condutor e Requisitante | **G3** |

---

## 2. Objetivos de Medição Estruturados (Template GQM)

Cada objetivo foi estruturado rigorosamente nas cinco dimensões conceituais definidas pelo modelo GQM:

### Objetivo G1 — Adequação Funcional {#g1}
- **Analisar:** O serviço de consulta de infrações de trânsito.
- **Com o propósito de:** Comparar e avaliar.
- **Com respeito à:** Adequação funcional (completude funcional, correção funcional e adequação funcional do fluxo de consulta).
- **Do ponto de vista do:** Cidadão/condutor do Distrito Federal e do requisitante institucional do Detran-DF.
- **No contexto da:** Execução da consulta de infrações por meio do Portal de Serviços e do aplicativo oficial, utilizando veículos reais registrados no DF.
- **Rastreabilidade:** questões [Q1.1](#q1-1), [Q1.2](#q1-2), [Q1.3](#q1-3); [cadeia completa de G1](rastreabilidade.md#rt-g1).

### Objetivo G2 — Eficiência de Desempenho {#g2}
- **Analisar:** O serviço de consulta de infrações de trânsito.
- **Com o propósito de:** Comparar e avaliar.
- **Com respeito à:** Eficiência de desempenho (tempo até a exibição completa da lista de infrações e volume de dados transferidos via rede).
- **Do ponto de vista da:** Equipe Técnica de TI e Gestão de Serviços Digitais do Detran-DF e do requisitante institucional do Detran-DF.
- **No contexto de:** Requisições síncronas de consulta realizadas em condições controladas de conectividade e em aparelhos representativos da base de usuários.
- **Rastreabilidade:** questões [Q2.1](#q2-1), [Q2.2](#q2-2); [cadeia completa de G2](rastreabilidade.md#rt-g2).

### Objetivo G3 — Cobertura de Contexto {#g3}
- **Analisar:** O serviço de consulta de infrações de trânsito.
- **Com o propósito de:** Comparar e avaliar.
- **Com respeito à:** Cobertura de contexto (capacidade de conclusão integral da tarefa mandatória de consulta frente à diversidade tecnológica e degradação de infraestrutura).
- **Do ponto de vista do:** Cidadão/condutor sob restrições técnicas de hardware ou rede e do requisitante institucional.
- **No contexto de:** Variação sistemática de plataformas de acesso (sistemas operacionais Android/iOS, navegadores web modernos) e perfis de conectividade (Wi-Fi de alta velocidade, dados móveis 4G e conexões com latência simulada).
- **Rastreabilidade:** questões [Q3.1](#q3-1), [Q3.2](#q3-2); [cadeia completa de G3](rastreabilidade.md#rt-g3).

---

## 3. Questões de Medição e Hipóteses

Para evitar a formulação de métricas diretas disfarçadas de questões, cada questão operacional foi desenhada como uma indagação analítica sobre o comportamento intrínseco dos canais frente aos atributos de qualidade. Cada questão é acompanhada por sua respectiva hipótese de teste falseável.

### Questões e hipóteses de G1 {#g1-questoes}

* <span id="q1-1"></span>**Questão Q1.1 (Completude Funcional):** Os dois canais apresentam as informações necessárias à identificação e compreensão da autuação de trânsito, conforme lista de referência definida na Fase 1?
  * <span id="h1-1"></span>**Hipótese H1.1:** Os dois canais apresentam paridade na completude dos rótulos essenciais da lista de referência da Fase 1. A hipótese foi revista porque o levantamento do produto mostrou que portal e aplicativo usam praticamente os mesmos rótulos ([ata 02](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/atas/ata-02-2026-10-21.md)).
  * **Métricas:** [M1.1.1](fase2-metricas.md#m1-1-1), [M1.1.2](fase2-metricas.md#m1-1-2); procedimento [P1](fase3-metodo.md#p1); [rastreabilidade](rastreabilidade.md#rt-q1-1).
* <span id="q1-2"></span>**Questão Q1.2 (Correção e Consistência Funcional):** As informações referentes ao status, valores monetários, pontuação e prazos das autuações apresentam consistência observável dos campos comuns entre os canais?
  * <span id="h1-2"></span>**Hipótese H1.2:** Não há divergências observáveis entre os canais para uma mesma infração consultada em intervalo temporal próximo.
  * **Métricas:** [M1.2.1](fase2-metricas.md#m1-2-1), [M1.2.2](fase2-metricas.md#m1-2-2); procedimento [P2](fase3-metodo.md#p2); [rastreabilidade](rastreabilidade.md#rt-q1-2).
* <span id="q1-3"></span>**Questão Q1.3 (Adequação das Operações):** A sequência operacional exigida para atingir o extrato final de infrações impõe etapas redundantes ou passos transacionais desnecessários em algum dos canais?
  * <span id="h1-3"></span>**Hipótese H1.3:** Os dois canais exigem o mesmo número de cliques e transições de tela até a exibição das infrações, como prevê o levantamento do produto na Fase 1.
  * **Métricas:** [M1.3.1](fase2-metricas.md#m1-3-1), [M1.3.2](fase2-metricas.md#m1-3-2); procedimento [P3](fase3-metodo.md#p3); [rastreabilidade](rastreabilidade.md#rt-q1-3).

### Questões e hipóteses de G2 {#g2-questoes}

* <span id="q2-1"></span>**Questão Q2.1 (Comportamento Temporal):** Qual canal apresenta menor tempo decorrido até a exibição completa da lista de infrações?
  * <span id="h2-1"></span>**Hipótese H2.1:** O aplicativo apresenta tempo mediano inferior ao do Portal de Serviços para exibir completamente a lista de infrações, nas mesmas condições de rede e para o mesmo veículo consultado.
  * **Métricas:** [M2.1.1](fase2-metricas.md#m2-1-1), [M2.1.2](fase2-metricas.md#m2-1-2); procedimento [P4](fase3-metodo.md#p4); [rastreabilidade](rastreabilidade.md#rt-q2-1).
* <span id="q2-2"></span>**Questão Q2.2 (Utilização de Recursos de Rede):** Qual o impacto de consumo de tráfego de rede gerado pela operação completa de consulta de infrações em cada canal?
  * <span id="h2-2"></span>**Hipótese H2.2:** O aplicativo apresenta menor volume médio de dados transferidos via rede na transação de consulta quando comparado ao Portal de Serviços.
  * **Métricas:** [M2.2.1](fase2-metricas.md#m2-2-1); procedimento [P5](fase3-metodo.md#p5); [rastreabilidade](rastreabilidade.md#rt-q2-2).

### Questões e hipóteses de G3 {#g3-questoes}

* <span id="q3-1"></span>**Questão Q3.1 (Completude de Contexto Tecnológico):** A funcionalidade de consulta de infrações é concluída com sucesso em todos os ambientes operacionais definidos no escopo da avaliação (combinações de sistemas operacionais e navegadores)?
  * <span id="h3-1"></span>**Hipótese H3.1:** O Portal de Serviços e o aplicativo permitem a conclusão integral da tarefa de consulta em 100% dos ambientes especificados no escopo (computador e celular), sem bloqueios impeditivos decorrentes da plataforma.
  * **Métricas:** [M3.1.1](fase2-metricas.md#m3-1-1), [M3.1.2](fase2-metricas.md#m3-1-2); procedimento [P6](fase3-metodo.md#p6); [rastreabilidade](rastreabilidade.md#rt-q3-1).
* <span id="q3-2"></span>**Questão Q3.2 (Flexibilidade em Condições de Rede Degradada):** A consulta de infrações continua sendo concluída quando os canais são submetidos a condições de rede degradada, em comparação com as condições de referência Wi-Fi e 4G?
  * <span id="h3-2"></span>**Hipótese H3.2:** A taxa de conclusão da consulta de infrações é menor sob conexões com latência simulada do que sob Wi-Fi e 4G em pelo menos um dos canais.
  * **Métricas:** [M3.2.1](fase2-metricas.md#m3-2-1), [M3.2.2](fase2-metricas.md#m3-2-2), [M3.2.3](fase2-metricas.md#m3-2-3); procedimento [P7](fase3-metodo.md#p7); [rastreabilidade](rastreabilidade.md#rt-q3-2).

---

## 4. Próximos Passos na Cadeia de Avaliação

A especificação formal aqui documentada é repassada diretamente ao responsável pelo nível quantitativo (**Philipe**), o qual definirá:
1. As fichas técnicas das métricas quantitativas associadas a cada questão;
2. As faixas de pontuação e os critérios formais de julgamento;
3. O diagrama visual hierárquico consolidado do GQM.

---

*Repositório do projeto:* [GitHub - 2026-2_T02_KATHERINE_JOHNSON](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON)  
*Versão 1.0 — 18/10/2026 — Documentação técnica oficial da equipe.*
