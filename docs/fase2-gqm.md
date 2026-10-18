# Fase 2 — Especificação da Avaliação: Objetivos, Questões e Hipóteses (GQM)

**Projeto Final FGA0315 Qualidade de Software 1 (UnB/FGA, 2026/2)**  
*Avaliação da consulta de infrações do Detran-DF: Portal de Serviços × Aplicativo Mobile*  
*Responsável pela especificação conceitual e operacional: Pedro Henrique*

---

## 1. Visão Geral e Rastreabilidade (Fase 1 → Fase 2)

A presente etapa do processo de avaliação da qualidade, orientada pela norma **ISO/IEC 25040:2011**, formaliza os objetivos de medição a partir da abordagem **Goal Question Metric (GQM)** (Basili et al., 1994).

A fundamentação da Fase 2 preserva estrita rastreabilidade com as decisões tomadas na Fase 1 do projeto:
- **Focos de Qualidade:** Derivados das características selecionadas e priorizadas pela equipe, sendo duas originárias do modelo de qualidade de produto da **ISO/IEC 25010:2023** (*Adequação Funcional* e *Eficiência de Desempenho*) e uma proveniente do modelo de qualidade em uso da **ISO/IEC 25010:2011** (*Cobertura de Contexto*). Conforme estipulado no regulamento da disciplina, aspectos de usabilidade e capacidade de interação foram terminantemente excluídos da modelagem.
- **Pontos de Vista:** Derivados da matriz de partes interessadas (*stakeholders*), incorporando as perspectivas centrais do **Cidadão/Condutor**, da **Equipe Técnica de TI / Fornecedores** e do **Requisitante Institucional (Detran-DF)**.

### Matriz de Rastreabilidade

| Característica (Fase 1) | Subcaracterísticas Consideradas | Foco de Qualidade (GQM) | Ponto de Vista (*Stakeholder*) | Objetivo GQM |
|---|---|---|---|---|
| **Adequação Funcional** (ISO/IEC 25010:2023) | Completude funcional, correção funcional, adequação funcional | Integridade, fidedignidade e concisão informacional | Cidadão / Condutor e Requisitante Institucional | **G1** |
| **Eficiência de Desempenho** (ISO/IEC 25010:2023) | Comportamento temporal, utilização de recursos | Latência de resposta, consumo de banda e sobrecarga de memória | Equipe Técnica de TI / Fornecedor e Requisitante | **G2** |
| **Cobertura de Contexto** (Qualidade em Uso) | Completude de contexto, flexibilidade operacional | Sucesso da tarefa em condições diversas de hardware e conectividade | Cidadão / Condutor e Requisitante | **G3** |

---

## 2. Objetivos de Medição Estruturados (Template GQM)

Cada objetivo foi estruturado rigorosamente nas cinco dimensões conceituais definidas pelo modelo GQM:

### Objetivo G1 — Adequação Funcional
- **Analisar:** O serviço de consulta de infrações de trânsito.
- **Com o propósito de:** Comparar e avaliar.
- **Com respeito à:** Adequação funcional (completude dos dados da autuação, correção das informações cadastrais/financeiras e concisão do fluxo operacional).
- **Do ponto de vista do:** Cidadão/condutor do Distrito Federal e do requisitante institucional do Detran-DF.
- **No contexto da:** Execução da consulta de infrações por meio do Portal de Serviços web e do aplicativo mobile oficial, utilizando veículos reais registrados no DF.

### Objetivo G2 — Eficiência de Desempenho
- **Analisar:** O serviço de consulta de infrações de trânsito.
- **Com o propósito de:** Comparar e avaliar.
- **Com respeito à:** Eficiência de desempenho (tempo de resposta percebido pelo cliente, volume de dados trafegados na rede e consumo de memória volátil).
- **Do ponto de vista da:** Equipe técnica de TI / fornecedores do sistema e do requisitante institucional do Detran-DF.
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

* **Questão Q1.1 (Completude Funcional):** Os canais web e mobile apresentam a integralidade dos dados detalhados necessários à identificação e compreensão da autuação de trânsito?
  * **Hipótese H1.1:** O Portal de Serviços web apresenta maior detalhamento e completude de campos informativos do auto de infração (como identificação do agente, tipificação infracional completa e imagem da autuação) do que o aplicativo mobile, devido a restrições de área de visualização em dispositivos móveis.
* **Questão Q1.2 (Correção e Consistência Funcional):** As informações referentes ao status, valores monetários, pontuação e prazos das autuações apresentam absoluta conformidade semântica e numérica entre o Portal de Serviços e o aplicativo mobile?
  * **Hipótese H1.2:** Não há divergências de dados cadastrais, financeiros ou situacionais entre o Portal de Serviços e o aplicativo mobile para um mesmo veículo consultado em intervalo temporal síncrono, dado que ambos consom a mesma base de dados centralizada do Detran-DF.
* **Questão Q1.3 (Adequação das Operações):** A sequência operacional exigida para atingir o extrato final de infrações impõe etapas redundantes ou passos transacionais desnecessários em algum dos canais?
  * **Hipótese H1.3:** O aplicativo mobile proporciona um caminho operacional mais enxuto (menor número de cliques e transições de tela) até a exibição das infrações do que o Portal de Serviços web, em razão da sessão de autenticação persistente integrada ao sistema operacional móvel.

### Objetivo G2 — Eficiência de Desempenho

* **Questão Q2.1 (Comportamento Temporal):** Qual canal apresenta menor tempo de resposta percebido para o carregamento integral e disponibilização visual do extrato de infrações?
  * **Hipótese H2.1:** O aplicativo mobile atinge tempo de resposta percebido sensivelmente inferior ao do Portal de Serviços web, por requerer apenas a transferência de dados estruturados em formato serializado, enquanto o portal demanda o download e a renderização completa do documento HTML, estilos e scripts.
* **Questão Q2.2 (Utilização de Recursos de Rede):** Qual o impacto de consumo de tráfego de rede gerado pela operação completa de consulta de infrações em cada canal?
  * **Hipótese H2.2:** O volume de bytes transferidos via rede na transação de consulta é substancialmente menor no aplicativo mobile quando comparado ao Portal de Serviços web, reduzindo o consumo de pacotes de dados móveis do cidadão.
* **Questão Q2.3 (Sobrecarga de Memória e Processamento):** A execução da consulta de infrações impõe consumo desproporcional de memória operacional no dispositivo cliente que comprometa a execução em terminais com recursos moderados?
  * **Hipótese H2.3:** O consumo de memória RAM alocada durante o ciclo de vida da consulta mantém-se dentro de limites aceitáveis para dispositivos móveis de entrada e intermediários, sem gerar picos anômalos de alocação de memória no canal móvel.

### Objetivo G3 — Cobertura de Contexto

* **Questão Q3.1 (Completude de Contexto Tecnológico):** A funcionalidade de consulta de infrações é concluída com sucesso em todos os ambientes operacionais definidos no escopo da avaliação (combinações de sistemas operacionais e navegadores)?
  * **Hipótese H3.1:** O Portal de Serviços web e o aplicativo mobile permitem a conclusão integral da tarefa de consulta em 100% dos ambientes de teste homologados (desktop e mobile), sem bloqueios impeditivos decorrentes da plataforma.
* **Questão Q3.2 (Flexibilidade e Resiliência em Redes Restritas):** A capacidade de entrega da consulta de infrações é preservada quando os canais são submetidos a condições degradadas de largura de banda e latência de rede?
  * **Hipótese H3.2:** O Portal de Serviços web manifesta maior índice de expiração de sessão e falhas por *timeout* em condições de conectividade restrita (rede 2G/3G simulada) em comparação ao aplicativo mobile, afetando a completude da tarefa no canal web sob condições adversas de infraestrutura.

---

## 4. Próximos Passos na Cadeia de Avaliação

A especificação formal aqui documentada é repassada diretamente ao responsável pelo nível quantitativo (**Philipe**), o qual definirá:
1. As fichas técnicas das métricas quantitativas associadas a cada questão;
2. As faixas de pontuação e os critérios formais de julgamento;
3. O diagrama visual hierárquico consolidado do GQM.

---

*Repositório do projeto:* [GitHub - 2026-2_T02_KATHERINE_JOHNSON](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON)  
*Versão 1.0 — 18/10/2026 — Documentação técnica oficial da equipe.*
