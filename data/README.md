# Datos de los notebooks

Los notebooks leen estos archivos directamente; ninguno necesita descargar nada para ejecutarse (salvo el notebook 26, cuyo tema es la descarga de datos de la API del Banco Mundial). La procedencia de cada archivo está en [`fuentes.json`](fuentes.json).

| Archivo | Notebooks | Origen |
| :--- | :--- | :--- |
| `pib_banco_mundial.csv` | 27 | Banco Mundial, *World Bank Open Data*, indicador `NY.GDP.MKTP.KD` (PIB en dólares a precios constantes de 2015), 23 países y el agregado mundial, 1990-2025. Licencia CC BY 4.0; consultado el 27 de noviembre de 2026; se regenera con `python scripts/descargar_banco_mundial.py`. |
| `ventas.csv`, `tiendas.csv`, `tipo_cambio.csv` | 34-38 | Sintéticos; se regeneran con `python scripts/generar_datos_ventas.py`. |

Los datos sintéticos de ventas no corresponden a ningún país: las tiendas, ciudades y estados tienen nombres genéricos (`Tienda Centro 1`, `Ciudad A`, `Estado 1`); los importes están en unidades monetarias (UM), sin una moneda concreta; la columna `tipo_cambio` de `tipo_cambio.csv` es un valor de ejemplo de unidades monetarias por dólar estadounidense, y los correos usan los dominios reservados para ejemplos `example.com`, `example.org` y `example.net` (RFC 2606).

El notebook `38` genera además, con NumPy y semilla fija, un archivo de ventas grande en `data_tmp/` (no versionado, en `.gitignore`). Su tamaño se controla con la variable de entorno `PY311_RENGLONES`: un millón de renglones por omisión (unos 63 MB en CSV) y 20,000 en la prueba automática.

## Verificación

```bash
python scripts/verificar_datos.py            # integridad (SHA-256)
python scripts/verificar_datos.py --enlaces  # además, estado de las URL de origen
```

Si una URL de origen deja de responder, los notebooks siguen funcionando: basta con actualizar la URL en `fuentes.json`. Si se reemplaza un archivo, se actualiza su `sha256` en el manifiesto. `verificar_datos.py` también falla si en `data/` hay un archivo de datos que no está en el manifiesto.

El Banco Mundial revisa sus cifras periódicamente: si se vuelve a ejecutar `scripts/descargar_banco_mundial.py` después de una revisión, el archivo cambia y hay que actualizar su `sha256`, su fecha de consulta y comprobar que el notebook 27 sigue funcionando.
