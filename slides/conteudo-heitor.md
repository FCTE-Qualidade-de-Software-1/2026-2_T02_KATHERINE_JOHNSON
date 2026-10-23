# Conteúdo dos slides — Heitor (problema, propósito, partes interessadas e escopo)

Para o Pedro Henrique montar na apresentação. Fonte: `artigo/secoes/fase1-proposito.tex` (Tabelas de decisões, partes interessadas e fora do escopo).

## Slide 1 — Problema e propósito

**Título:** Por que comparar o Portal de Serviços e o aplicativo

**Problema:** o mesmo serviço, a consulta de infrações, é oferecido em dois canais que consultam serviços de backend distintos. Um mesmo veículo pode aparecer com dados, tempos ou possibilidade de conclusão diferentes conforme o canal.

**Propósito:** verificar se os dois canais entregam a consulta com qualidade equivalente e, quando não entregam, onde está a diferença.

**Requisitante (hipotético):** Área de Governança Digital do Detran-DF.

| Decisão apoiada | Quem decide |
|---|---|
| D1 — Em qual canal e característica investir primeiro | Requisitante |
| D2 — Quais divergências de dados corrigir | Equipe técnica de TI |
| D3 — Qual canal recomendar em cada contexto de uso | Requisitante e atendimento |
| D4 — Quais contextos devem ter suporte garantido | Equipe técnica de TI |

**Fala (cerca de 1 min):** o cidadão consulta multas pelo portal ou pelo aplicativo, conforme o aparelho e a conexão que tem. Os dois canais usam o mesmo login, mas serviços diferentes para buscar as infrações, então nada garante que entreguem a mesma coisa. Nossa avaliação compara os dois. O requisitante é hipotético: a área de governança digital do Detran-DF, que usaria o resultado para quatro decisões concretas, cada uma com um responsável. O uso é comparativo: uma linha de base, não uma certificação.

## Slide 2 — Partes interessadas e escopo

**Título:** Para quem avaliamos e até onde vamos

| Parte interessada | Critério de sucesso | Influência |
|---|---|---|
| Requisitante (hipotético) | Julgamento por canal que ordene as melhorias | Propósito comparativo |
| Cidadão/condutor | Consulta completa, correta e concluída em qualquer contexto | Adequação funcional e cobertura de contexto (G1, G3) |
| Equipe técnica de TI | Medições reproduzíveis por canal e rede | Eficiência de desempenho (G2) |

Também mapeados: atendimento ao cidadão, órgãos de controle, equipe avaliadora.

**Dentro:** histórico de infrações por veículo, já autenticado, até os detalhes de uma infração; Portal (Chrome e Firefox no computador, Chrome no Android) e aplicativo 2.6.9 (Android de entrada e intermediário, iPhone); Wi-Fi, 4G e rede degradada simulada. Caixa-preta.

**Fora:** login, consulta pública de débitos, histórico por condutor, pagamento, recurso, indicação de condutor, veículo de outra UF, usabilidade.

**Fala (cerca de 1 min):** cada parte interessada tem um critério de sucesso e influenciou uma escolha. O cidadão em celular com rede ruim é a razão de termos a cobertura de contexto; a equipe técnica é o ponto de vista da eficiência de desempenho. No escopo, avaliamos só o histórico por veículo, a partir do menu de infrações, porque o login é diferente nos dois canais e distorceria a comparação. Cada corte tem uma justificativa no artigo. Os resultados valem só para as versões, os aparelhos e o período avaliados, e a amostra são veículos da própria equipe, com consentimento.
