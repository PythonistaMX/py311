# Datos de los notebooks

Los notebooks leen estos archivos directamente; ninguno necesita descargar nada para ejecutarse (salvo el notebook 26, cuyo tema es la descarga de datos del INEGI). La procedencia de cada archivo está en [`fuentes.json`](fuentes.json).

| Archivo | Notebooks | Origen |
| :--- | :--- | :--- |
| `covid_casos_diarios_estado.csv` | 38 | Casos confirmados diarios de COVID-19 por entidad, 2020-02-26 a 2022-04-30. Secretaría de Salud, DGE (datos abiertos); serie publicada por el tablero CONAHCYT, congelado desde el 30 de abril de 2022. |
| `ITAEE.csv` | 27 | INEGI, Indicador Trimestral de la Actividad Económica Estatal (exportado por el notebook 26). |
| `ventas.csv`, `tiendas.csv`, `tipo_cambio.csv` | 34-37 | Sintéticos; se regeneran con `python scripts/generar_datos_ventas.py`. |

## Verificación

```bash
python scripts/verificar_datos.py            # integridad (SHA-256)
python scripts/verificar_datos.py --enlaces  # además, estado de las URL de origen
```

Si una URL de origen deja de responder, los notebooks siguen funcionando: basta con actualizar la URL en `fuentes.json`. Si se reemplaza un archivo, se actualiza su `sha256` en el manifiesto.
