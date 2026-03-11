# Contribuir a Py311

Gracias por contribuir al curso Py311.

## Flujo recomendado

1. Haz fork del repositorio.
2. Crea una rama descriptiva desde `main`.
3. Realiza cambios pequenos y enfocados.
4. Abre un Pull Request con descripcion clara del cambio.

## Tipos de contribucion aceptados

- Correcciones de erratas o claridad pedagogica.
- Mejoras de ejemplos en notebooks.
- Actualizacion de dependencias y tooling.
- Pruebas automatizadas para el proyecto `streamlit-project/`.

## Criterios para aprobar PR

- El contenido debe mantener consistencia con la ruta didactica del curso.
- Los cambios no deben romper notebooks existentes.
- En `streamlit-project/` deben pasar:
  - `ruff check .`
  - `pytest --cov=src --cov-report=term-missing`
- Los cambios deben incluir contexto en el PR (problema, solucion, impacto).

## Estilo y convenciones

- Usa Python 3.11+.
- Prefiere nombres descriptivos en espanol para material didactico.
- Manten ejemplos reproducibles y autoexplicativos.
- Evita dependencias innecesarias.

## Reporte de errores

Incluye, de ser posible:

- Notebook o archivo afectado.
- Pasos para reproducir.
- Resultado esperado y actual.
- Captura de error o traceback.

## Licencia

Al contribuir, aceptas que tus aportes se publiquen bajo la licencia del repositorio.
