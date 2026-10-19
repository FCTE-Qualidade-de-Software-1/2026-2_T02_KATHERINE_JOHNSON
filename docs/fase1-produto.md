# Fase 1 — Descrição do Produto e Modelo de Qualidade

**Projeto Final FGA0315 Qualidade de Software 1 (UnB/FGA, 2026/2)**  
*Avaliação da consulta de infrações do Detran-DF: Portal de Serviços × aplicativo*  
*Responsável: Hugo Freitas Silva*  
*Data do levantamento: 18/10/2026*

---

## 1. Levantamento dos canais

### 1.1 Método do levantamento

O levantamento usou apenas informações acessíveis a qualquer cidadão, sem credenciais e sem acesso à infraestrutura do Detran-DF:

1. **Acesso público ao Portal de Serviços** em navegador desktop (Google Chrome, Linux), em 18/10/2026, com captura das telas públicas (ver Seção 1.6).
2. **Páginas oficiais do aplicativo** na Google Play e na App Store, e consulta à interface pública de busca da App Store (iTunes Lookup), em 18/10/2026.
3. **Inspeção do código cliente público do portal**, isto é, os arquivos que o próprio navegador baixa ao abrir a página e que qualquer usuário pode ver nas ferramentas de desenvolvedor. Essa inspeção não dá acesso ao código do servidor e serviu só para identificar rótulos de tela, rotas e serviços externos.

Itens que dependem de login com um veículo real ou de um aparelho com o aplicativo instalado estão marcados com **[VERIFICAR]** e serão confirmados na sessão de levantamento com a massa de dados (ver `dados/massa-de-dados.md`).

### 1.2 Identificação dos canais

| Item | Portal de Serviços | Aplicativo |
|---|---|---|
| Nome oficial | "Detran Digital", apresentado como "Portal de Serviços do Departamento de Trânsito do Distrito Federal (Detran/DF)" | "DETRAN-DF" nas duas lojas; a descrição na Google Play o chama de "DETRAN DIGITAL" |
| Endereço / identificador | <https://portal.detran.df.gov.br> | Android: `br.com.mesotec.detrandf` · iOS: `id1526746296` |
| Publicador | Detran-DF | App Store: "Departamento de Trânsito do Distrito Federal". Google Play: [VERIFICAR nome do desenvolvedor exibido] |
| Versão avaliada | Não há número de versão público; o pacote principal carregado em 18/10/2026 é `main-es2017.638a2c0c922c0af94e51.js` | 2.6.9 no iOS (publicada em 13/10/2026) e na Google Play (atualizada em 09/10/2026) [VERIFICAR versão instalada no aparelho de teste] |
| Primeira publicação | — | App Store: 17/08/2020 · Google Play: 14/08/2020 |
| Plataformas | Navegador em desktop e em celular | Android e iOS |
| Requisito mínimo | Não declarado [VERIFICAR navegadores suportados] | iOS 15.1 ou superior · Android: [VERIFICAR na página da Google Play, seção "Sobre este app"] |
| Tamanho do pacote | — | 41,5 MB no iOS |
| Instalações | — | Mais de 1 milhão na Google Play |
| Autenticação | CPF/CNPJ e senha, com reCAPTCHA, ou botão "Entrar com gov.br" | [VERIFICAR: conta própria do Detran-DF, gov.br ou ambas] |
| A consulta exige login? | Sim. As telas de infrações do veículo ficam na área logada e listam só os veículos vinculados ao CPF do usuário ("Veículos atuais de minha propriedade"). Há também a opção "Consultar veículo de outra UF". Não foi encontrada consulta de infrações por placa + RENAVAM sem login [VERIFICAR] | [VERIFICAR] |

### 1.3 Passos da consulta

Sequência provável no portal, deduzida das telas públicas e das rotas do código cliente. Deve ser refeita com um veículo real, contando cada tela e cada ação.

| # | Portal de Serviços | Aplicativo |
|---|---|---|
| 1 | Abrir <https://portal.detran.df.gov.br> | Abrir o aplicativo [VERIFICAR] |
| 2 | "Fazer login" e autenticar (CPF/CNPJ + senha + reCAPTCHA, ou gov.br) | Autenticar [VERIFICAR] |
| 3 | Menu "Infração" | [VERIFICAR] |
| 4 | Opção de histórico de infrações por veículo [VERIFICAR nome exato no menu] | [VERIFICAR] |
| 5 | Selecionar o veículo na lista "Veículos atuais de minha propriedade" | [VERIFICAR] |
| 6 | Ver a lista de infrações e escolher uma ("Selecione a multa desejada") | [VERIFICAR] |
| 7 | Ver a tela "Detalhes da infração" | [VERIFICAR] |

### 1.4 Campos exibidos por infração

A tela de detalhes do portal prevê os rótulos abaixo (extraídos do código cliente). Um rótulo previsto não garante que o dado apareça preenchido; a presença efetiva será conferida com veículo real. A coluna do aplicativo será preenchida no mesmo levantamento.

| Grupo | Rótulos previstos no portal | Aplicativo |
|---|---|---|
| Veículo | Placa · UF · Marca/Modelo | [VERIFICAR] |
| Identificação da infração | Infração · Descrição da Infração · Regulamento · Natureza · Auto Infração · Código Renainf · Órgão Autuador · Responsável pela Infração | [VERIFICAR] |
| Ocorrência | Data Infração · Hora Infração · Local da Infração · Velocidade Permitida · Velocidade Aferida | [VERIFICAR] |
| Prazos | Data da Notif. de Autuação · Data da Notif. de Penalidade · Data da Defesa Prévia · Identificação do Condutor Infrator · Data de Vencimento | [VERIFICAR] |
| Valores | Valor da Multa · Valor Correção · Valor Desconto · Valor Devido | [VERIFICAR] |
| Situação | Pontuação Infração/Status · Situação Pagamento · Situação Multa | [VERIFICAR] |

O campo "Código Renainf" traz a dica "Origem: RENAINF", o que indica que parte dos dados vem do Registro Nacional de Infrações de Trânsito, e não só da base do Detran-DF.

### 1.5 Lista de referência de campos (insumo para a questão Q1.1)

Para julgar a completude funcional sem depender de um dos canais como padrão, propõe-se uma lista de referência externa. Ela parte do conteúdo obrigatório do auto de infração (art. 280 do Código de Trânsito Brasileiro, Lei nº 9.503/1997) e acrescenta as informações de que o cidadão precisa para decidir o que fazer com a multa (pagar, recorrer, indicar condutor). Os textos legais foram conferidos no Planalto em 18/10/2026.

| ID | Campo de referência | Fundamento | Rótulo correspondente no portal |
|---|---|---|---|
| R01 | Tipificação da infração (código e descrição) | CTB, art. 280, I | Infração · Descrição da Infração |
| R02 | Enquadramento legal | Complementa o art. 280, I | Regulamento |
| R03 | Local da infração | CTB, art. 280, II | Local da Infração |
| R04 | Data da infração | CTB, art. 280, II | Data Infração |
| R05 | Hora da infração | CTB, art. 280, II | Hora Infração |
| R06 | Placa do veículo | CTB, art. 280, III | Placa |
| R07 | Marca/modelo do veículo | CTB, art. 280, III | Marca/Modelo |
| R08 | Órgão autuador | CTB, art. 280, V | Órgão Autuador |
| R09 | Número do auto de infração | Identifica a autuação em pagamento, defesa e recurso | Auto Infração |
| R10 | Natureza (gravidade) | CTB, art. 258 | Natureza |
| R11 | Pontuação | CTB, art. 259 | Pontuação Infração/Status |
| R12 | Valor da multa | CTB, art. 258 | Valor da Multa · Valor Devido |
| R13 | Data de vencimento | Necessária para pagar no prazo | Data de Vencimento |
| R14 | Prazo de defesa prévia ou de indicação do condutor | Necessário para exercer a defesa | Data da Defesa Prévia · Identificação do Condutor Infrator |
| R15 | Situação da infração | Indica se ainda há algo a fazer | Situação Pagamento · Situação Multa |

Ficam fora da lista os incisos IV (prontuário do condutor) e VI (assinatura do infrator) do art. 280, porque são dados pessoais que não fazem parte da consulta pelo proprietário. Velocidade permitida e aferida só se aplicam a infrações de velocidade e entram como campos condicionais, não na contagem geral. A definição da métrica e dos níveis cabe ao Philipe.

### 1.6 Evidências

| Arquivo | Conteúdo | Dados pessoais |
|---|---|---|
| `evidencias/fase1/portal-pagina-inicial-2026-10-18.png` | Página inicial pública do Portal de Serviços, com o nome oficial e o menu "Infração" | Nenhum (imagem ilustrativa do próprio portal) |
| `evidencias/fase1/portal-login-2026-10-18.png` | Tela de login: CPF/CNPJ, senha, reCAPTCHA e "Entrar com gov.br" | Nenhum (campos vazios) |

Prints pendentes, a fazer com veículo real e com tarja em placa, RENAVAM, CPF, nome, endereço e número do auto antes de entrar no repositório: lista de veículos, lista de infrações e detalhes de uma infração, nos dois canais. As regras de anonimização estão em `evidencias/fase1/README.md`.
