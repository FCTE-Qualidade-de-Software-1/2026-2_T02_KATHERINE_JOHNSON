# Avaliação Comparativa de Qualidade em Serviços Digitais de Governo: Portal de Serviços × Aplicativo na Consulta de Infrações do Detran-DF

Este site apresenta o Projeto Final da disciplina FGA0315 Qualidade de Software 1
(Engenharia de Software, UnB/FGA, semestre 2026/2), desenvolvido pela equipe Katherine Johnson.

<div class="kj-destaques">
<a class="kj-destaque" href="#cadeia">
<span class="kj-destaque__rotulo">Explore a avaliação</span>
<span class="kj-destaque__titulo">Cadeia da avaliação, da Fase 1 à Fase 4</span>
<span class="kj-destaque__texto">Diagramas clicáveis ligam cada uma das 14 métricas à característica, à questão, à hipótese, ao procedimento de coleta e à observação registrada.</span>
<span class="kj-destaque__acao">Ver os diagramas</span>
</a>
<a class="kj-destaque" href="#evidencias">
<span class="kj-destaque__rotulo">Dados e provas</span>
<span class="kj-destaque__titulo">Evidências das coletas</span>
<span class="kj-destaque__texto">Registros das seis sessões de 21 e 22/11/2026, capturas anonimizadas, dados brutos em CSV e desvios, organizados por sessão.</span>
<span class="kj-destaque__acao">Ver as evidências</span>
</a>
</div>

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

<div class="kj-painel" markdown>

## Cadeia da avaliação, da Fase 1 à Fase 4 {#cadeia}

Cada diagrama mostra, para um objetivo, como a característica escolhida na Fase 1 leva às
questões e hipóteses, às métricas, aos procedimentos de coleta e às observações da Fase 4. As
cores identificam a fase de cada elemento. Cada nó é um link para a seção correspondente:
clique nele ou percorra os nós com a tecla Tab e abra com Enter. Em telas estreitas, os
diagramas rolam na horizontal.

**Alternativa em texto:** a mesma cadeia está em tabelas na página de
[rastreabilidade](rastreabilidade.md), com uma linha por métrica.

<ul class="kj-legenda" aria-label="Cores por fase">
<li><span class="kj-legenda__cor kj-legenda__cor--f1"></span>Fase 1: característica e decisões</li>
<li><span class="kj-legenda__cor kj-legenda__cor--f2"></span>Fase 2: objetivo, questões e métricas</li>
<li><span class="kj-legenda__cor kj-legenda__cor--f3"></span>Fase 3: procedimentos e arquivos de dados</li>
<li><span class="kj-legenda__cor kj-legenda__cor--f4"></span>Fase 4: sessões e observações</li>
</ul>

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
    class C,D kjf1
    class G kjobj
    class Q11,Q12,Q13 kjq
    class M111,M112,M121,M122,M131,M132 kjm
    class P1,P2,P3,AP1,AP2,AP3 kjf3
    class R1 kjf4
    class F1 kjg1
    class F2 kjg2
    class F3 kjg3
    class F4 kjg4
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
    class C,D kjf1
    class G kjobj
    class Q21,Q22 kjq
    class M211,M212,M221 kjm
    class P4,P5,AP4,AP5 kjf3
    class R1 kjf4
    class F1 kjg1
    class F2 kjg2
    class F3 kjg3
    class F4 kjg4
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
    class C,D kjf1
    class G kjobj
    class Q31,Q32 kjq
    class M311,M312,M321,M322,M323 kjm
    class P6,P7,AP6,AP7 kjf3
    class R1,R2 kjf4
    class F1 kjg1
    class F2 kjg2
    class F3 kjg3
    class F4 kjg4
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
    click R2 href "fase4-analise/#resultados-p7"
```

*Figura 3 — Cadeia do objetivo G3, da Fase 1 à Fase 4. Alternativa em texto: [linhas de G3 na rastreabilidade](rastreabilidade.md#rt-g3). Fonte: elaborada pela equipe a partir das Fases 1 a 4.*


</div>

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
   [ação de melhoria](fase4-melhoria.md) (Entrega 2; resultados elegíveis conferidos, calculados
   e julgados por questão, objetivo e canal; lacunas de contexto permanecem explícitas).

A execução do projeto é acompanhada com métricas PSM/CID, descritas em
[Gestão](gestao.md), e as decisões da equipe ficam registradas nas [Atas](atas.md).

## Situação atual

A **Entrega 1** (Fases 1 e 2) foi concluída em 26/10/2026; a versão entregue, com o PDF do artigo,
está em [Releases](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/releases). As Fases 3 e 4 fazem parte da Entrega 2: o plano da Fase 3 foi executado em seis sessões de coleta (S01, S02, S03, S05, S06 e S08, em 21 e 22/11/2026). As segundas leituras elegíveis foram concluídas, os níveis calculados e as respostas GQM registradas. A adequação funcional não foi atendida; a eficiência de desempenho permanece inconclusiva pela não equivalência dos instrumentos de volume; a cobertura foi atendida no portal nos contextos medidos e não atendida no escopo observado para o aplicativo. Permanecem as lacunas do aplicativo na rede degradada e do contexto CT04. O andamento das tarefas pode ser acompanhado no
[quadro do backlog](https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/38) (acesso restrito aos membros da organização; as
[issues](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues) e os [milestones](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/milestones) são públicos).

<div class="kj-painel" markdown>

## Onde estão as evidências {#evidencias}

As evidências das coletas ficam no repositório, em [`evidencias/fase4/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase4)
(registros de sessão e capturas anonimizadas) e em [`dados/brutos/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/dados/brutos) (valores
registrados em CSV). A Tabela 1 indica onde está o material de cada sessão.

| Sessão e data | Procedimentos e caso | Registro da sessão | Capturas anonimizadas | Dados brutos |
|---|---|---|---|---|
| S01, 22/11 (piloto) | Telas e instrumentos; V2, com telas de V1 e V5 | [Registro da S01](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/S01-registro-2026-11-22.md) | 11 telas do portal, do Android e do iOS: [capturas da S01](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase4/capturas/S01) | Não entra no cálculo |
| S02, 22/11 | P1 a P3; V2 | [Registro da S02](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/S02-registro-2026-11-22.md); [segunda leitura](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/S02-segunda-leitura-2026-11-23.md) | Lista e detalhe nos dois canais: [capturas da S02](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase4/capturas/S02) | [`campos-por-infracao.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/campos-por-infracao.csv), [`comparacao-canais.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/comparacao-canais.csv), [`fluxo.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/fluxo.csv) |
| S03, 21/11 | P6 (CT01, CT03 e CT05); V1 | [Registro da S03](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/S03-registro-2026-11-21.md) | 9 tentativas: [capturas da S03](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase4/capturas/S03) (blocos B01 a B03) | [`tentativas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/tentativas.csv) |
| CT06, 22/11 | P6 no iOS; V5 | [Registro do CT06](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/S03-CT06-iphone-registro-2026-11-22.md) | 2 telas na pasta da S03 (bloco B04) | [`tentativas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/tentativas.csv) |
| S05, 22/11 | P6 (CT05, CT02 e CT01); V2 | [Registro da S05](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/S05-registro-2026-11-22.md) | 9 tentativas: [capturas da S05](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase4/capturas/S05) | [`tentativas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/tentativas.csv) |
| S06, 22/11 | P4 e P5; V4 | [Registro da S06](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/S06-registro-2026-11-22.md) | Gravações e leituras em armazenamento privado, sem captura pública | [`tempos.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/tempos.csv), [`volume.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/volume.csv) |
| S08, 22/11 | P7; V4 | [Registro da S08](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/S08-registro-2026-11-22.md) | Gravações em armazenamento privado, sem captura pública | [`tentativas.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/tentativas.csv), [`tempos.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/tempos.csv) |

*Tabela 1 — Evidências das coletas por sessão. Fonte: `evidencias/fase4/` e `dados/brutos/`.*

Mudanças em relação ao plano estão em [`desvios.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/desvios.csv), e o ambiente
de cada sessão em [`ambientes.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/brutos/ambientes.csv). Originais, vídeos sem tarja e
termos assinados ficam em armazenamento privado, com acesso restrito aos avaliadores.

### Outros materiais

- [Repositório do projeto](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON)
- [Releases](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/releases) — versões entregues, com o PDF do artigo
- [Artigo em LaTeX](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/artigo)
- [Plano de gestão PSM/CID](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/gestao)
- [Atas de reunião](atas.md)
- [Slides do Ponto de Controle 1 (PDF, 19/10/2026)](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/slides/ponto-de-controle-1-2026-10-19.pdf)
- [Evidências do levantamento da Fase 1](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase1)
- [Dados da avaliação e termo de consentimento](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/dados)
- [Registro de horas por issue](gestao-horas.md)

</div>

Dados pessoais de condutores e veículos usados na avaliação não são publicados. Prints e
registros aparecem anonimizados, com códigos como "Veículo V1".
