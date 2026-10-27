# Fase 2 — Especificação da Avaliação: Objetivos, Questões e Hipóteses (GQM)

**Projeto Final FGA0315 Qualidade de Software 1 (UnB/FGA, 2026/2)**  
*Avaliação da consulta de infrações do Detran-DF: Portal de Serviços × aplicativo*  
*Responsável pela especificação conceitual e operacional: Pedro Henrique*

---

## 1. Visão Geral e Rastreabilidade (Fase 1 → Fase 2)

A presente etapa do processo de avaliação da qualidade, orientada pela norma **ISO/IEC 25040:2011**, formaliza os objetivos de medição a partir da abordagem **Goal Question Metric (GQM)** (Basili et al., 1994).

A fundamentação da Fase 2 preserva estrita rastreabilidade com as decisões tomadas na Fase 1 do projeto:
- **Focos de Qualidade:** Derivados das características selecionadas e priorizadas pela equipe, sendo duas originárias do modelo de qualidade de produto da **ISO/IEC 25010:2023** (*Adequação Funcional* e *Eficiência de Desempenho*) e uma proveniente do modelo de qualidade em uso da **ISO/IEC 25010:2011** (*Cobertura de Contexto*). Conforme estipulado no regulamento da disciplina, aspectos de usabilidade e capacidade de interação foram terminantemente excluídos da modelagem.
- **Pontos de vista:** Derivados da matriz de partes interessadas (partes interessadas), incorporando as perspectivas centrais do **Cidadão/Condutor**, da **Equipe Técnica de TI e Gestão de Serviços Digitais do Detran-DF** e do **Requisitante Institucional (Detran-DF)**.

### Matriz de Rastreabilidade

| Característica (Fase 1) | Subcaracterísticas Consideradas | Foco de Qualidade (GQM) | Ponto de vista (parte interessada) | Objetivo GQM |
|---|---|---|---|---|
| **Adequação funcional** (ISO/IEC 25010:2023) | Completude funcional, correção funcional, adequação funcional | Completude, correção e adequação do fluxo de consulta | Cidadão / Condutor e Requisitante Institucional | **G1** |
| **Eficiência de desempenho** (ISO/IEC 25010:2023) | Comportamento temporal, utilização de recursos | Tempo até a exibição completa da lista de infrações e volume de dados transferidos via rede | Equipe Técnica de TI e Gestão de Serviços Digitais do Detran-DF e Requisitante Institucional | **G2** |
| **Cobertura de contexto** (Qualidade em Uso) | Completude de contexto, flexibilidade de contexto | Sucesso da tarefa em condições diversas de hardware e conectividade | Cidadão / Condutor e Requisitante | **G3** |

---

## 2. Objetivos de Medição Estruturados (Template GQM)

Cada objetivo foi estruturado rigorosamente nas cinco dimensões conceituais definidas pelo modelo GQM:

### Objetivo G1 — Adequação Funcional
- **Analisar:** O serviço de consulta de infrações de trânsito.
- **Com o propósito de:** Comparar e avaliar.
- **Com respeito à:** Adequação funcional (completude funcional, correção funcional e adequação funcional do fluxo de consulta).
- **Do ponto de vista do:** Cidadão/condutor do Distrito Federal e do requisitante institucional do Detran-DF.
- **No contexto da:** Execução da consulta de infrações por meio do Portal de Serviços e do aplicativo oficial, utilizando veículos reais registrados no DF.

### Objetivo G2 — Eficiência de Desempenho
- **Analisar:** O serviço de consulta de infrações de trânsito.
- **Com o propósito de:** Comparar e avaliar.
- **Com respeito à:** Eficiência de desempenho (tempo até a exibição completa da lista de infrações e volume de dados transferidos via rede).
- **Do ponto de vista da:** Equipe Técnica de TI e Gestão de Serviços Digitais do Detran-DF e do requisitante institucional do Detran-DF.
- **No contexto de:** Requisições síncronas de consulta realizadas em condições controladas de conectividade e em aparelhos representativos da base de usuários.

### Objetivo G3 — Cobertura de Contexto
- **Analisar:** O serviço de consulta de infrações de trânsito.
- **Com o propósito de:** Comparar e avaliar.
- **Com respeito à:** Cobertura de contexto (capacidade de conclusão integral da tarefa mandatória de consulta frente à diversidade tecnológica e degradação de infraestrutura).
- **Do ponto de vista do:** Cidadão/condutor sob restrições técnicas de hardware ou rede e do requisitante institucional.
- **No contexto de:** Variação sistemática de plataformas de acesso (sistemas operacionais Android/iOS, navegadores web modernos) e perfis de conectividade (Wi-Fi de alta velocidade, dados móveis 4G e conexões com latência simulada).

---

## 3. Questões de Medição e Hipóteses

Para evitar a formulação de métricas diretas disfarçadas de questões, cada questão operacional foi desenhada como uma indagação analítica sobre o comportamento intrínseco dos canais frente aos atributos de qualidade. Cada questão é acompanhada por sua respectiva hipótese de teste falseável.

### Objetivo G1 — Adequação Funcional

* **Questão Q1.1 (Completude Funcional):** Os dois canais apresentam as informações necessárias à identificação e compreensão da autuação de trânsito, conforme lista de referência definida na Fase 1?
  * **Hipótese H1.1:** Os dois canais apresentam paridade na completude dos rótulos essenciais da lista de referência da Fase 1. A hipótese foi revista porque o levantamento do produto mostrou que portal e aplicativo usam praticamente os mesmos rótulos ([ata 02](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/atas/ata-02-2026-10-21.md)).
* **Questão Q1.2 (Correção e Consistência Funcional):** As informações referentes ao status, valores monetários, pontuação e prazos das autuações apresentam consistência observável dos campos comuns entre os canais?
  * **Hipótese H1.2:** Não há divergências observáveis entre os canais para uma mesma infração consultada em intervalo temporal próximo.
* **Questão Q1.3 (Adequação das Operações):** A sequência operacional exigida para atingir o extrato final de infrações impõe etapas redundantes ou passos transacionais desnecessários em algum dos canais?
  * **Hipótese H1.3:** Os dois canais exigem o mesmo número de cliques e transições de tela até a exibição das infrações, como prevê o levantamento do produto na Fase 1.

### Objetivo G2 — Eficiência de Desempenho

* **Questão Q2.1 (Comportamento Temporal):** Qual canal apresenta menor tempo decorrido até a exibição completa da lista de infrações?
  * **Hipótese H2.1:** O aplicativo apresenta tempo mediano inferior ao do Portal de Serviços para exibir completamente a lista de infrações, nas mesmas condições de rede e para o mesmo veículo consultado.
* **Questão Q2.2 (Utilização de Recursos de Rede):** Qual o impacto de consumo de tráfego de rede gerado pela operação completa de consulta de infrações em cada canal?
  * **Hipótese H2.2:** O aplicativo apresenta menor volume médio de dados transferidos via rede na transação de consulta quando comparado ao Portal de Serviços.

### Objetivo G3 — Cobertura de Contexto

* **Questão Q3.1 (Completude de Contexto Tecnológico):** A funcionalidade de consulta de infrações é concluída com sucesso em todos os ambientes operacionais definidos no escopo da avaliação (combinações de sistemas operacionais e navegadores)?
  * **Hipótese H3.1:** O Portal de Serviços e o aplicativo permitem a conclusão integral da tarefa de consulta em 100% dos ambientes especificados no escopo (computador e celular), sem bloqueios impeditivos decorrentes da plataforma.
* **Questão Q3.2 (Flexibilidade em Condições de Rede Degradada):** A consulta de infrações continua sendo concluída quando os canais são submetidos a condições de rede degradada, em comparação com as condições de referência Wi-Fi e 4G?
  * **Hipótese H3.2:** A taxa de conclusão da consulta de infrações é menor sob conexões com latência simulada do que sob Wi-Fi e 4G em pelo menos um dos canais.

---

## 4. Próximos Passos na Cadeia de Avaliação

A especificação formal aqui documentada é repassada diretamente ao responsável pelo nível quantitativo (**Philipe**), o qual definirá:
1. As fichas técnicas das métricas quantitativas associadas a cada questão;
2. As faixas de pontuação e os critérios formais de julgamento;
3. O diagrama visual hierárquico consolidado do GQM.

---

*Repositório do projeto:* [GitHub - 2026-2_T02_KATHERINE_JOHNSON](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON)  
*Versão 1.0 — 18/10/2026 — Documentação técnica oficial da equipe.*
