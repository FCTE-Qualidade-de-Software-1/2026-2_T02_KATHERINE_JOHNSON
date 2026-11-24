# S03, S05, S06 e S08 (P4 a P7) e pendência da S02 — registro da segunda leitura independente

Registro da conferência feita em 23/11/2026. Não contém valores pessoais: somente classificações,
timestamps das gravações e contagens de bytes. As gravações, as capturas originais e as saídas dos
instrumentos ficam em `dados/privado/`, que o Git ignora.

## 1. Identificação

| Item | Registro |
|---|---|
| Sessões conferidas | S03 (21/11), S05 (22/11), S06 (22/11) e S08 (22 e 23/11); pendência de P3 da S02 (22/11) |
| Conferente | Heitor. Não participou da S03 B01 a B03 nem da S05 (script supervisionado por Pedro Druck) nem da S06 e da S08 (executadas por Hugo) |
| S03 B04 (iPhone, CT06) | Heitor executou o bloco; conferido por Philipe em 23/11/2026 (3 concluídas, iguais à primeira leitura), com registro em [S03-CT06-iphone-registro-2026-11-22.md](S03-CT06-iphone-registro-2026-11-22.md) |
| Data da conferência | 23/11/2026 |
| Independência | O conferente declara que marcou os tempos e classificou as tentativas sem consultar os valores da primeira leitura (CSV, registros das sessões e propostas automáticas) |
| Tolerância de tempo | 0,050 s (três quadros a 60 qps), desvio D031: as gravações têm taxa variável e a taxa nominal não está registrada |
| Material | P6: capturas em `evidencias/fase4/capturas/` e registro privado da S03 (repetições sem captura). P4 e P7: gravações em `dados/privado/S02/V4/`, marcadas quadro a quadro pelo timestamp. P5: saídas do CDP e do `adb dumpsys netstats` em `dados/privado/S02/V4/` |

## 2. Resultado geral

| Procedimento | Linhas | Concordância | Divergência | Situação |
|---|---:|---:|---:|---|
| P3, S02 B02 rep. 2 (rolagens) | 1 | — | 1 (resolvida) | Decisão conjunta de Heitor e Pedro Druck: 1 rolagem (o script registrou 2) |
| P6, S03 B01 a B03 e S05 | 23 | 23 | 0 | Conferido |
| P6, S03 B04 | 3 | 3 | 0 | Conferido por Philipe |
| P4, tempos da S06 (com tempo) | 44 | 41 | 3 (resolvidas) | 3 tempos acima da tolerância, resolvidos em conjunto com Hugo (Seção 7) |
| P4, S06 B04 (bloco excluído) e B09 rep. 1 | 13 | 13 | 0 | Exclusão do B04 e `erro_instrumento` da B09 rep. 1 confirmados |
| P7, classificação das tentativas da S08 | 55 | 55 | 0 | Conferido |
| P7, tempos M3.2.3 da S08 (com tempo) | 52 | 50 | 2 (resolvidas) | 2 tempos acima da tolerância, resolvidos em conjunto com Hugo (Seção 7) |
| P5, volume da S06 | 22 | 22 | 0 | Conferido |

Nos 96 tempos comparados, 24 coincidem no mesmo quadro e 72 diferem; a diferença mediana é de
0,017 s, cerca de um quadro a 60 qps. As cinco divergências acima de 0,050 s estão na Seção 7.

Regra aplicada ao CSV: na concordância (diferença até 0,050 s), o valor da primeira leitura é
mantido e o `revisor` recebe "Heitor". Na divergência, o `revisor` fica vazio até a marcação
conjunta, como manda a Fase 3 (P4, passo 6).

## 3. P3 — pendência da S02

| Sessão | Bloco | Rep. | Rolagens (script) | Rolagens (conferente, 23/11) | Decisão final | Quem decidiu |
|---|---|---:|---:|---:|---:|---|
| S02 | B02 | 2 | 2 | 1 | 1 | Heitor e Pedro Druck, revendo juntos a gravação: há um único gesto efetivo de rolagem até a lista |

O `fluxo.csv` passa a registrar 1 rolagem nessa repetição. Passos e transições não mudam, e a
rolagem não entra na M1.3.1 nem na M1.3.2.

## 4. P6 — execução por contexto

| Sessão | Bloco | Canal / contexto | Rep. | Primeira leitura | Segunda leitura | Resultado |
|---|---|---|---:|---|---|---|
| S03 | B01 | portal / CT01 | 1 | erro_instrumento | erro_instrumento | Concordância |
| S03 | B01 | portal / CT01 | 2 | erro_instrumento | erro_instrumento | Concordância |
| S03 | B01 | portal / CT01 | 3 | erro_instrumento | erro_instrumento | Concordância |
| S03 | B01 | portal / CT01 | 4 | erro_instrumento | erro_instrumento | Concordância |
| S03 | B01 | portal / CT01 | 5 | erro_instrumento | erro_instrumento | Concordância |
| S03 | B01 | portal / CT01 | 6 | concluida | concluida | Concordância |
| S03 | B01 | portal / CT01 | 7 | concluida | concluida | Concordância |
| S03 | B01 | portal / CT01 | 8 | concluida | concluida | Concordância |
| S03 | B02 | aplicativo / CT05 | 1 | falha | falha | Concordância |
| S03 | B02 | aplicativo / CT05 | 2 | falha | falha | Concordância |
| S03 | B02 | aplicativo / CT05 | 3 | falha | falha | Concordância |
| S03 | B03 | portal / CT03 | 1 | concluida | concluida | Concordância |
| S03 | B03 | portal / CT03 | 2 | concluida | concluida | Concordância |
| S03 | B03 | portal / CT03 | 3 | sessao_expirada | sessao_expirada | Concordância |
| S05 | B01 | aplicativo / CT05 | 1 | concluida | concluida | Concordância |
| S05 | B01 | aplicativo / CT05 | 2 | concluida | concluida | Concordância |
| S05 | B01 | aplicativo / CT05 | 3 | concluida | concluida | Concordância |
| S05 | B02 | portal / CT02 | 1 | concluida | concluida | Concordância |
| S05 | B02 | portal / CT02 | 2 | concluida | concluida | Concordância |
| S05 | B02 | portal / CT02 | 3 | concluida | concluida | Concordância |
| S05 | B03 | portal / CT01 | 1 | concluida | concluida | Concordância |
| S05 | B03 | portal / CT01 | 2 | concluida | concluida | Concordância |
| S05 | B03 | portal / CT01 | 3 | concluida | concluida | Concordância |

Na S03 B01, as repetições 1 a 5 foram falhas da ferramenta (aviso inicial sobre o menu, seletor do
menu e calendário que não abriu no primeiro clique), e não do serviço; elas foram repostas pelas
repetições 6 a 8. Na S03 B02, as três tentativas exibiram a mesma mensagem de erro do serviço ao
buscar os veículos. Na S03 B03, a repetição 3 voltou à tela de acesso por expiração da sessão.

## 5. P4 — tempos da S06

Tempos em segundos, marcados pelo timestamp do quadro. "Dif." é segunda menos primeira leitura.

### S06 B03 — M2.1.1, portal

| Rep. | Aquec. | Resultado (1ª / 2ª) | Início 1ª | Fim 1ª | Tempo 1ª | Início 2ª | Fim 2ª | Tempo 2ª | Dif. | Situação |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | sim | concluida / concluida | 1,266982 | 1,416989 | 0,150007 | 1,283804 | 1,449982 | 0,166178 | +0,016171 | Concordância |
| 2 |  | concluida / concluida | 1,252597 | 1,402608 | 0,150011 | 1,269617 | 1,402608 | 0,132991 | -0,017020 | Concordância |
| 3 |  | concluida / concluida | 1,259378 | 1,942706 | 0,683328 | 1,259378 | 1,942706 | 0,683328 | +0,000000 | Concordância |
| 4 |  | concluida / concluida | 1,251118 | 1,419008 | 0,16789 | 1,251118 | 1,419008 | 0,167890 | +0,000000 | Concordância |
| 5 |  | concluida / concluida | 1,250922 | 1,370953 | 0,120031 | 1,250922 | 1,370953 | 0,120031 | +0,000000 | Concordância |
| 6 |  | concluida / concluida | 1,248239 | 1,94824 | 0,700001 | 1,248239 | 2,014517 | 0,766278 | +0,066277 | **Divergência** |
| 7 |  | concluida / concluida | 1,256747 | 1,423423 | 0,166676 | 1,273380 | 1,423423 | 0,150043 | -0,016633 | Concordância |
| 8 |  | concluida / concluida | 1,250944 | 1,372855 | 0,121911 | 1,250944 | 1,339780 | 0,088836 | -0,033075 | Concordância |
| 9 |  | concluida / concluida | 1,273611 | 1,3903 | 0,116689 | 1,273611 | 1,373890 | 0,100279 | -0,016410 | Concordância |
| 10 |  | concluida / concluida | 1,265747 | 1,405981 | 0,140234 | 1,249473 | 1,405981 | 0,156508 | +0,016274 | Concordância |
| 11 |  | concluida / concluida | 1,255065 | 1,363944 | 0,108879 | 1,255065 | 1,363944 | 0,108879 | +0,000000 | Concordância |

### S06 B05 — M2.1.2, portal

| Rep. | Aquec. | Resultado (1ª / 2ª) | Início 1ª | Fim 1ª | Tempo 1ª | Início 2ª | Fim 2ª | Tempo 2ª | Dif. | Situação |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | sim | concluida / concluida | 1,25549 | 1,589767 | 0,334277 | 1,255490 | 1,573005 | 0,317515 | -0,016762 | Concordância |
| 2 |  | concluida / concluida | 1,25171 | 1,385039 | 0,133329 | 1,251710 | 1,418524 | 0,166814 | +0,033485 | Concordância |
| 3 |  | concluida / concluida | 1,257018 | 1,426565 | 0,169547 | 1,257018 | 1,409936 | 0,152918 | -0,016629 | Concordância |
| 4 |  | concluida / concluida | 1,248778 | 1,385165 | 0,136387 | 1,265254 | 1,401458 | 0,136204 | -0,000183 | Concordância |
| 5 |  | concluida / concluida | 1,245964 | 1,38449 | 0,138526 | 1,245964 | 1,384490 | 0,138526 | +0,000000 | Concordância |
| 6 |  | concluida / concluida | 1,25495 | 1,388278 | 0,133328 | 1,254950 | 1,371379 | 0,116429 | -0,016899 | Concordância |
| 7 |  | concluida / concluida | 1,245264 | 1,381195 | 0,135931 | 1,262064 | 1,414530 | 0,152466 | +0,016535 | Concordância |
| 8 |  | concluida / concluida | 1,239091 | 1,373669 | 0,134578 | 1,239091 | 1,373669 | 0,134578 | +0,000000 | Concordância |
| 9 |  | concluida / concluida | 1,253513 | 1,386841 | 0,133328 | 1,253513 | 1,403915 | 0,150402 | +0,017074 | Concordância |
| 10 |  | concluida / concluida | 1,249553 | 1,399547 | 0,149994 | 1,249553 | 1,383015 | 0,133462 | -0,016532 | Concordância |
| 11 |  | concluida / concluida | 1,247968 | 1,401038 | 0,15307 | 1,247968 | 1,401038 | 0,153070 | +0,000000 | Concordância |

### S06 B09 — M2.1.1, aplicativo (substitui o B04)

| Rep. | Aquec. | Resultado (1ª / 2ª) | Início 1ª | Fim 1ª | Tempo 1ª | Início 2ª | Fim 2ª | Tempo 2ª | Dif. | Situação |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 |  | erro_instrumento / erro_instrumento | — | — | — | — | — | — | — | Concordância (sem tempo) |
| 2 | sim | concluida / concluida | 2,130978 | 7,430067 | 5,299089 | 2,115554 | 7,430067 | 5,314513 | +0,015424 | Concordância |
| 3 |  | concluida / concluida | 1,452122 | 2,293878 | 0,841756 | 1,452122 | 2,260937 | 0,808815 | -0,032941 | Concordância |
| 4 |  | concluida / concluida | 1,836433 | 2,277822 | 0,441389 | 1,821058 | 2,258708 | 0,437650 | -0,003739 | Concordância |
| 5 |  | concluida / concluida | 1,438267 | 2,170656 | 0,732389 | 1,438267 | 2,170656 | 0,732389 | +0,000000 | Concordância |
| 6 |  | concluida / concluida | 1,8957 | 2,286656 | 0,390956 | 1,910829 | 2,304223 | 0,393394 | +0,002438 | Concordância |
| 7 |  | concluida / concluida | 1,356267 | 2,172644 | 0,816378 | 1,375117 | 2,172644 | 0,797527 | -0,018851 | Concordância |
| 8 |  | concluida / concluida | 1,427556 | 2,253367 | 0,825811 | 1,427556 | 2,253367 | 0,825811 | +0,000000 | Concordância |
| 9 |  | concluida / concluida | 1,418578 | 2,276922 | 0,858344 | 1,418578 | 2,292205 | 0,873627 | +0,015283 | Concordância |
| 10 |  | concluida / concluida | 1,505978 | 2,172822 | 0,666844 | 1,505978 | 2,172822 | 0,666844 | +0,000000 | Concordância |
| 11 |  | concluida / concluida | 1,4849 | 2,435711 | 0,950811 | 1,469536 | 2,484922 | 1,015386 | +0,064575 | **Divergência** |
| 12 |  | concluida / concluida | 1,749633 | 2,114756 | 0,365122 | 1,749633 | 2,146598 | 0,396965 | +0,031843 | Concordância |

### S06 B06 — M2.1.2, aplicativo

| Rep. | Aquec. | Resultado (1ª / 2ª) | Início 1ª | Fim 1ª | Tempo 1ª | Início 2ª | Fim 2ª | Tempo 2ª | Dif. | Situação |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | sim | concluida / concluida | 1,371756 | 1,987711 | 0,615956 | 1,354313 | 2,004895 | 0,650582 | +0,034626 | Concordância |
| 2 |  | concluida / concluida | 1,434644 | 2,008844 | 0,5742 | 1,434644 | 1,991588 | 0,556944 | -0,017256 | Concordância |
| 3 |  | concluida / concluida | 1,406811 | 2,0309 | 0,624089 | 1,406811 | 2,047785 | 0,640974 | +0,016885 | Concordância |
| 4 |  | concluida / concluida | 1,393533 | 1,959633 | 0,5661 | 1,393533 | 1,974215 | 0,580682 | +0,014582 | Concordância |
| 5 |  | concluida / concluida | 1,410489 | 2,009144 | 0,598656 | 1,410489 | 2,026606 | 0,616117 | +0,017461 | Concordância |
| 6 |  | concluida / concluida | 1,2807 | 2,096656 | 0,815956 | 1,295125 | 2,116442 | 0,821317 | +0,005361 | Concordância |
| 7 |  | concluida / concluida | 1,464789 | 2,229289 | 0,7645 | 1,464789 | 2,212251 | 0,747462 | -0,017038 | Concordância |
| 8 |  | concluida / concluida | 1,434822 | 2,251556 | 0,816733 | 1,434822 | 2,319901 | 0,885079 | +0,068346 | **Divergência** |
| 9 |  | concluida / concluida | 1,454122 | 2,212011 | 0,757889 | 1,434675 | 2,195818 | 0,761143 | +0,003254 | Concordância |
| 10 |  | concluida / concluida | 1,498967 | 2,156978 | 0,658011 | 1,538084 | 2,192672 | 0,654588 | -0,003423 | Concordância |
| 11 |  | concluida / concluida | 1,573211 | 2,196978 | 0,623767 | 1,573211 | 2,162432 | 0,589221 | -0,034546 | Concordância |

### S06 B04 — M2.1.1, aplicativo (excluído do cálculo)

O conferente assistiu às 12 gravações e confirmou a exclusão: a lista fica abaixo da área visível
e a gravação contém as pausas do script para rolar, então o intervalo definido no método não pode
ser isolado. A repetição 3 foi interrompida pelo instrumento na preparação. As 12 linhas ficam sem
tempo e com `revisor`.

## 6. P7 — tentativas e tempos M3.2.3 da S08

Tempos em segundos, marcados pelo timestamp do quadro. "Dif." é segunda menos primeira leitura.

### S08 B10 — portal, Wi-Fi

| Rep. | Aquec. | Resultado (1ª / 2ª) | Início 1ª | Fim 1ª | Tempo 1ª | Início 2ª | Fim 2ª | Tempo 2ª | Dif. | Situação |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | sim | concluida / concluida | 1,244356 | 1,377685 | 0,133329 | 1,244356 | 1,411017 | 0,166661 | +0,033332 | Concordância |
| 2 |  | concluida / concluida | 1,241503 | 1,324832 | 0,083329 | 1,241503 | 1,324832 | 0,083329 | +0,000000 | Concordância |
| 3 |  | concluida / concluida | 1,253015 | 1,336345 | 0,08333 | 1,253015 | 1,319678 | 0,066663 | -0,016667 | Concordância |
| 4 |  | concluida / concluida | 1,252844 | 1,319508 | 0,066664 | 1,252844 | 1,319508 | 0,066664 | +0,000000 | Concordância |
| 5 |  | concluida / concluida | 1,233313 | 1,283311 | 0,049998 | 1,233313 | 1,299979 | 0,066666 | +0,016668 | Concordância |
| 6 |  | concluida / concluida | 1,238571 | 1,321901 | 0,08333 | 1,238571 | 1,321901 | 0,083330 | +0,000000 | Concordância |
| 7 |  | concluida / concluida | 1,249389 | 1,299387 | 0,049998 | 1,249389 | 1,299387 | 0,049998 | +0,000000 | Concordância |
| 8 |  | concluida / concluida | 1,24068 | 1,32401 | 0,08333 | 1,257348 | 1,340676 | 0,083328 | -0,000002 | Concordância |
| 9 |  | concluida / concluida | 1,243573 | 1,326907 | 0,083334 | 1,226905 | 1,326907 | 0,100002 | +0,016668 | Concordância |
| 10 |  | concluida / concluida | 1,24485 | 1,311514 | 0,066664 | 1,244850 | 1,294847 | 0,049997 | -0,016667 | Concordância |
| 11 |  | concluida / concluida | 1,246579 | 1,329909 | 0,08333 | 1,246579 | 1,329909 | 0,083330 | +0,000000 | Concordância |

### S08 B12 — portal, rede degradada

| Rep. | Aquec. | Resultado (1ª / 2ª) | Início 1ª | Fim 1ª | Tempo 1ª | Início 2ª | Fim 2ª | Tempo 2ª | Dif. | Situação |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | sim | falha / falha | — | — | — | — | — | — | — | Concordância (sem tempo) |
| 2 |  | falha / falha | — | — | — | — | — | — | — | Concordância (sem tempo) |
| 3 |  | concluida / concluida | 1,216648 | 2,716659 | 1,500011 | 1,216648 | 2,783327 | 1,566679 | +0,066668 | **Divergência** |
| 4 |  | concluida / concluida | 1,216649 | 2,133334 | 0,916685 | 1,216649 | 2,133334 | 0,916685 | +0,000000 | Concordância |
| 5 |  | concluida / concluida | 1,233304 | 2,09999 | 0,866686 | 1,249972 | 2,099990 | 0,850018 | -0,016668 | Concordância |
| 6 |  | tempo_limite / tempo_limite | — | — | — | — | — | — | — | Concordância (sem tempo) |
| 7 |  | concluida / concluida | 1,233308 | 2,049992 | 0,816684 | 1,216640 | 2,033326 | 0,816686 | +0,000002 | Concordância |
| 8 |  | concluida / concluida | 1,216638 | 2,033321 | 0,816683 | 1,216638 | 2,016654 | 0,800016 | -0,016667 | Concordância |
| 9 |  | concluida / concluida | 1,233309 | 2,016654 | 0,783345 | 1,233309 | 2,016654 | 0,783345 | +0,000000 | Concordância |
| 10 |  | concluida / concluida | 1,233308 | 2,06696 | 0,833652 | 1,233308 | 2,083626 | 0,850318 | +0,016666 | Concordância |
| 11 |  | concluida / concluida | 1,215705 | 2,149047 | 0,933342 | 1,199038 | 2,165713 | 0,966675 | +0,033333 | Concordância |

### S08 B14 — portal, 4G

| Rep. | Aquec. | Resultado (1ª / 2ª) | Início 1ª | Fim 1ª | Tempo 1ª | Início 2ª | Fim 2ª | Tempo 2ª | Dif. | Situação |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | sim | concluida / concluida | 1,248055 | 1,448047 | 0,199992 | 1,248055 | 1,431380 | 0,183325 | -0,016667 | Concordância |
| 2 |  | concluida / concluida | 1,24379 | 1,493781 | 0,249991 | 1,243790 | 1,460448 | 0,216658 | -0,033333 | Concordância |
| 3 |  | concluida / concluida | 1,254584 | 1,387912 | 0,133328 | 1,271251 | 1,387912 | 0,116661 | -0,016667 | Concordância |
| 4 |  | concluida / concluida | 1,251331 | 1,401325 | 0,149994 | 1,267999 | 1,401325 | 0,133326 | -0,016668 | Concordância |
| 5 |  | concluida / concluida | 1,245863 | 1,362526 | 0,116663 | 1,245863 | 1,362526 | 0,116663 | +0,000000 | Concordância |
| 6 |  | concluida / concluida | 1,255025 | 1,388353 | 0,133328 | 1,255025 | 1,388353 | 0,133328 | +0,000000 | Concordância |
| 7 |  | concluida / concluida | 1,256406 | 1,439732 | 0,183326 | 1,239740 | 1,439732 | 0,199992 | +0,016666 | Concordância |
| 8 |  | concluida / concluida | 1,238889 | 1,372217 | 0,133328 | 1,238889 | 1,388884 | 0,149995 | +0,016667 | Concordância |
| 9 |  | concluida / concluida | 1,244524 | 1,361186 | 0,116662 | 1,227857 | 1,377853 | 0,149996 | +0,033334 | Concordância |
| 10 |  | concluida / concluida | 1,248615 | 1,39861 | 0,149995 | 1,248615 | 1,398610 | 0,149995 | +0,000000 | Concordância |
| 11 |  | concluida / concluida | 1,250526 | 1,40052 | 0,149994 | 1,250526 | 1,400520 | 0,149994 | +0,000000 | Concordância |

### S08 B11 — aplicativo, Wi-Fi

| Rep. | Aquec. | Resultado (1ª / 2ª) | Início 1ª | Fim 1ª | Tempo 1ª | Início 2ª | Fim 2ª | Tempo 2ª | Dif. | Situação |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | sim | concluida / concluida | 1,556144 | 1,936622 | 0,380478 | 1,570198 | 1,966697 | 0,396499 | +0,016021 | Concordância |
| 2 |  | concluida / concluida | 1,914333 | 2,314033 | 0,3997 | 1,942734 | 2,296631 | 0,353897 | -0,045803 | Concordância |
| 3 |  | concluida / concluida | 1,577322 | 2,244133 | 0,666811 | 1,577322 | 2,244133 | 0,666811 | +0,000000 | Concordância |
| 4 |  | concluida / concluida | 1,736256 | 2,077644 | 0,341389 | 1,736256 | 2,111178 | 0,374922 | +0,033533 | Concordância |
| 5 |  | concluida / concluida | 1,994811 | 2,410589 | 0,415778 | 1,994811 | 2,376348 | 0,381537 | -0,034241 | Concordância |
| 6 |  | concluida / concluida | 1,780878 | 2,130711 | 0,349833 | 1,795536 | 2,148684 | 0,353148 | +0,003315 | Concordância |
| 7 |  | concluida / concluida | 1,856867 | 2,3071 | 0,450233 | 1,856867 | 2,307100 | 0,450233 | +0,000000 | Concordância |
| 8 |  | concluida / concluida | 1,900556 | 2,292033 | 0,391478 | 1,900556 | 2,272416 | 0,371860 | -0,019618 | Concordância |
| 9 |  | concluida / concluida | 2,072433 | 2,4052 | 0,332767 | 2,072433 | 2,390606 | 0,318173 | -0,014594 | Concordância |
| 10 |  | concluida / concluida | 1,793822 | 2,285633 | 0,491811 | 1,812718 | 2,269598 | 0,456880 | -0,034931 | Concordância |
| 11 |  | concluida / concluida | 1,512556 | 2,3704 | 0,857844 | 1,496881 | 2,353101 | 0,856220 | -0,001624 | Concordância |

### S08 B15 — aplicativo, 4G

| Rep. | Aquec. | Resultado (1ª / 2ª) | Início 1ª | Fim 1ª | Tempo 1ª | Início 2ª | Fim 2ª | Tempo 2ª | Dif. | Situação |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | sim | concluida / concluida | 1,800433 | 2,200733 | 0,4003 | 1,800433 | 2,237497 | 0,437064 | +0,036764 | Concordância |
| 2 |  | concluida / concluida | 1,998867 | 2,380622 | 0,381756 | 1,966403 | 2,380622 | 0,414219 | +0,032463 | Concordância |
| 3 |  | concluida / concluida | 1,437389 | 2,400189 | 0,9628 | 1,420137 | 2,414326 | 0,994189 | +0,031389 | Concordância |
| 4 |  | concluida / concluida | 1,929478 | 2,261867 | 0,332389 | 1,962139 | 2,261867 | 0,299728 | -0,032661 | Concordância |
| 5 |  | concluida / concluida | 1,505122 | 2,322178 | 0,817056 | 1,471472 | 2,322178 | 0,850706 | +0,033650 | Concordância |
| 6 |  | concluida / concluida | 2,207411 | 3,0733 | 0,865889 | 2,191328 | 3,121095 | 0,929767 | +0,063878 | **Divergência** |
| 7 |  | concluida / concluida | 2,261 | 2,896256 | 0,635256 | 2,261000 | 2,896256 | 0,635256 | +0,000000 | Concordância |
| 8 |  | concluida / concluida | 1,437444 | 2,305767 | 0,868322 | 1,453433 | 2,322953 | 0,869520 | +0,001198 | Concordância |
| 9 |  | concluida / concluida | 1,420856 | 2,363011 | 0,942156 | 1,403050 | 2,345270 | 0,942220 | +0,000064 | Concordância |
| 10 |  | concluida / concluida | 1,942133 | 2,266711 | 0,324578 | 1,904732 | 2,266711 | 0,361979 | +0,037401 | Concordância |
| 11 |  | concluida / concluida | 1,8714 | 2,289078 | 0,417678 | 1,871400 | 2,325240 | 0,453840 | +0,036162 | Concordância |

As classificações de `tentativas.csv` e de `tempos.csv` coincidem nas 55 tentativas. Na rede
degradada (B12), as duas falhas na preparação (incluindo o aquecimento) foram confirmadas como falha
do serviço e continuam no denominador (D023); a repetição 6 passou de 60 s sem a lista (tempo limite).

## 7. Divergências e decisão conjunta com o Hugo

| Sessão | Bloco | Rep. | Tempo 1ª | Tempo 2ª | Dif. | Observação do conferente |
|---|---|---:|---:|---:|---:|---|
| S06 | B03 | 6 | 0,700001 | 0,766278 | +0,066277 | Tabela piscou antes de estabilizar; fim marcado 4 quadros depois |
| S06 | B09 | 11 | 0,950811 | 1,015386 | +0,064575 | Rolagem desacelerou aos poucos; estabilização marcada mais adiante |
| S06 | B06 | 8 | 0,816733 | 0,885079 | +0,068346 | Transição suave até o detalhe; fim marcado após sumir o carregamento |
| S08 | B12 | 3 | 1,500011 | 1,566679 | +0,066668 | Carregamento picotado na rede degradada; lista estabilizou depois |
| S08 | B15 | 6 | 0,865889 | 0,929767 | +0,063878 | Rolagem no 4G com atraso na renderização dos últimos itens |

Nas cinco, o conferente marcou o fim mais tarde que a proposta automática, porque a tela ainda
mudava depois do quadro proposto.

**Decisão conjunta (23/11/2026).** Heitor, Hugo (executor da S06 e da S08) e Philipe reviram as
cinco marcações e decidiram registrar a **marcação da segunda leitura** como valor final, porque a
tela ainda mudava depois do quadro da proposta automática. O `tempos.csv` passou a ter esses
valores (início, fim e tempo) e o `revisor` "Heitor e Hugo" nas cinco linhas.

## 8. P5 — volume da S06

| Bloco | Canal | Rep. | Aquec. | Bytes 1ª | Bytes 2ª | Resultado |
|---|---|---:|---|---:|---:|---|
| B07 | portal | 1 | sim | 10720 | 10720 | Concordância |
| B07 | portal | 2 |  | 10701 | 10701 | Concordância |
| B07 | portal | 3 |  | 10702 | 10702 | Concordância |
| B07 | portal | 4 |  | 10701 | 10701 | Concordância |
| B07 | portal | 5 |  | 10700 | 10700 | Concordância |
| B07 | portal | 6 |  | 10703 | 10703 | Concordância |
| B07 | portal | 7 |  | 10701 | 10701 | Concordância |
| B07 | portal | 8 |  | 10702 | 10702 | Concordância |
| B07 | portal | 9 |  | 10702 | 10702 | Concordância |
| B07 | portal | 10 |  | 10700 | 10700 | Concordância |
| B07 | portal | 11 |  | 10707 | 10707 | Concordância |
| B08 | aplicativo | 1 | sim | 77691 | 77691 | Concordância |
| B08 | aplicativo | 2 |  | 69623 | 69623 | Concordância |
| B08 | aplicativo | 5 |  | 57554 | 57554 | Concordância |
| B08 | aplicativo | 6 |  | 69709 | 69709 | Concordância |
| B08 | aplicativo | 7 |  | 59997 | 59997 | Concordância |
| B08 | aplicativo | 8 |  | 87811 | 87811 | Concordância |
| B08 | aplicativo | 9 |  | 67794 | 67794 | Concordância |
| B08 | aplicativo | 10 |  | 63629 | 63629 | Concordância |
| B08 | aplicativo | 11 |  | 57353 | 57353 | Concordância |
| B08 | aplicativo | 12 |  | 66189 | 66189 | Concordância |
| B08 | aplicativo | 13 |  | 60268 | 60268 | Concordância |

O volume é leitura de contador, não marcação de quadro: o conferente refez a soma do
`encodedDataLength` (portal) e a diferença do contador por UID (aplicativo) nas saídas privadas.
No B08, as repetições 3 e 4 não existem porque a conexão USB caiu na preparação, como mostram as
saídas privadas.

## 9. Resultado da conferência

Todas as linhas de `fluxo.csv`, `tentativas.csv`, `tempos.csv` e `volume.csv` têm `revisor`.
O `dados/scripts/calcular.py` foi rodado em 23/11/2026, depois das decisões acima, e gerou os
resultados oficiais em `dados/consolidados/resultados-metricas.csv` (42 resultados calculados).

## 10. Referências

- Primeira leitura: `dados/brutos/tentativas.csv`, `tempos.csv`, `volume.csv` e `fluxo.csv`, e os
  registros [S03](S03-registro-2026-11-21.md), [S05](S05-registro-2026-11-22.md),
  [S06](S06-registro-2026-11-22.md) e [S08](S08-registro-2026-11-22.md).
- Método: [Método e instruções para o avaliador](../../docs/fase3-metodo.md) (P4 a P7 e conferência
  por um segundo avaliador); limite de divergência no [modelo de sessão](modelo-sessao.md).
- Desvio D031 em `dados/brutos/desvios.csv`.
