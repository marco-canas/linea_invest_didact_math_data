# **Capítulo 9: Técnicas de Aprendizaje No Supervisado**  

*Aurélien Géron*  

Aunque la mayoría de las aplicaciones actuales del *Machine Learning* se basan en **aprendizaje supervisado** (y, por tanto, es donde se concentra la mayor inversión), la gran parte de los datos disponibles no están etiquetados: tenemos las características de entrada **X**, pero no las etiquetas **y**.  

El científico de la computación **Yann LeCun** dijo una vez:  

> *"Si la inteligencia fuera un pastel, el aprendizaje no supervisado sería el pastel, el aprendizaje supervisado sería el glaseado y el aprendizaje por refuerzo, la cereza."*  

En otras palabras, el **aprendizaje no supervisado** tiene un potencial enorme que apenas hemos comenzado a explorar.  



## **Ejemplo Práctico: Detección de Defectos en una Línea de Producción**  
Imagina que quieres crear un sistema que:  
1. Tome fotos de cada artículo en una línea de producción.  
2. Detecte cuáles están defectuosos.  

Puedes automatizar la captura de imágenes fácilmente, obteniendo **miles de fotos diarias**. En unas semanas, tendrías un gran conjunto de datos.  

**Problema:** No hay etiquetas.  

Si quisieras entrenar un **clasificador binario** (para predecir "defectuoso" vs. "normal"), necesitarías que expertos etiqueten manualmente todas las imágenes. Esto es:  
- **Lento.**  
- **Costoso.**  
- **Tedioso.**  

Como resultado, solo se etiqueta un **pequeño subconjunto**, el modelo tendrá un rendimiento limitado y, si el producto cambia, ¡habrá que repetir el proceso!  

**¿No sería ideal si el algoritmo pudiera aprender de los datos *sin etiquetas*?**  
Ahí entra el **aprendizaje no supervisado**.  


## **Lo que ya vimos (Capítulo 8)**  
En el capítulo anterior, cubrimos la tarea más común de aprendizaje no supervisado:  
- **Reducción de dimensionalidad** (como PCA).  

---

## **Temas de este Capítulo**  
En este capítulo exploraremos más tareas y algoritmos no supervisados:  

### **1. Agrupamiento (Clustering)**  
- **Objetivo:** Agrupar instancias similares en *clusters*.  
- **Aplicaciones:**  
  - Segmentación de clientes.  
  - Sistemas de recomendación.  
  - Búsqueda de imágenes.  
  - Reducción de dimensionalidad.  
- **Algoritmos clave:** *K-Means*, *DBSCAN*.  

### **2. Detección de Anomalías**  
- **Objetivo:** Aprender cómo son los datos "normales" para detectar casos anómalos (ej: productos defectuosos o tendencias inusuales en series de tiempo).  

### **3. Estimación de Densidad**  
- **Objetivo:** Calcular la **función de densidad de probabilidad (PDF)** del proceso que generó los datos.  
- **Usos:**  
  - Detección de anomalías (datos en regiones de baja densidad = posibles anomalías).  
  - Visualización y análisis exploratorio.  
- **Algoritmo clave:** *Modelos de Mezclas Gaussianas (GMM)*.  

---

## **¿Listo para el pastel?**  
Empezaremos con **clustering** (K-Means y DBSCAN), luego veremos **mezclas gaussianas** y cómo se usan para:  
✔ Estimación de densidad.  
✔ Clustering.  
✔ Detección de anomalías.  

---  
*Traducción adaptada del libro "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" de Aurélien Géron.*  

¿Necesitas ajustes en el tono o profundizar en algún concepto?