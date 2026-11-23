"""Executa blocos do app; grava diagnósticos e resultados individuais somente no privado."""
import argparse
import json
import os
from pathlib import Path
import time

import app_s02 as instrumento


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--caso', required=True)
    parser.add_argument('--bloco', required=True)
    parser.add_argument('--modo', choices=['tempo', 'volume', 'lista', 'p7'], required=True)
    parser.add_argument('--metrica', choices=['M2.1.1', 'M2.1.2'])
    # Sessão pública e rede só identificam o registro; a pasta privada continua S02/<caso>.
    parser.add_argument('--sessao', default='S06')
    parser.add_argument('--rede', choices=['wifi', '4g', 'degradada'], default='wifi')
    args = parser.parse_args()
    if not instrumento.re.fullmatch(r'S[0-9]{2}', args.sessao):
        parser.error('código de sessão inválido')
    if not instrumento.re.fullmatch(r'V[1-9][0-9]*', args.caso):
        parser.error('código de caso inválido')
    if not instrumento.re.fullmatch(r'B[0-9]{2}', args.bloco):
        parser.error('código de bloco inválido')
    if args.modo == 'tempo' and not args.metrica:
        parser.error('métrica obrigatória no modo tempo')
    privado = Path(instrumento.PRIV) / args.caso
    privado.mkdir(parents=True, exist_ok=True, mode=0o700)
    privado.chmod(0o700)
    instrumento.PRIV = str(privado)
    selecao = json.loads((privado / 'selecao.json').read_text())
    os.environ['VEICULO_HASH'] = selecao['hash_placa']
    os.environ['DATA'] = selecao['data_infracao']
    # P7: falhas do serviço entram no denominador; só erro de instrumento é reposto.
    contam = {'concluida'} | ({'falha', 'sessao_expirada', 'tempo_limite'} if args.modo == 'p7' else set())
    concluidas = 0
    for rep in range(1, 21):
        if concluidas == 11:
            return 0
        destino = privado / f'{args.bloco}-{rep:02d}.json'
        if destino.exists():
            anterior = json.loads(destino.read_text())
            if anterior.get('resultado') in contam:
                concluidas += 1
            # Preservar o erro: a reposição ganha novo número, sem sobrescrever registros.
            continue
        try:
            conectado = instrumento.app.adb('get-state').strip() == 'device'
        except Exception:
            conectado = False
        if not conectado:
            print(json.dumps({'bloco': args.bloco, 'etapa': 'aguardando_usb', 'proxima_repeticao': rep}), flush=True)
            return 2
        print(json.dumps({'bloco': args.bloco, 'repeticao': rep, 'etapa': 'iniciando'}), flush=True)
        inicio = instrumento.agora()
        try:
            if args.modo in {'lista', 'p7'}:
                resultado = instrumento.tempo_lista('M3.2.3' if args.modo == 'p7' else 'M2.1.1', f'{rep:02d}', args.bloco)
            elif args.modo == 'tempo':
                if args.metrica == 'M2.1.2':
                    resultado = instrumento.tempo_detalhe_na_lista(f'{rep:02d}', selecao['data_infracao'])
                else:
                    resultado = instrumento.tempo(args.metrica, f'{rep:02d}', selecao['data_infracao'])
            else:
                # Guardar as saídas completas do contador somente no privado.
                sh_original = instrumento.sh
                contador = []
                def sh_com_registro(*argumentos):
                    saida = sh_original(*argumentos)
                    if argumentos == ('dumpsys', 'netstats', 'detail'):
                        contador.append(saida)
                    return saida
                instrumento.sh = sh_com_registro
                try:
                    resultado = instrumento.volume(f'{rep:02d}')
                finally:
                    instrumento.sh = sh_original
                    for numero, texto in enumerate(contador):
                        arquivo = privado / f'{args.bloco}-{rep:02d}-contador-{numero}.txt'
                        arquivo.write_text(texto)
                        arquivo.chmod(0o600)
            resultado.setdefault('resultado', 'concluida')
            resultado.update(sessao=args.sessao, rede=args.rede, bloco=args.bloco, aquecimento=concluidas == 0,
                             repeticao=rep, inicio_execucao=inicio)
        except Exception as erro:
            # P7: tela que não carrega ou erro do app na preparação é falha do serviço, não reposta.
            servico = args.modo == 'p7' and (isinstance(erro, TimeoutError)
                                             or str(erro) == 'mensagem_de_erro_no_aplicativo')
            resultado = {'resultado': 'sessao_expirada' if isinstance(erro, instrumento.Expirou)
                         else 'falha' if servico else 'preparacao_ou_tentativa_interrompida',
                         'etapa': 'preparacao' if servico else '', 'tipo': type(erro).__name__,
                         'sessao': args.sessao, 'rede': args.rede, 'aquecimento': concluidas == 0,
                         'diagnostico_privado': str(erro), 'bloco': args.bloco, 'repeticao': rep,
                         'inicio_execucao': inicio}
        destino.write_text(json.dumps(resultado, ensure_ascii=False, indent=2))
        destino.chmod(0o600)
        resumo = {k: v for k, v in resultado.items() if k in {
            'resultado', 'bloco', 'repeticao', 'aquecimento', 'dica_tempo_s', 'bytes_transferidos', 'tipo'}}
        print(json.dumps(resumo, ensure_ascii=False), flush=True)
        if resultado['resultado'] == 'sessao_expirada' or resultado['resultado'] not in contam | {'falha', 'tempo_limite'}:
            return 1  # novo login ou diagnóstico do instrumento antes de continuar
        if resultado['resultado'] in contam:
            concluidas += 1
        time.sleep(1)
    return 0 if concluidas == 11 else 1


if __name__ == '__main__':
    raise SystemExit(main())
