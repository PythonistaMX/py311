# Fundamentos de Python para Ingeniería y Analítica de Datos (Py311)

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/codespaces)
[![License](https://img.shields.io/badge/License-CC--BY%204.0-blue.svg?style=for-the-badge)](LICENSE)
[![Polars](https://img.shields.io/badge/Backend-Polars-CD792C?style=for-the-badge&logo=polars&logoColor=white)](https://pola.rs/)

Este repositorio contiene el material oficial del curso **Py311**, primer curso de la ruta de Ingeniería de Datos con Python. Cubre los fundamentos de computación numérica, manipulación y visualización de datos, y presenta las herramientas modernas de análisis que se usarán a lo largo de toda la ruta.

---

## 🗺️ Ruta de Aprendizaje

### Prerequisitos recomendados

Este curso asume conocimiento previo de Python. Si necesitas construir esa base primero:

| Curso | Título | Repositorio |
| :--- | :--- | :--- |
| Py101 | Introducción a la Programación con Python | [PythonistaMX/py101](https://github.com/PythonistaMX/py101) |
| Py111 | Programación Orientada a Objetos con Python | [PythonistaMX/py111](https://github.com/PythonistaMX/py111) |

### Continuación de la ruta

Py311 es el punto de entrada de una ruta progresiva de ingeniería de datos moderna:

| Curso | Título | Estado |
| :--- | :--- | :--- |
| **Py311** | Fundamentos de Python para Ingeniería y Analítica de Datos | ✅ Este curso |
| Py321 | Orquestación con Apache Airflow | Próximamente |
| Py331 | Spark, PySpark y SparkSQL | Próximamente |
| Py341 | Pipelines batch y streaming con Apache Beam | Próximamente |
| Py351 | Streaming con Python (RabbitMQ y Kafka) | Próximamente |
| Py361 | Data Apps: Streamlit, Dash y FastAPI | Próximamente |
| Py371 | DataOps y Data Engineering Moderno | Próximamente |

---

## 🚀 Acerca del Curso

Un programa intensivo orientado a construir la base técnica necesaria para trabajar como ingeniero o analista de datos en entornos modernos. Al completarlo serás capaz de:

* **Dominar el ecosistema numérico:** NumPy, SciPy y álgebra lineal aplicada a datos.
* **Manipular datos con Pandas moderno:** Tipos eficientes, limpieza, agregaciones y ventanas.
* **Visualizar con precisión estadística:** Matplotlib y Seaborn, y como tema extra la gramática de gráficos de ggplot2 con plotnine.
* **Optimizar memoria y rendimiento:** PyArrow como formato común y Polars para análisis de alto rendimiento, incluido el procesamiento de datos más grandes que la memoria con consultas diferidas y *streaming*.
* **Ver un producto de datos en acción:** una demo de *dashboard* interactivo con Streamlit cierra el curso.

Todo el entorno se ejecuta en la nube mediante **GitHub Codespaces**, sin necesidad de instalación local.

---

## 📅 Temario y Estructura

El curso consta de **14 sesiones de 2 horas** (28 horas totales), divididas en 4 bloques, más una demo de *Streamlit* al final de la última sesión y un tema extra sobre la gramática de gráficos con *plotnine*:

| Bloque | Temática Principal | Tecnologías Clave |
| :--- | :--- | :--- |
| **I. Fundamentos** | Computación numérica y álgebra lineal vectorial | `NumPy`, `SciPy` |
| **II. Pandas Moderno** | Backend PyArrow, manipulación y limpieza de datos | `Pandas 3`, `PyArrow` |
| **III. Visualización** | Control fino y visualización estadística | `Matplotlib`, `Seaborn` |
| **IV. Arrow y Polars** | Formato Arrow, Polars, consultas diferidas y datos más grandes que la memoria | `PyArrow`, `Polars` |
| *Demo* | Un *dashboard* interactivo sin desarrollo web | `Streamlit` |

### 📚 Contenidos


#### 🧭 Tabla de contenidos (enlaces rápidos)
- [01_el_ecosistema_de_datos_con_python.ipynb](01_el_ecosistema_de_datos_con_python.ipynb)
- [02_conceptos_basicos_de_numpy.ipynb](02_conceptos_basicos_de_numpy.ipynb)
- [03_gestion_de_arreglos_de_numpy.ipynb](03_gestion_de_arreglos_de_numpy.ipynb)
- [04_arreglos_con_contenido_aleatorio.ipynb](04_arreglos_con_contenido_aleatorio.ipynb)
- [05_operaciones_basicas_con_arreglos.ipynb](05_operaciones_basicas_con_arreglos.ipynb)
- [06_manipulacion_de_arreglos_de_numpy.ipynb](06_manipulacion_de_arreglos_de_numpy.ipynb)
- [07_gestion_y_analisis_de_datos_de_numpy.ipynb](07_gestion_y_analisis_de_datos_de_numpy.ipynb)
- [08_algebra_lineal_con_numpy.ipynb](08_algebra_lineal_con_numpy.ipynb)
- [09_introduccion_a_pandas.ipynb](09_introduccion_a_pandas.ipynb)
- [10_tipos_de_datos_de_pandas.ipynb](10_tipos_de_datos_de_pandas.ipynb)
- [11_operaciones_basicas_con_dataframes.ipynb](11_operaciones_basicas_con_dataframes.ipynb)
- [12_indices_y_multiindices.ipynb](12_indices_y_multiindices.ipynb)
- [13_datos_categoricos.ipynb](13_datos_categoricos.ipynb)
- [14_uniones_y_mezclas_de_dataframes.ipynb](14_uniones_y_mezclas_de_dataframes.ipynb)
- [15_metodo_merge.ipynb](15_metodo_merge.ipynb)
- [16_metodo_filter.ipynb](16_metodo_filter.ipynb)
- [17_metodos_apply_y_transform.ipynb](17_metodos_apply_y_transform.ipynb)
- [18_metodos_de_enmascaramiento.ipynb](18_metodos_de_enmascaramiento.ipynb)
- [19_herramientas_de_analisis_de_datos.ipynb](19_herramientas_de_analisis_de_datos.ipynb)
- [20_limpieza_y_datos_faltantes.ipynb](20_limpieza_y_datos_faltantes.ipynb)
- [21_transformacion_de_objetos.ipynb](21_transformacion_de_objetos.ipynb)
- [22_gestion_de_fechas.ipynb](22_gestion_de_fechas.ipynb)
- [23_el_accesor_str_de_pandas.ipynb](23_el_accesor_str_de_pandas.ipynb)
- [24_metodos_groupby.ipynb](24_metodos_groupby.ipynb)
- [25_funciones_de_ventana.ipynb](25_funciones_de_ventana.ipynb)
- [26_extraccion_y_almacenamiento.ipynb](26_extraccion_y_almacenamiento.ipynb)
- [27_visualizacion_de_datos_con_pandas.ipynb](27_visualizacion_de_datos_con_pandas.ipynb)
- [28_introduccion_a_matplotlib.ipynb](28_introduccion_a_matplotlib.ipynb)
- [29_figuras_y_ejes_de_matplotlib.ipynb](29_figuras_y_ejes_de_matplotlib.ipynb)
- [30_personalizacion_de_graficos_de_matplotlib.ipynb](30_personalizacion_de_graficos_de_matplotlib.ipynb)
- [31_tipos_basicos_de_graficos.ipynb](31_tipos_basicos_de_graficos.ipynb)
- [32_introduccion_a_seaborn.ipynb](32_introduccion_a_seaborn.ipynb)
- [33_objetos_de_seaborn.ipynb](33_objetos_de_seaborn.ipynb)
- [34_introduccion_a_pyarrow.ipynb](34_introduccion_a_pyarrow.ipynb) (incluye autoestudio)
- [35_introduccion_a_polars.ipynb](35_introduccion_a_polars.ipynb)
- [36_expresiones_de_polars.ipynb](36_expresiones_de_polars.ipynb) (incluye autoestudio)
- [37_polars_avanzado.ipynb](37_polars_avanzado.ipynb) (incluye autoestudio)
- [38_consultas_diferidas_y_datos_grandes.ipynb](38_consultas_diferidas_y_datos_grandes.ipynb) (incluye autoestudio)
- [39_introduccion_a_streamlit.ipynb](39_introduccion_a_streamlit.ipynb) (demo)
- [40_gramatica_de_graficos_con_plotnine.ipynb](40_gramatica_de_graficos_con_plotnine.ipynb) (tema extra)

#### 🔹 Módulo 1: Fundamentos Numéricos
* `01` - El ecosistema de datos con Python (NumPy, SciPy y herramientas clave).
* `02` - Conceptos básicos de NumPy (arreglos y vectores).
* `03` - Creación de arreglos con funciones especializadas y lectura/escritura de archivos.
* `04` - Generación de datos sintéticos y aleatorios.
* `05` - Indexado, rebanado, modificación de arreglos y *broadcasting*.
* `06` - Manipulación y transformación de arreglos.
* `07` - Análisis numérico y estadístico básico.
* `08` - Álgebra lineal aplicada a datos.

#### 🔹 Módulo 2: Pandas Moderno y Estructura
* `09` - Introducción a Pandas.
* `10` - Tipos de datos de Pandas y funciones de conversión de tipos.
* `11` - Operaciones estructurales en DataFrames: `sort_values()`, `sort_index()`, `rename()` y métodos de indexado.
* `12` - Índices simples (`pd.Index`) y multiíndices (`pd.MultiIndex`).
* `13` - Datos categóricos: `pd.cut()`, `pd.qcut()` y `pd.get_dummies()`.
* `14` - Uniones y mezclas de DataFrames.
* `15` - El método `merge()`: uniones inner, outer, left y right.
* `16` - El método `filter()`: filtrado de columnas e índices por etiqueta.
* `17` - Transformaciones personalizadas: `apply()`, `transform()`, `map()` y `pipe()`.
* `18` - Técnicas de enmascaramiento avanzado: `mask()`, `where()` y `clip()`.
* `19` - Herramientas de análisis de datos: `value_counts()`, `corr()`, `cov()`, `eval()`, `assign()` y más.
* `20` - Valores nulos (`np.nan`, `pd.NA`, `pd.NaT`) y estrategias de imputación.
* `21` - Transformación y limpieza de objetos.
* `22` - Gestión de fechas: `pd.date_range()`, `.dt`, indexación temporal y `resample()`.
* `23` - El accesor `.str`: manipulación vectorizada de cadenas de caracteres.
* `24` - Agregaciones avanzadas: `groupby`, `crosstab` y `pivot_table`.
* `25` - Window functions (funciones de ventana): `shift`, `rolling` y `expanding`.
* `26` - Extracción y almacenamiento de datos.
* `27` - Visualización de datos con Pandas.

#### 🔹 Módulo 3: Visualización Estadística
* `28` - Introducción a Matplotlib (fundamentos).
* `29` - Figuras, ejes y gráficos de líneas en Matplotlib (`figure`, `axes`, subplots, marcadores, colores, leyendas).
* `30` - Personalización de gráficos de Matplotlib (títulos, etiquetas, límites, rejillas, marcas, guardado, estilos e imágenes).
* `31` - Tipos básicos de gráficos (scatter, line, bar, histogramas).
* `32` - Introducción a Seaborn: funciones relacionales, categóricas, de distribución, de regresión y matriciales; formatos largo y ancho; integración con Matplotlib; funciones a nivel de figura (`relplot`, `displot`, `catplot`, `lmplot`), rejillas y estética.
* `33` - La interfaz de objetos de Seaborn (`seaborn.objects`): la gramática de gráficos en Seaborn, con marcas, estadísticas, movimientos, escalas, facetas y su equivalencia con plotnine.

> **📊 Nota:** Matplotlib para control fino de bajo nivel; las funciones de Seaborn para exploración rápida; `seaborn.objects` como introducción a la gramática de gráficos, que se estudia a fondo con plotnine en el tema extra `40`.

#### 🔹 Módulo 4: Arrow y Polars
* `34` - **Introducción a PyArrow:** formato columnar, arrays, `pyarrow.compute`, tablas y schemas, Parquet y Feather, y Arrow en Pandas 3 y Polars. *Autoestudio:* tipos anidados, ChunkedArray y RecordBatch, y conjuntos de datos particionados con `pyarrow.dataset`.
* `35` - **Introducción a Polars:** dataframes, lectura y escritura, contextos, selección con selectores, filtros, nulos, agrupación, y la integración de Polars con Pandas, PyArrow y NumPy (cuándo se copian los datos, nulo y `NaN`).
* `36` - **Expresiones en Polars:** reglas de las expresiones, condicionales, tipos y `cast()`, `Categorical` y `Enum`, namespaces `.str` y `.dt`, funciones de ventana y guía de traducción Pandas 3 → Polars. *Autoestudio:* listas y structs.
* `37` - **Combinación y remodelado de tablas con Polars:** joins y `pivot()`/`unpivot()`. *Autoestudio:* combinación por la clave más cercana (`join_asof`).
* `38` - **Consultas diferidas y datos grandes:** modo diferido, `scan_csv()` y `scan_parquet()`, lectura del plan con `explain()` y sus optimizaciones, `collect()` y el motor streaming, `sink_parquet()`/`sink_csv()`, conjuntos particionados con el esquema de Hive y un ejemplo completo con un archivo de ventas grande generado con NumPy. *Autoestudio:* SQL, `pl.collect_all()`, `pl.PartitionBy` y `collect_batches()`, y una medición de rendimiento frente a Pandas.

Los notebooks `34` a `38` usan los mismos datos sintéticos de ventas (`data/ventas.csv`, `data/tiendas.csv` y `data/tipo_cambio.csv`), que se regeneran con `python scripts/generar_datos_ventas.py`. El notebook `38` genera además, con NumPy y sin descargas, un archivo de ventas grande en `data_tmp/`: por omisión, un millón de renglones (unos 63 MB en CSV); la variable de entorno `PY311_RENGLONES` cambia el tamaño.

#### 📘 Autoestudio

Algunas secciones avanzadas de los notebooks `34` a `38` no se ven en clase: llevan el título «📘 Autoestudio», un aviso con lo que se aprende, los requisitos y el tiempo estimado, y terminan con un ejercicio y una celda que comprueba el resultado con `assert`. Ninguna sección de clase depende de ellas.

| Notebook | Sección | Requisitos (en clase) | Tiempo |
| :--- | :--- | :--- | :---: |
| [`34`](34_introduccion_a_pyarrow.ipynb) | Tipos anidados | 34: arrays y `pyarrow.compute` | 10 min |
| [`34`](34_introduccion_a_pyarrow.ipynb) | ChunkedArray y RecordBatch | 34: arrays | 10 min |
| [`34`](34_introduccion_a_pyarrow.ipynb) | Conjuntos de datos particionados con PyArrow | 34: tablas y Parquet | 10 min |
| [`36`](36_expresiones_de_polars.ipynb) | Listas y structs | 36: expresiones y `.str`; recomendado: «Tipos anidados» del 34 | 15 min |
| [`37`](37_polars_avanzado.ipynb) | Combinación por la clave más cercana (`join_asof`) | 37: joins; 22: fechas | 10 min |
| [`38`](38_consultas_diferidas_y_datos_grandes.ipynb) | SQL en Polars | 37: joins; 38: modo diferido y ejemplo completo | 15 min |
| [`38`](38_consultas_diferidas_y_datos_grandes.ipynb) | Varias consultas a la vez (`pl.collect_all`) | 38: plan y ejecución | 5 min |
| [`38`](38_consultas_diferidas_y_datos_grandes.ipynb) | Destinos particionados y lotes (`pl.PartitionBy`, `collect_batches()`) | 38: `sink_parquet()` y ejemplo completo | 10 min |
| [`38`](38_consultas_diferidas_y_datos_grandes.ipynb) | Medición de rendimiento: Pandas y Polars | 38 completo; 24: `groupby` | 20 min |
| | | **Total** | **≈ 105 min** |

Los notebooks nunca dependen de un enlace externo para obtener sus datos: cada archivo de `data/` está versionado en el repositorio y su procedencia (fuente, URL de origen, cobertura, licencia y huella SHA-256) se registra en [`data/fuentes.json`](data/fuentes.json). `python scripts/verificar_datos.py` comprueba la integridad de los archivos y, con `--enlaces`, informa qué URL de origen dejaron de responder; *GitHub Actions* lo ejecuta en cada PR y cada mes. La única excepción deliberada es el notebook `26`, cuyo tema es precisamente descargar datos del INEGI.

#### 🎬 Demo: una *data app* con Streamlit
* `39` - **Demo de Streamlit:** un *dashboard* web sin HTML, CSS ni JavaScript, construido con *Polars* y los gráficos de *Matplotlib* y *Seaborn* del curso. Es una demostración de cierre: no se evalúa y ningún *notebook* depende de ella.

> **Nota sobre la numeración:** la demo conserva el `39` porque la app de referencia ([PythonistaMX/streamlit-project](https://github.com/PythonistaMX/streamlit-project)) lo cita como N39, y el tema extra conserva el `40`.

#### ⭐ Tema extra: Gramática de gráficos
* `40` - **La gramática de gráficos con plotnine:** origen (Wilkinson y ggplot2), datos ordenados, mapeos estéticos, geometrías y capas, estadísticas, posiciones, escalas, coordenadas, facetas, temas, un caso práctico con los datos de ventas y equivalencias ggplot2 → plotnine.

---

## 📁 Estructura del repositorio

| Ruta | Contenido |
| :--- | :--- |
| `01_*.ipynb` … `40_*.ipynb` | Notebooks del curso. |
| `data/` | Datos de ejemplo y su manifiesto de procedencia (`fuentes.json`). |
| `scripts/` | Programas auxiliares: generador de los datos de ventas y verificador de los datos (`verificar_datos.py`). |
| `img/` | Imágenes usadas en los notebooks. |
| `streamlit-project/` | Submódulo con la versión de referencia de la app de la demo `39` ([PythonistaMX/streamlit-project](https://github.com/PythonistaMX/streamlit-project)), con pruebas y CI/CD. |
| `data_tmp/`, `mi_app_streamlit/` | Archivos que generan los notebooks al ejecutarse; están en `.gitignore`. |

### Pruebas automáticas

En cada *push* y *pull request* a `main`, el workflow **Notebooks Smoke Test** ejecuta todos los notebooks completos con las versiones fijadas en `requirements.txt`, incluidas las secciones de autoestudio y sus soluciones. Para que termine en pocos segundos, define `PY311_RENGLONES=20000`, de modo que el notebook `38` genera un archivo grande reducido. Las celdas que muestran un error a propósito llevan la etiqueta `raises-exception`; cualquier otro error hace fallar la prueba. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para las convenciones de los notebooks.

---

## 🛠️ Instalación y Uso

¡Olvídate de configurar entornos locales! Este repositorio está configurado para **GitHub Codespaces**.

1. Haz clic en el botón **"Code"** (verde) arriba a la derecha.
2. Ve a la pestaña **"Codespaces"**.
3. Haz clic en **"Create codespace on main"**.

El entorno se iniciará automáticamente con:
* Python 3.11
* JupyterLab
* Todas las librerías instaladas (Polars, Streamlit, etc.)
* Puertos configurados para visualizar tus apps.

### Ejecución Local (Opcional)
Si prefieres trabajar en tu máquina:

```bash
# Clonar el repositorio (con el submódulo streamlit-project)
git clone --recurse-submodules https://github.com/PythonistaMX/py311.git
cd py311

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Iniciar Jupyter
jupyter lab
```

---

## 📖 Recursos Adicionales

* [Documentación oficial de NumPy](https://numpy.org/doc/stable/)
* [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
* [Documentación oficial de Matplotlib](https://matplotlib.org/stable/)
* [Documentación oficial de Seaborn](https://seaborn.pydata.org/)
* [Documentación oficial de PyArrow](https://arrow.apache.org/docs/python/)
* [Documentación oficial de Polars](https://docs.pola.rs/)
* [Documentación oficial de Streamlit](https://docs.streamlit.io/)
* [Documentación oficial de plotnine](https://plotnine.org/) y el libro [*ggplot2: Elegant Graphics for Data Analysis*](https://ggplot2-book.org/)

---

## 📝 Licencia

Este proyecto está bajo la licencia **Creative Commons Atribución 4.0 Internacional (CC-BY 4.0)**.

**Eres libre de:**
- ✅ Compartir el material en cualquier medio o formato
- ✅ Adaptar, remezclar y crear contenido derivado
- ✅ Usar con fines comerciales

**Con la condición de:**
- 📌 **Atribución:** Debes dar crédito apropiado, proporcionar un enlace a la licencia e indicar si se han realizado cambios.

Para más información, visita: https://creativecommons.org/licenses/by/4.0/

Véase el archivo [LICENSE](LICENSE) para los términos completos.
