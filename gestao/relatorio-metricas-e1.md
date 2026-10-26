# Relatório de Medição e Governança — Release E1 (Fases 1 e 2)

Este documento consolida os resultados das métricas de gestão do projeto referentes à **Entrega 1 (Release E1)**, fundamentadas no modelo *Practical Software Measurement* (PSM) sob as categorias **CID** (Desempenho de Processos, Calendário e Progresso, e Recursos e Custos).

---

## 1. Resumo dos Indicadores CID

| Categoria CID | Métrica | Sigla | Fórmula | Meta | Valor Obtido | Status |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| **Desempenho** | Taxa de Retrabalho em PRs | $TR_{PR}$ | $(PR_{ajustes} / PR_{total}) \times 100$ | $\le 30\%$ | 25% | OK |
| **Calendário** | Percentual de Issues Concluídas | $PIC_{E1}$ | $(I_{fechadas} / I_{planejadas}) \times 100$ | $100\%$ | 100% | OK |
| **Recursos** | Taxa de Variação de Esforço | $TVE$ | $((H_{reais} - H_{est}) / H_{est}) \times 100$ | $\pm 20\%$ | 4,1% | OK |

---

## 2. Detalhamento por Categoria

### 2.1. Desempenho de Processos ($TR_{PR}$)
Avalia a qualidade inicial das entregas submetidas à revisão por pares na branch `main`.
* **Total de Pull Requests mesclados ($PR_{total}$):** 12
* **PRs que exigiram commits adicionais pós-revisão ($PR_{ajustes}$):** 3
* **Cálculo:** $TR_{PR} = (3 / 12) \times 100 = 25,0\%$

### 2.2. Calendário e Progresso ($PIC_{E1}$)
Mede a aderência ao cronograma planejado para a Release E1 (Fases 1 e 2 da ISO/IEC 25040). As métricas incluem a *issue* agregadora (#2) e as tarefas secundárias de retrabalho exigidas para atingir a meta (#25, #26, #45).
* **Issues planejadas para a Release E1 ($I_{planejadas}$):** 14
* **Issues concluídas até o fechamento da Release ($I_{fechadas}$):** 14
* **Cálculo:** $PIC_{E1} = (14 / 14) \times 100 = 100,0\%$

### 2.3. Recursos e Custos ($TVE$ e $PCI_i$)
Compara o esforço planejado com o esforço real reportado nas *issues* do GitHub e consolida o percentual de contribuição individual ($PCI_i$).

#### Esforço por Integrante
| Integrante (Responsável) | Horas Estimadas ($H_{est}$) | Horas Reais Executadas ($H_{reais}$) | Variação (%) | Total de Issues Encerradas |
| :--- | :---: | :---: | :---: | :---: |
| Daniel de Oliveira Lira | 8h | 10h | +25% | 2 |
| Heitor Macedo Ricardo | 8h | 8h | 0% | 2 |
| Hugo Freitas Silva | 7h | 7h | 0% | 2 |
| Pedro Druck Montalvão Reis | 7h | 7h | 0% | 5 |
| Pedro Henrique Ferreira Xavier | 9h | 9h | 0% | 3 |
| Philipe Amancio Reis Caetano | 8h | 8h | 0% | 2 |
| Ações em Equipe Conjunta | 1h | 1h | 0% | *embutidas* |
| **Total Global** | **48h** | **50h** | **+4,1%** | **14** |

*Cálculo da Taxa de Variação de Esforço:* $TVE = ((50 - 48) / 48) \times 100 = 4,1\%$

#### Percentual de Contribuição Individual ($PCI_i$)
| Integrante | Papel Principal na E1 | Contribuição ($PCI_i$) |
| :--- | :--- | :---: |
| Daniel de Oliveira Lira | Gestão do repositório, integração, Metodologia e métricas CID | 16,67% |
| Heitor Macedo Ricardo | Definição de propósito, restrições, escopo, Introdução e GitPage | 16,67% |
| Hugo Freitas Silva | Revisão técnica, testes locais e validação de Pull Requests | 16,67% |
| Pedro Druck Montalvão Reis | Revisão ortográfica, padronização e enquadramento ODS | 16,67% |
| Pedro Henrique Ferreira Xavier | Definição de métricas GQM, hipóteses e estruturação da Fase 2 | 16,66% |
| Philipe Amancio Reis Caetano | Elaboração da abordagem GQM e geração de diagramas e tabelas | 16,66% |
| **Total** | — | **100,00%** |

---

## 3. Análise Gerencial e Decisões Tomadas

* **Gargalos Identificados:** Durante a execução da Entrega 1, verificou-se colisão temporal entre branches (arquivos da Fase 1 retidos na branch da GitPage) e dependência sequencial na etapa final de integração do artigo LaTeX para execução da revisão ortográfica completa.
* **Qualidade e Retrabalho:** O modelo impôs a adoção de ações corretivas. O estouro do limite de páginas e inconsistências nas métricas (ex.: Hipótese H1.1) forçaram a abertura imediata de sub-issues corretivas de alta prioridade (#26, #45). As revisões cruzadas nos Pull Requests permitiram mitigar o impacto, resultando numa taxa de retrabalho aceitável ($TR_{PR} = 25\%$).
* **Esforço e Planeamento:** A Taxa de Variação de Esforço cravou exíguos 4,1%, o que aponta para um planeamento sólido. O único desvio pontual de esforço (+25%) ocorreu na configuração do repositório, exigindo ajustes minuciosos de CI/CD.
* **Ações Corretivas para a Entrega 2 (E2):**
  1. Garantir que PRs de conteúdo documental (`artigo/` e `docs/`) apontem exclusivamente para a `main`, mantendo branches de infraestrutura isoladas.
  2. Aumentar a margem de segurança do planeamento (+20%) para a absorção da curva de aprendizagem das ferramentas de testes empíricos de desempenho da Fase 3.
  3. Registrar as horas reais imediatamente no ato de abertura do Pull Request de cada *issue*, evitando represamento na coleta de métricas de esforço no fechamento da release.