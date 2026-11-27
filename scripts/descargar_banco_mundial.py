"""Descarga del Banco Mundial el PIB por país que usa el notebook 27.

Crea ``data/pib_banco_mundial.csv`` a partir de la API pública de
World Bank Open Data (https://api.worldbank.org/v2/), sin claves de acceso.

* Indicador: ``NY.GDP.MKTP.KD``, PIB en dólares estadounidenses a precios
  constantes de 2015.
* Países: 23 países de las siete regiones del Banco Mundial, más el agregado
  mundial (``WLD``).
* Años: 1990 a 2025.

El archivo está en formato largo, un renglón por país y año, con las columnas
``codigo`` (código ISO 3166-1 alfa-3), ``pais``, ``region``, ``año`` y ``pib``.
Los renglones se ordenan por código y año, y los valores se escriben tal como
los entrega la API, así que el resultado sólo cambia si el Banco Mundial
revisa sus datos. La copia versionada en ``data/`` se consultó el 27 de
noviembre de 2026.

Fuente: World Bank Open Data, licencia CC BY 4.0
(https://datacatalog.worldbank.org/public-licenses#cc-by).

Uso::

    python scripts/descargar_banco_mundial.py
"""

import csv
import json
import time
import urllib.request
from pathlib import Path

API = "https://api.worldbank.org/v2/es"
INDICADOR = "NY.GDP.MKTP.KD"
INICIO, FIN = 1990, 2025
PAISES = [
    # América del Norte
    "CAN", "USA",
    # América Latina y el Caribe
    "ARG", "BRA", "CHL", "COL",
    # Europa y Asia central
    "DEU", "ESP", "FRA", "POL",
    # Asia oriental y el Pacífico
    "AUS", "CHN", "IDN", "JPN",
    # Asia meridional
    "BGD", "IND",
    # Oriente Medio y Norte de África
    "EGY", "MAR", "SAU",
    # África al sur del Sahara
    "ETH", "KEN", "NGA", "ZAF",
    # Agregado mundial
    "WLD",
]
DESTINO = Path(__file__).resolve().parent.parent / "data" / "pib_banco_mundial.csv"


def consultar(url: str, intentos: int = 3) -> list:
    """Regresa la respuesta JSON de la API; reintenta si el servidor tarda."""
    peticion = urllib.request.Request(url, headers={"User-Agent": "py311-datos"})
    for intento in range(1, intentos + 1):
        try:
            with urllib.request.urlopen(peticion, timeout=180) as respuesta:
                return json.load(respuesta)
        except OSError:
            if intento == intentos:
                raise
            time.sleep(5 * intento)
    raise RuntimeError("sin respuesta")


def main() -> None:
    codigos = ";".join(PAISES)
    metadatos, registros = consultar(
        f"{API}/country/{codigos}/indicator/{INDICADOR}"
        f"?format=json&date={INICIO}:{FIN}&per_page=2000"
    )
    if metadatos["pages"] != 1:
        raise RuntimeError("la respuesta llegó en varias páginas; aumenta per_page")
    _, paises = consultar(f"{API}/country/{codigos}?format=json&per_page=100")
    region = {p["id"]: p["region"]["value"].strip() for p in paises}

    renglones = sorted(
        (r["countryiso3code"], r["country"]["value"], region[r["countryiso3code"]],
         int(r["date"]), r["value"])
        for r in registros
    )
    faltantes = [r[:4] for r in renglones if r[4] is None]
    if faltantes:
        raise RuntimeError(f"hay valores faltantes: {faltantes[:5]}")

    with DESTINO.open("w", encoding="utf-8", newline="") as f:
        escritor = csv.writer(f, lineterminator="\n")
        escritor.writerow(["codigo", "pais", "region", "año", "pib"])
        for codigo, pais, reg, anio, valor in renglones:
            escritor.writerow([codigo, pais, reg, anio, repr(float(valor))])
    print(f"{DESTINO.name}: {len(renglones)} renglones; "
          f"datos del Banco Mundial actualizados el {metadatos['lastupdated']}")


if __name__ == "__main__":
    main()
