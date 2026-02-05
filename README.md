# Introducción a Ingeniería y Analítica de Datos con Python (Py311)

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/codespaces)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Polars](https://img.shields.io/badge/Backend-Polars-CD792C?style=for-the-badge&logo=polars&logoColor=white)](https://pola.rs/)

> **Próxima Edición:** 23 de Febrero | Lunes a Jueves | 12 Sesiones Online

Este repositorio contiene el material oficial del curso **"Introducción a Ingeniería y Analítica de Datos con Python"**. Un programa intensivo diseñado para transformar tu perfil técnico, pasando de la manipulación básica de datos a la construcción de pipelines de ingeniería modernos y escalables.

## 🚀 Acerca del Curso

Este no es otro curso básico de Pandas. Es una formación en **Ingeniería de Datos Moderna** donde aprenderás a:

* **Optimizar Memoria:** Uso de backends modernos (PyArrow) y tipos de datos eficientes.
* **Escalar Procesos:** Transición de Pandas a **Polars** y **Dask** para Big Data.
* **Construir Productos:** Despliegue de dashboards interactivos con **Streamlit**.
* **Analizar Profundamente:** Técnicas de *Windowing*, ETL avanzado y visualización estadística.

Todo el entorno se ejecuta en la nube mediante **GitHub Codespaces**, eliminando problemas de instalación local.

---

## 📅 Temario y Estructura

El curso consta de **12 sesiones de 2 horas** (24 horas totales), divididas en 5 bloques estratégicos:

| Bloque | Temática Principal | Tecnologías Clave |
| :--- | :--- | :--- |
| **I. Fundamentos** | Computación numérica y álgebra lineal vectorial. | `NumPy`, `SciPy` |
| **II. Estructura** | Pandas Moderno: Backend PyArrow y optimización. | `Pandas 2.0`, `PyArrow` |
| **III. Analítica** | ETL, Limpieza avanzada, Windowing y Crosstabs. | `Pandas`, `Window Ops` |
| **IV. Ingeniería** | Formatos binarios, Polars y Computación Distribuida. | `Parquet`, `Polars`, `Dask` |
| **V. Producto** | Visualización estadística y Data Apps interactivas. | `Seaborn`, `Streamlit` |

### 📚 Lista de Contenidos (Notebooks)

#### 🔹 Módulo 1: Fundamentos Numéricos
* `01` - El proyecto SciPy y el ecosistema de datos.
* `02` - Conceptos básicos de NumPy (Arreglos y Vectores).
* `03` - Gestión de memoria y tipos de datos en NumPy.
* `04` - Generación de datos sintéticos y aleatorios.
* `05` - Aritmética vectorizada (Broadcasting).
* `06` - Manipulación y transformación de arreglos.
* `07` - Análisis numérico y estadístico básico.
* `08` - Álgebra lineal aplicada a datos.

#### 🔹 Módulo 2: Pandas Moderno y Estructura
* `09` - Introducción a Pandas y el backend **PyArrow**.
* `10` - Tipos de datos y optimización (`category` vs `object`).
* `11` - Operaciones estructurales en DataFrames.
* `12` - Índices jerárquicos y optimización de búsquedas.
* `13` - Relaciones entre datos: Uniones y Concatenaciones.
* `14` - `Merge` avanzado y comparativas de rendimiento.

#### 🔹 Módulo 3: ETL y Analítica Avanzada
* `15` - Filtrado complejo y consultas (`query`, `filter`).
* `16` - Transformaciones personalizadas (`apply`, `map`).
* `17` - **Técnicas de Ventana (Windowing):** Rolling, Expanding y Shift.
* `18` - Gestión de calidad de datos.
* `19` - Estrategias de imputación y manejo de nulos.
* `20` - Transformación y limpieza de strings/objetos.
* `21` - Agregaciones avanzadas: `groupby`, `crosstab` y `pivot_table`.

#### 🔹 Módulo 4: Ingeniería de Alto Rendimiento
* `22` - **I/O Eficiente:** Formato **Parquet** vs CSV.
* `30` - **Introducción a Polars:** El futuro de los DataFrames rápidos.
* `31` - **Computación Distribuida con Dask:** Procesamiento Out-of-Core.

#### 🔹 Módulo 5: Visualización y Despliegue
* `23` - Visualización rápida con Pandas.
* `24` - La gramática de gráficos: Matplotlib.
* `25` - Personalización de elementos gráficos.
* `26` - Tipos de gráficos fundamentales.
* `28` - Visualización estadística con **Seaborn**.
* `29` - Objetos y temas en Seaborn.
* `32` - **Proyecto Final:** Data Apps interactivas con **Streamlit**.

---

## 🛠️ Instalación y Uso

¡Olvídate de configurar entornos locales! Este repositorio está configurado para **GitHub Codespaces**.

1.  Haz clic en el botón **"Code"** (verde) arriba a la derecha.
2.  Ve a la pestaña **"Codespaces"**.
3.  Haz clic en **"Create codespace on main"**.

El entorno se iniciará automáticamente con:
* Python 3.11
* JupyterLab
* Todas las librerías instaladas (Polars, Dask, Streamlit, etc).
* Puertos configurados para ver tus apps.

### Ejecución Local (Opcional)
Si prefieres trabajar en tu máquina:

```bash
# Clonar el repositorio
git clone [https://github.com/tusuario/py311.git](https://github.com/tusuario/py311.git)
cd py311

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Iniciar Jupyter
jupyter lab
