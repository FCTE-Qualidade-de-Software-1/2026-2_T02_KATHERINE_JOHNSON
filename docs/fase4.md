# Fase 4 — Execução e julgamento

A Fase 4 executa o plano da [Fase 3](fase3.md): obtém as medidas nos dois canais, calcula as
quatorze métricas da [Fase 2](fase2.md), responde às questões do GQM e julga a qualidade do
Portal de Serviços e do aplicativo em relação ao propósito definido na [Fase 1](fase1.md).
Ela também inclui a [ação de melhoria](fase4-melhoria.md), exigida na Entrega 2 e justificada
pelas evidências coletadas.

> **Situação em 24/11/2026.** Os registros de seis sessões (S01, S02, S03, S05, S06 e S08) foram
> conferidos em segunda leitura independente para os procedimentos elegíveis. As divergências de
> tempo foram resolvidas em conjunto; o cálculo reproduzível atribui níveis aos resultados elegíveis.
> Permanecem duas lacunas: aplicativo na rede degradada e CT04. A
> [análise](fase4-analise.md) responde às questões e julga objetivos por canal sem transformar
> essas lacunas em zero ou aprovação. A
> [proposta de processo e templates de melhoria](fase4-melhoria.md) está entregue, sem comprovação de
> eficácia no serviço.
>
> **Para conferir os números:** [Medições por métrica](fase4-medicoes.md) mostra cada leitura bruta
> por trás de cada resultado, com link para a linha exata do CSV, a captura e a segunda leitura.

O [acompanhamento da coleta](fase4-coleta.md) reúne as pendências da #46 e o histórico de
reagendamento; a [consolidação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/dados/consolidados/resultados-metricas.csv) registra valores,
níveis, proveniência e limitações após a conferência. A coleta ocorreu em 21 e 22/11.

## 1. Atividades, responsáveis e prazos

| Atividade | Issue | Responsáveis | Prazo | Situação em 24/11 | Onde está o resultado |
|---|---|---|---|---|---|
| Coleta das medições e dados brutos (S01, S02, S03, S05, S06 e S08) | [#47](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/47) | Hugo, Pedro Druck, Philipe | 18/11/2026 | Concluída: segundas leituras registradas, níveis calculados e issue fechada em 24/11 | [Medições por métrica](fase4-medicoes.md), `dados/brutos/` e `evidencias/fase4/` |
| Análise, respostas às questões GQM e julgamento | [#48](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/48) | Pedro Henrique, Philipe; revisão de Heitor | 20/11/2026 | Resultados, níveis, respostas, julgamentos e oportunidades registrados; aprovação do revisor pendente | [Análise e julgamento GQM](fase4-analise.md) e artigo |
| Ação de melhoria obrigatória | [#36](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/36) | Pedro Druck | 21/11/2026 | Processo e templates entregues; revisão e eficácia pendentes | [Ação de melhoria](fase4-melhoria.md) |

*Tabela 1 — Atividades da Fase 4. Fonte: issues #36, #47 e #48 e coleta intermediária PSM/CID de 10/11/2026.*

As datas seguem o planejamento confirmado na [ata 04](atas.md) e o cronograma das sessões em
[Cronograma e bloqueios](fase3-cronograma.md) (ver Tabela 1 daquela página).

## 2. Como a coleta foi executada

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
| Instrumentos e dicionário de dados | Oito CSV com os registros das sessões e as convenções de cálculo | [`dados/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/dados) |
| Evidências anonimizadas | Capturas, vídeos tratados e configuração de rede | [`evidencias/fase4/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/evidencias/fase4) |
| Registro de sessão | Piloto, blocos, conferência e desvios | [`evidencias/fase4/modelo-sessao.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/modelo-sessao.md) |
| Medições por métrica | Cada leitura das 14 métricas ligada à linha do CSV, à captura e à segunda leitura | [Medições por métrica](fase4-medicoes.md) |
| Estrutura da análise | Procedimento, dependências da #47 e modelos de consolidação | [Análise e julgamento GQM](fase4-analise.md); [`dados/consolidados/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/dados/consolidados) |
| Release da Entrega 2 | Tag e PDF do artigo | [Releases](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/releases); publicação pendente |

*Tabela 2 — Materiais da Fase 4. Fonte: elaborada pela equipe.*

## 4. Resultados e julgamento

Os resultados por métrica, os níveis e as respostas estão na página
[Análise e julgamento GQM](fase4-analise.md) e na consolidação vinculada. O resumo abaixo segue a
regra de que uma questão só é atendida quando todas as métricas aplicáveis alcançam ao menos o nível
mínimo aceitável.

| Objetivo GQM | Característica | Resultado |
|---|---|---|
| [G1](fase4-analise.md#julg-g1) | [Adequação funcional](fase4-medicoes.md#g1) | Não atendido nos dois canais: M1.1.1 Inaceitável (33,33%); M1.2.2 Inaceitável (0/1). A ausência de R14 foi observada no aplicativo. |
| [G2](fase4-analise.md#julg-g2) | [Eficiência de desempenho](fase4-medicoes.md#g2) | Atendido nos dois canais no caso V4/Wi-Fi: tempos e volumes Excelentes, portal mais rápido (H2.1 contrariada); a comparação de volume (H2.2) é inconclusiva porque os instrumentos têm escopos diferentes. |
| [G3](fase4-analise.md#julg-g3) | [Cobertura de contexto](fase4-medicoes.md#g3) | Portal atendido nos contextos medidos (até Alvo na rede degradada); aplicativo não atendido no escopo observado por falha 0/3 em CT05/2.6.3; CT04 e aplicativo degradado não avaliados. |

*Tabela 3 — Resultados por objetivo de medição. Fonte: [Objetivos, questões e hipóteses](fase2-gqm.md) e [análise](fase4-analise.md#julgamento); cada característica leva às medições.*

## 5. Limitações já conhecidas

- **iOS:** o CT06 foi inventariado e executado em 22/11 no iPhone D04 (3 de 3, caso V5,
  aplicativo 2.7.1), com segunda leitura independente registrada. O iOS não oferece contador de bytes por
  aplicativo, então a M2.2.1 não é medida nele (D008); a execução sem registrador independente
  está registrada como desvio (D028).
- **Lacunas de cobertura:** o aplicativo na rede degradada não foi medido (D021) e o CT04 não tem
  aparelho; as duas ficam inconclusivas, nunca zero.
- **Veículo real:** os termos foram aplicados, conforme confirmação de Hugo em 22/11/2026, e permanecem privados; a coleta usou veículos com infração e titulares disponíveis
  (bloqueio B01, com consentimento concluído). Novas sessões dependem das mesmas condições.
- **Métrica M3.1.2:** é exclusiva do portal e não serve para comparar com o aplicativo.
- **Validade dos resultados:** os resultados valem para os veículos, aparelhos, redes e datas
  efetivamente medidos e não representam todos os usuários do Detran-DF.
