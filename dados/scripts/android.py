#!/usr/bin/env python3
"""Inventário do aparelho Android para P6 (S03): versões do sistema, do Chrome e do aplicativo.

Uso, com um único aparelho ligado por USB e a depuração ativada:

    python3 dados/scripts/android.py --sessao S03 --contexto CT05 --dispositivo D03

Imprime uma linha JSON com as colunas de `dados/brutos/ambientes.csv` que vêm do aparelho
(modelo, cpu, ram_gb, so_build, navegador_versao, aplicativo_versao, resolucao, data_hora).
Rede, gravador, FPS e evidência são preenchidos pelo registrador. Só lê o aparelho; não
registra número de série, IMEI, MAC, IP ou SSID (dados/README.md).
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta

PACOTE = "br.com.mesotec.detrandf"
CHROME = "com.android.chrome"
BRASILIA = timezone(timedelta(hours=-3))


def adb(*args):
    resultado = subprocess.run(
        ["adb", "shell", *args], capture_output=True, text=True, check=False
    )
    if resultado.returncode != 0:
        sys.exit(f"adb shell {' '.join(args)} falhou: {resultado.stderr.strip()}")
    return resultado.stdout.replace("\r", "")


def versao_pacote(pacote):
    saida = adb("dumpsys", "package", pacote)
    nome = re.search(r"versionName=(\S+)", saida)
    codigo = re.search(r"versionCode=(\d+)", saida)
    if not nome:
        return "nao_instalado"
    return f"{nome.group(1)} ({codigo.group(1)})" if codigo else nome.group(1)


def one_ui(valor):
    """Samsung grava a versão como inteiro (60000 = One UI 6.0); vazio em outras marcas."""
    if not valor.isdigit():
        return ""
    numero = int(valor)
    return f"; One UI {numero // 10000}.{numero // 100 % 100}"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--sessao", default="S03")
    parser.add_argument("--contexto", required=True, help="CT03, CT04 ou CT05")
    parser.add_argument("--dispositivo", required=True, help="D02 ou D03")
    args = parser.parse_args()

    prop = lambda nome: adb("getprop", nome).strip()  # noqa: E731
    memoria = re.search(r"MemTotal:\s+(\d+)", adb("cat", "/proc/meminfo"))
    tamanho = re.search(r"Physical size: (\S+)", adb("wm", "size"))
    portal = args.contexto == "CT03"
    print(json.dumps({
        "sessao": args.sessao,
        "contexto": args.contexto,
        "canal": "portal" if portal else "aplicativo",
        "dispositivo": args.dispositivo,
        "modelo": f"{prop('ro.product.manufacturer')} {prop('ro.product.model')}",
        "cpu": prop("ro.soc.model") or prop("ro.board.platform"),
        "ram_gb": round(int(memoria.group(1)) / 1_000_000, 1) if memoria else "",
        "so_build": f"Android {prop('ro.build.version.release')} "
        f"(API {prop('ro.build.version.sdk')}); {prop('ro.build.display.id')}"
        f"{one_ui(prop('ro.build.version.oneui'))}",
        "navegador_versao": f"Chrome {versao_pacote(CHROME)}" if portal else "nao_se_aplica",
        "aplicativo_versao": "nao_se_aplica" if portal else f"{PACOTE} {versao_pacote(PACOTE)}",
        "resolucao": tamanho.group(1) if tamanho else "",
        "data_hora": datetime.now(BRASILIA).isoformat(timespec="seconds"),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
