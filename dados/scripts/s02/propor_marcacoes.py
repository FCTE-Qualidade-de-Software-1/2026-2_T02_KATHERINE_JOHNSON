"""Propõe fim visual dos screencasts; a revisão independente continua obrigatória.

Compara a região principal com o último quadro estável, ignorando cabeçalho e lateral.
Não publica imagens nem substitui a conferência visual dos quadros. A marca inicial é a
proposta do instrumento, preservada ao lado da nova proposta de fim.
"""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageChops, ImageStat


def sinal(path):
    with Image.open(path) as im:
        area = im.crop((int(im.width * .10), int(im.height * .10),
                        int(im.width * .66), int(im.height * .88)))
        return area.convert('L').resize((280, 220))


def propor(registro, raiz):
    dados = json.loads(registro.read_text())
    pasta = raiz / dados['gravacao']
    ts = json.loads((pasta / 'timestamps.json').read_text())
    imagens = sorted(pasta.glob('*.jpg'))
    if len(imagens) != len(ts) or not imagens:
        raise ValueError('Quadros e timestamps incompatíveis')
    final = sinal(imagens[-1])
    erros = [ImageStat.Stat(ImageChops.difference(sinal(p), final)).mean[0] for p in imagens]
    # Todos os quadros seguintes precisam permanecer próximos do estado final.
    candidato = len(imagens) - 1
    while candidato > 0 and max(erros[candidato - 1:]) < 1.5:
        candidato -= 1
    inicial = dados['quadro_inicial']
    if inicial < 0 or candidato <= inicial:
        raise ValueError('Não foi possível propor intervalo positivo')
    resultado = {
        'origem': str(registro.relative_to(raiz)),
        'estado': 'proposta_automatica_pendente_de_conferencia_visual_e_independente',
        'quadro_inicial_proposto': inicial,
        'quadro_final_proposto': candidato,
        'inicio_s_proposto': round(ts[inicial] - ts[0], 6),
        'fim_s_proposto': round(ts[candidato] - ts[0], 6),
        'tempo_s_proposto': round(ts[candidato] - ts[inicial], 6),
        'tempo_instrumento_s': dados.get('tempo_s'),
        'diferenca_media_final': round(erros[candidato], 6),
    }
    return resultado


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('registros', nargs='+')
    args = parser.parse_args()
    raiz = Path(__file__).resolve().parents[3]
    for nome in args.registros:
        p = Path(nome).resolve()
        if not p.is_relative_to(raiz / 'dados/privado'):
            parser.error('usar somente registros privados')
        resultado = propor(p, raiz)
        destino = p.with_name(p.stem + '-marcacao-proposta.json')
        destino.write_text(json.dumps(resultado, ensure_ascii=False, indent=2))
        destino.chmod(0o600)
        print(json.dumps({k: resultado[k] for k in ['estado', 'tempo_s_proposto']}))


if __name__ == '__main__':
    main()
