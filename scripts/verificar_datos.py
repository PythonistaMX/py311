"""Verifica los datos de data/ contra el manifiesto data/fuentes.json.

Uso:
    python scripts/verificar_datos.py            # integridad (SHA-256); falla si algo no coincide
    python scripts/verificar_datos.py --enlaces  # además revisa que las URL de origen respondan

Los notebooks leen siempre la copia local de data/, de modo que un enlace roto
no impide ejecutarlos. La revisión de enlaces sólo informa: sirve para saber
cuándo una fuente cambió de lugar y hay que actualizar el manifiesto.
"""

import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "data"
MANIFIESTO = DATOS / "fuentes.json"


def sha256(ruta: Path) -> str:
    h = hashlib.sha256()
    with ruta.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def verificar_integridad(archivos: list[dict]) -> list[str]:
    errores = []
    for entrada in archivos:
        ruta = DATOS / entrada["archivo"]
        if not ruta.exists():
            errores.append(f"{entrada['archivo']}: no existe")
            continue
        obtenido = sha256(ruta)
        if obtenido != entrada["sha256"]:
            errores.append(f"{entrada['archivo']}: SHA-256 {obtenido} no coincide con el manifiesto")
        else:
            print(f"[OK]     {entrada['archivo']}")
    return errores


def revisar_url(url: str, timeout: float = 20) -> str:
    peticion = urllib.request.Request(url, headers={"User-Agent": "py311-verificar-datos"})
    try:
        with urllib.request.urlopen(peticion, timeout=timeout) as respuesta:
            return f"HTTP {respuesta.status}"
    except urllib.error.HTTPError as exc:
        return f"HTTP {exc.code}"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return f"sin respuesta ({getattr(exc, 'reason', exc)})"


def revisar_enlaces(archivos: list[dict]) -> list[str]:
    rotos = []
    for entrada in archivos:
        for fuente in entrada.get("urls", []):
            estado = revisar_url(fuente["url"])
            marca = "[OK]    " if estado.startswith("HTTP 2") else "[AVISO] "
            print(f"{marca}{entrada['archivo']}: {estado} {fuente['url']}")
            if marca.startswith("[AVISO]"):
                rotos.append(f"{entrada['archivo']}: {estado} {fuente['url']}")
                if os.environ.get("GITHUB_ACTIONS"):
                    print(f"::warning title=Enlace sin respuesta::{entrada['archivo']}: {estado} {fuente['url']}")
    return rotos


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--enlaces", action="store_true", help="revisar también las URL de origen")
    args = parser.parse_args()

    archivos = json.loads(MANIFIESTO.read_text(encoding="utf-8"))["archivos"]

    errores = verificar_integridad(archivos)
    if args.enlaces:
        rotos = revisar_enlaces(archivos)
        if rotos:
            print(f"\n{len(rotos)} enlace(s) no respondieron. Los notebooks no se ven afectados;"
                  " conviene actualizar las URL en data/fuentes.json.")

    if errores:
        print("\nErrores de integridad:\n  " + "\n  ".join(errores))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
