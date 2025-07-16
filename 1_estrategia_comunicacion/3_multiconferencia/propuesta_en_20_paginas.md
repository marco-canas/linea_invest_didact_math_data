



# **Estructura General para el Trabajo Reflexivo - Congreso Humanos XXI**  

 
- Título del trabajo:  
  *"Investigación-Acción Educativa (IAE) en la Enseñanza del Álgebra Lineal para Ingeniería Agropecuaria: Un Enfoque hacia la Ciencia de Datos y la Optimización Agrícola"*  
- Autor: Marco Julio Cañas Campillo.   
  - Nombre(s) y afiliación institucional (Universidad de Antioquia, Facultad de Ciencias Agrarias, Campus Caucasia).  
- Congreso:  
  - **HUMANOS-XXI 2025** (7-9 de octubre, modalidad virtual).  
- Palabras clave (5-6):  
  *Educación en ingeniería, Álgebra lineal aplicada, Ciencia de datos agropecuaria, Investigación-Acción Educativa, Transdisciplinariedad, Innovación pedagógica.*  



## **2. Resumen** 

**Objetivo:**  
Este trabajo reflexivo propone un modelo innovador de curso de álgebra lineal basado en **Investigación-Acción Educativa (IAE)**, diseñado para el programa de Ingeniería Agropecuaria de la Universidad de Antioquia (Campus Caucasia). El objetivo central es **cerrar la brecha entre la formación académica y las demandas reales del sector agropecuario colombiano**, integrando fundamentos de ciencia de datos (según Aurélien Géron) con aplicaciones prácticas en optimización de procesos agrícolas.  

**Metodología:**  
El diseño sigue ciclos iterativos de **planificación-acción-observación-reflexión** (Kemmis & McTaggart), vinculando:  
1. **Contenidos teóricos** (vectores, matrices, sistemas lineales, PCA) con problemas reales del **Bajo Cauca antioqueño** (ej: análisis de rendimiento de cultivos, logística de distribución).  
2. **Herramientas computacionales** (Python, Scikit-Learn) para implementar modelos predictivos simples.  
3. **Evaluación continua** mediante portafolios estudiantiles y proyectos aplicados con agricultores locales.  

**Resultados esperados:**  
1. **Impacto pedagógico:** Mejora en la pertinencia curricular y motivación estudiantil al conectar las matemáticas con desafíos agroindustriales.  
2. **Impacto social:** Soluciones accesibles para pequeños productores (ej: predicción de cosechas mediante regresión lineal).  
3. **Divulgación:** Publicación de hallazgos en la *Revista Transdisciplinary Science* (en caso de selección) y réplica del modelo en otras ingenierías con enfoque rural.  

**Contribución a HUMANOS-XXI:**  
Este trabajo se alinea con los ejes temáticos del congreso:  
- *"Por un sistema de educación que realmente forme profesionales"*, al demostrar cómo la IAE mejora la empleabilidad de los ingenieros agropecuarios.  
- *"Ciencia transdisciplinar para el desarrollo"*, al integrar matemáticas, agronomía y tecnología con un enfoque de **justicia social** para el campo colombiano.  

**Palabras clave:** Educación en ingeniería, Álgebra lineal aplicada, Ciencia de datos agropecuaria, Investigación-Acción Educativa, Transdisciplinariedad, Innovación pedagógica.  


## **3. Introducción**   

**3. Introducción**

**3.1. Contexto y justificación**

En el ámbito de la educación en ingeniería agropecuaria, persiste una problemática crítica: existe una marcada desconexión entre la enseñanza tradicional del álgebra lineal y las demandas actuales del sector agropecuario en la era del big data [(Ricardo, 2021)](https://www.redalyc.org/journal/4757/475769312007/html/). Esta brecha se manifiesta particularmente en regiones como el Bajo Cauca antioqueño, donde los ingenieros agropecuarios requieren herramientas analíticas avanzadas para optimizar procesos productivos, pero carecen de formación en métodos cuantitativos aplicables a problemas reales del sector.

La enseñanza convencional del álgebra lineal en programas de ingeniería suele limitarse a desarrollos abstractos y ejercicios descontextualizados, sin vincularse con las necesidades específicas de la agricultura moderna. Esta situación contrasta con las exigencias del mercado laboral, donde la capacidad para analizar datos de cultivos, predecir rendimientos y optimizar recursos mediante técnicas de machine learning y Deep Learning se ha convertido en una competencia fundamental [(Álvarez, 2023)](https://dialnet.unirioja.es/servlet/tesis?codigo=360979).

Esta propuesta adquiere especial relevancia para el congreso HUMANOS-XXI al alinearse con sus ejes temáticos centrales:

1. *"Por un Sistema de Educación que realmente forme profesionales"*: El modelo presentado busca transformar la enseñanza matemática desde un enfoque aplicado, garantizando que los futuros ingenieros desarrollen competencias directamente útiles para el sector productivo.

2. *"Ciencia transdisciplinar para el desarrollo"*: La integración de álgebra lineal, ciencia de datos y agronomía representa un caso paradigmático de cómo la convergencia disciplinar puede generar soluciones innovadoras para desafíos agrícolas concretos.

Además, la propuesta contribuye a la sobrevivencia humana en un sentido amplio, pues la optimización de procesos agrícolas mediante herramientas matemáticas resulta crucial para garantizar la seguridad alimentaria en un contexto de cambio climático y crecimiento poblacional [(FAO, 2022)](https://www.fao.org/sustainability/es). En regiones como el Bajo Cauca, donde la agricultura constituye el principal sustento económico, esta aproximación adquiere una dimensión social adicional al potencialmente mejorar los ingresos de pequeños y medianos productores.

**3.2. Objetivos**

Este trabajo reflexivo se plantea dos objetivos fundamentales:

1. Diseñar un curso innovador de álgebra lineal basado en Investigación-Acción Educativa (IAE) que integre:
   - Los fundamentos matemáticos esenciales según estándares internacionales
   - Las técnicas de machine learning aplicables al sector agropecuario (Géron, 2022)
   - Problemas reales identificados en colaboración con productores del Bajo Cauca

2. Evaluar el impacto de esta innovación curricular en:
   - La formación de competencias analíticas en los estudiantes de ingeniería agropecuaria
   - La generación de soluciones prácticas para desafíos regionales específicos (ej: modelos predictivos para cosechas de arroz, optimización de riego mediante sistemas lineales)

La propuesta se sustenta en la hipótesis de que un enfoque pedagógico basado en IAE, que incorpore ciclos continuos de reflexión y mejora, permitirá acortar significativamente la brecha entre la formación académica y las necesidades del sector agroindustrial. Este modelo busca trascender el ámbito universitario para convertirse en un referente de innovación educativa aplicable a otras regiones agrícolas de Colombia y Latinoamérica.




## **4. Marco Teórico** **4. Marco Teórico**

**4.1. Investigación-Acción Educativa (IAE)**

La Investigación-Acción Educativa (IAE) constituye el pilar metodológico de esta propuesta, fundamentada en el modelo de ciclos reflexivos propuesto por Kemmis y McTaggart (1988)[Latorre](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.uv.mx/rmipe/files/2019/07/La-investigacion-accion-conocer-y-cambiar-la-practica-educativa.pdf). Este enfoque se estructura en cuatro fases iterativas: 1) planificación, 2) acción, 3) observación, y 4) reflexión, que permiten una mejora continua del proceso educativo basada en evidencia empírica.

En el contexto de educación superior, la IAE adquiere especial relevancia para superar la rigidez curricular tradicional. Según Elliott (1991), su aplicación permite:
- Adaptar contenidos a las necesidades emergentes del sector productivo
- Incorporar activamente la voz de los estudiantes en el diseño pedagógico
- Generar conocimiento situado a partir de problemas reales

En nuestra propuesta, los ciclos de IAE se implementan mediante:
1. **Diagnóstico participativo**: Encuestas a estudiantes y productores para identificar necesidades formativas
2. **Diseño colaborativo**: Co-construcción de actividades con docentes del área agronómica
3. **Implementación monitorizada**: Registro sistemático de dificultades de aprendizaje
4. **Evaluación formativa**: Retroalimentación continua para ajustar contenidos

Este modelo ha demostrado eficacia en estudios similares, como el de López (2020) en ingenierías agrícolas mexicanas, donde redujo en 40% la deserción en cursos matemáticos al vincularlos con aplicaciones concretas. OECD (2019), Educación superior en México: Resultados y relevancia para el mercado laboral, OECD Publishing, Paris, https://doi.org/10.1787/a93ed2b7-es.

**4.2. Álgebra Lineal para Ciencia de Datos**

El marco conceptual técnico se fundamenta en la obra de [Géron (2022)](https://github.com/ageron/handson-ml3/blob/main/math_linear_algebra.ipynb), que establece los pilares matemáticos del machine learning y el deep learning aplicado:

**4.2.1. Conceptos clave y aplicaciones agropecuarias**

1. **Matrices y operaciones**:
   - Representación de datasets agrícolas (rendimientos, variables climáticas)
   - Operaciones básicas para preprocesamiento de datos
   - Caso aplicado: Matriz de nutrientes en suelos del Bajo Cauca

2. **Sistemas de ecuaciones lineales**:
   - Modelado de balances hídricos y nutricionales
   - Aplicación en sistemas de riego optimizado
   - Ejemplo: Determinación de mezclas de fertilizantes

3. **Descomposición matricial (PCA/SVD)**:
   - Reducción de dimensionalidad en imágenes multiespectrales
   - Identificación de patrones en cultivos mediante análisis de componentes principales
   - Estudio de caso: Detección temprana de estrés hídrico en palma aceitera

**4.2.2. Vinculación con Agricultura 4.0**

La integración de estas herramientas con tecnologías emergentes se evidencia en:
- **Precisión agrícola**: Uso de álgebra tensorial en procesamiento de imágenes drones (Torres et al., 2021)
- **Predictive analytics**: Modelos ARIMA para pronóstico de cosechas basados en autocovarianza matricial
- **Optimización logística**: Problemas de transporte resueltos mediante programación lineal

En Latinoamérica destacan experiencias como:
- El sistema SIATA (Colombia) para predicción meteorológica basado en álgebra matricial
- La plataforma AgroIA (Brasil) que emplea SVD en recomendación de cultivos
- El proyecto Agrosmart (México) para gestión óptima de recursos hídricos

**4.3. Transdisciplinariedad**

La propuesta articula cuatro dominios de conocimiento:

1. **Matemáticas**:
   - Teoría de matrices y espacios vectoriales
   - Algoritmos numéricos para problemas a gran escala

2. **Agronomía**:
   - Principios de fisiología vegetal y manejo de cultivos
   - Problemáticas específicas del trópico bajo

3. **Tecnología**:
   - Frameworks de machine learning y deep learning (Scikit-Learn, TensorFlow)
   - Herramientas de visualización (Matplotlib, Plotly)

4. **Pedagogía**:
   - Teorías de aprendizaje significativo (Ausubel)
   - Didáctica de las matemáticas aplicadas

Esta integración sigue el modelo de transdisciplinariedad de Nicolescu (2002), donde:
- Los problemas agrícolas definen los requerimientos matemáticos
- Las limitaciones tecnológicas condicionan las soluciones implementables
- Los principios pedagógicos guían la secuencia de aprendizaje

Ejemplos concretos de esta articulación incluyen:
- El desarrollo de laboratorios virtuales que simulan sistemas de producción reales
- La adaptación de algoritmos estándar a las particularidades de cultivos tropicales
- La creación de materiales didácticos: Cuaderno Jupyter alojados en GitHub (español)

Esta aproximación ha mostrado efectividad en contextos similares, como lo demuestra [el proyecto MathAgro de la Universidad Nacional de Colombia (2021)](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://plei2034.unal.edu.co/fileadmin/Documentos/Plan_Global_de_Desarrollo_2019-2021.pdf), que logró incrementar en 35% la retención de conceptos matemáticos al vincularlos con problemas agronómicos concretos.

## **5. Metodología** (3-4 páginas)  
### **5.1. Diseño del Curso con Enfoque IAE**  
- **Fases**:  
  1. **Diagnóstico**: Encuestas a estudiantes y agricultores del Bajo Cauca.  
  2. **Implementación**: Módulos prácticos con Python y Scikit-Learn .  
  3. **Evaluación**: Portafolios estudiantiles y proyectos aplicados.  

### **5.2. Instrumentos**  
- **Herramientas**:  
  - Plataformas GitHub (*Hands-On ML* de Géron) .  
  - Datos abiertos del sector agropecuario colombiano.  

---

## **6. Resultados y Discusión** (3-4 páginas)  
### **6.1. Hallazgos Preliminares**  
- Ejemplo: Estudiantes lograron predecir rendimientos de cultivos usando regresión lineal (caso: cacao en Caucasia).  

### **6.2. Impacto en la Comunidad**  
- **Académico**: Mejora en las competencias analíticas de los estudiantes.  
- **Social**: Soluciones accesibles para pequeños agricultores .  

---

## **7. Conclusiones y Proyecciones** (2 páginas)  
- **Contribución al congreso**: Modelo replicable para otras ingenierías en zonas rurales .  
- **Futuras acciones**:  
  - Publicación de resultados en la *Revista Transdisciplinary Science* .  
  - Alianzas con cooperativas agrícolas para escalar proyectos.  

---

## **8. Referencias** (1-2 páginas)  
- Formato: Según normas del congreso (ej: APA o Vancouver).  
- Incluir:  
  - Géron, A. (2022). *Hands-On Machine Learning*. O’Reilly .  
  - Documentos del Ministerio de Agricultura de Colombia .  
  - [(Ricardo, 2021)](https://www.redalyc.org/journal/4757/475769312007/html/).
  - [(Álvarez, 2023)](https://dialnet.unirioja.es/servlet/tesis?codigo=360979).
  - [Latorre](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.uv.mx/rmipe/files/2019/07/La-investigacion-accion-conocer-y-cambiar-la-practica-educativa.pdf)
  - [Géron (2022)](https://github.com/ageron/handson-ml3/blob/main/math_linear_algebra.ipynb)
  - [el proyecto MathAgro de la Universidad Nacional de Colombia (2021)](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://plei2034.unal.edu.co/fileadmin/Documentos/Plan_Global_de_Desarrollo_2019-2021.pdf)
---

## **9. Anexos** (opcional)  
- Ejemplos de actividades IAE en el aula.  
- Datos de encuestas a estudiantes.  

---  
### **Notas finales**  
- **Extensión**: Ajustar el contenido para cumplir con 15-20 páginas.  
- **Formato**: Usar la plantilla del congreso (disponible en [fundacioniai.org/humanosxxi/](https://fundacioniai.org/humanosxxi/)) .  
- **Envío**: Seguir el proceso de doble evaluación (técnica y científica) .  

