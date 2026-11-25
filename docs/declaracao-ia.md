# Declaração de Uso de Ferramentas de Inteligência Artificial

**Projeto Final FGA0315 Qualidade de Software 1 (UnB/FGA, 2026/2)**  
*Avaliação da consulta de infrações do Detran-DF: Portal de Serviços × aplicativo*  
*Responsável pela consolidação: Pedro Henrique*

---

## 1. Diretrizes de Uso Ético e Transparência

Em atendimento aos critérios C10, F2-C9 e AG-C3 da disciplina FGA0315, a equipe Katherine Johnson registra o uso de ferramentas de inteligência artificial e os procedimentos de verificação adotados em cada entrega.

**Compromissos assumidos por todos os membros da equipe:**
1. Nenhuma decisão metodológica, julgamento de qualidade ou definição de métrica foi terceirizada sem validação técnica crítica;
2. Todas as informações normativas (ISO/IEC 25010, ISO/IEC 25040, ISO/IEC/IEEE 15939) e legais (Código de Trânsito Brasileiro) foram conferidas diretamente em suas fontes primárias oficiais;
3. Textos gerados foram exaustivamente revisados, expurgando jargões descontextualizados, inconsistências conceituais e qualquer elemento informal (como emojis, ícones ou figuras meramente decorativas);
4. Toda citação direta ou paráfrase baseou-se em bibliografia acadêmica reconhecida e indexada no arquivo de referências BibTeX.

---

## 2. Declaração da Entrega 2 (AG-C3)

Na Entrega 2, a equipe Katherine Johnson usou ferramentas de inteligência artificial como apoio à
preparação dos roteiros e instrumentos de coleta da Fase 3 e à organização dos registros e à
revisão do artigo e da GitPage na Fase 4. A IA também auxiliou na documentação da gestão do
projeto e na elaboração da proposta de melhoria.

Os integrantes conduziram ou supervisionaram as sessões de avaliação da consulta de infrações no
Portal de Serviços e no aplicativo do Detran-DF. A equipe definiu o método, conferiu as evidências e
interpretou os resultados segundo os critérios GQM. Na sessão S02, por exemplo, um segundo integrante
fez uma leitura independente das capturas de tela, das gravações e dos demais registros originais
para conferir os resultados de P1 a P3.
O [registro da segunda leitura no PR #77](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/77)
documenta a conferência e a divergência identificada.

### Usos registrados na Entrega 2

| Registro | Ferramenta | Tarefa | Conferência registrada |
|---|---|---|---|
| Heitor | Claude Code | Apoio aos registros de gestão, à redação da GitPage e dos slides de PSM/CID, à documentação da coleta em iOS e à estimativa das próprias horas. | Conferiu os registros nas issues, nos PRs, no histórico de commits e nas atas. Conferiu as descrições das imagens uma a uma, forneceu os dados da coleta em iOS e revisou e aceitou a estimativa de horas. |
| Heitor (GitPage, 23/11) | Claude Code | Mapeamento das páginas da GitPage em busca de contradições, correção de situações desatualizadas e de termos fora do padrão, tarjas adicionais em três capturas da Fase 1, página de rastreabilidade, âncoras estáveis, diagramas clicáveis na página inicial e ajustes de acessibilidade. | Heitor decidiu o tratamento das contradições, das tarjas e dos termos; os pontos que dependem da equipe ficaram sinalizados, sem decisão da ferramenta. Os vínculos da rastreabilidade foram conferidos contra as Fases 1 a 4; a construção do site com `mkdocs build --strict` e a verificação dos links e âncoras não apontaram erros. |
| Hugo (GitPage, artigo e revisões, 24/11) | Claude Code | Página de medições por métrica gerada a partir dos CSV, com links para as linhas dos dados, gráficos dos tempos e ligação entre as fases ([PR #93](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/93)); atualização de situações desatualizadas; ajuste de Q2.2 e G2 à regra da Fase 2; corte da tabela de métricas repetida pelo diagrama GQM para o artigo voltar às 15 páginas; identificação da versão no artigo; apoio à revisão dos PRs #89 e #92 e à resposta sobre a gestão. | Hugo pediu e acompanhou cada etapa e decidiu as mudanças. O ajuste de G2 foi justificado no PR #93 e aprovado por Pedro Druck. `calcular.py` reproduz os 47 resultados oficiais; os testes de `dados/tests`, o `mkdocs build --strict`, a verificação dos links e o `validar_pdf.py` passaram. |
| Registros técnicos da equipe | Codex (OpenAI) | Apoio aos roteiros e modelos de coleta e análise (#46 e #48), à documentação da proposta de melhoria (#36), à atualização do artigo e à preparação desta declaração. | Cotejo com as fases anteriores, os dados disponíveis e os registros no GitHub, além das verificações de compilação e do PDF. A revisão da declaração pela equipe é acompanhada na [issue #49](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/49). |

### Declarações individuais da Entrega 2

Declarações dadas pelas próprias pessoas em 23 e 24/11/2026, registradas como indicado em cada uma.

#### Heitor — 23/11/2026

> Declaro que foram utilizadas ferramentas de Inteligência Artificial, como o ChatGPT e o Claude, como recursos auxiliares durante o desenvolvimento deste trabalho. Essas ferramentas foram empregadas para apoiar a pesquisa, esclarecer conceitos, organizar ideias e auxiliar na revisão e elaboração de textos. Todo o conteúdo gerado foi analisado, revisado e adaptado, sendo o autor responsável pela verificação das informações e pela versão final do trabalho.

#### Philipe — 23/11/2026

*Declaração dada verbalmente a Heitor, que a registrou a pedido porque Philipe estava sem computador. O texto-base é o da declaração de Heitor, que Philipe aprovou como sua em 23/11/2026; a confirmação fica registrada em comentário da própria pessoa no PR.*

> Declaro que foram utilizadas ferramentas de Inteligência Artificial, como o ChatGPT e o Claude, como recursos auxiliares durante o desenvolvimento deste trabalho. Essas ferramentas foram empregadas para apoiar a pesquisa, esclarecer conceitos, organizar ideias e auxiliar na revisão e elaboração de textos. Todo o conteúdo gerado foi analisado, revisado e adaptado, sendo o autor responsável pela verificação das informações e pela versão final do trabalho.


#### Pedro Henrique — 23/11/2026

*Declaração dada verbalmente a Heitor, que a registrou a pedido porque Pedro Henrique estava sem computador. O texto-base é o da declaração de Heitor, que Pedro Henrique aprovou como sua em 23/11/2026; a confirmação fica registrada em comentário da própria pessoa no PR.*

> Declaro que foram utilizadas ferramentas de Inteligência Artificial, como o ChatGPT e o Claude, como recursos auxiliares durante o desenvolvimento deste trabalho. Essas ferramentas foram empregadas para apoiar a pesquisa, esclarecer conceitos, organizar ideias e auxiliar na revisão e elaboração de textos. Todo o conteúdo gerado foi analisado, revisado e adaptado, sendo o autor responsável pela verificação das informações e pela versão final do trabalho.

#### Daniel — 23/11/2026

*Declaração dada verbalmente a Heitor, que a registrou a pedido. O texto-base é o da declaração de Heitor, que Daniel autorizou usar como sua em 23/11/2026; a confirmação fica registrada em comentário da própria pessoa no PR.*

> Declaro que foram utilizadas ferramentas de Inteligência Artificial, como o ChatGPT e o Claude, como recursos auxiliares durante o desenvolvimento deste trabalho. Essas ferramentas foram empregadas para apoiar a pesquisa, esclarecer conceitos, organizar ideias e auxiliar na revisão e elaboração de textos. Todo o conteúdo gerado foi analisado, revisado e adaptado, sendo o autor responsável pela verificação das informações e pela versão final do trabalho.

#### Pedro Druck — 24/11/2026

*Declaração confirmada por Pedro Druck por mensagem em 24/11/2026, com o mesmo texto-base das demais; a confirmação foi registrada por Philipe na aprovação do [PR #96](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/96).*

> Declaro que foram utilizadas ferramentas de Inteligência Artificial, como o ChatGPT e o Claude, como recursos auxiliares durante o desenvolvimento deste trabalho. Essas ferramentas foram empregadas para apoiar a pesquisa, esclarecer conceitos, organizar ideias e auxiliar na revisão e elaboração de textos. Todo o conteúdo gerado foi analisado, revisado e adaptado, sendo o autor responsável pela verificação das informações e pela versão final do trabalho.

## 3. Registro individual da Entrega 1

A Tabela abaixo documenta pormenorizadamente a ferramenta empregada, a finalidade específica e o procedimento de auditoria e ajuste humano realizado por cada integrante da equipe.

| Integrante | Ferramenta e Versão | Tarefa Específica Executada | Procedimento de Verificação e Ajuste Humano |
|---|---|---|---|
| **Daniel** | Claude Sonnet 5.5 / ChatGPT | Auxílio na elaboração da estrutura da Seção Metodologia e na automação de tarefas no Git | Revisão manual do fluxo de fases da ISO/IEC 25040, validação das fórmulas de métricas PSM/CID e adequação às regras do repositório. |
| **Heitor** | Claude Sonnet 5.5 | Estruturação inicial do texto de introdução, tabela de partes interessadas e configuração MkDocs | Checagem de conformidade com os objetivos reais do Detran-DF, verificação dos critérios de sucesso por parte interessada e remoção de elementos visuais incompatíveis. |
| **Hugo** | Claude Code (Claude Opus 5.5) | Apoio na organização do levantamento público dos canais e na revisão do texto da descrição do produto, do modelo de qualidade e dos diagramas | Levantamento e redação feitos pelo autor; dados conferidos nas telas públicas do portal, nas lojas de aplicativos, no CTB e na ISO/IEC 25010:2023. Limitação da Entrega 1: campos que dependem de login serão conferidos na Fase 3. |
| **Pedro Druck** | Claude Sonnet 5.5 | Apoio na estruturação da matriz de priorização de características e síntese da família ISO/IEC 25000 | Verificação dos textos oficiais das metas dos ODS (ONU/IBGE) e conferência pontual das subcaracterísticas presentes na versão ISO/IEC 25010:2023. |
| **Pedro Henrique** | Claude Sonnet 5.5 | Elaboração do rascunho dos objetivos no template GQM, formulação das hipóteses e referencial teórico GQM/PSM | Auditoria minuciosa para garantir ausência de termos de usabilidade (proibida pela professora); reestruturação das questões para eliminar métricas disfarçadas; checagem das citações bibliográficas de Basili et al. (1994) e McGarry et al. (2002); validação de consistência dos slides em Beamer. |
| **Philipe** | Claude Sonnet 5.5 | Estruturação tabular das fichas de métricas e formulação preliminar dos níveis de pontuação | Conferência manual da viabilidade de coleta em caixa-preta sem acesso ao código-fonte; ajuste dos limiares de julgamento conforme referências técnicas de mercado. |

**Fonte:** elaborada pela equipe com base nas declarações individuais de uso de ferramentas de inteligência artificial.

---

*Declaração da Entrega 1: versão 1.0 — 18/10/2026 — Documento de conformidade da equipe KATHERINE JOHNSON.*

## 4. Histórico dos registros da Entrega 2

As situações e pendências descritas abaixo correspondem às datas de cada registro.

### Heitor — registros de acompanhamento e coleta

Claude Code (Claude Opus 5.5, conforme o registro individual) apoiou o levantamento de commits,
issues e PRs, as seções da página Gestão e o slide “Antes do plano”. Em 10/11, também apoiou a
coleta intermediária da E2, o plano PSM/CID v1.2, a transcrição da ata 03 a partir do PDF da
retrospectiva da E1 e os slides de PSM/CID. Na primeira atividade, Heitor conferiu os valores no
GitHub e nas atas 01 e 02. Na atualização de 10/11, conferiu os números no GitHub e aprovou as
decisões antes da publicação.

Em 16/11, o registro cita Claude Code (Claude Sonnet 5.5) como apoio às páginas da Fase 4 e da
ação de melhoria, às descrições das imagens da Fase 3 e ao rascunho do acompanhamento PSM/CID.
Heitor conferiu situações, prazos e responsáveis nas issues e nos PRs e revisou as descrições
imagem a imagem. Em 22/11, a ferramenta apoiou o registro do iPhone e da execução do P6 no iOS,
o tratamento das capturas e a estimativa de horas com base em registros datados. Heitor forneceu
os dados da coleta e conferiu e aceitou a estimativa.

### Complemento da Fase 3 — 13/11/2026

Codex (OpenAI) apoiou a complementação documental da issue #46: ambiente planejado, massa justificada, cronograma, modelos CSV e síntese LaTeX, a partir da issue e dos arquivos existentes. Foram preservadas as pendências empíricas e não foram gerados resultados de coleta. A verificação técnica inclui construção da GitPage e o verificador disponível no repositório; a revisão humana por autores e revisor designado permanece pendente, assim como a validação dos instrumentos no piloto. Este registro não declara aprovação humana nem execução de sessões.

### Preparação da análise da Fase 4 — 16/11/2026

Codex (OpenAI) apoiou o roteiro de análise da issue #48, os modelos de consolidação e a síntese LaTeX. As regras foram cotejadas com as Fases 1–3 e os CSV disponíveis. Naquela data, a revisão humana por Pedro Henrique, Philipe e Heitor estava pendente e os resultados aguardavam a coleta da #47; a análise foi integrada pelo PR #92 em 24/11.


### Fechamento documental — 22/11/2026

Codex (OpenAI) apoiou a entrega da proposta de processo e templates da #36, a atualização do
artigo e sua compilação, a consulta de issues/PRs e o fechamento PSM da E2. As observações S03
foram atribuídas à branch e ao commit de origem, sem converter registros não conferidos em
medições oficiais. A declaração de Hugo sobre +1 h na E2 foi registrada com a base de estimativa
explicitada (depois substituída pela declaração registrada no [registro de horas](gestao-horas.md)), sem inventar a distribuição real por issue ou as horas dos demais integrantes.
As verificações automáticas e a inspeção do PDF são técnicas; a aprovação dos autores e dos
revisores designados permanece dependente de registro humano no PR.
