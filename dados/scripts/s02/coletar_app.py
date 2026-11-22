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
    parser.add_argument('--modo', choices=['tempo', 'volume'], required=True)
    parser.add_argument('--metrica', choices=['M2.1.1', 'M2.1.2'])
    args = parser.parse_args()
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
    concluidas = 0
    for rep in range(1, 21):
        if concluidas == 11:
            return 0
        destino = privado / f'{args.bloco}-{rep:02d}.json'
        if destino.exists():
            anterior = json.loads(destino.read_text())
            if anterior.get('resultado') == 'concluida':
                concluidas += 1
            # Preservar o erro: a reposição ganha novo número, sem sobrescrever registros.
            continue
        print(json.dumps({'bloco': args.bloco, 'repeticao': rep, 'etapa': 'iniciando'}), flush=True)
        inicio = instrumento.agora()
        try:
            if args.modo == 'tempo':
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
            resultado.update(resultado='concluida', sessao='S06', bloco=args.bloco, aquecimento=concluidas == 0,
                             repeticao=rep, inicio_execucao=inicio)
        except Exception as erro:
            resultado = {'resultado': 'sessao_expirada' if isinstance(erro, instrumento.Expirou)
                         else 'preparacao_ou_tentativa_interrompida', 'tipo': type(erro).__name__,
                         'diagnostico_privado': str(erro), 'bloco': args.bloco, 'repeticao': rep,
                         'inicio_execucao': inicio}
        destino.write_text(json.dumps(resultado, ensure_ascii=False, indent=2))
        destino.chmod(0o600)
        resumo = {k: v for k, v in resultado.items() if k in {
            'resultado', 'bloco', 'repeticao', 'aquecimento', 'dica_tempo_s', 'bytes_transferidos', 'tipo'}}
        print(json.dumps(resumo, ensure_ascii=False), flush=True)
        if resultado['resultado'] != 'concluida':
            return 1
        concluidas += 1
        time.sleep(1)
    return 0 if concluidas == 11 else 1


if __name__ == '__main__':
    raise SystemExit(main())
