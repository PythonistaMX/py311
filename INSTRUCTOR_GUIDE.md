# Instructor Guide - Py311

Guía operativa para impartir el curso con consistencia técnica y pedagógica.

## Estructura sugerida (14 sesiones de 2 horas, 28 horas)

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
| 12 | 34, 35 | PyArrow (unos 75 min) y Polars, parte 1 (unos 45 min: dataframes, lectura y escritura, contextos, selección y filtros) |
| 13 | 35, 36 | Polars, parte 2 (unos 45 min: transformaciones, nulos, agrupación y la sección «Polars, pandas y Arrow») y expresiones de Polars (unos 75 min) |
| 14 | 37, 38, 39 | Combinación y remodelado (unos 30 min), consultas diferidas y datos grandes (unos 60 min) y demo de Streamlit (unos 30 min, con `streamlit-project/`) |
| Extra | 40 | Gramática de gráficos con plotnine: sesión adicional o estudio independiente |

Las secciones marcadas con «📘 Autoestudio» en los notebooks 34, 36, 37 y 38 (unos 105 minutos en total) no se ven en clase. Se sugiere asignarlas como actividad puente entre sesiones; cada una termina con un ejercicio que el alumno comprueba solo con `assert` y una solución oculta.

| Notebook | Sección de autoestudio | Tiempo | Sugerencia |
| :--- | :--- | :---: | :--- |
| 34 | Tipos anidados; ChunkedArray y RecordBatch; Conjuntos de datos particionados con PyArrow | 30 min | Entre las sesiones 12 y 13. |
| 36 | Listas y structs | 15 min | Entre las sesiones 13 y 14. |
| 37 | Combinación por la clave más cercana (`join_asof`) | 10 min | Después de la sesión 14. |
| 38 | SQL en Polars; Varias consultas a la vez; Destinos particionados y lotes; Medición de rendimiento | 50 min | Después de la sesión 14. |

Ninguna sección de clase depende del autoestudio. El esquema de carpetas de Hive, que también aparece en el autoestudio del 34, se explica desde cero en la clase del 38.

## Resultados de aprendizaje por bloque

- Fundamentos: modelar datos numéricos y aplicar álgebra lineal básica.
- Pandas: limpiar, transformar, agregar y analizar series temporales.
- Visualización: seleccionar y construir gráficos con criterio con Matplotlib y Seaborn.
- Arrow y Polars: usar Arrow y Polars para rendimiento e interoperabilidad con Pandas y NumPy, y procesar datos más grandes que la memoria con consultas diferidas, el motor streaming y conjuntos particionados.
- Demo de Streamlit (no evaluada): reconocer cómo un análisis se convierte en una *data app*.
- Tema extra: describir cualquier gráfico con los componentes de la gramática de gráficos (datos, mapeos, geometrías, estadísticas, escalas, coordenadas, facetas y temas) y construirlo con plotnine.

## Evaluación sugerida

- 40% ejercicios guiados por notebook.
- 20% quiz técnico (conceptos y lectura de código).
- 40% proyecto final: un análisis reproducible en *notebook* con un conjunto de datos de `data/` (fuera de sesión). Presentarlo como app de Streamlit es opcional.

## Rúbrica del proyecto final (100 puntos)

- 25 pts: Corrección funcional (el *notebook* se ejecuta de principio a fin sin errores).
- 20 pts: Calidad de datos (carga, limpieza, validaciones).
- 20 pts: Análisis y visualización (claridad de métricas y gráficos).
- 15 pts: Comunicación de resultados (narrativa, títulos y conclusiones).
- 10 pts: Calidad de código (modularidad, nombres, legibilidad).
- 10 pts: Evidencia de pruebas y/o lint.

## Checklist previa a clase

- Entorno de Codespaces listo y dependencias instaladas.
- Notebooks de la sesión abren y ejecutan celdas clave; el workflow *Notebooks Smoke Test* de `main` está en verde.
- Dataset de ejemplo disponible (`data/`). Los datos de ventas de los notebooks 34-38 se regeneran con `python scripts/generar_datos_ventas.py` (semilla fija). `python scripts/verificar_datos.py` confirma que los archivos están completos.
- Espacio en disco para el notebook `38`: con el tamaño de clase (un millón de renglones, el valor por omisión de `PY311_RENGLONES`) crea unos 100 MB en `data_tmp/` y los borra en su celda final de limpieza. Comprueba con `df -h .` que el Codespace tenga al menos 500 MB libres. Si la máquina es lenta o tiene poco espacio, reduce el tamaño cambiando el valor por omisión en la celda que lee `PY311_RENGLONES`.
- `streamlit-project/` ejecuta localmente: `streamlit run app.py`.
- La demo `39` escribe su versión de la app en `mi_app_streamlit/` (ignorada por git); el submódulo `streamlit-project/` no se modifica.
- Pruebas del proyecto en verde: `ruff check .` y `pytest`.

## Checklist de cierre de módulo

- Se cubrieron objetivos de aprendizaje definidos.
- Alumnos entregaron evidencia de ejecución (captura o commit).
- Se registraron dudas frecuentes para retroalimentar notebooks.
- Se asignaron actividades puente para la siguiente sesión.

## Riesgos comunes y mitigación

- Diferencias de entorno: usar Codespaces por defecto.
- Versiones de librerías: mantener dependencias alineadas.
- Tiempo insuficiente: priorizar notebooks troncales y dejar extras como tarea. Las sesiones más cargadas son la 5 (cinco notebooks de Pandas), la 9 y la 10 (visualización) y la 14 (tres notebooks: 37, 38 y la demo 39). En la 14, el 37 va rápido porque las uniones y el remodelado ya se vieron con Pandas (14, 15 y 24); si falta tiempo, el ejemplo completo del 38 puede ejecutarse de una vez y comentarse sobre los resultados, y la demo puede acortarse. El notebook `40` (plotnine) es extra.
