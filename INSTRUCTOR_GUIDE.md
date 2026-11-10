# Instructor Guide - Py311

Guía operativa para impartir el curso con consistencia técnica y pedagógica.

## Estructura sugerida (15 sesiones, 2 horas)

| Sesión | Notebooks | Tema |
| :--- | :--- | :--- |
| 1 | 01-03 | Ecosistema y NumPy básico |
| 2 | 04-06 | Arreglos aleatorios, operaciones y manipulación |
| 3 | 07-08 | Análisis con NumPy y álgebra lineal |
| 4 | 09-11 | Introducción a Pandas, tipos y operaciones básicas |
| 5 | 12-16 | Índices, categóricos, uniones, `merge` y `filter` |
| 6 | 17-20 | `apply`/`transform`, máscaras, análisis y limpieza |
| 7 | 21-23 | Transformación, fechas y texto |
| 8 | 24-26 | `groupby`, ventanas, lectura y escritura |
| 9 | 27-29 | Gráficas con Pandas; figuras, ejes y líneas en Matplotlib |
| 10 | 30-31 | Personalización de Matplotlib y tipos básicos de gráficos |
| 11 | 32-33 | Seaborn |
| 12 | 34 | PyArrow |
| 13 | 35-36 | Fundamentos y expresiones de Polars |
| 14 | 37-38 | Polars avanzado y Dask |
| 15 | 39 | Streamlit y proyecto integrador (`streamlit-project/`) |
| Extra | 40 | Gramática de gráficos con plotnine: sesión adicional o estudio independiente |

## Resultados de aprendizaje por bloque

- Fundamentos: modelar datos numéricos y aplicar álgebra lineal básica.
- Pandas: limpiar, transformar, agregar y analizar series temporales.
- Visualización: seleccionar y construir gráficos con criterio con Matplotlib y Seaborn.
- Herramientas modernas: usar Arrow/Polars para rendimiento e interoperabilidad.
- Escalado: entender el paso a computación paralela con Dask.
- Data Apps: publicar un dashboard funcional en Streamlit.
- Tema extra: describir cualquier gráfico con los componentes de la gramática de gráficos (datos, mapeos, geometrías, estadísticas, escalas, coordenadas, facetas y temas) y construirlo con plotnine.

## Evaluación sugerida

- 40% ejercicios guiados por notebook.
- 20% quiz técnico (conceptos y lectura de código).
- 40% proyecto final en Streamlit.

## Rúbrica del proyecto final (100 puntos)

- 25 pts: Corrección funcional (app ejecuta sin errores).
- 20 pts: Calidad de datos (carga, limpieza, validaciones).
- 20 pts: Análisis y visualización (claridad de métricas y gráficos).
- 15 pts: UX básica (navegación, filtros, feedback al usuario).
- 10 pts: Calidad de código (modularidad, nombres, legibilidad).
- 10 pts: Evidencia de pruebas y/o lint.

## Checklist previa a clase

- Entorno de Codespaces listo y dependencias instaladas.
- Notebooks de la sesión abren y ejecutan celdas clave; el workflow *Notebooks Smoke Test* de `main` está en verde.
- Dataset de ejemplo disponible (`data/`). Los datos de ventas de los notebooks 34-37 se regeneran con `python scripts/generar_datos_ventas.py` (semilla fija).
- `streamlit-project/` ejecuta localmente: `streamlit run app.py`.
- El notebook 39 escribe su versión de la app en `mi_app_streamlit/` (ignorada por git); el submódulo `streamlit-project/` no se modifica.
- Pruebas del proyecto en verde: `ruff check .` y `pytest`.

## Checklist de cierre de módulo

- Se cubrieron objetivos de aprendizaje definidos.
- Alumnos entregaron evidencia de ejecución (captura o commit).
- Se registraron dudas frecuentes para retroalimentar notebooks.
- Se asignaron actividades puente para la siguiente sesión.

## Riesgos comunes y mitigación

- Diferencias de entorno: usar Codespaces por defecto.
- Versiones de librerías: mantener dependencias alineadas.
- Tiempo insuficiente: priorizar notebooks troncales y dejar extras como tarea. Las sesiones más cargadas son la 5 (cinco notebooks de Pandas), la 9 y la 10 (visualización); el notebook `40` (plotnine) es extra.
