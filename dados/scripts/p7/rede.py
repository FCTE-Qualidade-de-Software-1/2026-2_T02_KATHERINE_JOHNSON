"""Rede temporária de P7. Requer sudo nas ações de escrita; não executa coletas.

Não executar enquanto P4/P5 estiverem medindo. Credenciais e diagnósticos ficam no privado.
"""
import argparse
import json
import os
from pathlib import Path
import re
import secrets
import subprocess

RAIZ = Path(__file__).resolve().parents[3]
PRIV = RAIZ / 'dados/privado/P7'
AP = 'kqap0'
IFB = 'kqifb0'
CONEXAO = 'katherine-p7-temporaria'
SSID = 'KATHERINE-P7'


def comando(*args, tolerar=False):
    p = subprocess.run(args, text=True, capture_output=True, timeout=30)
    if p.returncode and not tolerar:
        PRIV.mkdir(parents=True, exist_ok=True, mode=0o700)
        arquivo = PRIV / 'erro-comando.txt'
        arquivo.write_text(p.stdout + p.stderr)
        arquivo.chmod(0o600)
        raise RuntimeError('Comando de rede falhou; diagnóstico mantido no privado')
    return p.stdout


def salvar(estado):
    PRIV.mkdir(parents=True, exist_ok=True, mode=0o700)
    arquivo = PRIV / 'estado.json'
    arquivo.write_text(json.dumps(estado, indent=2))
    arquivo.chmod(0o600)
    if os.geteuid() == 0 and (os.environ.get('SUDO_UID') or os.environ.get('PKEXEC_UID')):
        import pwd
        uid = int(os.environ.get('SUDO_UID') or os.environ['PKEXEC_UID'])
        gid = pwd.getpwuid(uid).pw_gid
        os.chown(PRIV, uid, gid)
        os.chown(arquivo, uid, gid)


def normal(estado):
    if estado.get('egress'):
        comando('tc', 'qdisc', 'del', 'dev', estado['uplink'], 'root')
        estado['egress'] = False
        salvar(estado)
    if estado.get('ingress'):
        comando('tc', 'qdisc', 'del', 'dev', estado['uplink'], 'ingress')
        estado['ingress'] = False
        salvar(estado)
    if estado.get('ifb'):
        comando('ip', 'link', 'del', IFB)
        estado['ifb'] = False
        salvar(estado)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('acao', choices=['preparar', 'uplink', 'degradar', 'normal', 'restaurar', 'estado'])
    args = parser.parse_args()
    arquivo = PRIV / 'estado.json'
    estado = json.loads(arquivo.read_text()) if arquivo.exists() else {}
    if args.acao == 'estado':
        print(json.dumps({k: v for k, v in estado.items() if k != 'senha'}))
        return
    if args.acao == 'uplink':
        # Só o computador como cliente (P7 do portal): registra o uplink, sem criar ponto de acesso.
        if estado and estado.get('preparacao') not in {'restaurado', 'falhou'}:
            parser.error('já existe estado; conferir ou restaurar antes de preparar novamente')
        rotas = json.loads(comando('ip', '-j', 'route', 'show', 'default'))
        uplink = min((r for r in rotas if r.get('dev')), key=lambda r: r.get('metric', 0))['dev']
        salvar({'uplink': uplink, 'ap': False, 'conexao': False, 'preparacao': 'uplink_sem_ponto_de_acesso'})
        print(json.dumps({'uplink': uplink, 'preparacao': 'uplink_sem_ponto_de_acesso'}))
        return
    if os.geteuid() != 0:
        parser.error('executar esta ação com sudo no terminal local; nunca enviar a senha ao chat')
    if args.acao == 'preparar':
        if estado and estado.get('preparacao') not in {'restaurado', 'falhou'}:
            parser.error('já existe estado; conferir ou restaurar antes de preparar novamente')
        rotas = json.loads(comando('ip', '-j', 'route', 'show', 'default'))
        rotas = [r for r in rotas if r.get('dev') and r['dev'] != AP]
        uplink = min(rotas, key=lambda r: r.get('metric', 0))['dev']
        link = comando('iw', 'dev', uplink, 'link')
        freq = re.search(r'freq: (\d+)', link)
        if not freq:
            parser.error('a preparação exige uma conexão Wi-Fi ativa como uplink')
        freq = int(freq.group(1))
        if 2412 <= freq <= 2472:
            banda, canal = 'bg', (freq - 2407) // 5
        elif 5180 <= freq <= 5825:
            banda, canal = 'a', (freq - 5000) // 5
        else:
            parser.error('frequência não suportada por este roteiro; não alterar a rede')
        existentes = comando('nmcli', '-g', 'NAME', 'connection', 'show').splitlines()
        if CONEXAO in existentes or (Path('/sys/class/net') / AP).exists():
            parser.error('nome de conexão/interface já existe; não será sobrescrito')
        estado = {'uplink': uplink, 'canal': canal, 'ssid': SSID,
                  'senha': secrets.token_urlsafe(18), 'ap': False, 'conexao': False}
        salvar(estado)
        try:
            comando('iw', 'dev', uplink, 'interface', 'add', AP, 'type', '__ap')
            estado['ap'] = True
            salvar(estado)
            # A interface virtual herda o MAC do uplink e o wpa_supplicant a recusa: usar MAC local.
            mac = '02:' + ':'.join(f'{b:02x}' for b in secrets.token_bytes(5))
            comando('ip', 'link', 'set', 'dev', AP, 'address', mac)
            comando('nmcli', 'device', 'set', AP, 'managed', 'yes')
            comando('nmcli', 'connection', 'add', 'type', 'wifi', 'ifname', AP,
                    'con-name', CONEXAO, 'ssid', SSID, 'wifi.mode', 'ap',
                    'wifi.band', banda, 'wifi.channel', str(canal), 'ipv4.method', 'shared',
                    'ipv6.method', 'disabled', 'wifi-sec.key-mgmt', 'wpa-psk',
                    'wifi-sec.psk', estado['senha'])
            estado['conexao'] = True
            salvar(estado)
            comando('nmcli', 'connection', 'up', CONEXAO)
        except Exception:
            if estado.get('conexao'):
                comando('nmcli', 'connection', 'delete', CONEXAO, tolerar=True)
            if estado.get('ap'):
                comando('iw', 'dev', AP, 'del', tolerar=True)
            estado.update(ap=False, conexao=False, preparacao='falhou')
            salvar(estado)
            raise
        estado['preparacao'] = 'ponto_de_acesso_criado_validacao_pendente'
        salvar(estado)
        print('Ponto de acesso temporário criado. Credenciais no arquivo privado; validar ambos os clientes antes de coletar.')
        return
    if not estado:
        parser.error('não há configuração própria registrada para alterar ou restaurar')
    if args.acao == 'degradar':
        if estado.get('egress') or estado.get('ingress') or estado.get('ifb'):
            parser.error('já há limitação própria registrada; restaurar o perfil normal antes')
        qdiscs = json.loads(comando('tc', '-j', 'qdisc', 'show', 'dev', estado['uplink']))
        if any(q.get('kind') not in {'noqueue', 'mq', 'fq_codel', 'pfifo_fast'} for q in qdiscs):
            parser.error('há configuração de fila não padrão; não será sobrescrita')
        if (Path('/sys/class/net') / IFB).exists():
            parser.error('interface IFB já existe; não será reutilizada')
        estado['qdisc_antes'] = qdiscs
        salvar(estado)
        try:
            comando('ip', 'link', 'add', IFB, 'type', 'ifb')
            estado['ifb'] = True
            salvar(estado)
            comando('ip', 'link', 'set', IFB, 'up')
            parametros = ['netem', 'delay', '300ms', '50ms', 'distribution', 'normal',
                          'rate', '1mbit', 'loss', '1%']
            comando('tc', 'qdisc', 'replace', 'dev', estado['uplink'], 'root', *parametros)
            estado['egress'] = True
            salvar(estado)
            comando('tc', 'qdisc', 'add', 'dev', estado['uplink'], 'handle', 'ffff:', 'ingress')
            estado['ingress'] = True
            salvar(estado)
            comando('tc', 'filter', 'add', 'dev', estado['uplink'], 'parent', 'ffff:',
                    'protocol', 'all', 'u32', 'match', 'u32', '0', '0', 'action',
                    'mirred', 'egress', 'redirect', 'dev', IFB)
            comando('tc', 'qdisc', 'replace', 'dev', IFB, 'root', *parametros)
        except Exception:
            normal(estado)
            raise
        print('Perfil aplicado nos dois sentidos do uplink. Validar tráfego, tempos e contadores nos dois clientes antes de coletar.')
    elif args.acao == 'normal':
        normal(estado)
        print('Limitação temporária removida; conferir restauração nos dois clientes.')
    elif args.acao == 'restaurar':
        normal(estado)
        if estado.get('conexao'):
            comando('nmcli', 'connection', 'down', CONEXAO, tolerar=True)
            comando('nmcli', 'connection', 'delete', CONEXAO)
        if estado.get('ap'):
            comando('iw', 'dev', AP, 'del')
        estado.update(ap=False, conexao=False, preparacao='restaurado')
        salvar(estado)
        print('Ponto de acesso e limitação temporários removidos; rede original a conferir.')


if __name__ == '__main__':
    main()
