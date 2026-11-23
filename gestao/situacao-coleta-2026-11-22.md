# KATHERINE JOHNSON: situação das Fases 3 e 4 em 22/11/2026

Avaliação portal × app do Detran-DF (FGA0315 QSW1). Este arquivo é a passagem de bastão da coleta:
o que já está feito, o que falta e os pontos de atenção.

## 1. Onde está cada coisa

| Branch | Conteúdo | Situação |
|---|---|---|
| `feat/piloto-s01` | Piloto S01 (Hugo e Philipe): registro, capturas, ambientes, desvios D011 e D012 e as páginas da Fase 3 sobre o piloto | No GitHub; falta PR/merge |
| `feat/pedro-s03-fase4` | Fase 3 (ambiente, massa, cronograma) e Fase 4: S03, S05 e S02 (P1–P3), scripts e desvios | No GitHub após o push deste commit; falta PR/merge |

- **Dados publicados:** `dados/brutos/*.csv` e os registros em `evidencias/fase4/`:
  - `S03-registro-2026-11-21.md`
  - `S05-registro-2026-11-22.md`
  - `S02-registro-2026-11-22.md`

  As capturas tarjadas ficam em `evidencias/fase4/capturas/`.
- **Material privado (fora do Git):** `dados/privado/S01/` e `dados/privado/S02/`, com:
  - gravações;
  - valores dos campos;
  - folhas de miniaturas usadas na contagem das transições.

  Esse material está **só no computador do Philipe** (Acer Nitro). Quem fizer a segunda leitura
  precisa recebê-lo por canal privado. **Não publicar.**
- **Scripts:**
  - P6: `dados/scripts/p6/` (portal e app).
  - S02: `dados/scripts/s02/` (P1–P5).
  - Cada pasta tem um `README.md` com os comandos.

## 2. O que foi feito

### Fase 3 (planejamento e piloto)

- Páginas da Fase 3 atualizadas: método, ambiente (com a Tabela 1a, inventário efetivo dos aparelhos), dados e cronograma.
- O **piloto S01** foi conduzido por Hugo e Philipe, com 11 verificações: 8 aprovadas, 1 parcial e 2 bloqueadas.
  - **Liberados:** P1, P2, P4 e P6.
  - **Parciais:** P3 e P5.
  - **Bloqueado:** P7.
- O computador usado para a depuração USB está registrado em cada sessão.

### Fase 4 (coleta)

Toda a coleta de 22/11 usou o **usuário A**, titular do veículo **V2**, com a infração **V2-I1**.

**P6 (S05):**

| Bloco | Contexto | Resultado | Situação |
|---|---|---|---|
| S05 B01 | CT05 app (Motorola edge 60 neo, app 2.7.0) | 3/3 concluídas | ✅ registrado |
| S05 B02 | CT02 portal (Firefox 160, Ubuntu) | 3/3 concluídas | ✅ registrado |
| S05 B03 | CT01 portal (Chrome 158, Ubuntu) | 3/3 concluídas | ✅ registrado |

- Com CT01 e CT02 no mesmo grupo, o computador passa a ter resultado na M3.1.1 para o V2.
- O problema de login gov.br no Firefox (D005) foi **resolvido**. Agora o login é feito sem controle remoto e o mesmo perfil é reaberto com controle remoto e restauração de sessão.

**S02 (referência, CT01 + CT05):**

| Protocolo | Resultado (1ª leitura) | Situação |
|---|---|---|
| P1 — presença dos campos | Lista: 5/15 nos dois canais. Detalhe: portal 17/17, app 16/17 (sem R14) | ✅ registrado; falta a 2ª leitura |
| P2 — comparação entre canais | 16 de 17 paritários; R14 ausente no app | ✅ registrado; falta a 2ª leitura |
| P3 — passos / transições / rolagens | Portal 4 / 3 / 0; app 6 / 5 / 2 (3 repetições iguais em cada canal) | ✅ registrado; falta a 2ª leitura |
| P4 — tempos | — | ⏳ não executado |
| P5 — volume | — | ⏳ não executado |

**Regra decidida para o P3 (D015):** abrir um diálogo que ocupa a tela conta como transição. Fechá-lo e voltar à tela anterior não conta.

**Desvios novos nesta branch:**
- D009, D010 e D013 (S05);
- D014 (S02 com o V2, executada por script, P4 e P5 pendentes);
- D015 (regra das transições).

**Validação da estrutura dos CSVs:** passa quando o campo `revisor` está preenchido. O
`calcular.py --validar` real (o do CI) **ainda falha** com "conferência independente pendente",
porque nenhuma linha tem revisor. Isso só se resolve com a revisão independente (item 3 da lista
de atenção).

## 3. O que falta

### Para fechar a S02

1. **Decidir quando começa a medição da M2.1.1.** A proposta é a partir do clique ou toque em "Consultar".
2. **P4:**
   - M2.1.1 e M2.1.2, com 1 aquecimento e 10 válidas por métrica e canal (44 medições mais aquecimentos);
   - marcação dos quadros nas gravações e 2ª leitura.
3. **P5:** M2.2.1, com 1 aquecimento e 10 válidas por canal (22 medições).
   - Portal: soma do `encodedDataLength`.
   - App: contador do UID.
   - Os escopos dos dois canais diferem.
4. Atualizar o `S02-registro-2026-11-22.md` e os CSVs `tempos.csv` e `volume.csv`.

O P4 e o P5 precisam do titular do V2 logado, do Motorola com depuração USB e do Chrome com
controle remoto.

### Outros

- CT03 (Chrome do Android) com o V2: opcional.
- Data e via do consentimento do titular do V2 e confirmação do código V2 (Hugo).
- CT04: continua pendente.
- Análise (#48), com os resultados do `calcular.py`.
- PRs e merge das duas branches.
- Declaração de uso de IA (`docs/declaracao-ia.md`): preencher **só quando tudo estiver finalizado**.

## 4. Lista de pontos de atenção

| # | Ponto | Situação |
|---|---|---|
| 1 | Registrar o computador usado na depuração USB em cada sessão | ✅ feito |
| 2 | Rede controlada (S04/P7) com os mesmos aparelhos: hotspot do Windows + clumsy + 4G do Motorola | ⏸️ adiado |
| 3 | Revisão independente: 2ª leitura de P2, P3 e P4, preenchimento do campo `revisor` e conferência das tarjas e metadados das capturas por outro integrante | ⏸️ adiado. Sem ela o CI não passa |
| 4 | Datas no Project 38 (Hugo) | ⏸️ adiado |
| 5 | Consolidar a tabela de critérios (#46) depois do merge | ⏸️ adiado |
