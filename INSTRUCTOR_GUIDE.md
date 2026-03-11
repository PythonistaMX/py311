# Instructor Guide - Py311

Guia operativa para impartir el curso con consistencia tecnica y pedagogica.

## Estructura sugerida (12 sesiones, 2 horas)

1. Sesion 1-2: Ecosistema y NumPy (01-08).
2. Sesion 3-6: Pandas moderno (09-26).
3. Sesion 7-8: Visualizacion (27-32).
4. Sesion 9: PyArrow y Polars (33-36).
5. Sesion 10: Dask (37).
6. Sesion 11-12: Streamlit y proyecto integrador (38 + `streamlit-project/`).

## Resultados de aprendizaje por bloque

- Fundamentos: modelar datos numericos y aplicar algebra lineal basica.
- Pandas: limpiar, transformar, agregar y analizar series temporales.
- Visualizacion: seleccionar y construir graficos con criterio.
- Herramientas modernas: usar Arrow/Polars para rendimiento e interoperabilidad.
- Escalado: entender el paso a computacion paralela con Dask.
- Data Apps: publicar un dashboard funcional en Streamlit.

## Evaluacion sugerida

- 40% ejercicios guiados por notebook.
- 20% quiz tecnico (conceptos y lectura de codigo).
- 40% proyecto final en Streamlit.

## Rubrica del proyecto final (100 puntos)

- 25 pts: Correccion funcional (app ejecuta sin errores).
- 20 pts: Calidad de datos (carga, limpieza, validaciones).
- 20 pts: Analisis y visualizacion (claridad de metricas y graficos).
- 15 pts: UX basica (navegacion, filtros, feedback al usuario).
- 10 pts: Calidad de codigo (modularidad, nombres, legibilidad).
- 10 pts: Evidencia de pruebas y/o lint.

## Checklist previa a clase

- Entorno de Codespaces listo y dependencias instaladas.
- Notebooks de la sesion abren y ejecutan celdas clave.
- Dataset de ejemplo disponible (`data/`).
- `streamlit-project/` ejecuta localmente: `streamlit run app.py`.
- Pruebas del proyecto en verde: `ruff check .` y `pytest`.

## Checklist de cierre de modulo

- Se cubrieron objetivos de aprendizaje definidos.
- Alumnos entregaron evidencia de ejecucion (captura o commit).
- Se registraron dudas frecuentes para retroalimentar notebooks.
- Se asignaron actividades puente para la siguiente sesion.

## Riesgos comunes y mitigacion

- Diferencias de entorno: usar Codespaces por defecto.
- Versiones de librerias: mantener dependencias alineadas.
- Tiempo insuficiente: priorizar notebooks troncales y dejar extras como tarea.
