# INC-01 — Falha ao buscar veículos no aplicativo

| Campo | Registro |
|---|---|
| Abertura documental | 22/11/2026, a partir do relato de 21/11 |
| Origem | S03 / B02 / CT05 / P6 / repetições 1–3 |
| Fonte | [Registro S03, commit 14ab804](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/14ab804210f4b1be2aaa84e1946d9e11079a9a28/evidencias/fase4/S03-registro-2026-11-21.md) |
| Contexto | Aplicativo Android 2.6.3; Wi-Fi; aparelho superior ao planejado (D006) |
| Pré-condição relatada | Titular autenticado; V1 com infração no portal; vínculo privado a conferir |
| Caminho | Infrações → Histórico de infrações por veículo → lista de veículos |
| Esperado | Lista carregada, seleção de V1 e acesso ao detalhe V1-I1 |
| Observado no relato | “Ocorreu um erro ao buscar os veículos, por favor, tente novamente mais tarde.”; lista inacessível |
| Recorrência | 3/3 falhas; não é estimativa populacional |
| Impacto | Interrupção da consulta antes da lista e do detalhe |
| Métrica e decisões | Q3.1/M3.1.1; D4 e D1 |
| Conferência | Philipe designado no relato; leitura independente pendente |
| Consentimento e vínculo | Conferência pendente com Hugo |
| Causa | Desconhecida; sem atribuição ao cliente, servidor, rede ou dados |
| Tratamento | Processo e matriz de regressão desta pasta |
| Encaminhamento | Não realizado; requisitante e equipe técnica são hipotéticos |
| Estado | Preliminar, aberto; correção no serviço não comprovada |

*Tabela 1 — Ficha de incidente. Fonte: S03 no commit indicado.*

## Fechamento após reavaliação

Registrar intervenção e versão, sessão/bloco, três resultados por contexto, conferente e data,
comparação com a referência e decisão **corrigido e reavaliado**, **persiste** ou **inconclusivo**.
Esta ficha não declara que essas atividades ocorreram. Nunca publicar identificadores, tokens
ou dados de autenticação na ficha ou nas capturas.
