# Aprendizaje Inverso 

El **aprendizaje inverso con Jupyter** que propone Lorena Barba (en su libro *[Jupyter for Education](https://jupyter4edu.github.io/jupyter-edu-book/)*) es una adaptación del modelo de **Flipped Classroom (Aula Invertida)** que aprovecha las capacidades interactivas y de reproducibilidad de los **Jupyter Notebooks** para transformar la enseñanza de disciplinas técnicas, especialmente en matemáticas, ciencias e ingenierías. A continuación, te explico sus principios clave y cómo puedes integrarlo en tu docencia investigativa bajo el enfoque de **Investigación Acción Educativa (IAE)**:

---

### **1. Concepto central: "Invertir" con Jupyter Notebooks**  
Barba propone que los estudiantes interactúen **antes de la clase** con notebooks que combinen:  
- **Explicaciones teóricas** (en celdas Markdown).  
- **Código ejecutable** (Python, R, etc.) para experimentar con conceptos.  
- **Visualizaciones dinámicas** (gráficos, animaciones).  
- **Ejercicios autoevaluables** (usando widgets o herramientas como `nbgrader`).  

**Ejemplo en tu contexto:**  
- Subes a GitHub un notebook sobre *optimización de funciones* con:  
  - Teoría + representaciones TRRS (fórmulas, gráficos, tablas).  
  - Código Python para modificar parámetros y observar cambios.  
  - Un problema aplicado a datos reales del Bajo Cauca (ej. maximizar producción agrícola).  

---

### **2. Beneficios para la docencia investigativa (IAE)**  
- **Autonomía:** Los estudiantes exploran a su ritmo, liberando tiempo en clase para discusión profunda (ABPP).  
- **Reproducibilidad:** Los notebooks documentan el proceso de aprendizaje, facilitando tu investigación sobre su eficacia.  
- **Interdisciplinariedad:** Ideal para STEAMS, al integrar código (ciencia), arte (visualizaciones) y contexto social (datos locales).  

**Caso de éxito de Barba:**  
En su curso *"Practical Numerical Methods with Python"*, los estudiantes resolvían problemas de ingeniería con notebooks antes de clases, luego discutían errores y soluciones. Resultó en mayor engagement y comprensión conceptual.

---

### **3. Cómo implementarlo en tu práctica**  
#### **a) Diseño de materiales**  
- Usa **JupyterLab** o **Google Colab** para crear notebooks accesibles.  
- Incluye **representaciones múltiples** (TRRS):  
  - **Gráficos interactivos** (Plotly, Matplotlib).  
  - **Ejemplos generados por IA** (ChatGPT para crear problemas contextualizados).  
- **Vincula tus videos de @DiMathData** explicando los conceptos clave.  

#### **b) Metodología IAE + Aprendizaje Inverso**  
1. **Diagnóstico:** Identifica cuellos de botella (ej. estudiantes no comprenden derivadas).  
2. **Planificación:** Diseña un notebook con:  
   - Video introductorio (AI).  
   - Ejemplo de ABPP (calcular costos óptimos para una finca cafetera).  
3. **Acción:** Implementa y recoge datos (tiempos de ejecución, errores comunes).  
4. **Reflexión:** Usa los notebooks de los estudiantes como evidencia para ajustar el enfoque.  

#### **c) Herramientas recomendadas**  
- **nbgrader:** Para evaluar automáticamente tareas en Jupyter.  
- **Voilà:** Convierte notebooks en dashboards interactivos para estudiantes menos técnicos (ej. Lic. Educación Infantil).  
- **Binder:** Permite ejecutar tus notebooks en línea sin instalar nada.  

---

### **4. Ejemplo concreto para tu congreso**  
**Título del notebook:** *"Modelando la deforestación en el Bajo Cauca con Python"*  
- **Pre-clase:** Los estudiantes exploran un notebook con:  
  - Datos reales (ej. imágenes satelitales).  
  - Código para calcular tasas de cambio (matemáticas + ciencia de datos).  
  - Preguntas reflexivas (STEAMS: impacto social y ambiental).  
- **En clase:** Discuten cómo mejorar el modelo (ABPP) y generan representaciones alternativas (TRRS).  

---

### **5. Recursos adicionales**  
- **Libro de Barba:** [Jupyter for Education](https://jupyter4edu.github.io/jupyter-edu-book/) (capítulos 3 y 5).  
- **Repositorio inspirador:** [Lorena Barba's GitHub](https://github.com/barbagroup) con ejemplos de notebooks educativos.  

--- 

### **Conclusión**  
El aprendizaje inverso con Jupyter alinea perfectamente con tu enfoque de **IAE** y los modelos pedagógicos que usas (AI, ABPP, STEAMS, TRRS). Además, te permite:  
- **Investigar** el impacto de herramientas digitales en el aprendizaje.  
- **Demostrar** en el CUICIID 2025 cómo la docencia universitaria puede ser **reproducible, interactiva y centrada en problemas reales**.  

¿Te gustaría ayuda para diseñar un notebook específico para alguna de tus clases?