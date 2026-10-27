# Plano de Medição e Gestão do Projeto (PSM/CID)

**Projeto Final FGA0315 Qualidade de Software 1 (UnB/FGA, 2026/2)**  
*Avaliação da consulta de infrações do Detran-DF: Portal de Serviços × Aplicativo Mobile*  
**Equipe:** Katherine Johnson (Turma T02)  
**Responsável pela Gestão e Integração:** Daniel  

---

## 1. Visão Geral e Alinhamento Metodológico

Este documento estabelece o plano de acompanhamento quantitativo do projeto de avaliação da qualidade dos canais digitais do Detran-DF. Em conformidade com as exigências da disciplina (Premissa 3 e Seção 2 da especificação do trabalho final), o gerenciamento da equipe adota a estrutura do *Practical Software Measurement* (PSM) (McGarry et al., 2002) e o processo de medição da norma **ISO/IEC/IEEE 15939:2017**.

O objetivo deste plano é transformar os dados operacionais gerados no repositório Git da equipe (*issues*, *commits*, *pull requests* e registros de horas) em indicadores objetivos que apoiem a tomada de decisões corretivas de gestão durante a execução das entregas. As métricas foram estruturadas cobrindo obrigatoriamente as três categorias do modelo PSM/CID:

1. **Desempenho dos Processos** (*Process Performance*);
2. **Calendário e Progresso** (*Schedule and Progress*);
3. **Recursos e Custos** (*Resources and Cost*).

---

## 2. Infraestrutura de Rastreabilidade no GitHub

Para assegurar que todas as medições possuam origem verificável (Premissas 4 e 5), a coleta de dados baseia-se nas seguintes convenções de uso do repositório:

* **Milestones:** Agrupam a totalidade do escopo de cada marco avaliativo (`Milestone E1` para as Fases 1 e 2; `Milestone E2` para as Fases 3 e 4).
* **Issues Padronizadas:** Toda tarefa técnica ou gerencial possui uma *issue* vinculada a um responsável, contendo um *checklist* de critérios de aceitação e campos explícitos para **Estimativa inicial de horas ($H_{est}$)** e **Horas reais executadas ($H_{real}$)**.
* **Fluxo de Branches e Pull Requests (PRs):** Nenhuma alteração é enviada diretamente à *branch* `main`. Todo trabalho exige a abertura de um *Pull Request* revisado por um par designado na matriz de revisão cruzada da equipe.
* **Labels de Categorização:** Identificam a natureza do artefato (`tipo:artigo`, `tipo:docs`, `tipo:gestao`, `tipo:dados`) ; o status de revisão é registrado pelo próprio fluxo de revisão do pull request no GitHub (*Approved* ou *Changes requested*).

---

## 3. Especificação das Métricas de Gestão (PSM/CID)

Foram definidas quatro métricas para o monitoramento da equipe: uma para Desempenho dos Processos (**M-DP1**), uma para Calendário e Progresso (**M-CP1**) e duas para Recursos e Custos (**M-RC1** e **M-RC2**), sendo esta última utilizada diretamente para quantificar o esforço individual exigido pelo critério **AG-C5** (Tabela de Contribuição).

### 3.1. Categoria: Desempenho dos Processos

| Atributo | Especificação da Métrica M-DP1 |
| :--- | :--- |
| **Identificador e Nome** | **M-DP1 — Taxa de Retrabalho em Revisão por Pares ($TR_{PR}$)** |
| **Categoria PSM/CID** | Desempenho dos Processos — Qualidade do Processo e Conformidade |
| **Definição** | Mede a proporção de *Pull Requests* (PRs) submetidos pelos integrantes que não foram aprovados na primeira inspeção do revisor designado, exigindo novos *commits* corretivos antes do *merge* na *branch* `main`. |
| **Medidas Base** | 1. $N_{PR\_total}$: Número total de *Pull Requests* abertos e avaliados no período.<br>2. $N_{PR\_retrabalho}$: Número de *Pull Requests* que receberam solicitação de ajustes (*Changes Requested*) ou *commits* adicionais pós-revisão. |
| **Procedimento de Cálculo** | $TR_{PR} = \left( \frac{N_{PR\_retrabalho}}{N_{PR\_total}} \right) \times 100$ |
| **Unidade de Medida** | Percentual (%) |
| **Fonte dos Dados** | Histórico de *Pull Requests* e registros de *Code Review* no repositório GitHub da equipe. |
| **Procedimento e Frequência de Coleta** | Coleta manual/automatizada via interface de *Pull Requests* do GitHub, realizada em dois momentos por entrega: no meio do ciclo (Quarta-feira, 21/10) e no fechamento da integração (Domingo, 25/10). |
| **Critérios de Interpretação** | Orientação: **Menor é melhor**.<br>• **Adequado (Verde):** $TR_{PR} \le 30\%$ (alta aderência aos padrões de qualidade e checklists).<br>• **Alerta (Amarelo):** $30\% < TR_{PR} \le 50\%$ (inconsistências moderadas de formatação ou conteúdo).<br>• **Crítico (Vermelho):** $TR_{PR} > 50\%$ (falha sistemática no entendimento dos critérios da rubrica). |
| **Decisão de Gestão Disparada** | • Se **Alerta**: O integrador (Daniel) e o revisor de padronização (Pedro Druck) reforçarão os itens de verificação nos comentários das *issues* ativas.<br>• Se **Crítico**: Realizar reunião extraordinária de alinhamento de 15 minutos e tornar obrigatório o preenchimento de autoavaliação contra a rubrica da professora na descrição do PR antes de solicitar revisão. |

---

### 3.2. Categoria: Calendário e Progresso

| Atributo | Especificação da Métrica M-CP1 |
| :--- | :--- |
| **Identificador e Nome** | **M-CP1 — Índice de Cumprimento de Marcos do Cronograma ($ICM$)** |
| **Categoria PSM/CID** | Calendário e Progresso — Progresso de Marcos e Tarefas |
| **Definição** | Avalia a razão entre a quantidade de *issues* efetivamente concluídas (fechadas após aprovação de PR) e a quantidade de *issues* planejadas para estarem concluídas até a data da medição no *Milestone* ativo. |
| **Medidas Base** | 1. $I_{concluidas}$: Quantidade acumulada de *issues* fechadas até a data de corte $t$.<br>2. $I_{planejadas}$: Quantidade acumulada de *issues* cujo prazo planejado vence até a data de corte $t$. |
| **Procedimento de Cálculo** | $ICM = \left( \frac{I_{concluidas}}{I_{planejadas}} \right) \times 100$ |
| **Unidade de Medida** | Percentual (%) |
| **Fonte dos Dados** | Painel do *Milestone* ativo (`Milestone E1`) e datas de fechamento das *issues* no GitHub. |
| **Procedimento e Frequência de Coleta** | Verificação da listagem de *issues* do *Milestone* em dois pontos de controle internos: Quarta-feira (21/10 às 22h) e Sábado (24/10 às 20h, véspera da revisão cruzada final). |
| **Critérios de Interpretação** | Orientação: **Maior é melhor** (idealmente $\ge 100\%$).<br>• **No Prazo (Verde):** $ICM \ge 85\%$.<br>• **Atraso Moderado (Amarelo):** $70\% \le ICM < 85\%$ (ou atraso de até $1$ dia em tarefa com dependência).<br>• **Atraso Crítico (Vermelho):** $ICM < 70\%$ (ou bloqueio na cadeia crítica: Fase 1 $\rightarrow$ Fase 2 $\rightarrow$ Integração). |
| **Decisão de Gestão Disparada** | • Se **Atraso Moderado**: Renegociar prazo interno em até $12$ horas sem afetar a data de integração de sábado.<br>• Se **Atraso Crítico**: Reatribuir imediatamente a subtarefa bloqueada para um integrante que já tenha concluído sua entrega (fatiamento de escopo da *issue*) para impedir atraso na compilação do artigo ou na atualização da GitPage. |

---

### 3.3. Categoria: Recursos e Custos

| Atributo | Especificação da Métrica M-RC1 |
| :--- | :--- |
| **Identificador e Nome** | **M-RC1 — Taxa de Variação de Esforço ($TVE$)** |
| **Categoria PSM/CID** | Recursos e Custos — Esforço de Pessoal |
| **Definição** | Quantifica o desvio percentual entre o esforço real despendido (em horas-pessoa) e o esforço inicialmente estimado para as tarefas da equipe, permitindo identificar subestimação de complexidade ou sobrecarga técnica. |
| **Medidas Base** | 1. $H_{real\_i}$: Horas reais registradas pelo integrante $i$ nas suas *issues*.<br>2. $H_{est\_i}$: Horas estimadas inicialmente para as *issues* do integrante $i$. |
| **Procedimento de Cálculo** | Cálculo por integrante ou global da equipe:<br>$TVE = \left( \frac{\sum H_{real} - \sum H_{est}}{\sum H_{est}} \right) \times 100$ |
| **Unidade de Medida** | Percentual (%) e Horas (h) |
| **Fonte dos Dados** | Seção "Gestão de Esforço (PSM/CID)" preenchida no corpo de cada *issue* do GitHub. |
| **Procedimento e Frequência de Coleta** | Consolidação no [registro de horas da GitPage](https://fcte-qualidade-de-software-1.github.io/2026-2_T02_KATHERINE_JOHNSON/gestao-horas/) e no relatório de métricas em `gestao/` na Quarta-feira (21/10 — parcial) e no Domingo (25/10 — fechamento da E1). |
| **Critérios de Interpretação** | Orientação: **Próximo de $0\%$ é ideal**.<br>• **Controlado (Verde):** $-20\% \le TVE \le +20\%$.<br>• **Desvio Moderado (Amarelo):** $+20\% < TVE \le +40\%$ ou $-40\% \le TVE < -20\%$.<br>• **Sobrecarga / Erro de Estimativa (Vermelho):** $TVE > +40\%$ (esforço real muito acima do previsto). |
| **Decisão de Gestão Disparada** | • Se $TVE > +40\%$ para um integrante específico na medição de quarta-feira: O gestor transferirá a tarefa secundária desse membro (ex.: formatação de tabelas em Markdown para a GitPage ou revisão preliminar) para o integrante com menor $TVE$ acumulado.<br>• Para a Entrega 2: Recalibrar a estimativa base de horas das *issues* futuras utilizando o fator de correção observado na Entrega 1. |

---

| Atributo | Especificação da Métrica M-RC2 |
| :--- | :--- |
| **Identificador e Nome** | **M-RC2 — Percentual de Contribuição Individual ($PCI_i$)** |
| **Categoria PSM/CID** | Recursos e Custos — Alocação e Distribuição de Esforço |
| **Definição** | Determina a proporção exata do esforço total do projeto realizada por cada integrante $i$ da equipe, garantindo transparência na avaliação individual e equilíbrio na distribuição de trabalho. |
| **Medidas Base** | 1. $H_{real\_i}$: Total de horas reais executadas e comprovadas via *commits*/PRs pelo integrante $i$.<br>2. $H_{real\_total} = \sum_{i=1}^{6} H_{real\_i}$: Esforço total em horas de todos os $6$ membros da equipe. |
| **Procedimento de Cálculo** | $PCI_i = \left( \frac{H_{real\_i}}{\sum_{j=1}^{6} H_{real\_j}} \right) \times 100$<br>Restrição de fechamento: $\sum_{i=1}^{6} PCI_i = 100\%$. |
| **Unidade de Medida** | Percentual (%) |
| **Fonte dos Dados** | Horas reais registradas nas *issues* concluídas e auditadas contra o histórico de *commits* e *Pull Requests*. |
| **Procedimento e Frequência de Coleta** | Apuração parcial na Quarta-feira (21/10) e apuração definitiva no Domingo (25/10) para geração do Apêndice de Contribuição do artigo. |
| **Critérios de Interpretação** | Meta de equilíbrio para $6$ integrantes: $\approx 16,67\%$ por integrante.<br>• **Equilibrado (Verde):** $14\% \le PCI_i \le 20\%$.<br>• **Desbalanceado (Amarelo):** $11\% \le PCI_i < 14\%$ ou $20\% < PCI_i \le 23\%$.<br>• **Inaceitável (Vermelho):** $PCI_i < 11\%$ ou $PCI_i > 23\%$. |
| **Decisão de Gestão Disparada** | • Se um integrante apresentar $PCI_i < 14\%$ na medição parcial: Atribuir tarefas adicionais de suporte na integração, revisão de referências BibTeX, verificação de links da GitPage ou preparação dos slides.<br>• No fechamento: Publicar os valores exatos de $PCI_i$ na Tabela de Contribuição do Apêndice do artigo, conforme exigido pelo critério **AG-C5**. |

---

## 4. Resumo do Ciclo de Coleta na Entrega 1 (Milestone E1)

As medições serão coletadas, analisadas e documentadas em relatórios de acompanhamento na pasta `gestao/` seguindo o calendário abaixo:

| Ponto de Coleta | Data Prevista | Escopo da Medição | Artefato Gerado |
| :--- | :--- | :--- | :--- |
| **Coleta 1 (Intermediária)** | Quarta-feira, 21/10/2026 | Rascunhos da Fase 1, referenciais e objetivos/questões GQM | Atualização do registro de horas, cálculo parcial de **M-DP1**, **M-CP1**, **M-RC1** e registro da 1ª decisão de gestão. |
| **Coleta 2 (Fechamento E1)** | Domingo, 25/10/2026 | Fase 2 completa, GitPage, integração do artigo e revisões cruzadas | Gráficos consolidados das 3 categorias, registro final de decisões e geração da Tabela de Contribuição (**M-RC2**). |

---

## 5. Modelo de Registro de Medições e Decisões de Gestão

A tabela abaixo será preenchida a cada coleta para compor a seção de Gestão da GitPage, os slides da apresentação e o histórico de evidências do repositório:

| Data da Coleta | Métrica | Valor Medido | Status (Cor) | Interpretação Técnica | Decisão de Gestão Tomada e Responsável |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `[21/10/2026]` | **M-DP1** ($TR_{PR}$) | `[Ex.: 33,3%]` | `[Amarelo]` | `[Ex.: 2 de 6 PRs exigiram ajustes de padronização LaTeX]` | `[Ex.: Padronizar cabeçalhos de tabelas antes do merge — Daniel]` |
| `[21/10/2026]` | **M-CP1** ($ICM$) | `[Ex.: 83,3%]` | `[Amarelo]` | `[Ex.: 5 de 6 entregas previstas concluídas; 1 em revisão]` | `[Ex.: Priorizar revisão do PR pendente até 12h de quinta — Revisor]` |
| `[21/10/2026]` | **M-RC1** ($TVE$) | `[Ex.: +12,5%]` | `[Verde]` | `[Ex.: Esforço real ligeiramente acima do estimado na Fase 1]` | `[Ex.: Manter alocação atual sem necessidade de remanejamento]` |
| `[21/10/2026]` | **M-RC2** ($PCI_i$) | `[Min: 15% / Max: 19%]` | `[Verde]` | `[Ex.: Distribuição de horas dentro da faixa de equilíbrio]` | `[Ex.: Nenhuma ação corretiva necessária no momento]` |

---

## Referências Normativas e Metodológicas

* **ISO/IEC/IEEE 15939:2017.** *Systems and software engineering — Measurement process*. International Organization for Standardization, Geneva, Switzerland, 2017.
* **McGarry, J., Card, D., Jones, C., Layman, B., Clark, E., Dean, J., & Hall, F.** *Practical Software Measurement: Objective Information for Decision Makers*. Addison-Wesley Professional, 2002.

---
## Histórico de alterações

| Versão | Data | Alteração |
|---|---|---|
| 1.0 | 19/10/2026 | Versão inicial do plano |
| 1.1 | 26/10/2026 | Faixa verde da M-DP1 passa de $\le 25\%$ para $\le 30\%$, por decisão da equipe no fechamento da E1 |
| 1.1 | 26/10/2026 | As horas passam a ser consolidadas no registro de horas da GitPage e no `gestao/relatorio-metricas-e1.md`, em vez de planilha; os gráficos de esforço e de issues por integrante são gerados por `gestao/gerar_metricas_psm.py`, e M-DP1 e M-CP1 são apresentadas em tabela |
| 1.1 | 26/10/2026 | As labels `revisao:*` foram substituídas pelo estado de revisão do próprio pull request no GitHub |

*Versão 1.1 — 26/10/2026 — Equipe Katherine Johnson (FGA0315/UnB).*