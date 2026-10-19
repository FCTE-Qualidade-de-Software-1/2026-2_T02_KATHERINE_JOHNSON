# Roteiro da Sessão de Levantamento com Veículo Real

**Objetivo:** fechar os itens da issue #5 que só podem ser verificados com login: prints das telas logadas, contagem de passos, campos efetivamente exibidos e os itens pendentes de `docs/fase1-produto.md`.  
**Duração estimada:** 40 minutos por veículo.  
**Responsável:** Hugo Freitas Silva, com o proprietário do veículo presente.

## 1. Antes da sessão

- [ ] Termo de consentimento assinado (`dados/consentimento.md`) e código do veículo atribuído (V1, V2...).
- [ ] Aplicativo DETRAN-DF instalado e atualizado no aparelho de teste; anotar versão em Configurações > Apps.
- [ ] Navegador Chrome atualizado no computador de teste.
- [ ] Gravação de tela ligada nos dois aparelhos (servirá também para contar passos).
- [ ] Rede Wi-Fi estável; anotar o tipo de rede no formulário.

## 2. Durante a sessão

O proprietário digita a própria senha. A equipe não anota nem guarda credenciais.

Para cada canal (portal no computador, aplicativo no celular):

1. Abrir o canal e iniciar a gravação.
2. Fazer login. Para o portal, anotar o caminho usado (CPF + senha + reCAPTCHA ou gov.br).
3. Ir até "Histórico de infrações por veículo", anotando o nome exato de cada menu e botão.
4. Selecionar o veículo e abrir a lista de infrações.
5. Abrir o detalhamento de uma infração (de preferência, uma de velocidade e uma de outro órgão).
6. Capturar as telas da Seção 4.
7. Sair da conta e encerrar a gravação.

## 3. Formulário (preencher e copiar para `docs/fase1-produto.md`)

| Item | Portal de Serviços | Aplicativo |
|---|---|---|
| Data e hora da sessão | | |
| Aparelho, sistema e navegador ou versão do app | | |
| Rede | | |
| Rótulo do item de menu do passo 3 | | |
| Rótulo da tela de seleção do veículo (passo 5) | | |
| Número de telas do login até o detalhamento | | |
| Número de ações (toques/cliques) do login até o detalhamento | | |
| Campos da lista de referência (R01 a R15) exibidos preenchidos | | |
| Campos exibidos que não estão na lista de referência | | |
| Divergências entre canais para a mesma infração | | |
| Comportamento sem rede (desligar a rede na lista de infrações) | | |

## 4. Prints a capturar

| Arquivo | Tela |
|---|---|
| `portal-lista-veiculos-<data>.png` / `app-android-lista-veiculos-<data>.png` | Lista de veículos |
| `portal-lista-infracoes-<data>.png` / `app-android-lista-infracoes-<data>.png` | Lista de infrações |
| `portal-detalhes-infracao-<data>.png` / `app-android-detalhes-infracao-<data>.png` | Detalhamento de uma infração |
| `app-android-login-<data>.png` | Tela de login do aplicativo |

Antes do commit, aplicar as regras de anonimização do `README.md` desta pasta: tarja opaca sobre placa, RENAVAM, chassi, CPF, nome, endereço e número do auto, e remoção de metadados.

## 5. Depois da sessão

- [ ] Atualizar `docs/fase1-produto.md` com os valores do formulário.
- [ ] Atualizar a tabela anonimizada em `dados/massa-de-dados.md`.
- [ ] Atualizar a tabela "Prints pendentes" do `README.md` desta pasta.
- [ ] Se a contagem de passos ou os campos mudarem algo do artigo, ajustar `artigo/secoes/fase1-produto.tex`.
- [ ] Registrar as horas na issue #5.
