# Fase 1 — Priorização das Características, Cobertura de Contexto e ODS

**Projeto Final FGA0315 Qualidade de Software 1 (UnB/FGA, 2026/2)**  
*Avaliação da consulta de infrações do Detran-DF: Portal de Serviços × aplicativo*  
*Responsável: Pedro Druck Montalvão Reis*  
*Data da conferência das fontes: 19/10/2026*

Esta página é a versão completa da seção do artigo em `artigo/secoes/fase1-priorizacao.tex`. O artigo traz o resumo; aqui estão a justificativa de cada nota, a análise de sensibilidade e as fontes. As partes interessadas e as decisões D1 a D4 vêm da seção de propósito, partes interessadas e escopo (Heitor); as subcaracterísticas vêm de [Produto e modelo de qualidade](fase1-produto.md). O resultado alimenta os objetivos de [Fase 2](fase2-gqm.md).

---

## 1. Candidatas e exclusões prévias

O conjunto de candidatas parte das nove características de produto da ISO/IEC 25010:2023 e da cobertura de contexto do modelo de qualidade em uso (ISO/IEC 25010:2011).

| Característica | Situação antes da pontuação | Motivo |
|---|---|---|
| Capacidade de interação (antiga usabilidade) | Excluída | Exigência da disciplina; incluir usabilidade tornaria o critério C5 "Insuficiente" |
| Manutenibilidade | Excluída | Depende de acesso ao código-fonte |
| Flexibilidade (modelo de produto) | Excluída | Depende de acesso ao código-fonte |
| Segurança operacional (*safety*) | Excluída | Trata de evitar danos a pessoas e bens; não se aplica a uma consulta de dados |
| Adequação funcional, eficiência de desempenho, compatibilidade, confiabilidade, segurança | Candidatas | — |
| Cobertura de contexto | Candidata | Característica do modelo de qualidade em uso (ver Seção 5) |

"Flexibilidade" aparece com dois sentidos: característica do modelo de produto de 2023 (excluída acima) e subcaracterística da cobertura de contexto de 2011 (ver o [modelo adaptado](fase1-produto.md)). No texto, o segundo sentido sempre vem qualificado como flexibilidade de contexto.

## 2. Método e critérios

Matriz de pontuação ponderada, seguida de classificação MoSCoW (Clegg e Barker, 1994). Cada candidata recebe nota de 1 a 5 em cinco critérios; a nota final é a soma de nota × peso, com máximo de 55 pontos.

| Critério | Peso | Justificativa do peso |
|---|---:|---|
| Impacto para o cidadão | 3 | O cidadão é quem usa a consulta e fornece o ponto de vista de G1 e G3 |
| Risco para o requisitante | 2 | Consequência para o Detran-DF de uma falha não detectada. Pesa menos que o impacto, porque o risco institucional decorre em grande parte do dano ao cidadão (evita contar duas vezes) |
| Relação com o propósito comparativo | 3 | A avaliação existe para comparar os canais e apoiar as decisões D1 a D4 |
| Viabilidade de medir em caixa-preta | 2 | Sem código, servidores ou base do órgão, o que não é observável não gera evidência válida. Peso intermediário para que uma característica importante e inviável apareça na discussão de trade-offs, e não só no cálculo |
| Esforço de coleta (5 = baixo) | 1 | O prazo é limitado, mas esforço é custo e não valor |

## 3. Notas e justificativas

| Característica | Impacto | Risco | Propósito | Viabilidade | Esforço | Total |
|---|---:|---:|---:|---:|---:|---:|
| Adequação funcional | 5 | 4 | 5 | 5 | 4 | **52** |
| Cobertura de contexto | 4 | 4 | 5 | 4 | 2 | **45** |
| Eficiência de desempenho | 4 | 3 | 4 | 4 | 3 | **41** |
| Segurança | 5 | 5 | 1 | 1 | 1 | 31 |
| Confiabilidade | 4 | 4 | 2 | 1 | 1 | 29 |
| Compatibilidade | 2 | 2 | 2 | 1 | 3 | 21 |

**Adequação funcional (52).**
Impacto 5: os dados da autuação (infração, valores, pontuação, prazos) determinam se o cidadão paga, recorre ou indica condutor dentro do prazo.
Risco 4: dado ausente ou divergente entre canais leva a contestação e a atendimento presencial; não é 5 porque o proprietário pode conferir a notificação que recebeu.
Propósito 5: a paridade de dados é o núcleo da comparação (D1 e D2).
Viabilidade 5: tudo é observável nas telas, com a lista de referência R01–R15 da Fase 1.
Esforço 4: a lista de referência já existe; resta comparar campo a campo para cada veículo da massa de dados.

**Cobertura de contexto (45).**
Impacto 4: o cidadão fora do contexto previsto (aparelho antigo, rede ruim) fica sem a consulta naquele canal; não é 5 porque existe o outro canal.
Risco 4: parte dos cidadãos fica sem acesso a um serviço público digital.
Propósito 5: é o que diferencia os canais e sustenta D3 e D4.
Viabilidade 4: conclusão é um resultado binário e observável; o limite são os aparelhos que a equipe tem.
Esforço 2: exige vários aparelhos (Android de entrada e intermediário, iPhone), navegadores e condições de rede.

**Eficiência de desempenho (41).**
Impacto 4: tempo e dados transferidos afetam todo uso, em especial com plano de dados limitado; não é 5 porque não impede concluir a consulta.
Risco 3: desempenho ruim reduz o uso do canal digital, sem consequência legal direta.
Propósito 4: apoia D1 e D3; D2 e D4 dependem mais de dados e contexto.
Viabilidade 4: tempo e dados transferidos são observáveis; memória e capacidade, não.
Esforço 3: exige repetições por canal e por condição de rede, com ferramentas diferentes em cada canal.

**Segurança (31).**
Impacto 5 e risco 5: a consulta exibe dados pessoais (CPF, placa, infrações); um vazamento envolve responsabilidade pela Lei Geral de Proteção de Dados (Lei nº 13.709/2018).
Propósito 1: não ajuda a decidir D1 a D4.
Viabilidade 1: testes de segurança exigiriam autorização formal do órgão.
Esforço 1: exigiria conhecimento especializado.

**Confiabilidade (29).**
Impacto 4 e risco 4: indisponibilidade impede a consulta.
Propósito 2: as decisões D1 a D4 não dependem dela.
Viabilidade 1: disponibilidade e maturidade exigem monitoramento por semanas, além do prazo.
Esforço 1: pelo mesmo motivo.

**Compatibilidade (21).**
Impacto 2 e risco 2: a troca de dados com o gov.br e o RENAINF só é percebida pelo cidadão quando falha, e a autenticação está fora do escopo.
Propósito 2: não discrimina os canais, que compartilham o servidor de identidade.
Viabilidade 1: ocorre no servidor, não é observável.
Esforço 3: seria moderado se houvesse o que coletar.

## 4. Resultado, MoSCoW e sensibilidade

Classificação: *Must* com 40 pontos ou mais, *Could* de 25 a 39, *Won't* abaixo de 25 ("não nesta avaliação"). O corte coincide com a maior descontinuidade da lista (41 → 31 pontos) e respeita a premissa de três a quatro características.

| Característica | Total | MoSCoW |
|---|---:|---|
| Adequação funcional | 52 | Must |
| Cobertura de contexto | 45 | Must |
| Eficiência de desempenho | 41 | Must |
| Segurança | 31 | Could |
| Confiabilidade | 29 | Could |
| Compatibilidade | 21 | Won't |

**Relação com a numeração dos objetivos.** G1 (adequação funcional), G2 (eficiência de desempenho) e G3 (cobertura de contexto) seguem a ordem de apresentação do modelo de qualidade, não a prioridade. Pela matriz, a prioridade é adequação funcional, cobertura de contexto e eficiência de desempenho.

**Sensibilidade.** Variando cada um dos cinco pesos entre 1 e 3 (3⁵ = 243 combinações, notas fixas):

- as três características escolhidas permanecem as três primeiras em 242 de 243 combinações;
- a adequação funcional fica em primeiro lugar em 243 de 243;
- a cobertura de contexto supera a eficiência de desempenho em 207 de 243 (85%); a ordem entre as duas é menos robusta que a escolha do conjunto.

Para reproduzir:

```python
import itertools
S = {"AF": [5,4,5,5,4], "ED": [4,3,4,4,3], "CC": [4,4,5,4,2],
     "SEG": [5,5,1,1,1], "CONF": [4,4,2,1,1], "COMP": [2,2,2,1,3]}
tot = lambda s, w: sum(a*b for a, b in zip(s, w))
n = top3 = cc_gt_ed = 0
for w in itertools.product([1, 2, 3], repeat=5):
    n += 1
    r = sorted(S, key=lambda k: -tot(S[k], w))
    top3 += set(r[:3]) == {"AF", "ED", "CC"}
    cc_gt_ed += tot(S["CC"], w) > tot(S["ED"], w)
print(n, top3, cc_gt_ed)   # 243 242 207
```

## 5. Trade-offs

- **Segurança fora.** Evita testes sem autorização do órgão e reduz o esforço, mas a avaliação nada conclui sobre a proteção dos dados pessoais exibidos. É a perda mais relevante e deve constar das limitações.
- **Confiabilidade fora.** Disponibilidade exigiria monitoramento por semanas. Falhas pontuais entram como consulta não concluída na métrica M3.2.2 (taxa de falhas ou expiração de sessão), o que cobre só uma parte do atributo.
- **Compatibilidade fora.** A integração com o gov.br e o RENAINF ocorre no servidor; fica a recomendação de avaliá-la com acesso do órgão.
- **Cobertura de contexto dentro.** É a mais cara (vários aparelhos e redes, esforço 2) e a única que trata diretamente da decisão D3; sem ela, a comparação seria só de dados e de tempo.

## 6. Justificativa da cobertura de contexto

**Por que uma característica do modelo de qualidade em uso entra num trabalho de qualidade de produto.** O propósito é comparar canais que são usados em contextos diferentes (computador ou celular, rede estável ou degradada), e a decisão D3 pede saber qual canal recomendar em cada contexto. O modelo de produto descreve propriedades do produto, mas não tem característica cuja pergunta seja se a tarefa se conclui em cada contexto especificado. A ISO/IEC 25019:2023 mantém o contexto de uso como pré-requisito da qualidade em uso e prevê que mudanças de contexto sejam monitoradas por avaliações da qualidade em uso, o que sustenta esse tipo de avaliação mesmo sem a característica.

**Limitação registrada.** A definição vem da ISO/IEC 25010:2011, edição substituída pelas ISO/IEC 25010:2023 e 25019:2023. A 25019:2023 retirou a cobertura de contexto do modelo. As medidas associadas estão na ISO/IEC 25022:2016.

**Diferença para usabilidade.**

| Aspecto | Cobertura de contexto (incluída) | Usabilidade / capacidade de interação (excluída) |
|---|---|---|
| Pergunta | A consulta é concluída neste dispositivo, navegador, sistema e rede? | O usuário opera a interface com eficácia, eficiência e satisfação? |
| Evidência | Conclusão e tempo, registrados por roteiro fixo | Desempenho e opinião de usuários |
| Quem mede | Avaliadores da equipe | Usuários representativos |
| Resultado | Conclui ou não, por contexto | Escala de facilidade ou satisfação |

Não se mede satisfação, facilidade de aprendizado, estética, acessibilidade da interface nem proteção contra erro do usuário. A própria ISO/IEC 25010:2023 trata a capacidade de interação como pré-requisito da usabilidade, que pertence ao modelo de qualidade em uso.

## 7. ODS, metas e indicadores

| ODS | Meta | Indicador | Pertinência ao software |
|---|---|---|---|
| 16 — Paz, justiça e instituições eficazes | 16.6 — Desenvolver instituições eficazes, responsáveis e transparentes em todos os níveis | 16.6.2 — Proporção da população satisfeita com a última experiência com serviços públicos | A consulta é um serviço público digital. Os resultados mostram onde ele deixa de ser equivalente entre os canais, lento ou inacessível |
| 9 — Indústria, inovação e infraestrutura | 9.c — Aumentar significativamente o acesso às tecnologias de informação e comunicação e se empenhar para oferecer acesso universal e a preços acessíveis à internet nos países menos desenvolvidos, até 2020 | 9.c.1 — Proporção da população coberta por rede móvel, por tecnologia | Vínculo indireto: ter rede móvel não garante acessar o serviço, e G3 mede se a consulta conclui nessa rede |

**ODS 16 (principal).** A avaliação não mede o indicador 16.6.2, que depende de opinião e pertence à usabilidade, fora do escopo. Ela produz evidências sobre causas objetivas (divergência de dados, tempo, falha de conclusão) que afetam a experiência do cidadão e alimentam as decisões D1 a D4.

**ODS 9 (secundário).** O texto da meta 9.c se dirige aos países menos desenvolvidos e ao prazo de 2020; o Brasil não está nesse grupo, então a relação é temática. O indicador 9.c.1 mede cobertura de rede, não conclusão de serviço; o objetivo G3 mede o que falta entre os dois.

**Considerado e descartado: ODS 3, meta 3.6** ("Até 2020, reduzir pela metade as mortes e os ferimentos globais por acidentes em estradas"; indicador 3.6.1, taxa de mortalidade por lesões de trânsito). O vínculo é com a fiscalização de trânsito, e a qualidade do software de consulta não permite inferir efeito sobre acidentes.

## 8. Referencial SQuaRE: o que foi conferido

| Afirmação do artigo | Fonte conferida em 19/10/2026 |
|---|---|
| A família SQuaRE tem divisões de gestão da qualidade (2500n), modelos (2501n), medição (2502n), requisitos (2503n) e avaliação (2504n) | Prefácio da ISO/IEC 25010:2023 (prévia pública) |
| A ISO/IEC 25010:2023 e a 25019:2023, junto com a 25002, substituem a ISO/IEC 25010:2011 | Prefácios da ISO/IEC 25010:2023 e 25019:2023 (prévias públicas) |
| A 25019:2023 retirou a cobertura de contexto como característica do modelo de qualidade em uso | Prefácio da ISO/IEC 25019:2023: "context coverage which was shown as quality characteristics in the quality-in-use model of the previous version is removed" |
| A 25019:2023 mantém o contexto de uso como pré-requisito da qualidade em uso | Escopo e introdução da ISO/IEC 25019:2023 |
| Capacidade de interação é pré-requisito da usabilidade (modelo de qualidade em uso) | ISO/IEC 25010:2023, definição 3.4, nota 2 |
| Definições de adequação funcional, completude, correção e apropriação funcional, eficiência de desempenho, comportamento temporal, utilização de recursos e capacidade | ISO/IEC 25010:2023, definições 3.1 e 3.2 |
| A ISO/IEC 25040 teve segunda edição em setembro de 2024 | Página da norma em iso.org (<https://www.iso.org/standard/83467.html>), conferida em 26/10/2026: edição 2, publicada em 2024-09 |
| A ISO/IEC 25022:2016 foi confirmada em revisão de 2022 | Página da norma em iso.org (<https://www.iso.org/standard/35746.html>), conferida em 26/10/2026: "last reviewed and confirmed in 2022"; a norma está no estágio 90.92 (a ser revisada) |

## 9. Fontes dos ODS

- Textos das metas em português: Nações Unidas Brasil, páginas dos ODS [3](https://brasil.un.org/pt-br/sdgs/3), [9](https://brasil.un.org/pt-br/sdgs/9) e [16](https://brasil.un.org/pt-br/sdgs/16), acesso em 19/10/2026.
- Textos dos indicadores (em inglês, traduzidos pela equipe): [Global indicator framework for the Sustainable Development Goals](https://unstats.un.org/sdgs/indicators/Global-Indicator-Framework-after-2025-review-English.pdf) (A/RES/71/313; E/CN.3/2025/6), acesso em 19/10/2026.
- Dados brasileiros na plataforma ODS Brasil do IBGE (<https://odsbrasil.gov.br>), conferidos em 26/10/2026 nas páginas dos objetivos 16 e 9: o indicador 16.6.2 está classificado como "Sem dados", e o 9.c.1, como "Produzido". O artigo não afirma que haja dados nacionais para os indicadores.

## 10. Situação após a Entrega 1

- Notas e pesos da matriz: revisados e aprovados no [PR #18](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/pull/18) e integrados ao artigo.
- Edição da ISO/IEC 25040: o artigo usa a edição de 2011 como base do processo e registra, no referencial teórico, que a segunda edição (2024) a substituiu.
- Declaração de uso de IA: linha de Pedro Druck atualizada na GitPage e no artigo.
- Pendente: confirmar com a professora, no ponto de controle, a inclusão da cobertura de contexto.

---

**Referências**

- Clegg, D.; Barker, R. *Case Method Fast-Track: A RAD Approach*. Addison-Wesley, 1994.
- ISO/IEC 25010:2011; ISO/IEC 25010:2023; ISO/IEC 25019:2023; ISO/IEC 25022:2016; ISO/IEC 25023:2016; ISO/IEC 25040:2011; ISO/IEC 25040:2024.
- United Nations General Assembly. *Transforming our world: the 2030 Agenda for Sustainable Development* (A/RES/70/1), 2015.
