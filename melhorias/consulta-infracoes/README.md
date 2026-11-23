# Tratamento e regressão de falhas na consulta de infrações

Entrega técnica da #36: **proposta de processo com templates técnicos**, preparada em
22/11/2026. Responsável original da #36: Pedro Druck; apoio técnico nesta entrega: Hugo;
revisor designado: Daniel. A ação implementada é o procedimento de diagnóstico, encaminhamento e reavaliação
abaixo. Não foi alterado o código do Detran-DF nem comprovada redução de falhas no serviço.

## Achado e decisão apoiada

S03 de 21/11 relata **3/3 falhas** no aplicativo Android 2.6.3 (B02/CT05) ao buscar os veículos.
No mesmo estudo, o portal teve 3/3 conclusões em B01/CT01 e duas conclusões e uma expiração em
B03/CT03. Fonte imutável: [registro S03, commit 14ab804](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KATHERINE_JOHNSON/blob/14ab804210f4b1be2aaa84e1946d9e11079a9a28/evidencias/fase4/S03-registro-2026-11-21.md).

Os termos de consentimento foram aplicados, conforme confirmação de Hugo em 22/11/2026;
as vias assinadas permanecem privadas. São observações **preliminares**: conferência independente e conciliação do vínculo privado dos códigos dos
veículos ainda pendentes. O aparelho e a versão do aplicativo diferem do planejamento (D006).
Não sustentam ranking geral, causa técnica ou nível oficial. P6 não mede M3.2.2, exclusiva de
P7, e as execuções não são pares válidos de P2.

A interrupção antes da lista impede consultar os detalhes. Por isso se prioriza investigar
G3/Q3.1/M3.1.1, apoiando **D4** (plataformas com suporte) e **D1** (investimento). Um bloqueio
completo da tarefa precede a otimização de tempos ainda não medidos. Não se avalia usabilidade
nem se compara a recorrência com cenários sem execução.

## Procedimento entregue

| Etapa | Ação | Saída e condição |
|---|---|---|
| Conferir | Outro avaliador confere capturas, versão, código do veículo e consentimento. Só então preenche `revisor` | Ficha INC-01; sem conferência, achado preliminar |
| Reproduzir | Mesmo veículo, aparelho, versão e rede; titular autenticado; três tentativas P6 por contexto | Novo bloco oficial, inventário e evidência por tentativa; preservar S03 |
| Isolar configuração | Se houver intervenção ou atualização oficial, testar em bloco separado; registrar versões e demais mudanças | Matriz RG01–RG04; não presumir que atualizar corrige |
| Encaminhar | Preparar diagnóstico anonimizado com passos, mensagem e recorrência para a equipe técnica hipotética | Ficha pronta; nenhum envio externo realizado nesta entrega |
| Reavaliar | Após intervenção identificada, repetir P6 e comparar blocos equivalentes | Pelo menos 2/3 aprova o contexto; 3/3 é meta local de regressão, sem alterar a Fase 2 |
| Cobrir o escopo | Avaliar CT04/CT05/CT06 separadamente; declarar indisponíveis; recalcular conforme Fase 3 | Validação dos CSV e análise revisada na #48 |

*Tabela 1 — Tratamento e reavaliação. Fonte: S03 e procedimento P6 da Fase 3.*

O incidente termina como **corrigido e reavaliado**, **persiste** ou **inconclusivo**. Não reiniciar
a contagem para apagar falhas nem interpretar erro como ausência de infrações. Não trocar conta,
veículo ou versão silenciosamente. A eventual recomendação do portal (D3) depende de resultados
conferidos e se limita aos contextos avaliados.

## Artefatos e inspeção

- `incidente.md`: ficha técnica preenchida com o achado e suas lacunas.
- `regressao.csv`: quatro cenários planejados; não são tentativas executadas nem dados oficiais.
- `verificar.py`: inspeção offline das referências e da matriz; não consulta o Detran-DF.

```bash
python3 melhorias/consulta-infracoes/verificar.py
```

Os scripts P6 existentes na branch de coleta não são duplicados. Novas execuções usam
`dados/brutos/`, o inventário e os scripts de cálculo já existentes. O consentimento e os
originais permanecem privados; apenas evidências anonimizadas e revisadas podem ser publicadas.

## Aceitação e eficácia

O processo, a ficha e a matriz estão entregues e são descritos no artigo e em
`docs/fase4-melhoria.md`. A inspeção automática confere fonte imutável e quatro cenários P6.
A revisão humana designada a Daniel e a conferência da evidência permanecem pendentes;
não se atribui aprovação ao autor original da #36 ou ao conferente sem registro. A eficácia
sobre o produto só pode ser declarada após intervenção identificada e reavaliação equivalente.
