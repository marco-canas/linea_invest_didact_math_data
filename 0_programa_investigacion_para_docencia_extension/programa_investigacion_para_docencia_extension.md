

# Prompt para generar un programa de investigación para docencia y extensión  

Dame un programa que defina mi actividad investigativa para enriquecimiento de la docencia y la extensión a través de la investigación en los siguientes frentes: desarrollo del pensamiento crítico y el pensamiento computacional para el aprendizaje del cálculo diferencial, integral, vectorial y de varias variables, la geometría vectorial, el álgebra lineal (para la formación en ciencias agrarias con Python para la ciencia de datos), las matemáticas I y II para fundamentación matemática de los estudiantes de la Facultad de Ciencias Económicas y la formación en Machine Learning y Deep Learning para estudiantes de G-Líderes del programa de Administración de empresas de la Universidad de Antioquia. También la investigación en la aplicación el algoritmo Sarimax para la predicción de epidemias de dengue en función de datos meteorológicos en Caucasia - Antioquia.   


# **Programa de Actividad Investigativa**   

Programa pensado para enriquecer la docencia y la extensión en los frentes que indicas. Lo organizo en: objetivos, líneas de investigación (con proyectos ejemplo), actividades docentes y de extensión, metodología y herramientas (stack técnico), cronograma por fases, productos esperados y métricas/indicadores de éxito. Puedes tomarlo como base para un plan institucional, una postulación a convocatoria o para presentar ante tu facultad.

# Programa de Actividad Investigativa: “Matemáticas Computacionales y Ciencia de Datos para la Docencia, la Extensión y la Predicción Epidemiológica (MCC-Data)”

## 1. Resumen ejecutivo

Diseñar e implementar un programa de investigación-aplicada que potencie la enseñanza del cálculo, álgebra lineal y geometría vectorial a través de herramientas computacionales (Python, Jupyter), integre formación en Machine Learning y Deep Learning para estudiantes de Administración y programas afines, y desarrolle una línea aplicada de predicción de epidemias (SARIMAX) basada en datos meteorológicos y epidemiológicos en Caucasia — Antioquia. El programa busca producir recursos docentes reutilizables (cuadernos, videos), prototipos de modelos predictivos, formación de semilleros y productos de extensión (workshops, cursos cortos, asesorías).

## 2. Objetivos

**Objetivo general**

* Fortalecer la docencia y la extensión mediante investigación aplicada en enseñanza de matemáticas (cálculo, álgebra lineal, geometría) y ciencia de datos, y desarrollar modelos predictivos SARIMAX para dengue en Caucasia que informen decisiones locales de salud pública.

**Objetivos específicos**

1. Diseñar materiales didácticos interactivos (Jupyter notebooks + vídeos) que integren contenido teórico y prácticas en Python para cálculo, álgebra lineal, geometría vectorial y matemáticas I-II.
2. Implementar un currículo de formación en Machine Learning y Deep Learning (básico → avanzado) dirigido a estudiantes “G-Líderes” del programa de Administración.
3. Investigar y validar modelos SARIMAX (y compararlos con enfoques ML/Deep Learning) para predicción temprana de brotes de dengue usando datos meteorológicos y epidemiológicos.
4. Generar un semillero interdisciplinario (estudiantes de Administración, Agrarias, Matemáticas, Estadística, Ingeniería) para proyectos de investigación y extensión.
5. Difundir resultados mediante publicaciones, talleres locales y repositorios de acceso abierto.

## 3. Líneas de investigación (frentes) y proyectos ejemplo

### A. Enseñanza computacional del Cálculo (diferencial, integral, vectorial y multivariable)

**Proyectos**

* P1.1: “Visualizaciones interactivas para límites, derivadas e integrales” — notebooks con ipywidgets, animaciones y actividades autoguiadas.
* P1.2: “Proyecto de aprendizaje por problemas: optimización económica con cálculo multivariable” — casos aplicados a administración y agrarias.

**Productos**

* 30 notebooks (Jupyter) con guías y ejercicios, 20 mini-videos tutoriales, banco de evaluaciones automáticas (nbgrader / GitHub).

### B. Geometría vectorial y Álgebra lineal aplicada a ciencias agrarias con Python

**Proyectos**

* P2.1: “Álgebra lineal aplicada a modelos de mezcla y sensibilidad en suelos” — prácticas con numpy, scipy y visualización 3D.
* P2.2: “Mapeo vectorial y geometría para modelado espacial simple” — integración con geopandas para datos territoriales.

**Productos**

* Módulos reutilizables (notebooks), datasets de práctica, guías para docentes de agrarias.

### C. Matemáticas I y II: Fundamentos para Ciencias Económicas

**Proyectos**

* P3.1: “Módulos de reforzamiento adaptativo” — ejercicios automatizados con retroalimentación.
* P3.2: “Laboratorio de modelado microeconómico con Python” — integración de cálculo y álgebra.

**Productos**

* Paquetes de contenido alineado con DBA/plan de estudios, talleres de formación docente.

### D. Machine Learning y Deep Learning para estudiantes G-Líderes (Administración)

**Proyectos**

* P4.1: Curso modular (3 niveles) con casos empresariales: regresión, clasificación, series temporales, redes neuronales.
* P4.2: “Capstone” aplicado: proyecto en equipo (ej.: predicción de demanda, segmentación de clientes).

**Productos**

* Curso completo (notebooks + vídeos + rúbrica de evaluación), 10 proyectos estudiantiles públicos en GitHub.

### E. SARIMAX para predicción de epidemias de dengue (Caucasia - Antioquia)

**Proyectos**

* P5.1: “Recolección y limpieza de series meteorológicas y epidemiológicas (2007–actual)” — pipeline reproducible.
* P5.2: “Modelado SARIMAX y comparación con modelos ML/Deep Learning” — validación, pronóstico, explicación (SHAP para ML).
* P5.3: “Dashboard de alerta temprana y manual de uso para autoridades locales” — entregable de extensión.

**Productos**

* Dataset limpio y documentado, notebook reproducible SARIMAX (statsmodels), informe técnico, dashboard ligero (Streamlit/Voila).

## 4. Metodología y flujo de trabajo (aplicable a todas las líneas)

1. **Revisión conceptual y necesidades locales**: consulta con docentes, gestores de salud (para dengue), y actores en agrarias y administración.
2. **Diseño instruccional**: crear objetivos de aprendizaje, rúbricas, y artefactos (notebooks + videos).
3. **Desarrollo reproducible**: GitHub + GitHub Actions para CI de notebooks, datos documentados, licencias abiertas.
4. **Implementación experimental**: pruebas con grupos piloto (estudiantes), recolección de retroalimentación.
5. **Evaluación y ajuste**: indicadores de aprendizaje y desempeño de modelos.
6. **Extensión**: talleres, cursos cortos y transferencia a actores locales (salud pública, productores).

## 5. Stack técnico recomendado (Python-centered)

* Python 3.9+
* Data wrangling: pandas, numpy
* Series temporales / SARIMAX: statsmodels (SARIMAX), pmdarima (auto_arima)
* ML/DL: scikit-learn, xgboost, tensorflow/keras, pytorch (opcional)
* Visualización: matplotlib, plotly, geopandas (espacial), ipywidgets, bokeh, streamlit/voila para dashboards
* Reproducibilidad: Jupyter, nbformat, nbgrader, Binder/Colab, Docker (opcional)
* Control de versiones: git + GitHub (repositorios públicos para extensión)
* Documentación: Markdown, LaTeX en notebooks, README detallados
* Herramientas de explicación de modelos: SHAP, eli5

## 6. Cronograma sugerido (3 años; se puede ajustar)

**Año 1 — Fundamentos y prototipos**

* Q1: Revisión bibliográfica, consulta con actores, conformación de semillero.
* Q2: Desarrollo de módulos de cálculo y álgebra (notebooks piloto).
* Q3: Diseño del curso ML nivel 1 para G-Líderes.
* Q4: Inicio de recolección de datos meteorológicos/epidemiológicos y primer pipeline de limpieza.

**Año 2 — Escalamiento y validación**

* Q1–Q2: Implementación de evaluaciones automáticas y talleres docentes.
* Q2–Q3: Desarrollo y validación inicial de modelos SARIMAX; comparaciones con modelos ML.
* Q3–Q4: Piloto con dashboard de alertas, cursos ML nivel 2.

**Año 3 — Consolidación y extensión**

* Q1: Publicación de resultados (informes técnicos, preprints) y entrega de recursos a la comunidad universitaria.
* Q2: Talleres de extensión en Caucasia y capacitación a equipos de salud locales.
* Q3–Q4: Postulación a convocatorias de financiación y confección de paquetes docentes/curso masivo.

## 7. Productos esperados y diseminación

* Repositorio GitHub con estructura clara (código, datos sintetizados/metadata, notebooks, dockerfile).
* Biblioteca de ~50 notebooks interactivos y ~40 video-tutoriales (5–15 min).
* Informes técnicos sobre modelado SARIMAX y su desempeño (métricas, visualizaciones).
* Dashboard/Prototipo de alerta temprana (Streamlit / Voila).
* Artículos o comunicados para revistas nacionales y memoria de eventos.
* Talleres y cursos de extensión (certificados).

## 8. Indicadores de éxito (KPIs)

* Número de notebooks producidos y descargados; número de videos publicados.
* Número de estudiantes capacitados y calificaciones promedio pre/post (ganancia de aprendizaje).
* Exactitud y utilidad de modelos SARIMAX: MAE/RMSE en horizonte 1–12 semanas, AUC para detección de picos (según diseño).
* Transferencia: número de talleres realizados con autoridades locales y adopción del dashboard.
* Producción académica: artículos, comunicaciones y proyectos de grado vinculados.

## 9. Estructura de equipo y roles

* **Investigador principal (tú)**: coordinación general, diseño curricular y proyectos SARIMAX.
* **Co-investigadores**: docente de agrarias, docente de estadística, profesional en salud pública (Caucasia).
* **Técnico de datos / DevOps**: pipeline de datos y despliegue de dashboard.
* **Semilleros**: 6–12 estudiantes (rotativos) para desarrollo y experimentos.
* **Colaboradores externos**: alcaldía/Secretaría de Salud municipal, IDEAM (o fuentes meteorológicas), Fedearroz u otras entidades locales.

## 10. Consideraciones éticas y de datos

* Privacidad de datos epidemiológicos: aplicar protocolos de anonimización y consensos con la entidad que provea datos.
* Consentimiento para uso de datos cuando aplique.
* Gestión responsable de modelos predictivos: comunicar incertidumbre y límites; evitar alarmismo; coordinar comunicación con autoridades sanitarias.

## 11. Gestión de datos y reproducibilidad

* Estructura de carpetas estandarizada (raw, processed, notebooks, results).
* Metadatos y diccionarios de datos.
* Versionado de datos y código (git), snapshots de datasets (cuando sea legalmente permitido).
* Licencias abiertas (ej.: CC-BY para materiales educativos; MIT/Apache para código).

## 12. Financiamiento y sostenibilidad (ideas)

* Postulación a convocatorias universitarias y nacionales (becas internas, MinCiencias, fondos regionales).
* Proyectos colaborativos con alcaldía/Secretaría de Salud para cofinanciar la línea SARIMAX.
* Cursos de extensión con arancel para sostenibilidad (becas para estudiantes).

## 13. Ejemplo de actividad concreta: Pipeline SARIMAX (resumen técnico)

1. **Recolección**: series semanales/mensuales de casos de dengue (salud municipal) y variables meteorológicas (precipitación, temperatura, humedad).
2. **Preprocesamiento**: imputación, transformación (differences, log), análisis estacional.
3. **Exploración**: autocorrelaciones (ACF/PACF), cross-correlation entre meteorología y casos.
4. **Selección de orden**: auto_arima para propuestas iniciales; pruebas AIC/BIC.
5. **Modelo SARIMAX**: estimación con exógenas (X = variables meteorológicas retardadas).
6. **Validación**: ventana móvil (rolling forecast) y métricas (MAE, RMSE).
7. **Comparación**: benchmarks con modelos ML (Random Forests para series, LSTM) y análisis de interpretabilidad.
8. **Despliegue**: notebook reproducible + script para actualización semanal + dashboard básico.

## 14. Plan corto para empezar (primer mes)

* Reunión con stakeholders (docencia + salud municipal).
* Definir 3 módulos prioritarios a digitalizar (p.ej., límites/derivadas; sistemas lineales; regresión para administración).
* Crear repositorio base y plantilla de notebook.
* Primer taller de reclutamiento de semilleros.

---

Si quieres, te lo entrego en formato listo para presentar (por ejemplo: **documento Word / PDF** con portada, cronograma Gantt y presupuesto estimado) o **un repositorio inicial en GitHub** con la plantilla de notebooks y un ejemplo SARIMAX mínimo. Dime cuál prefieres y lo genero inmediatamente (por ejemplo: PDF o plantilla de GitHub).
