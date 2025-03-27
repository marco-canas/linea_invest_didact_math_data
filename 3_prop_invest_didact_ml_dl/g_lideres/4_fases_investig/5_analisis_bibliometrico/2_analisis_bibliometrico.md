# Secuencia de actividades para ell análisis bibliométrico  


Esta es una **estructura detallada** para realizar un análisis bibliométrico riguroso sobre tu tema, siguiendo estándares metodológicos y herramientas especializadas como VOSviewer, Bibliometrix o Scopus Analyzer:

---

## **1. Definición del objetivo y alcance**  
- **Pregunta de investigación**:  
  *¿Cómo se relaciona el desarrollo de habilidades digitales en la educación superior con la empleabilidad de los egresados?*  
- **Delimitación**:  
  - Período temporal: Últimos 10 años (2014–2024).  
  - Bases de datos: Scopus, Web of Science, ERIC, SciELO.  
  - Idiomas: Español e inglés.  
  - Criterios de exclusión: Estudios sin revisión por pares, artículos no relacionados con empleabilidad.  

---

## **2. Búsqueda y recolección de datos**  
### **Estrategia de búsqueda**  
- **Palabras clave** (usando operadores booleanos):  
  ```python
  ("digital skills" OR "digital literacy" OR "ICT competencies")  
  AND  
  ("higher education" OR "universities" OR "tertiary education")  
  AND  
  ("employability" OR "job market" OR "labor insertion")  
  ```
- **Ejemplo en Scopus**:  
  ```sql
  TITLE-ABS-KEY ( ("digital skills" OR "digital competence") AND ("higher education") AND ("employability") ) AND PUBYEAR > 2013  
  ```

### **Herramientas para exportar datos**:  
  - Exportar resultados en formato `.csv` o `.bib` desde las bases de datos.  
  - Usar gestores bibliográficos: Zotero, Mendeley.  

---

## **3. Análisis bibliométrico**  
### **Herramientas recomendadas**:  
  - **Bibliometrix** (paquete de R): Para análisis de redes y tendencias.  
  - **VOSviewer**: Para visualización de mapas de coocurrencia.  
  - **Excel**: Para estadísticas descriptivas.  

### **Pasos**:  
#### **a) Análisis de desempeño**  
  - **Productividad**:  
    - Autores más prolíficos (Leyes de Lotka/Bradford).  
    - Revistas clave (ej. *Computers & Education*, *Journal of Employability*).  
    - Países/instituciones líderes (mapas geográficos con Tableau).  
  - **Ejemplo de tabla**:  
    | País | Publicaciones | Citas totales |  
    |------|---------------|---------------|  
    | España | 45 | 620 |  
    | EE.UU. | 38 | 890 |  

#### **b) Análisis de ciencia de redes**  
  - **Redes de coautoría**: Identificar colaboraciones entre autores/países.  
  - **Coocurrencia de palabras clave**:  
    - Clusters temáticos (ej. "digital skills", "curriculum design", "soft skills").  
    - Tendencias temporales (ej. aumento de "IA" o "big data" post-2020).  
  - **Mapa de VOSviewer**:  
    ![Ejemplo de mapa de coocurrencia](https://tinyurl.com/2p8d7v9x) *(Enlace ilustrativo)*.  

#### **c) Análisis de impacto**  
  - Índice h de autores/revistas.  
  - Artículos más citados (ej. *"Digital Competence and Employability" de Cabrera et al., 2020*).  

---

## **4. Análisis temático cualitativo**  
- **Identificación de categorías emergentes**:  
  1. **Habilidades digitales demandadas**:  
     - Programación, análisis de datos, gestión de TIC.  
  2. **Barreras para la empleabilidad**:  
     - Brecha entre formación universitaria y necesidades empresariales.  
  3. **Estrategias pedagógicas**:  
     - Aprendizaje basado en proyectos, simulaciones virtuales.  

- **Ejemplo de codificación en NVivo**:  
  ```python
  # Código: Habilidades técnicas  
  Citas relacionadas: "Los egresados con competencias en Python tienen un 30% más de probabilidades de empleo" (Smith, 2021).  
  ```

---

## **5. Visualización y reporte**  
### **Resultados clave**:  
  - **Gráfico de tendencias temporales**: Aumento del 150% en publicaciones sobre el tema desde 2018.  
  - **Tabla de brechas**:  
    | Habilidad | Demanda empresarial | Oferta universitaria |  
    |-----------|----------------------|-----------------------|  
    | Big Data  | 85%                  | 45%                   |  

### **Discusión**:  
  - Relacionar hallazgos con marcos teóricos (ej. modelo **DigComp** de la UE).  
  - Contrastar con estudios de casos como el informe **OECD Skills Outlook 2023**.  

---

## **6. Recomendaciones finales**  
1. **Para instituciones educativas**:  
   - Integrar certificaciones digitales (ej. Google Analytics, Azure Fundamentals).  
2. **Para políticas públicas**:  
   - Alinear estándares educativos con el marco **ESCO** (habilidades digitales para la UE).  

---

## **Recursos útiles**  
- **Tutorial Bibliometrix**: [Enlace](https://www.bibliometrix.org/vignettes/Introduction_to_bibliometrix.html)  
- **Plantilla de informe**: [Descargar](https://templates.office.com) (Buscar "literature review template").  

