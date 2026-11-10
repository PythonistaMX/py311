# Contribuir a Py311

Gracias por contribuir al curso Py311.

## Flujo recomendado

1. Haz *fork* del repositorio.
2. Crea una rama descriptiva desde `main`.
3. Realiza cambios pequeños y enfocados.
4. Abre un *Pull Request* con una descripción clara del cambio.

## Tipos de contribución aceptados

- Correcciones de erratas o de claridad pedagógica.
- Mejoras de ejemplos en los *notebooks*.
- Actualización de dependencias y herramientas.
- Pruebas automatizadas para el proyecto `streamlit-project/` (en su propio repositorio, [PythonistaMX/streamlit-project](https://github.com/PythonistaMX/streamlit-project)).

## Convenciones de los *notebooks*

- **Numeración.** Los *notebooks* se numeran con dos dígitos (`NN_tema.ipynb`) en el orden en que se imparten. Si se agrega, divide o renumera un *notebook*, actualiza la tabla de contenidos y la descripción de módulos del `README.md`, la estructura de sesiones de `INSTRUCTOR_GUIDE.md` y las referencias a otros *notebooks* dentro del texto.
- **Estructura.** Cada celda de código va precedida de una celda de texto que explica lo que hace (por ejemplo, «La siguiente celda...»). La sintaxis de funciones y métodos se presenta en un bloque de código seguido de «Donde:» y la descripción de cada argumento.
- **Sin salidas guardadas.** Limpia las salidas antes de hacer *commit* (en JupyterLab: *Edit → Clear Outputs of All Cells*).
- **Errores intencionales.** Si una celda muestra un error a propósito, agrégale la etiqueta `raises-exception` (en JupyterLab: barra lateral derecha → *Common Tools* → *Cell Tags*). Sin esa etiqueta, el CI la considera una falla.
- **Archivos generados.** Los archivos que crea un *notebook* se escriben en `data_tmp/`, que está en `.gitignore`. Usa nombres que no coincidan con los de otros *notebooks*. Si un *notebook* necesita escribir fuera de `data_tmp/`, agrega esos archivos a `.gitignore`.
- **Datos.** Los datos de ejemplo van en `data/`. Si son sintéticos, incluye en `scripts/` el programa que los genera, con una semilla fija.

## Criterios para aprobar un PR

- El contenido debe mantener consistencia con la ruta didáctica del curso.
- El CI (*Notebooks Smoke Test*) debe pasar: ejecuta todos los *notebooks* completos con las versiones de `requirements.txt`. El *notebook* `26`, que descarga datos del INEGI, se ejecuta en un paso que no bloquea.
- En `streamlit-project/` deben pasar:
  - `ruff check .`
  - `pytest --cov=src --cov-report=term-missing`
- Los cambios deben incluir contexto en el PR (problema, solución, impacto).

## Estilo y convenciones

- Usa Python 3.11 o posterior.
- Prefiere nombres descriptivos en español para el material didáctico.
- Mantén los ejemplos reproducibles y autoexplicativos.
- Evita dependencias innecesarias. Si agregas una, fíjala con `==` en `requirements.txt`.

## Reporte de errores

Incluye, de ser posible:

- *Notebook* o archivo afectado.
- Pasos para reproducir.
- Resultado esperado y actual.
- Captura del error o *traceback*.

## Licencia

Al contribuir, aceptas que tus aportes se publiquen bajo la licencia del repositorio.
