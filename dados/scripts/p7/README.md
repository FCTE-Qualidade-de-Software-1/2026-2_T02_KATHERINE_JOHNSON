# Preparação da rede de P7

Não executar ações de escrita durante as medições de P4/P5. O roteiro usa somente comandos
locais e exige senha administrativa no terminal do responsável, nunca no chat. Na preparação
de 22/11, `sudo -n true` informou que a autenticação interativa é necessária.

## Topologia proposta e limite

O Wi-Fi conectado é o uplink. Uma interface AP virtual, no mesmo canal, atende o Android.
Portal e app devem passar pelo mesmo uplink antes da coleta. O adaptador anuncia suporte
simultâneo a modo cliente e AP no mesmo canal, mas isso ainda precisa ser validado na prática.
Criar a interface não comprova que o perfil funciona nem libera o bloco.

Quando só o portal participa (S08), `uplink` registra a interface de saída sem criar AP,
e `degradar`/`restaurar` atuam sobre ela. Sem `sudo` interativo, usar `pkexec` com caminho
absoluto; a senha é digitada na janela do sistema:

```bash
python3 dados/scripts/p7/rede.py uplink
pkexec /usr/bin/python3 "$PWD/dados/scripts/p7/rede.py" degradar
pkexec /usr/bin/python3 "$PWD/dados/scripts/p7/rede.py" restaurar
```

Em 22/11 esse fluxo foi executado no B12 da S08: o perfil foi aplicado no `wlo1` e na IFB,
validado pelos contadores e removido, com a fila original conferida. O AP não foi criado nem testado.

O comando abaixo cria apenas o AP temporário; não aplica degradação:

```bash
sudo python3 dados/scripts/p7/rede.py preparar
```

O SSID é `KATHERINE-P7`. A senha temporária fica somente em `dados/privado/P7/estado.json`.
Não publicar o arquivo nem fotografar credenciais. Conectar o Android ao AP e verificar,
sem expor IP/SSID privados, que os dois canais usam o uplink comum.

## Perfis e conferência

- Wi-Fi: AP validado, sem limitação; medir download, upload e latência nos dois clientes.
- Degradada: atraso 300 ±50 ms, 1 Mbit/s e perda de 1% por sentido, na saída do uplink e na
  entrada redirecionada à interface IFB. Conferir configuração, contadores, conectividade e
  efeito nos dois clientes antes das tentativas.
- 4G: Android em 4G/LTE, com Wi-Fi desligado, compartilhando a conexão móvel com o computador
  por USB. Conferir a tecnologia ativa e a rota do computador. 5G não deve ser rotulado como 4G.

```bash
sudo python3 dados/scripts/p7/rede.py degradar
sudo python3 dados/scripts/p7/rede.py normal
sudo python3 dados/scripts/p7/rede.py restaurar
```

`normal` remove somente a limitação própria, mantendo o AP. `restaurar` também remove o AP
criado pelo roteiro. Uma falha na restauração deve ser resolvida e registrada, sem declarar
restauração bem-sucedida. Confirmar a volta da rede original nos dois clientes.

O roteiro recusa filas personalizadas e nomes de interface/conexão já existentes. Diagnósticos,
senha e estado ficam no privado. Regras preexistentes precisam ser preservadas. Os testes simulam falhas e não alteram a rede.

Após validação, executar por rede/canal um aquecimento e dez tentativas, gravando as concluídas
para marcação de M3.2.3. Guardar falhas e sessões expiradas no denominador, registrar os desvios
e exigir a segunda leitura. O clique/toque em Consultar é o início da nova coleta do caso V4.
