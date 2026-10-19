# Conteúdo dos slides — Hugo (produto e modelo de qualidade)

Para o Pedro Henrique montar na apresentação. Figuras: `artigo/figuras/diagrama-contexto.tex` e `artigo/figuras/modelo-qualidade.tex` (TikZ, entram direto no Beamer).

## Slide 1 — O produto: Portal de Serviços × aplicativo

**Título:** A consulta de infrações em dois canais

| | Portal de Serviços | Aplicativo DETRAN-DF |
|---|---|---|
| Acesso | portal.detran.df.gov.br | Google Play e App Store, versão 2.6.9 |
| Login | CPF/CNPJ + senha + reCAPTCHA, ou gov.br | [VERIFICAR] |
| Abrangência | Só veículos do CPF logado | [VERIFICAR] |

Figura: diagrama de contexto (Figura 1 do artigo).

**Fala (cerca de 1 min):** os dois canais consultam o mesmo backend do Detran-DF, que também busca dados no RENAINF. Avaliamos só o que chega ao cidadão: campos, passos, tempo, dados transferidos e se a consulta conclui em cada contexto. Capacidade do servidor e correção absoluta dos dados ficam fora, porque a avaliação é caixa-preta. Como a consulta exige login do proprietário, a massa de dados depende de consentimento por escrito.

## Slide 2 — Modelo de qualidade adaptado

**Título:** Três características, oito subcaracterísticas

Figura: modelo de qualidade (Figura 2 do artigo).

Principais adaptações:
- Cobertura de contexto vem da ISO/IEC 25010:2011, porque a ISO/IEC 25019:2023 a removeu; as medidas seguem na ISO/IEC 25022:2016.
- Completude de contexto sem satisfação: só conclusão da consulta e tempo.
- Correção funcional como consistência entre canais.
- Apropriação funcional como contagem de passos, seguindo o exemplo da própria norma.
- Utilização de recursos só pela rede, único recurso medido igualmente nos dois canais.

**Fala (cerca de 1 min):** partimos do modelo de produto da 25010:2023 e do modelo de qualidade em uso de 2011. Cada inclusão e exclusão está justificada por uma parte interessada. Capacidade de interação, que é a antiga usabilidade, ficou fora por exigência da disciplina.
