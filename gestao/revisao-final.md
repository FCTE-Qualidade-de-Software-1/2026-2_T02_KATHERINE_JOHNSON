# Revisão Final de Português e Padronização do Artigo

> **Atualização de 27/10/2026.** Este documento registra a revisão feita em 19/10, antes da integração
> do artigo. Desde então, o artigo foi integrado no PR #50, as marcas `[VERIFICAR]` do LaTeX foram
> resolvidas, a declaração de IA ganhou a linha de fonte e o `artigo/scripts/verificar.py` termina sem
> erros. O padrão de redação da Seção 2 continua valendo para a Entrega 2.

**Projeto Final FGA0315 Qualidade de Software 1 (UnB/FGA, 2026/2)**  
*Responsável: Pedro Druck Montalvão Reis*  
*Primeira passada: 19/10/2026, sobre as seções que estavam na `main` (base: commit `35d4e17`)*

Este documento registra a revisão final do artigo: o padrão adotado, o que foi corrigido, o que ficou como observação para os autores e o roteiro da passada final depois da integração. Ele também alimenta a métrica M-DP1 do [plano PSM/CID](plano-psm.md), porque conta os defeitos encontrados na revisão.

## 1. Escopo e limites desta passada

O artigo ainda não está integrado: não há `main.tex`. A seção do Pedro Druck (priorização e referencial SQuaRE) está no PR #18, aberto. A do Heitor (propósito, partes interessadas e escopo) **não está na `main`**: o PR #16 foi mesclado na branch `feat/gitpage-mkdocs` 37 segundos depois de o PR #15 ter ido para a `main`, e o conteúdo ficou de fora (`artigo/secoes/fase1-proposito.tex`, `docs/fase1-proposito.md`, `slides/conteudo-heitor.md`). Isso precisa de um novo PR a partir de `feat/heitor-proposito-escopo` ou de `feat/gitpage-mkdocs`. Esta passada cobriu as seções que estão na `main`:

| Arquivo | Autor |
|---|---|
| `artigo/secoes/fase1-produto.tex` | Hugo |
| `artigo/secoes/fase2-objetivos.tex` | Pedro Henrique |
| `artigo/secoes/fase2-metricas.tex` | Philipe |
| `artigo/secoes/referencial-gqm.tex` | Pedro Henrique |
| `artigo/secoes/declaracao-ia.tex` | Pedro Henrique (não alterado; ver Seção 5) |
| `artigo/referencias.bib` | Todos |
| `docs/fase2-gqm.md`, `atas/modelo-ata.md`, `gestao/plano-psm.md` | Terminologia dos canais |

**A revisão final da issue só termina depois da integração (sábado, 24/10).** A Seção 6 descreve como repetir as verificações no artigo integrado.

Ferramentas: o script `artigo/scripts/verificar.py` faz as verificações mecânicas (rótulos, citações, `.bib`, legenda, fonte e chamada de figuras e tabelas, emojis, termos). A compilação de teste usou o Tectonic 0.17 com a classe `article`, não o modelo SBC, que ainda não está no repositório; por isso o resultado de páginas e de caixas estouradas não vale para o artigo final.

## 2. Padrão de redação e terminologia

| Usar | Evitar | Observação |
|---|---|---|
| Portal de Serviços | Portal Web, portal web, Portal de Serviços web | Termo padronizado da equipe |
| aplicativo | app, aplicativo mobile, App Mobile | "app" só em nome de arquivo ou de nó de diagrama |
| consulta de infrações | consulta de multas | Termo padronizado da equipe |
| adequação funcional | Adequação Funcional (caixa alta) | Característica; minúscula no texto, maiúscula só no início de frase ou de célula |
| apropriação funcional | adequação funcional do fluxo | Subcaracterística da adequação funcional; usar o nome da subcaracterística evita repetir o da característica |
| eficiência de desempenho | eficiência (sozinho) | "Eficiência" sozinha só aparece em "eficiência de desempenho" ou ao citar o modelo de qualidade em uso |
| cobertura de contexto | — | Subcaracterísticas: completude de contexto e flexibilidade de contexto |
| flexibilidade de contexto | flexibilidade operacional, flexibilidade | "Flexibilidade" também é característica do modelo de produto de 2023 (fora do escopo); qualificar sempre |
| partes interessadas | stakeholders | Termo usado na seção de propósito e escopo |
| ponto de vista | Ponto de Vista | Elemento do *template* GQM |
| *template* GQM, em cinco elementos | cinco dimensões | Basili, Caldiera e Rombach (1994) |
| ambientes especificados no escopo | ambientes homologados | "Homologar" é termo de entrega de software; não se aplica |
| computador, celular | desktop, mobile | Português corrente |
| caixa-preta | black-box, caixa preta | Com hífen |

**Formatação.**

- Seções e subseções em maiúscula inicial em cada palavra (como já estava em todos os arquivos); subsubseções e legendas em maiúscula só na primeira palavra.
- Nomes dos níveis de pontuação com maiúscula inicial: Inaceitável, Mínimo aceitável, Alvo, Excelente.
- Toda figura ou tabela com `\caption`, `\label`, linha `Fonte:` e chamada no texto (`Tabela~\ref{...}`, `Figura~\ref{...}`).
- Citações de normas pelo ano da edição no `.bib`; um único `\cite` por afirmação.

## 3. Resultado das verificações automáticas

| Verificação | Antes (`main`) | Depois (esta branch) |
|---|---:|---:|
| Rótulo duplicado ou referência a rótulo inexistente | 0 | 0 |
| Citação sem entrada no `.bib` | 0 | 0 |
| Entrada do `.bib` nunca citada | 0 | 0 |
| Entrada `@standard` (tipo não reconhecido pelo BibTeX do SBC) | 6 | 0 |
| Tabela ou figura sem linha `Fonte:` | 7 | 1 (tabela da declaração de IA) |
| Tabela nunca chamada no texto | 1 | 0 |
| Termos fora do padrão detectados pelo script | 17 | 0 |
| Emojis e símbolos decorativos | 0 | 0 |
| Marcas `[VERIFICAR]` nos `.tex` | 3 | 3 (dos autores; ver Seção 4) |

Compilação de teste com todas as seções: sem `??` no PDF, sem citação indefinida.

## 4. Correções aplicadas

| Arquivo | Correção |
|---|---|
| `referencias.bib` | Seis entradas `@standard` convertidas para `@misc` com `author`; `basili1994gqm` passou de `@techreport` para `@incollection` (é capítulo de enciclopédia); o livro de Van Solingen e Berghout é de 1999, não de 2002, e a chave passou de `van2002goal` para `van1999goal` (ano e ISBN 0-07-709553-7 conferidos em registro bibliográfico) |
| `fase2-objetivos.tex` | Terminologia dos canais (17 ocorrências de "web", "mobile", "portal web"); "stakeholder" por "parte interessada"; "Basili e Rombach" por "Basili, Caldiera e Rombach", conforme a entrada citada; "adequação funcional do fluxo de consulta" por "apropriação funcional da consulta"; "ambientes homologados" por "ambientes especificados no escopo"; "flexibilidade operacional" por "flexibilidade de contexto"; maiúsculas indevidas em nomes de características, de questões e de títulos; legendas em maiúscula só na primeira palavra; advérbios de ênfase ("rigorosamente", "terminantemente", "expressamente") e jargão ("extrato final", "passos transacionais", "ecossistemas de software, hardware e infraestrutura física") reescritos; linhas `Fonte:` nas três tabelas |
| `fase2-metricas.tex` | Terminologia dos canais; `Tabela~\ref{tab:niveis-nao-percentuais}` passou a ser chamada no texto; linhas `Fonte:` nas três tabelas; o diagrama GQM, que só era citado por caminho de arquivo, entrou como Figura com legenda, fonte e chamada |
| `referencial-gqm.tex` | "cinco dimensões" por "cinco elementos"; chave do livro atualizada; "grandezas mensuráveis coletadas em software" por "grandezas medidas"; *pull requests* em itálico, como *issues* |
| `docs/fase2-gqm.md` | Mesmas correções de terminologia e de caixa da versão do artigo |
| `atas/modelo-ata.md`, `gestao/plano-psm.md` | "Aplicativo Mobile" por "aplicativo" no subtítulo |

## 5. Observações para os autores (não alteradas)

Estas observações dependem de decisão do autor ou de conteúdo, não de padronização.

**Pedro Henrique (Fase 2, objetivos).**

- O ponto de vista de G3 é só o cidadão na tabela de objetivos, mas "cidadão/condutor e requisitante" na tabela de rastreabilidade; G1 e G2 incluem o requisitante nas duas. Alinhar (critério F2-C11).
- As questões Q2.1 e Q2.2 ("Qual canal apresenta menor tempo…?", "Qual canal transfere menor volume…?") estão perto de métrica em forma de pergunta, o que o critério F2-C2 pune. Sugestão: perguntar se o desempenho dos canais é equivalente e deixar o tempo e o volume para as métricas.
- A hipótese H1.1 supõe que o Portal de Serviços é mais completo; o levantamento do Hugo encontrou praticamente os mesmos rótulos nos dois canais (nota do PR #14).
- "navegadores web modernos" em G3 é vago diante da seção de escopo (Chrome e Firefox em computador, Chrome em celular).
- A Fase 2 não remete à seção de priorização (`subsec:priorizacao`, PR #18). Depois da integração, acrescentar a chamada na Seção de rastreabilidade (F2-C11).
- A numeração G1 a G3 segue a ordem do modelo de qualidade; pela matriz de priorização a ordem de prioridade é G1, G3, G2. O texto da priorização já diz isso.

**Philipe (Fase 2, métricas).**

- Três marcas `[VERIFICAR]` no texto do artigo (parágrafo de M2.1.1, M3.1.x e M3.2.x) precisam ser resolvidas antes da release.
- O texto cita "referências usuais de engenharia de interação" sem citação; `docs/fase2-metricas.md` atribui as faixas a Nielsen. Ou entra a referência no `.bib`, ou o trecho sai. Como a engenharia de interação é vizinha da usabilidade, o termo merece cuidado (F2-C12).
- O diagrama GQM (`artigo/figuras/diagram.png`, 8192 × 2697 px) fica ilegível na largura da página: os textos dos nós ficam menores que 3 pt. Regenerar em outra orientação ou dividir por objetivo (F2-C6 e C9).
- Duas tabelas da Fase 2 estouram a largura na compilação de teste (rastreabilidade e quadro de questões e hipóteses); conferir no modelo SBC.

**Hugo (Fase 1, produto).**

- Nenhuma correção necessária no texto. A afirmação de que a ISO/IEC 25019:2023 retirou a cobertura de contexto foi conferida no prefácio da norma e está correta.

**Pedro Henrique e Daniel (declaração de IA e metodologia).**

- `artigo/secoes/declaracao-ia.tex` e `docs/declaracao-ia.md` **não foram alterados nesta passada**. Pendências: a tabela não tem linha `Fonte:`; a versão da ferramenta está informada de forma desigual entre os integrantes (alguns com versão, outros sem); a linha do Pedro Druck precisa ser atualizada pelo próprio integrante.
- A Metodologia e a Fase 2 citam a ISO/IEC 25040:2011; a segunda edição é de setembro de 2024 (entrada `iso25040_2024` no PR #18). Decidir qual citar e citar uma só.

## 6. Roteiro da passada final (após a integração)

Executar sábado à noite, depois da integração do Daniel, e repetir no domingo antes da release.

| # | Passo | Como |
|---|---|---|
| 1 | Compilar com o modelo SBC e abrir o PDF | Sem `??`, sem avisos de citação indefinida, sem tabela estourando a margem |
| 2 | Rodar as verificações mecânicas | `python3 artigo/scripts/verificar.py`; meta: zero erros |
| 3 | Conferir o sumário e a numeração | Seções e subseções na ordem da Fase 1, Fase 2, referencial e metodologia; chamadas `Seção~\ref` e `Tabela~\ref` apontando para o item certo |
| 4 | Ler o artigo inteiro em voz alta | Concordância, concisão, termos da Seção 2 |
| 5 | Conferir cada figura e tabela | Legenda, fonte, chamada no texto, legibilidade no tamanho impresso (em especial o diagrama GQM e o diagrama de contexto) |
| 6 | Conferir o `.bib` | Ano e edição de cada norma, tipo da entrada, nenhuma entrada sem uso; `@misc` com `author` |
| 7 | Resolver todas as marcas `[VERIFICAR]` do PDF | Cada uma vira afirmação conferida ou sai do texto |
| 8 | Conferir o limite de páginas | No máximo 15 páginas, incluindo referências e apêndices que integram o PDF (a tabela de contribuição não conta) |
| 9 | Conferir o link do repositório e da release no corpo do artigo | Link abre; versão (tag) corresponde à release E1 |
| 10 | Conferir a declaração de IA | Uma linha por integrante, com ferramenta, tarefa e como foi conferido; sem emojis ou ícones |
| 11 | Registrar os defeitos achados | Tabela da Seção 3, na coluna "Depois", para a métrica M-DP1 |

## 7. Situação dos critérios de aceitação da issue

| Critério | Situação |
|---|---|
| Revisão textual em todas as seções | Feita nas seções da `main`; faltam as do Heitor (fora da `main`, ver Seção 1), do Pedro Druck (PR #18), da Metodologia e da Introdução |
| Legendas, numeração, fontes e chamadas | Verificadas por script e corrigidas; pendentes a tabela da declaração de IA e as seções ainda não mescladas |
| Consistência do `.bib` | Verificada e corrigida (tipos, autoria, ano, chaves); revisar de novo depois do PR #18 |
| Padronização de termos | Padrão definido (Seção 2) e aplicado às seções da `main` |
