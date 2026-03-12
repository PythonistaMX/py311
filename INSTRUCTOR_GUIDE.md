# Instructor Guide - Py311

Guía operativa para impartir el curso con consistencia técnica y pedagógica.

## Estructura sugerida (12 sesiones, 2 horas)

1. Sesión 1-2: Ecosistema y NumPy (01-08).
2. Sesión 3-6: Pandas moderno (09-27).
3. Sesión 7-8: Visualización (28-33).
4. Sesión 9: PyArrow y Polars (34-37).
5. Sesión 10: Dask (38).
6. Sesión 11-12: Streamlit y proyecto integrador (39 + `streamlit-project/`).

## Resultados de aprendizaje por bloque

- Fundamentos: modelar datos numéricos y aplicar álgebra lineal básica.
- Pandas: limpiar, transformar, agregar y analizar series temporales.
- Visualización: seleccionar y construir gráficos con criterio.
- Herramientas modernas: usar Arrow/Polars para rendimiento e interoperabilidad.
- Escalado: entender el paso a computación paralela con Dask.
- Data Apps: publicar un dashboard funcional en Streamlit.

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
- Notebooks de la sesión abren y ejecutan celdas clave.
- Dataset de ejemplo disponible (`data/`).
- `streamlit-project/` ejecuta localmente: `streamlit run app.py`.
- Pruebas del proyecto en verde: `ruff check .` y `pytest`.

## Checklist de cierre de módulo

- Se cubrieron objetivos de aprendizaje definidos.
- Alumnos entregaron evidencia de ejecución (captura o commit).
- Se registraron dudas frecuentes para retroalimentar notebooks.
- Se asignaron actividades puente para la siguiente sesión.

## Riesgos comunes y mitigación

- Diferencias de entorno: usar Codespaces por defecto.
- Versiones de librerías: mantener dependencias alineadas.
- Tiempo insuficiente: priorizar notebooks troncales y dejar extras como tarea.
