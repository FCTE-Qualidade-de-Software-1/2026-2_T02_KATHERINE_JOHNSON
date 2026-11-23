# Fase 4 — Execução e julgamento

A Fase 4 executa o plano da [Fase 3](fase3.md): obtém as medidas nos dois canais, calcula as
quatorze métricas da [Fase 2](fase2.md), responde às questões do GQM e julga a qualidade do
Portal de Serviços e do aplicativo em relação ao propósito definido na [Fase 1](fase1.md).
Ela também inclui a [ação de melhoria](fase4-melhoria.md), exigida na Entrega 2 e justificada
pelas evidências coletadas.

> **Situação em 23/11/2026.** Os oito CSV têm registros de seis sessões (S01, S02, S03, S05, S06 e S08), cobrindo P1
> a P7 com duas lacunas declaradas: o aplicativo na rede degradada e o contexto CT04. Os valores
> são primeira leitura, exceto P1 a P3 da S02, que tiveram segunda leitura independente (uma rolagem
> do P3 segue pendente); sem a conferência completa, não há nível de pontuação. A
> [análise](fase4-analise.md) traz os valores observados e mantém os objetivos inconclusivos. A
> [proposta de processo e templates de melhoria](fase4-melhoria.md) está entregue, sem comprovação de
> eficácia no serviço.

O [acompanhamento da coleta](fase4-coleta.md) reúne as pendências da #46, a proposta de
reagendamento e o cálculo reproduzível da #47. O prazo original da coleta (18/11) foi
reprogramado e a coleta ocorreu em 21 e 22/11. Sem a segunda leitura, a consolidação registra valores
observados sem níveis de qualidade.

## 1. Atividades, responsáveis e prazos

| Atividade | Issue | Responsáveis | Prazo | Situação em 22/11 | Onde ficará o resultado |
|---|---|---|---|---|---|
| Coleta das medições e dados brutos (sessões S02 a S05) | [#47](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/47) | Hugo, Pedro Druck, Philipe | 18/11/2026 | S01 e S03 com relatos; dados oficiais pendentes de conferência | `dados/brutos/` e `evidencias/fase4/` |
| Análise, respostas às questões GQM e julgamento | [#48](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/48) | Pedro Henrique, Philipe; revisão de Heitor | 20/11/2026 | Aguarda os dados conferidos da #47 | [Análise e julgamento GQM](fase4-analise.md) e artigo |
| Ação de melhoria obrigatória | [#36](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/36) | Pedro Druck | 21/11/2026 | Processo e templates entregues; revisão e eficácia pendentes | [Ação de melhoria](fase4-melhoria.md) |

*Tabela 1 — Atividades da Fase 4. Fonte: issues #36, #47 e #48 e coleta intermediária PSM/CID de 10/11/2026.*

As datas seguem o planejamento confirmado na [ata 04](atas.md) e o cronograma das sessões em
[Cronograma e bloqueios](fase3-cronograma.md) (ver Tabela 1 daquela página).

## 2. Como a coleta será executada

O método, os sete procedimentos (P1 a P7) e a rastreabilidade entre cada métrica e seu
procedimento estão em [Método e instruções para o avaliador](fase3-metodo.md). O ambiente e os
dispositivos estão em [Recursos e ambiente](fase3-ambiente.md), e a massa de dados e os
instrumentos em [Massa e instrumentos de coleta](fase3-dados.md).

Regras de integridade que valem para toda a fase:

- cada sessão é registrada no modelo de sessão, com conferência independente por outro
  integrante, antes de o valor final entrar nos arquivos CSV;
- falhas do serviço entram no cálculo e não são substituídas para melhorar o resultado; só erros
  do instrumento de medição geram desvio e reposição, sempre identificados;
- métrica que não for medida é registrada como inconclusiva, sem nível de pontuação, e não
  sustenta conclusão sobre o objetivo que depende dela;
- os resultados comparam os canais por métrica e por contexto, sem unir aparelhos ou redes
  diferentes em uma única mediana;
- dados pessoais não são publicados. Placas, Renavam, nomes e números de auto aparecem como
  "Veículo V1" e "V1-I1", e originais, termos assinados e arquivos HAR ficam fora do repositório
  público.

## 3. Onde estão os dados e as evidências

| Material | Conteúdo | Localização |
|---|---|---|
| Instrumentos e dicionário de dados | Oito CSV-modelo e as convenções de cálculo | [`dados/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/dados) |
| Evidências anonimizadas | Capturas, vídeos tratados e configuração de rede | [`evidencias/fase4/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase4) |
| Registro de sessão | Piloto, blocos, conferência e desvios | [`evidencias/fase4/modelo-sessao.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/modelo-sessao.md) |
| Estrutura da análise | Procedimento, dependências da #47 e modelos de consolidação | [Análise e julgamento GQM](fase4-analise.md); [`dados/consolidados/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/dados/consolidados) |
| Release da Entrega 2 | Tag e PDF do artigo | [Releases](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/releases); publicação prevista para 22/11/2026 |

*Tabela 2 — Materiais da Fase 4. Fonte: elaborada pela equipe.*

## 4. Resultados e julgamento

Não há resultados oficiais elegíveis: todos os valores são primeira leitura e dependem da segunda
leitura independente. A página [Análise e julgamento GQM](fase4-analise.md) traz os valores
observados e o estado de cada questão, hoje inconclusiva. Depois da conferência (#48), esta seção terá
um resultado por objetivo, com o valor de cada métrica, o nível de pontuação, a resposta a cada
questão e o julgamento por característica e por canal.

| Objetivo GQM | Característica | Resultado |
|---|---|---|
| G1 | Adequação funcional | Primeira leitura: sem campo divergente; um campo ausente no aplicativo (16/17); 4 contra 6 passos. Inconclusivo |
| G2 | Eficiência de desempenho | Primeira leitura (caso V4, Wi-Fi): portal mais rápido; volumes de escopos diferentes. Inconclusivo |
| G3 | Cobertura de contexto | Primeira leitura: cinco contextos de P6; P7 sem o aplicativo na rede degradada. Inconclusivo |

*Tabela 3 — Resultados por objetivo de medição. Fonte: [Objetivos, questões e hipóteses](fase2-gqm.md).*

## 5. Limitações já conhecidas

- **iOS:** o iPhone é de Heitor e o CT06 foi inventariado e executado em 22/11 (3 de 3, caso V5,
  aplicativo 2.7.1), pendente de conferência independente. O iOS não oferece contador de bytes por
  aplicativo, então a M2.2.1 não é medida nele (D008), e o executor é também o titular (D028).
- **Lacunas de cobertura:** o aplicativo na rede degradada não foi medido (D021) e o CT04 não tem
  aparelho; as duas ficam inconclusivas, nunca zero.
- **Veículo real:** os termos foram aplicados, conforme confirmação de Hugo em 22/11/2026, e permanecem privados; a coleta depende de veículo com infração e titular disponível
  (bloqueio B01, com consentimento concluído). Sem veículo elegível ou titular disponível, as sessões são adiadas e o impacto é registrado na #47.
- **Métrica M3.1.2:** é exclusiva do portal e não serve para comparar com o aplicativo.
- **Validade dos resultados:** os resultados valem para os veículos, aparelhos, redes e datas
  efetivamente medidos e não representam todos os usuários do Detran-DF.
