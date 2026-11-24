# Avaliação Comparativa de Qualidade em Serviços Digitais de Governo: Portal de Serviços × Aplicativo na Consulta de Infrações do Detran-DF

Este site apresenta o Projeto Final da disciplina FGA0315 Qualidade de Software 1
(Engenharia de Software, UnB/FGA, semestre 2026/2), desenvolvido pela equipe Katherine Johnson.

## O que está sendo avaliado

O projeto avalia a qualidade da **consulta de infrações de trânsito** oferecida pelo Detran-DF
em dois canais: o **Portal de Serviços**, acessado pelo navegador, e o **aplicativo** oficial
para Android e iOS. O objetivo é comparar os dois canais quanto às mesmas características de
qualidade, usando apenas medições externas, observáveis por quem usa o serviço (avaliação
caixa-preta).

As características avaliadas são:

| Característica | Modelo de referência |
|---|---|
| Adequação funcional | ISO/IEC 25010:2023 (qualidade do produto) |
| Eficiência de desempenho | ISO/IEC 25010:2023 (qualidade do produto) |
| Cobertura de contexto | ISO/IEC 25010:2011 (qualidade em uso) e ISO/IEC 25022:2016 |

## Como o trabalho está organizado

A avaliação segue o processo de avaliação de produto da ISO/IEC 25040, dividido em quatro fases.
A [Metodologia](metodologia.md) descreve o método em visão geral e o passo a passo de cada fase.

1. **[Fase 1](fase1.md)** — estabelecer os requisitos da avaliação: propósito, partes
   interessadas, descrição do produto, modelo de qualidade, priorização e escopo.
2. **[Fase 2](fase2.md)** — especificar a avaliação com o método GQM: objetivos, questões,
   hipóteses, métricas, níveis de pontuação e critérios de julgamento.
3. **[Fase 3](fase3.md)** — plano de avaliação: método, ambiente, massa de dados e cronograma
   (plano executado em seis sessões de coleta, em 21 e 22/11/2026).
4. **[Fase 4](fase4.md)** — executar a avaliação e julgar os resultados, com a
   [ação de melhoria](fase4-melhoria.md) (Entrega 2; valores de primeira leitura, com segunda
   leitura independente concluída só para P1 a P3 da S02 e, por isso, sem níveis de pontuação).

A execução do projeto é acompanhada com métricas PSM/CID, descritas em
[Gestão](gestao.md), e as decisões da equipe ficam registradas nas [Atas](atas.md).

## Cadeia da avaliação, da Fase 1 à Fase 4 {#cadeia}

Os três diagramas abaixo mostram, para cada objetivo, como a característica escolhida na Fase 1
leva às questões e hipóteses, às métricas, aos procedimentos de coleta e às observações da
Fase 4. Cada nó é um link para a seção correspondente: clique nele ou percorra os nós com a
tecla Tab e abra com Enter. Os diagramas podem ser rolados na horizontal em telas estreitas.
**Alternativa em texto:** a mesma cadeia está em tabelas na página de
[rastreabilidade](rastreabilidade.md), com uma linha por métrica.

### G1 — Adequação funcional {#cadeia-g1}

```mermaid-cadeia
flowchart LR
    accTitle: Cadeia do objetivo G1, adequação funcional
    accDescr: A característica adequação funcional da Fase 1 e as decisões D1 e D2 levam ao objetivo G1, às questões Q1.1, Q1.2, Q1.3 com suas hipóteses, às métricas M1.1.1, M1.1.2, M1.2.1, M1.2.2, M1.3.1, M1.3.2, aos procedimentos P1, P2, P3, aos arquivos de dados e às observações da Fase 4. Cada nó é um link para a seção correspondente.
    subgraph F1["Fase 1"]
        C["Adequação funcional"]
        D["Decisões D1 e D2"]
    end
    subgraph F2["Fase 2"]
        G["G1"]
        Q11["Q1.1 e H1.1<br/>Completude funcional"]
        Q12["Q1.2 e H1.2<br/>Consistência funcional"]
        Q13["Q1.3 e H1.3<br/>Adequação das operações"]
        M111["M1.1.1<br/>Campos na lista"]
        M112["M1.1.2<br/>Campos no detalhe"]
        M121["M1.2.1<br/>Campos consistentes"]
        M122["M1.2.2<br/>Infrações sem divergência"]
        M131["M1.3.1<br/>Passos até a lista"]
        M132["M1.3.2<br/>Transições de tela"]
    end
    subgraph F3["Fase 3"]
        P1["P1<br/>Registro de campos"]
        P2["P2<br/>Comparação entre canais"]
        P3["P3<br/>Contagem do fluxo"]
        AP1["campos-por-infracao.csv"]
        AP2["comparacao-canais.csv"]
        AP3["fluxo.csv"]
    end
    subgraph F4["Fase 4"]
        R1["S02: P1 a P3, caso V2"]
    end
    C --> G
    D --> G
    G --> Q11
    G --> Q12
    G --> Q13
    Q11 --> M111
    M111 --> P1
    Q11 --> M112
    M112 --> P1
    Q12 --> M121
    M121 --> P2
    Q12 --> M122
    M122 --> P2
    Q13 --> M131
    M131 --> P3
    Q13 --> M132
    M132 --> P3
    P1 --> AP1
    P2 --> AP2
    P3 --> AP3
    AP1 --> R1
    AP2 --> R1
    AP3 --> R1
    click C href "fase1-priorizacao/#resultado-priorizacao"
    click D href "fase1-proposito/#decisoes"
    click G href "fase2-gqm/#g1"
    click Q11 href "fase2-gqm/#q1-1"
    click Q12 href "fase2-gqm/#q1-2"
    click Q13 href "fase2-gqm/#q1-3"
    click M111 href "fase2-metricas/#m1-1-1"
    click M112 href "fase2-metricas/#m1-1-2"
    click M121 href "fase2-metricas/#m1-2-1"
    click M122 href "fase2-metricas/#m1-2-2"
    click M131 href "fase2-metricas/#m1-3-1"
    click M132 href "fase2-metricas/#m1-3-2"
    click P1 href "fase3-metodo/#p1"
    click P2 href "fase3-metodo/#p2"
    click P3 href "fase3-metodo/#p3"
    click AP1 href "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/campos-por-infracao.csv"
    click AP2 href "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/comparacao-canais.csv"
    click AP3 href "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/fluxo.csv"
    click R1 href "fase4-analise/#resultados-s02"
```

*Figura 1 — Cadeia do objetivo G1, da Fase 1 à Fase 4. Alternativa em texto: [linhas de G1 na rastreabilidade](rastreabilidade.md#rt-g1). Fonte: elaborada pela equipe a partir das Fases 1 a 4.*

### G2 — Eficiência de desempenho {#cadeia-g2}

```mermaid-cadeia
flowchart LR
    accTitle: Cadeia do objetivo G2, eficiência de desempenho
    accDescr: A característica eficiência de desempenho da Fase 1 e as decisões D1 e D3 levam ao objetivo G2, às questões Q2.1, Q2.2 com suas hipóteses, às métricas M2.1.1, M2.1.2, M2.2.1, aos procedimentos P4, P5, aos arquivos de dados e às observações da Fase 4. Cada nó é um link para a seção correspondente.
    subgraph F1["Fase 1"]
        C["Eficiência de desempenho"]
        D["Decisões D1 e D3"]
    end
    subgraph F2["Fase 2"]
        G["G2"]
        Q21["Q2.1 e H2.1<br/>Comportamento temporal"]
        Q22["Q2.2 e H2.2<br/>Utilização de recursos de rede"]
        M211["M2.1.1<br/>Tempo até a lista"]
        M212["M2.1.2<br/>Tempo até o detalhe"]
        M221["M2.2.1<br/>Volume transferido"]
    end
    subgraph F3["Fase 3"]
        P4["P4<br/>Medição de tempo"]
        P5["P5<br/>Medição de volume"]
        AP4["tempos.csv"]
        AP5["volume.csv"]
    end
    subgraph F4["Fase 4"]
        R1["S06: P4 e P5, caso V4"]
    end
    C --> G
    D --> G
    G --> Q21
    G --> Q22
    Q21 --> M211
    M211 --> P4
    Q21 --> M212
    M212 --> P4
    Q22 --> M221
    M221 --> P5
    P4 --> AP4
    P5 --> AP5
    AP4 --> R1
    AP5 --> R1
    click C href "fase1-priorizacao/#resultado-priorizacao"
    click D href "fase1-proposito/#decisoes"
    click G href "fase2-gqm/#g2"
    click Q21 href "fase2-gqm/#q2-1"
    click Q22 href "fase2-gqm/#q2-2"
    click M211 href "fase2-metricas/#m2-1-1"
    click M212 href "fase2-metricas/#m2-1-2"
    click M221 href "fase2-metricas/#m2-2-1"
    click P4 href "fase3-metodo/#p4"
    click P5 href "fase3-metodo/#p5"
    click AP4 href "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/tempos.csv"
    click AP5 href "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/volume.csv"
    click R1 href "fase4-analise/#resultados-v4"
```

*Figura 2 — Cadeia do objetivo G2, da Fase 1 à Fase 4. Alternativa em texto: [linhas de G2 na rastreabilidade](rastreabilidade.md#rt-g2). Fonte: elaborada pela equipe a partir das Fases 1 a 4.*

### G3 — Cobertura de contexto {#cadeia-g3}

```mermaid-cadeia
flowchart LR
    accTitle: Cadeia do objetivo G3, cobertura de contexto
    accDescr: A característica cobertura de contexto da Fase 1 e as decisões D1, D3 e D4 levam ao objetivo G3, às questões Q3.1, Q3.2 com suas hipóteses, às métricas M3.1.1, M3.1.2, M3.2.1, M3.2.2, M3.2.3, aos procedimentos P6, P7, aos arquivos de dados e às observações da Fase 4. Cada nó é um link para a seção correspondente.
    subgraph F1["Fase 1"]
        C["Cobertura de contexto"]
        D["Decisões D1, D3 e D4"]
    end
    subgraph F2["Fase 2"]
        G["G3"]
        Q31["Q3.1 e H3.1<br/>Completude de contexto"]
        Q32["Q3.2 e H3.2<br/>Flexibilidade em rede degradada"]
        M311["M3.1.1<br/>Conclusão por plataforma"]
        M312["M3.1.2<br/>Conclusão por navegador"]
        M321["M3.2.1<br/>Conclusão por rede"]
        M322["M3.2.2<br/>Falhas ou expiração"]
        M323["M3.2.3<br/>Tempo por rede"]
    end
    subgraph F3["Fase 3"]
        P6["P6<br/>Execução por contexto"]
        P7["P7<br/>Execução por condição de rede"]
        AP6["tentativas.csv"]
        AP7["tentativas.csv e tempos.csv"]
    end
    subgraph F4["Fase 4"]
        R1["S03, S05 e CT06: P6"]
        R2["S08: P7, caso V4"]
    end
    C --> G
    D --> G
    G --> Q31
    G --> Q32
    Q31 --> M311
    M311 --> P6
    Q31 --> M312
    M312 --> P6
    Q32 --> M321
    M321 --> P7
    Q32 --> M322
    M322 --> P7
    Q32 --> M323
    M323 --> P7
    P6 --> AP6
    P7 --> AP7
    AP6 --> R1
    AP7 --> R2
    click C href "fase1-priorizacao/#resultado-priorizacao"
    click D href "fase1-proposito/#decisoes"
    click G href "fase2-gqm/#g3"
    click Q31 href "fase2-gqm/#q3-1"
    click Q32 href "fase2-gqm/#q3-2"
    click M311 href "fase2-metricas/#m3-1-1"
    click M312 href "fase2-metricas/#m3-1-2"
    click M321 href "fase2-metricas/#m3-2-1"
    click M322 href "fase2-metricas/#m3-2-2"
    click M323 href "fase2-metricas/#m3-2-3"
    click P6 href "fase3-metodo/#p6"
    click P7 href "fase3-metodo/#p7"
    click AP6 href "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/tentativas.csv"
    click AP7 href "https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/tentativas.csv"
    click R1 href "fase4-analise/#resultados-p6"
    click R2 href "fase4-analise/#resultados-v4"
```

*Figura 3 — Cadeia do objetivo G3, da Fase 1 à Fase 4. Alternativa em texto: [linhas de G3 na rastreabilidade](rastreabilidade.md#rt-g3). Fonte: elaborada pela equipe a partir das Fases 1 a 4.*

## Situação atual

A **Entrega 1** (Fases 1 e 2) foi concluída em 26/10/2026; a versão entregue, com o PDF do artigo,
está em [Releases](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/releases). As Fases 3 e 4 fazem parte da Entrega 2: o plano da Fase 3 foi executado em seis sessões de coleta (S01, S02, S03, S05, S06 e S08, em 21 e 22/11/2026) e a Fase 4 traz os valores observados, a análise e a ação de melhoria entregue. Os valores são de primeira leitura, a conferência independente está concluída apenas para P1 a P3 da S02 (uma rolagem do P3 segue pendente) e os objetivos de medição permanecem inconclusivos; as lacunas (aplicativo na rede degradada e contexto CT04) estão declaradas. O andamento das tarefas pode ser acompanhado no
[quadro do backlog](https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/38) (acesso restrito aos membros da organização; as
[issues](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues) e os [milestones](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/milestones) são públicos).

## Onde estão as evidências

- [Repositório do projeto](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON)
- [Releases](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/releases) — versões entregues, com o PDF do artigo
- [Artigo em LaTeX](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/artigo)
- [Plano de gestão PSM/CID](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/gestao)
- [Atas de reunião](atas.md)
- [Slides do Ponto de Controle 1 (PDF, 19/10/2026)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/slides/ponto-de-controle-1-2026-10-19.pdf)
- [Evidências do levantamento da Fase 1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase1)
- [Evidências e registro de sessão da Fase 4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase4)
- [Dados da avaliação e termo de consentimento](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/dados)
- [Registro de horas por issue](gestao-horas.md)

Dados pessoais de condutores e veículos usados na avaliação não são publicados. Prints e
registros aparecem anonimizados, com códigos como "Veículo V1".
