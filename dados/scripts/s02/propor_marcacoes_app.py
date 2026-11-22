"""Propõe timestamps no vídeo privado; não certifica marcação visual ou revisão independente."""
import argparse
import json
from pathlib import Path
import av
from PIL import ImageChops, ImageStat


def sinal(im):
    w, h = im.size
    return im.crop((w * .05, h * .13, w * .95, h * .87)).convert('L').resize((180, 300))


def propor(path, ponto=(540, 1854)):
    with av.open(str(path)) as container:
        tempos, sinais, toques = [], [], []
        for frame in container.decode(video=0):
            im = frame.to_image()
            tempos.append(float(frame.time))
            sinais.append(sinal(im))
            # Região central do botão Consultar no Samsung observado. Só para M2.1.1.
            x, y = ponto
            toques.append(im.crop((x - 30, y - 30, x + 30, y + 30)).convert('L'))
    if len(tempos) < 3:
        raise ValueError('Vídeo insuficiente')
    inicial = next((i for i, toque in enumerate(toques)
                    if ImageStat.Stat(ImageChops.difference(toque, toques[0])).mean[0] > 6), None)
    erro = [ImageStat.Stat(ImageChops.difference(s, sinais[-1])).mean[0] for s in sinais]
    final = len(tempos) - 1
    while final > 0 and max(erro[final - 1:]) < 1.5:
        final -= 1
    if inicial is None or final <= inicial:
        raise ValueError('Não foi possível propor intervalo positivo')
    return {'estado': 'proposta_automatica_pendente_de_conferencia_visual_e_independente',
            'quadro_inicial_proposto': inicial, 'quadro_final_proposto': final,
            'inicio_s_proposto': round(tempos[inicial], 6), 'fim_s_proposto': round(tempos[final], 6),
            'tempo_s_proposto': round(tempos[final] - tempos[inicial], 6),
            'limite': 'Inclui a rolagem executada até o resultado ficar visível; conferir o indicador de toque e a lista completa na gravação.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('videos', nargs='+')
    args = parser.parse_args()
    privado = Path(__file__).resolve().parents[3] / 'dados/privado'
    for nome in args.videos:
        path = Path(nome).resolve()
        if not path.is_relative_to(privado) or not any(m in path.name for m in ['M2.1.1', 'M2.1.2']):
            parser.error('usar somente vídeos privados de P4 no Samsung observado')
        ponto = (540, 1854)
        if 'M2.1.2' in path.name:
            registro = next((json.loads(p.read_text()) for p in path.parent.glob('B06-*.json')
                             if json.loads(p.read_text()).get('gravacao', '').endswith(path.name)), None)
            if not registro or not registro.get('ponto_toque'):
                parser.error('metadados do ponto de toque ausentes para o detalhe')
            ponto = registro['ponto_toque']
        resultado = propor(path, ponto)
        destino = path.with_suffix('.marcacao-proposta.json')
        destino.write_text(json.dumps(resultado, ensure_ascii=False, indent=2))
        destino.chmod(0o600)
        print(json.dumps({'estado': resultado['estado'], 'tempo_s_proposto': resultado['tempo_s_proposto']}))


if __name__ == '__main__':
    main()
