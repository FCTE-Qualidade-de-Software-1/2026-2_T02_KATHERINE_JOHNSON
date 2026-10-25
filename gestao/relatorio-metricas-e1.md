# Relatório de Medição e Governança — Release E1 (Fases 1 e 2)

Este documento consolida os resultados das métricas de gestão do projeto referentes à **Entrega 1 (Release E1)**, fundamentadas no modelo *Practical Software Measurement* (PSM) sob as categorias **CID** (Desempenho de Processos, Calendário e Progresso, e Recursos e Custos).

---

## 1. Resumo dos Indicadores CID

| Categoria CID | Métrica | Sigla | Fórmula | Meta | Valor Obtido | Status |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| **Desempenho** | Taxa de Retrabalho em PRs | $TR_{PR}$ | $(PR_{ajustes} / PR_{total}) \times 100$ | $\le 30\%$ | `[X]%` | `[OK/Alerta]` |
| **Calendário** | Percentual de Issues Concluídas | $PIC_{E1}$ | $(I_{fechadas} / I_{planejadas}) \times 100$ | $100\%$ | `[X]%` | `[OK/Alerta]` |
| **Recursos** | Taxa de Variação de Esforço | $TVE$ | $((H_{reais} - H_{est}) / H_{est}) \times 100$ | $\pm 20\%$ | `[X]%` | `[OK/Alerta]` |

---

## 2. Detalhamento por Categoria

### 2.1. Desempenho de Processos ($TR_{PR}$)
Avalia a qualidade inicial das entregas submetidas à revisão por pares na branch `main`.
* **Total de Pull Requests mesclados ($PR_{total}$):** `[X]`
* **PRs que exigiram commits adicionais pós-revisão ($PR_{ajustes}$):** `[X]`
* **Cálculo:** $TR_{PR} = (\text{[X]} / \text{[X]}) \times 100 = \text{[X]}\%$

### 2.2. Calendário e Progresso ($PIC_{E1}$)
Mede a aderência ao cronograma planejado para a Release E1 (Fases 1 e 2 da ISO/IEC 25040).
* **Issues planejadas para a Release E1 ($I_{planejadas}$):** `[X]`
* **Issues concluídas até o fechamento da Release ($I_{fechadas}$):** `[X]`
* **Cálculo:** $PIC_{E1} = (\text{[X]} / \text{[X]}) \times 100 = \text{[X]}\%$

### 2.3. Recursos e Custos ($TVE$ e $PCI_i$)
Compara o esforço planejado com o esforço real reportado nas *issues* do GitHub e consolida o percentual de contribuição individual ($PCI_i$).

#### Esforço por Issue
| Issue | Descrição / Tarefa | Responsável | Horas Estimadas ($H_{est}$) | Horas Reais ($H_{reais}$) | Variação (%) |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **#1** | Setup do Repositório e Governança PSM/CID | Daniel Lira | `[X]h` | `[X]h` | `[X]%` |
| **#2** | Metodologia e Integração do Artigo (E1) | Daniel Lira | `[X]h` | `[X]h` | `[X]%` |
| **#3** | Propósito, Escopo e Introdução (Fase 1) | Heitor Ricardo | `[X]h` | `[X]h` | `[X]%` |
| **#4** | Estruturação e Publicação da GitPage (MkDocs) | Heitor Ricardo | `[X]h` | `[X]h` | `[X]%` |
| **#5** | Especificação GQM, Hipóteses e Fase 2 | Pedro Henrique | `[X]h` | `[X]h` | `[X]%` |
| **#6** | Diagramação GQM e Tabelas de Métricas | Philipe Caetano | `[X]h` | `[X]h` | `[X]%` |
| **#7** | Revisão Técnica e Validação de PRs | Hugo Silva | `[X]h` | `[X]h` | `[X]%` |
| **#8** | Padronização, Revisão Textual e ODS | Pedro Druck | `[X]h` | `[X]h` | `[X]%` |
| **Total** | — | — | **`[X]h`** | **`[X]h`** | **`[X]%`** |

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
* **Qualidade e Retrabalho:** As revisões cruzadas nos Pull Requests permitiram identificar precocemente ajustes de formatação de diagramas GQM, alinhamento de referências bibliográficas (`.bib`) e padronização terminológica das normas ISO/IEC 25010 e 25040 antes da geração da Release.
* **Ações Corretivas para a Entrega 2 (E2):**
  1. Garantir que PRs de conteúdo documental (`artigo/` e `docs/`) apontem exclusivamente para a `main`, mantendo branches de infraestrutura isoladas.
  2. Registrar as horas reais imediatamente no ato de abertura do Pull Request de cada *issue*, evitando represamento na coleta de métricas de esforço no fechamento da release.