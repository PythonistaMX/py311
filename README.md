# Fundamentos de Python para Ingeniería y Analítica de Datos (Py311)

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/codespaces)
[![License](https://img.shields.io/badge/License-CC--BY%204.0-blue.svg?style=for-the-badge)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Polars](https://img.shields.io/badge/Backend-Polars-CD792C?style=for-the-badge&logo=polars&logoColor=white)](https://pola.rs/)

> **Próxima Edición:** 23 de Febrero | Lunes a Jueves | 12 Sesiones Online

Este repositorio contiene el material oficial del curso **Py311**, primer curso de la ruta de Ingeniería de Datos con Python. Cubre los fundamentos de computación numérica, manipulación y visualización de datos, y presenta las herramientas modernas de análisis y escalado que se usarán a lo largo de toda la ruta.

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
| Py331 | Procesamiento distribuido con Apache Spark | Próximamente |
| Py341 | Pipelines unificados con Apache Beam | Próximamente |
| Py351 | Streaming Systems (Kafka/RabbitMQ) | Próximamente |
| Py361 | Data Apps (Streamlit/FastAPI) | Próximamente |
| Py371 | Buenas prácticas de Ingeniería de Datos (DataOps) | Próximamente |

---

## 🚀 Acerca del Curso

Un programa intensivo orientado a construir la base técnica necesaria para trabajar como ingeniero o analista de datos en entornos modernos. Al completarlo serás capaz de:

* **Dominar el ecosistema numérico:** NumPy, SciPy y álgebra lineal aplicada a datos.
* **Manipular datos con Pandas moderno:** Tipos eficientes, limpieza, agregaciones y ventanas.
* **Visualizar con precisión estadística:** Matplotlib, Seaborn y Plotnine (gramática de gráficos).
* **Optimizar memoria y rendimiento:** PyArrow como backend y Polars para análisis de alto rendimiento.
* **Construir productos de datos:** Dashboards interactivos con Streamlit sin necesidad de desarrollo web.
* **Escalar más allá de la memoria local:** Procesamiento paralelo y distribuido con Dask.

Todo el entorno se ejecuta en la nube mediante **GitHub Codespaces**, sin necesidad de instalación local.

---

## 📅 Temario y Estructura

El curso consta de **12 sesiones de 2 horas** (24 horas totales), divididas en 6 bloques estratégicos:

| Bloque | Temática Principal | Tecnologías Clave |
| :--- | :--- | :--- |
| **I. Fundamentos** | Computación numérica y álgebra lineal vectorial | `NumPy`, `SciPy` |
| **II. Pandas Moderno** | Backend PyArrow, manipulación y limpieza de datos | `Pandas 2.0`, `PyArrow` |
| **III. Visualización** | Gramática de gráficos, estadística y control fino | `Matplotlib`, `Seaborn`, `Plotnine` |
| **IV. Herramientas Modernas** | Formato Arrow, Polars y optimización de memoria | `PyArrow`, `Polars` |
| **V. Data Apps** | Dashboards interactivos sin desarrollo web | `Streamlit` |
| **VI. Escalado** | Procesamiento paralelo y escalabilidad distribuida | `Dask` |

### 📚 Contenidos

#### 🧭 Tabla de contenidos (enlaces rápidos)
- Módulo 1: [01](01_el_proyecto_scipy.ipynb) [02](02_conceptos_basicos_de_numpy.ipynb) [03](03_gestion_de_arreglos_de_numpy.ipynb) [04](04_arreglos_con_contenido_aleatorio.ipynb) [05](05_operaciones_basicas_con_arreglos.ipynb) [06](06_manipulacion_de_arreglos_de_numpy.ipynb) [07](07_gestion_y_analisis_de_datos_de_numpy.ipynb) [08](08_algebra_lineal_con_numpy.ipynb)
- Módulo 2: [09](09_introduccion_a_pandas.ipynb) [10](10_tipos_de_datos_de_pandas.ipynb) [11](11_operaciones_basicas_con_dataframes.ipynb) [12](12_indices_y_multiindices.ipynb) [13](13_datos_categoricos.ipynb) [14](14_uniones_y_mezclas_de_dataframes.ipynb) [15](15_metodo_merge.ipynb) [16](16_metodo_filter.ipynb) [17](17_metodos_apply_y_transform.ipynb) [18](18_metodos_de_enmascaramiento.ipynb) [19](19_gestion_de_datos.ipynb) [20](20_limpieza_y_datos_faltantes.ipynb) [21](21_transformacion_de_objetos.ipynb) [22](22_metodos_groupby.ipynb) [23](23_extraccion_y_almacenamiento.ipynb) [24](24_visualizacion_de_datos_con_pandas.ipynb)
- Módulo 3: [25](25_introduccion_a_matplotlib.ipynb) [26](26_elementos_de_un_grafico.ipynb) [27](27_tipos_basicos_de_graficos.ipynb) [28](28_introduccion_a_plotnine.ipynb) [29](29_introduccion_a_seaborn.ipynb) [30](30_objetos_de_seaborn.ipynb)
- Módulo 4: [31](31_introduccion_a_pyarrow.ipynb) [32](32_introduccion_a_polars.ipynb) [33](33_polars_avanzado.ipynb)
- Módulo 5: [34](34_introduccion_a_streamlit.ipynb)
- Módulo 6: [35](35_introduccion_a_dask.ipynb)

#### 🔹 Módulo 1: Fundamentos Numéricos
* `01` - El proyecto SciPy y el ecosistema de datos.
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
* `11` - Operaciones estructurales en DataFrames.
* `12` - Índices simples (`pd.Index`) y multiíndices (`pd.MultiIndex`).
* `13` - Datos categóricos y relaciones.
* `14` - Uniones y mezclas de DataFrames.
* `15` - El método `merge()`: uniones inner, outer, left y right.
* `16` - El método `filter()`: filtrado de columnas e índices por etiqueta.
* `17` - Transformaciones personalizadas (`apply`, `transform`).
* `18` - Técnicas de enmascaramiento avanzado.
* `19` - Gestión de calidad de datos.
* `20` - Estrategias de imputación y manejo de nulos.
* `21` - Transformación y limpieza de objetos.
* `22` - Agregaciones avanzadas: `groupby`, `crosstab`, `pivot_table` y `window functions`.
* `23` - Extracción y almacenamiento de datos.
* `24` - Visualización de datos con Pandas.

#### 🔹 Módulo 3: Visualización Estadística
* `25` - Introducción a Matplotlib (fundamentos).
* `26` - Elementos de un gráfico (títulos, ejes, leyendas, estilos).
* `27` - Tipos básicos de gráficos (scatter, line, bar, histogramas).
* `28` - Plotnine (gramática de gráficos para reportes reproducibles).
* `29` - Introducción a Seaborn (visualización estadística rápida).
* `30` - Objetos especializados en Seaborn (regresión, correlación, distribuciones).

> **📊 Nota:** Plotnine (basado en ggplot2) es ideal para reportes reproducibles y migración desde R. Seaborn para exploración iterativa. Matplotlib para control fino de bajo nivel.

#### 🔹 Módulo 4: Herramientas Modernas de Datos
* `31` - **Introducción a PyArrow:** arrays, tablas y backend para Pandas.
* `32` - **Introducción a Polars:** API expresiva y evaluación lazy.
* `33` - **Polars Avanzado:** window functions, optimización y decisiones arquitectónicas.

#### 🔹 Módulo 5: Data Apps Interactivas
* `34` - **Introducción a Streamlit:** dashboards web sin HTML/CSS/JavaScript.

#### 🔹 Módulo 6: Computación Distribuida
* `35` - **Introducción a Dask:** procesamiento paralelo y escalabilidad out-of-core.

---

## 🛠️ Instalación y Uso

¡Olvídate de configurar entornos locales! Este repositorio está configurado para **GitHub Codespaces**.

1. Haz clic en el botón **"Code"** (verde) arriba a la derecha.
2. Ve a la pestaña **"Codespaces"**.
3. Haz clic en **"Create codespace on main"**.

El entorno se iniciará automáticamente con:
* Python 3.11
* JupyterLab
* Todas las librerías instaladas (Polars, Dask, Streamlit, etc.)
* Puertos configurados para visualizar tus apps.

### Ejecución Local (Opcional)
Si prefieres trabajar en tu máquina:

```bash
# Clonar el repositorio
git clone https://github.com/PythonistaMX/py311.git
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

* [Documentación oficial de Pandas](https://pandas.pydata.org/docs/)
* [Documentación oficial de Polars](https://docs.pola.rs/)
* [Documentación oficial de Dask](https://docs.dask.org/)
* [Documentación oficial de Streamlit](https://docs.streamlit.io/)

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
