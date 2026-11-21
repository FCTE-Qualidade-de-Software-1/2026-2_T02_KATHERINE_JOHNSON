# S01 — Registro recebido do portal no PC

## Proveniência e escopo

Transcrição do relatório `relatorio_portal_detran_df.pdf` fornecido pelo responsável pela coleta,
mais a tabela de dez repetições enviada separadamente na mesma solicitação. O relatório descreve
uma sessão S01, contexto PC-portal, canal portal, em 20/11/2026. Os códigos V1 e V1-I1 são usados
sem guardar a correspondência com pessoa ou veículo.

O arquivo-fonte informa horário de Brasília entre 21:38 e 21:41. Esse horário é posterior ao
primeiro relógio consultado durante a inspeção e anterior à revisão atual, às 21:54 de Brasília
em 20/11/2026; portanto, a cronologia é compatível com uma sessão ocorrida mais tarde no mesmo
dia. A tabela de dez repetições enviada com o PDF é tratada como atualização da medição. O PDF
anterior ainda descreve tempo e volume como não medidos; a tabela atualiza esses campos, mas não
informa método de marcação do tempo, instrumento/unidade-base do volume nem repetição de
aquecimento. Esses limites ficam explícitos e impedem validar a série como resultado oficial.

S01 é piloto e não entra nos resultados oficiais da Fase 4. Este registro preserva o que as fontes
relatam sem transformar o piloto em resultado oficial.

## A. Presença dos campos, conforme o relatório

O relatório informa que a primeira lista observada tinha 6 de 15 campos preenchidos. No detalhe
de V1-I1, informa 15 de 15 campos principais e 2 de 2 campos condicionais de velocidade. Os
valores não foram transcritos. Segundo o relatório, placa, órgão, número do auto, pontuação e
situação estavam presentes na lista; os demais campos principais estavam ausentes. No detalhe,
todos os campos principais e os dois campos de velocidade estavam presentes.

O relatório registra que a placa estava preenchida no filtro da consulta e que “Regulamento” e
“Data da Defesa Prévia” eram os rótulos vistos no detalhe. Esses fatos permanecem atribuídos ao
relatório fornecido.

## B. Fluxo e disponibilidade, conforme o relatório

| Repetição | Horário informado (Brasília) | Cliques/seleções | Transições | Rolagens manuais | Resultado |
|---:|---:|---:|---:|---:|---|
| 1 | 21:38:16 | 4 | 3 | 0 | lista concluída; detalhe observado |
| 2 | 21:40:50 | 4 | 3 | 0 | lista concluída; detalhe observado |
| 3 | 21:41:41 | 4 | 3 | 0 | lista concluída; detalhe observado |

O caminho descrito foi Infração → Histórico de infrações por veículo → Selecionar → Consultar.
O relatório afirma que o fluxo se repetiu nas três execuções e registra 3 de 3 detalhes abertos.
As rolagens para preparar imagens ocorreram fora do percurso. O relatório não quantifica possível
deslocamento automático da página.

## C. Capturas anonimizadas extraídas do relatório

As duas imagens abaixo foram extraídas como imagens raster incorporadas no PDF; os valores já
estão cobertos por pixels pretos na própria imagem extraída. A lista de veículos mostra cabeçalho
e linhas cobertas. O detalhe contém somente seis rótulos e não comprova todos os campos. O relatório
diz que a captura da lista de infrações foi omitida após a revisão de privacidade; ela não foi
extraída nem incluída.

| Arquivo no repositório | Alcance e limite |
|---|---|
| `capturas/S01/S01-portal-lista-veiculos.png` | Lista com valores cobertos; não identifica veículo. |
| `capturas/S01/S01-portal-detalhe-V1-I1-parcial.png` | Seis rótulos com valores cobertos; evidência parcial, não sustenta a contagem completa de campos. |
| Captura da lista de infrações | Não incluída: o relatório informa que o recorte não passou na revisão de privacidade. |

## D. Tempo e volume

O PDF informa que, quando foi gerado, não havia aquecimento nem tentativas cronometradas e que a
interface não expunha o total Transferred. A tabela de dez repetições fornecida junto ao PDF
atualiza esses valores. A tabela identifica as repetições, mas não traz timestamps/quadros, método
de timing, instrumento de volume, unidade-base nem aquecimento separado. As estatísticas abaixo
são cálculo descritivo dos números recebidos, não validação independente dos instrumentos.

| Repetição | Abrir lista (ms) | Abrir detalhe (ms) | Transferido (kB) |
|---:|---:|---:|---:|
| 1 | 842 | 472 | 38,6 |
| 2 | 765 | 438 | 38,4 |
| 3 | 913 | 521 | 38,7 |
| 4 | 801 | 459 | 38,5 |
| 5 | 788 | 447 | 38,6 |
| 6 | 956 | 536 | 38,8 |
| 7 | 826 | 483 | 38,4 |
| 8 | 874 | 498 | 38,6 |
| 9 | 752 | 424 | 38,5 |
| 10 | 819 | 466 | 38,7 |
| **Média aritmética** | **833,6** | **474,4** | **38,58** |
| **Mediana** | **822,5** | **469,0** | **38,6** |
| **P90 (posto mais próximo)** | **913** | **521** | **38,7** |

Não atribuir nível de qualidade nem incorporar esses valores ao cálculo automatizado como
resultado oficial. Para isso, a sessão precisa ter inventário correspondente, aquecimento
registrado, método de timing reproduzível e unidade/instrumento de transferência confirmados.
Como os valores estão associados ao piloto S01, eles também permanecem fora do cálculo oficial.

## Registros oficiais

Os CSV de resultados oficiais não recebem linhas desta sessão: S01 é piloto e a reconciliação dos
valores de tempo/volume não está comprovada pelos metadados do relatório. Use `docs/fase3-metodo.md` e
`dados/README.md` para lançar futuras sessões elegíveis, após execução e conferência independente.

### Capturas incluídas

![Lista de veículos do portal com linhas e valores cobertos por tarjas opacas](capturas/S01/S01-portal-lista-veiculos.png)

![Detalhe parcial do portal com os valores cobertos por tarjas opacas](capturas/S01/S01-portal-detalhe-V1-I1-parcial.png)
