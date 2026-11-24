# Fase 4 — Ação de melhoria

**Atualização em 22/11/2026.** Foi entregue uma **proposta de processo com templates técnicos**
para tratar e reavaliar falhas na consulta. A entrega da
[issue #36](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/issues/36)
contém processo, ficha de incidente, matriz de regressão e inspeção automática. Sua revisão humana
permanece pendente. Não foi alterado o serviço do Detran-DF nem medida a eficácia da ação.

## Evidência e escolha {#evidencia}

O [registro S03 no commit 14ab804](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/14ab804210f4b1be2aaa84e1946d9e11079a9a28/evidencias/fase4/S03-registro-2026-11-21.md)
relata três falhas em três tentativas no aplicativo Android 2.6.3 (CT05/B02), ao buscar veículos.
No portal, CT01 teve três conclusões em três tentativas; CT03 teve duas conclusões e uma expiração.
Os consentimentos foram aplicados, conforme confirmação de Hugo em 22/11/2026; as vias assinadas
permanecem privadas. As contagens foram confirmadas na
[segunda leitura independente de P6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/main/evidencias/fase4/segunda-leitura-p4-p7-2026-11-23.md#4-p6--execução-por-contexto)
(23/11) e resultaram em M3.1.1 Inaceitável, 0/1 plataforma, nesse caso
([medições de M3.1.1](fase4-medicoes.md#m3-1-1)). O aparelho e a versão do aplicativo diferem do
planejamento (D006), e o CT05 com o aplicativo 2.7.0, em outro aparelho e veículo, concluiu 3 de 3.
Por isso não se atribui causa técnica nem superioridade geral. O achado pertence a Q3.1/P6, não às taxas de rede de P7.

O bloqueio completo antes da lista motiva priorizar a investigação de cobertura de contexto,
apoiando D4 (plataformas com suporte) e D1 (investimento), sem avaliar usabilidade. Não se compara
a recorrência com contextos não executados nem se presume o resultado final da #48.

## Entrega técnica {#entrega-tecnica}

| Item | Registro |
|---|---|
| Tipo da ação | Proposta de processo com templates técnicos |
| Processo e artefatos | [Pasta da melhoria](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/tree/main/melhorias/consulta-infracoes) |
| Fluxo entregue | Conferir incidente → reproduzir configuração → isolar intervenção → preparar diagnóstico → reavaliar |
| Templates | Ficha INC-01 preenchida com o achado e matriz RG01–RG04 com quatro cenários planejados |
| Métrica e decisões | G3/Q3.1/M3.1.1; D4 e D1 |
| Reavaliação | Três tentativas P6 por contexto/versão; mínimo 2/3 para aprovação; meta local 3/3, sem mudar os níveis da Fase 2 |
| Inspeção técnica | Script offline confere fonte imutável, condições e critérios da matriz; não executa consultas |
| Revisão humana | Daniel é o revisor designado da #36; aprovação não presumida |
| Eficácia no produto | Não medida; depende de intervenção identificada e nova execução equivalente |

*Tabela 1 — Rastreabilidade da ação. Fonte: S03, Fases 1–3 e issue #36.*

```bash
python3 melhorias/consulta-infracoes/verificar.py
```

A inspeção não substitui a revisão humana nem certifica correção do serviço. As novas execuções
usam os instrumentos existentes de P6; não houve duplicação dos scripts da branch de coleta.
Falhas permanecem no denominador, versões são separadas por bloco e contextos indisponíveis
ficam não avaliados. O incidente só pode ser encerrado como corrigido após reavaliação conferida.
