# Relatório de Medição e Governança — Release E1 (Fases 1 e 2)

Este documento consolida os resultados das métricas de gestão do projeto referentes à **Entrega 1 (Release E1)**, fundamentadas no modelo *Practical Software Measurement* (PSM) sob as categorias **CID** (Desempenho de Processos, Calendário e Progresso, e Recursos e Custos).

---

## 1. Resumo dos Indicadores CID

| Categoria CID | Métrica | Sigla | Fórmula | Meta | Valor Obtido | Status |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| **Desempenho** | M-DP1 — Taxa de Retrabalho em PRs | $TR_{PR}$ | $(PR_{ajustes} / PR_{total}) \times 100$ | $\le 30\%$ | 0% | Verde |
| **Calendário** | M-CP1 — Índice de Cumprimento de Marcos | $ICM$ | $(I_{concluidas} / I_{planejadas}) \times 100$ | $\ge 85\%$ | 100% | Verde |
| **Recursos** | M-RC1 — Taxa de Variação de Esforço | $TVE$ | $((H_{reais} - H_{est}) / H_{est}) \times 100$ | $\pm 20\%$ | +10% | Verde |

---

## 2. Detalhamento por Categoria

### 2.1. Desempenho de Processos ($TR_{PR}$)
Avalia a qualidade inicial das entregas submetidas à revisão por pares na branch `main`.
* **Critério (plano PSM/CID):** conta como retrabalho o PR que recebeu *Changes Requested* ou commits depois da primeira revisão.
* **Total de Pull Requests mesclados na `main` até o fechamento da E1 ($PR_{total}$):** 14 (#13, #14, #15, #17, #18, #19, #20, #21, #22, #23, #24, #43, #44 e #50)
* **PRs com *Changes Requested* ou commits pós-revisão ($PR_{ajustes}$):** 0
* **Cálculo:** $TR_{PR} = (0 / 14) \times 100 = 0\%$ (Verde)
* **Observação:** a métrica não capta a espera pela revisão; os PRs #18, #19, #21, #23 e #24 aguardaram de 2 a 7 dias pela aprovação.

### 2.2. Calendário e Progresso ($ICM$)
Mede a aderência ao cronograma planejado para a Release E1 (Fases 1 e 2 da ISO/IEC 25040). As métricas incluem a *issue* agregadora (#2) e as tarefas secundárias de retrabalho exigidas para atingir a meta (#25, #26, #45).
* **Issues planejadas para a Release E1 ($I_{planejadas}$):** 15 (#1 a #12, #25, #26 e #45; a #27 foi fechada como duplicada da #2 e não entra na conta)
* **Issues concluídas até o fechamento da Release ($I_{concluidas}$):** 15
* **Cálculo:** $ICM = (15 / 15) \times 100 = 100\%$ (Verde)

### 2.3. Recursos e Custos ($TVE$ e $PCI_i$)
Compara o esforço planejado com o esforço real reportado nas *issues* do GitHub e consolida o percentual de contribuição individual ($PCI_i$).

#### Esforço por Integrante
Horas registradas no campo *Horas reais executadas* de cada *issue* da E1 (atualizado em 26/10/2026). A #25, compartilhada pelos seis integrantes, teve sua 1 h dividida igualmente; a #27, fechada como duplicada da #2, não entra na conta.

| Integrante (Responsável) | Horas Estimadas ($H_{est}$) | Horas Reais Executadas ($H_{reais}$) | Variação (%) | Issues |
| :--- | :---: | :---: | :---: | :---: |
| Daniel de Oliveira Lira | 8,2h | 10,2h | +24,5% | 3 |
| Heitor Macedo Ricardo | 8,2h | 10,2h | +24,5% | 3 |
| Hugo Freitas Silva | 7,2h | 7,2h | 0% | 3 |
| Pedro Druck Montalvão Reis | 9,2h | 10,2h | +10,9% | 4 |
| Pedro Henrique Ferreira Xavier | 9,2h | 8,2h | −10,9% | 4 |
| Philipe Amâncio Reis Caetano | 8,2h | 9,2h | +12,2% | 3 |
| **Total Global** | **50h** | **55h** | **+10%** | **15** |

*Cálculo da Taxa de Variação de Esforço:* $TVE = ((55 - 50) / 50) \times 100 = +10\%$ (Verde, dentro de $\pm 20\%$). Individualmente, Daniel e Heitor ficaram em +24,5% (Amarelo).

#### Percentual de Contribuição Individual ($PCI_i$)
O $PCI_i$ medido segue o plano ($PCI_i = H_{reais,i} / \sum H_{reais} \times 100$), com as horas da tabela anterior. A contribuição final publicada no apêndice do artigo é uma decisão de gestão: a equipe atribuiu 16,67% a cada integrante, porque a contribuição também inclui atividades que não aparecem diretamente nas métricas do GitHub, como a revisão do trabalho dos colegas, o retorno dado a cada entrega e a organização da equipe.

| Integrante | Papel Principal na E1 | $PCI_i$ medido (horas) | Contribuição final (decisão da equipe) |
| :--- | :--- | :---: | :---: |
| Daniel de Oliveira Lira | Gestão do repositório, integração, Metodologia e métricas CID | 18,5% | 16,67% |
| Heitor Macedo Ricardo | Definição de propósito, restrições, escopo, Introdução e GitPage | 18,5% | 16,67% |
| Hugo Freitas Silva | Revisão técnica, testes locais e validação de Pull Requests | 13,0% | 16,67% |
| Pedro Druck Montalvão Reis | Revisão ortográfica, padronização e enquadramento ODS | 18,5% | 16,67% |
| Pedro Henrique Ferreira Xavier | Definição de métricas GQM, hipóteses e estruturação da Fase 2 | 14,8% | 16,66% |
| Philipe Amâncio Reis Caetano | Elaboração da abordagem GQM e geração de diagramas e tabelas | 16,7% | 16,66% |
| **Total** | — | **100,0%** | **100,00%** |

---

## 3. Análise Gerencial e Decisões Tomadas

* **Gargalos Identificados:** Durante a execução da Entrega 1, verificou-se colisão temporal entre branches (arquivos da Fase 1 retidos na branch da GitPage) e dependência sequencial na etapa final de integração do artigo LaTeX para execução da revisão ortográfica completa.
* **Qualidade e Retrabalho:** O modelo impôs a adoção de ações corretivas. O estouro do limite de páginas e inconsistências nas métricas (ex.: Hipótese H1.1) forçaram a abertura imediata de sub-issues corretivas de alta prioridade (#26, #45). Esses ajustes foram tratados como issues próprias, e não como correções dentro dos PRs: nenhum PR recebeu pedido de ajustes ou commits após a revisão ($TR_{PR} = 0\%$). O gargalo do processo foi a espera pela revisão, de até 7 dias, e não o retrabalho.
* **Esforço e Planeamento:** A Taxa de Variação de Esforço global foi de +10% (Verde). Os maiores desvios individuais foram de Daniel e Heitor (+24,5%, Amarelo), concentrados na configuração do repositório (#1) e na seção de propósito e na GitPage (#3 e #4). Pelas horas, o PCI de Hugo (13,0%) ficaria na faixa Amarela do plano. A equipe avaliou que as horas não captam a revisão do trabalho dos colegas, o retorno dado a cada entrega e a organização da equipe, e decidiu atribuir contribuição igual (16,67%) a todos os integrantes.
* **Ações Corretivas para a Entrega 2 (E2):**
  1. Garantir que PRs de conteúdo documental (`artigo/` e `docs/`) apontem exclusivamente para a `main`, mantendo branches de infraestrutura isoladas.
  2. Aumentar a margem de segurança do planeamento (+20%) para a absorção da curva de aprendizagem das ferramentas de testes empíricos de desempenho da Fase 3.
  3. Registrar as horas reais imediatamente no ato de abertura do Pull Request de cada *issue*, evitando represamento na coleta de métricas de esforço no fechamento da release.