"""Propõe timestamps no vídeo privado; não certifica marcação visual ou revisão independente."""
import argparse
import json
from pathlib import Path
import av
from PIL import ImageChops, ImageStat


def sinal(im):
    w, h = im.size
    return im.crop((w * .05, h * .13, w * .95, h * .87)).convert('L').resize((180, 300))


def propor(path, ponto=(540, 1854), dica_s=None):
    """Sem dica: fim = primeiro quadro estável igual ao último. Com dica (rolagem contínua):
    a referência é um quadro do platô da lista 0,5 s antes da detecção, com tolerância ao
    efeito de esticar da rolagem no fim da página."""
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
    dif = lambda a, b: ImageStat.Stat(ImageChops.difference(a, b)).mean[0]
    base = 0
    if dica_s is not None:
        # Ignorar os quadros iniciais do gravador: base = primeiro quadro estável por 5 quadros.
        base = next((i for i in range(1, len(tempos) - 5)
                     if all(dif(sinais[i], sinais[j]) < 1 for j in range(i + 1, i + 6))), 0)
    inicial = next((i for i in range(base, len(toques)) if dif(toques[i], toques[base]) > 6), None)
    if dica_s is None:
        ref, tolerancia = len(tempos) - 1, 1.5
        erro = [dif(x, sinais[ref]) for x in sinais]
        final = ref
        while final > 0 and max(erro[final - 1:ref + 1]) < tolerancia:
            final -= 1
    else:
        # Rolagem contínua: o platô da lista alterna repouso e "esticar". A referência é o quadro
        # de repouso mais típico entre 1,0 s e 0,3 s antes da detecção; o fim é o primeiro quadro
        # após o toque idêntico a ele (pode atrasar até um ciclo de rolagem, ~0,1 s).
        if inicial is None:
            raise ValueError('Toque não identificado')
        janela = [i for i in range(len(tempos)) if tempos[inicial] + dica_s - 1.0 <= tempos[i] <= tempos[inicial] + dica_s - 0.3]
        if len(janela) < 3:
            raise ValueError('Platô insuficiente para referência')
        amostra = janela[::max(1, len(janela) // 15)]
        mediana = lambda i: sorted(dif(sinais[i], sinais[j]) for j in amostra)[len(amostra) // 2]
        ref, tolerancia = min(amostra, key=mediana), 1.5
        erro = [dif(x, sinais[ref]) for x in sinais]
        final = next(i for i in range(inicial + 1, ref + 1) if erro[i] < tolerancia)
    if inicial is None or final <= inicial:
        raise ValueError('Não foi possível propor intervalo positivo')
    return {'estado': 'proposta_automatica_pendente_de_conferencia_visual_e_independente',
            'quadro_inicial_proposto': inicial, 'quadro_final_proposto': final,
            'inicio_s_proposto': round(tempos[inicial], 6), 'fim_s_proposto': round(tempos[final], 6),
            'tempo_s_proposto': round(tempos[final] - tempos[inicial], 6),
            'referencia_quadro': ref, 'tolerancia': tolerancia,
            'limite': 'Proposta por diferença de imagem; conferir o indicador de toque e a lista na gravação. No B04 inclui rolagem;'
                      ' com rolagem contínua, o fim inclui o curso de uma rolagem rápida.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('videos', nargs='+')
    args = parser.parse_args()
    privado = Path(__file__).resolve().parents[3] / 'dados/privado'
    for nome in args.videos:
        path = Path(nome).resolve()
        if not path.is_relative_to(privado) or not any(m in path.name for m in ['M2.1.1', 'M2.1.2', 'M3.2.3']):
            parser.error('usar somente vídeos privados de P4/P7 no Samsung observado')
        # Registros novos guardam o ponto de toque; só o B04 antigo usa a posição fixa observada.
        registro = next((json.loads(p.read_text()) for p in path.parent.glob('B[0-9][0-9]-[0-9][0-9].json')
                         if json.loads(p.read_text()).get('gravacao', '').endswith(path.name)), None)
        ponto = (registro or {}).get('ponto_toque')
        if not ponto:
            if 'M2.1.1' not in path.name or '-B' in path.name:
                parser.error('metadados do ponto de toque ausentes')
            ponto = (540, 1854)
        dica = (registro or {}).get('dica_tempo_s') if (registro or {}).get('rolagem') == 'continua' else None
        resultado = propor(path, ponto, dica)
        destino = path.with_suffix('.marcacao-proposta.json')
        destino.write_text(json.dumps(resultado, ensure_ascii=False, indent=2))
        destino.chmod(0o600)
        print(json.dumps({'estado': resultado['estado'], 'tempo_s_proposto': resultado['tempo_s_proposto']}))


if __name__ == '__main__':
    main()
