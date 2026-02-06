# Introducción a Ingeniería y Analítica de Datos con Python (Py311)

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Codespaces](https://img.shields.io/badge/GitHub-Codespaces-brightgreen?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/codespaces)
[![License](https://img.shields.io/badge/License-CC--BY%204.0-blue.svg?style=for-the-badge)](LICENSE)
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

El curso consta de **12 sesiones de 2 horas** (24 horas totales), divididas en 6 bloques estratégicos:

| Bloque | Temática Principal | Tecnologías Clave |
| :--- | :--- | :--- |
| **I. Fundamentos** | Computación numérica y álgebra lineal vectorial. | `NumPy`, `SciPy` |
| **II. Pandas Moderno** | Backend PyArrow, manipulación y limpieza de datos. | `Pandas 2.0`, `PyArrow` |
| **III. Visualización** | Gramática de gráficos (ggplot2-like), estadística y control fino. | `Matplotlib`, `Seaborn`, `Plotnine` |
| **IV. Ingeniería Moderna** | Arrow, Polars y optimización de memoria. | `PyArrow`, `Polars` |
| **V. Data Apps** | Dashboards interactivos sin necesidad de web development. | `Streamlit` |
| **VI. Escalado** | Procesamiento paralelo y escalabilidad distribuida. | `Dask` |

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
* `09` - Introducción a Pandas.
* `10` - Tipos de datos y optimización (`category` vs `object`).
* `11` - Operaciones estructurales en DataFrames.
* `12` - Índices jerárquicos y optimización de búsquedas.
* `13` - Datos categóricos y relaciones.
* `14` - `Merge` avanzado y comparativas de rendimiento.
* `15` - Filtrado complejo (`filter`, `query`).
* `16` - Transformaciones personalizadas (`apply`, `transform`).
* `17` - Técnicas de enmascaramiento avanzado.
* `18` - Gestión de calidad de datos.
* `19` - Estrategias de imputación y manejo de nulos.
* `20` - Uniones y mezclas de DataFrames.
* `21` - Transformación y limpieza de objetos.
* `22` - Agregaciones avanzadas: `groupby`, `crosstab`, `pivot_table` y `window functions`.
* `23` - Extracción y almacenamiento de datos.
* `24` - Visualización de datos con Pandas.

#### 🔹 Módulo 3: Visualización Estadística
* `25` - Introducción a Matplotlib (fundamentos).
* `26` - Elementos de un gráfico (títulos, ejes, leyendas, estilos).
* `27` - Tipos básicos de gráficos (scatter, line, bar, histogramas).
* `28` - Plotnine (Gramática de gráficos para profesionales - reproducibilidad).
* `29` - Introducción a Seaborn (visualización estadística rápida).
* `30` - Objetos especializados en Seaborn (regresión, correlación, distribuciones).

> **📊 Nota Profesional:** Plotnine (basado en ggplot2) es ideal para reportes reproducibles y migración desde R. Seaborn para exploración iterativa. Matplotlib para control fino de bajo nivel.

#### 🔹 Módulo 4: Ingeniería de Datos Moderna
* `31` - **Introducción a PyArrow:** Arrays, Tables y Backend Pandas.
* `32` - **Introducción a Polars:** API expresiva y evaluación lazy.
* `33` - **Polars Avanzado:** Window functions, optimización y decisiones arquitectónicas.

#### 🔹 Módulo 5: Data Apps Interactivas
* `34` - **Introducción a Streamlit:** Dashboards web sin HTML/CSS/JavaScript.

#### 🔹 Módulo 6: Computación Distribuida
* `36` - **Introducción a Dask:** Procesamiento paralelo y escalabilidad out-of-core.

---

## 🛠️ Instalación y Uso

¡Olvídate de configurar entornos locales! Este repositorio está configurado para **GitHub Codespaces**.

1. Haz clic en el botón **"Code"** (verde) arriba a la derecha.
2. Ve a la pestaña **"Codespaces"**.
3. Haz clic en **"Create codespace on master"**.

El entorno se iniciará automáticamente con:
* Python 3.11
* JupyterLab
* Todas las librerías instaladas (Polars, Dask, Streamlit, etc).
* Puertos configurados para ver tus apps.

### Ejecución Local (Opcional)
Si prefieres trabajar en tu máquina:

```bash
# Clonar el repositorio
git clone https://github.com/tusuario/py311.git
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

* **Documentación oficial de Pandas:** https://pandas.pydata.org/docs/
* **Documentación oficial de Polars:** https://docs.pola.rs/
* **Documentación oficial de Dask:** https://docs.dask.org/
* **Documentación oficial de Streamlit:** https://docs.streamlit.io/

---

## 📝 Licencia

Este proyecto está bajo la licencia **Creative Commons Atribución 4.0 Internacional (CC-BY 4.0)**.

**Eres libre de:**
- ✅ Compartir el material en cualquier medio o formato
- ✅ Adaptar, remezclar y crear contenido derivado
- ✅ Usar con fines comerciales

**Con la condición de:**
- 📌 **Atribución:** Debes dar crédito apropiado, proporcionar un enlace a la licencia e indicar si se han realizado cambios

Para más información, visita: https://creativecommons.org/licenses/by/4.0/

Véase el archivo [LICENSE](LICENSE) para los términos completos.

---

## 👨‍💼 Autor

Material educativo oficial del programa de Ingeniería de Datos.

