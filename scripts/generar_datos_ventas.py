"""Genera los datos de ejemplo de los notebooks 34 a 38 (PyArrow y Polars).

Crea en ``data/``:

* ``ventas.csv``: 20,000 ventas de una cadena de tiendas, 2024-2025.
* ``tiendas.csv``: catálogo de 14 tiendas.
* ``tipo_cambio.csv``: tipo de cambio de ejemplo (unidades monetarias por dólar
  estadounidense) en días hábiles.

Los datos son sintéticos y se generan con una semilla fija, así que el
resultado es siempre el mismo. No corresponden a ningún país: tiendas,
ciudades y estados tienen nombres genéricos, los importes están en
unidades monetarias (UM) sin moneda concreta y los correos usan los
dominios reservados para ejemplos (RFC 2606). Algunos defectos son
intencionales, para los ejemplos de limpieza y de joins:

* ``descuento`` tiene valores nulos.
* Algunos correos tienen mayúsculas o espacios de más.
* Unas cuantas ventas tienen ``tienda_id`` 99, que no existe en ``tiendas.csv``.
* Las tiendas 13 y 14 no tienen ventas.

Uso::

    python scripts/generar_datos_ventas.py
"""

from datetime import date, datetime, timedelta
from pathlib import Path

import numpy as np
import polars as pl

SEMILLA = 311
N_VENTAS = 20_000
DATA = Path(__file__).resolve().parent.parent / "data"

TIENDAS = [
    # tienda_id, nombre, ciudad, estado, region, fecha_apertura, metros_cuadrados
    # Nombres, ciudades y estados son genéricos y no corresponden a ningún país.
    (1, "Tienda Centro 1", "Ciudad A", "Estado 1", "Centro", "2015-03-01", 850),
    (2, "Tienda Centro 2", "Ciudad A", "Estado 1", "Centro", "2017-06-15", 1200),
    (3, "Tienda Centro 3", "Ciudad A", "Estado 1", "Centro", "2019-09-01", 700),
    (4, "Tienda Centro 4", "Ciudad B", "Estado 2", "Centro", "2018-02-20", 950),
    (5, "Tienda Oeste 1", "Ciudad C", "Estado 3", "Oeste", "2016-11-10", 1100),
    (6, "Tienda Oeste 2", "Ciudad D", "Estado 3", "Oeste", "2020-01-15", 650),
    (7, "Tienda Norte 1", "Ciudad E", "Estado 4", "Norte", "2014-08-01", 1300),
    (8, "Tienda Norte 2", "Ciudad F", "Estado 4", "Norte", "2021-04-12", 600),
    (9, "Tienda Norte 3", "Ciudad G", "Estado 5", "Norte", "2019-05-30", 800),
    (10, "Tienda Sur 1", "Ciudad H", "Estado 6", "Sur", "2017-10-05", 900),
    (11, "Tienda Sur 2", "Ciudad I", "Estado 7", "Sur", "2022-02-01", 750),
    (12, "Tienda Centro 5", "Ciudad J", "Estado 8", "Centro", "2023-07-01", 680),
    (13, "Tienda Oeste 3", "Ciudad K", "Estado 9", "Oeste", "2026-01-15", 600),
    (14, "Tienda Sur 3", "Ciudad L", "Estado 10", "Sur", "2026-02-01", 550),
]

PRODUCTOS = [
    # producto, categoria, precio de lista (unidades monetarias)
    ("Audífonos inalámbricos", "Electrónica", 1499.0),
    ("Altavoz portátil", "Electrónica", 899.0),
    ("Cargador USB-C", "Electrónica", 349.0),
    ("Teclado mecánico", "Electrónica", 1899.0),
    ("Juego de sartenes", "Hogar", 1299.0),
    ("Cafetera de goteo", "Hogar", 799.0),
    ("Toallas de baño", "Hogar", 299.0),
    ("Cuaderno de espiral", "Papelería", 65.0),
    ("Bolígrafos de gel (12)", "Papelería", 120.0),
    ("Mochila escolar", "Papelería", 649.0),
    ("Balón de fútbol", "Deportes", 459.0),
    ("Colchoneta de yoga", "Deportes", 389.0),
]

NOMBRES = ["ana", "luis", "sofia", "carlos", "maria", "jorge", "lucia", "diego", "elena", "pablo",
           "valeria", "miguel", "fernanda", "ricardo", "paula", "andres", "camila", "javier"]
APELLIDOS = ["garcia", "lopez", "martinez", "hernandez", "perez", "sanchez", "ramirez", "torres",
             "flores", "rivera", "gomez", "diaz", "morales", "castro"]
# Dominios reservados para ejemplos (RFC 2606).
DOMINIOS = ["example.com", "example.org", "example.net"]


def generar_ventas(rng: np.random.Generator) -> pl.DataFrame:
    inicio = datetime(2024, 1, 1)
    dias = (datetime(2025, 12, 31) - inicio).days + 1
    fechas = [
        inicio + timedelta(days=int(d), hours=int(h), minutes=int(m), seconds=int(s))
        for d, h, m, s in zip(
            rng.integers(0, dias, N_VENTAS),
            rng.integers(9, 21, N_VENTAS),
            rng.integers(0, 60, N_VENTAS),
            rng.integers(0, 60, N_VENTAS),
        )
    ]

    # Tiendas 1-12 con distinto volumen; 0.5 % de las ventas con tienda_id 99 (no existe).
    pesos = np.array([10, 12, 6, 7, 9, 5, 11, 4, 6, 7, 5, 3], dtype=float)
    tienda_id = rng.choice(np.arange(1, 13), N_VENTAS, p=pesos / pesos.sum())
    tienda_id[rng.random(N_VENTAS) < 0.005] = 99

    idx_producto = rng.integers(0, len(PRODUCTOS), N_VENTAS)
    producto = [PRODUCTOS[i][0] for i in idx_producto]
    categoria = [PRODUCTOS[i][1] for i in idx_producto]
    precio = np.array([PRODUCTOS[i][2] for i in idx_producto])
    # Variación de precio de ±5 %, redondeada a dos decimales.
    precio_unitario = np.round(precio * rng.uniform(0.95, 1.05, N_VENTAS), 2)

    cantidad = rng.choice([1, 1, 1, 2, 2, 3, 4, 5], N_VENTAS)
    canal = rng.choice(["tienda", "en línea"], N_VENTAS, p=[0.7, 0.3])

    descuento = rng.choice([0.0, 0.0, 0.0, 0.05, 0.10, 0.15], N_VENTAS).astype(object)
    descuento[rng.random(N_VENTAS) < 0.05] = None

    correos = []
    for _ in range(N_VENTAS):
        correo = f"{rng.choice(NOMBRES)}.{rng.choice(APELLIDOS)}@{rng.choice(DOMINIOS)}"
        r = rng.random()
        if r < 0.02:
            correo = correo.upper()
        elif r < 0.04:
            correo = f"  {correo} "
        correos.append(correo)

    return (
        pl.DataFrame({
            "fecha_hora": fechas,
            "tienda_id": tienda_id,
            "canal": canal,
            "producto": producto,
            "categoria": categoria,
            "cantidad": cantidad,
            "precio_unitario": precio_unitario,
            "descuento": pl.Series(list(descuento), dtype=pl.Float64),
            "cliente_email": correos,
        })
        .sort("fecha_hora")
        .with_row_index("venta_id", offset=1)
        .with_columns(pl.col("venta_id").cast(pl.Int64))
    )


def generar_tiendas() -> pl.DataFrame:
    columnas = ["tienda_id", "nombre", "ciudad", "estado", "region", "fecha_apertura", "metros_cuadrados"]
    return pl.DataFrame(TIENDAS, schema=columnas, orient="row")


def generar_tipo_cambio(rng: np.random.Generator) -> pl.DataFrame:
    fechas, valores = [], []
    valor = 17.0
    dia = date(2024, 1, 1)
    while dia <= date(2025, 12, 31):
        if dia.weekday() < 5:  # sólo días hábiles (lunes a viernes)
            # Paseo aleatorio que tiende a regresar a 18.5 (valor de ejemplo).
            valor = round(valor + 0.03 * (18.5 - valor) + rng.normal(0, 0.08), 4)
            fechas.append(dia)
            valores.append(valor)
        dia += timedelta(days=1)
    return pl.DataFrame({"fecha": fechas, "tipo_cambio": valores})


def main() -> None:
    rng = np.random.default_rng(SEMILLA)
    DATA.mkdir(exist_ok=True)
    ventas = generar_ventas(rng)
    ventas.write_csv(DATA / "ventas.csv", datetime_format="%Y-%m-%d %H:%M:%S")
    generar_tiendas().write_csv(DATA / "tiendas.csv")
    generar_tipo_cambio(rng).write_csv(DATA / "tipo_cambio.csv")
    print(f"ventas.csv: {ventas.height} renglones")


if __name__ == "__main__":
    main()
