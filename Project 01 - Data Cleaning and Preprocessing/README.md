# Proyecto 01 - Limpieza y Preprocesamiento de Datos

## 📋 Descripción del Proyecto

Este proyecto forma parte del portafolio de análisis de datos y se enfoca en las etapas iniciales del flujo de trabajo de ciencia de datos: **exploración y preprocesamiento de información**.

El objetivo principal es demostrar competencias en:

- ✅ Carga de datos de archivos
  
- ✅ Análisis exploratorio de datos (EDA)
  
- ✅ Identificación y tratamiento de valores faltantes
  
- ✅ Detección y manejo de outliers
  
- ✅ Normalización y transformación de datos
  
- ✅ Validación de calidad de datos

---

## 📁 Estructura del Proyecto

```
Project 01 - Data Cleaning and Preprocessing/
├── README.md                    # Este archivo
├── EUR-USD.csv                  # Dataset de tasas de cambio EUR-USD
└── loan-data.csv                # Dataset de datos de préstamos
```

---

## 📊 Datasets

### 1. **EUR-USD.csv**

- Conjunto de datos que recopila las tasas de cambio mensuales entre el euro (EUR) y el dólar estadounidense (USD) correspondientes al año 2015.

- Su propósito es homogeneizar la información financiera del conjunto de datos principal, convirtiendo los importes de los préstamos y los pagos registrados en euros a dólares estadounidenses mediante la tasa de cambio correspondiente a cada mes.
  
- Desde un punto de vista técnico, la incorporación de este conjunto de datos permite aplicar técnicas de **integración de datos (Data Integration)**, combinando información procedente de distintas fuentes para enriquecer el conjunto de datos principal y garantizar la consistencia de las variables monetarias.
  
  * *Estructura del conjunto de datos:*
    
    El conjunto de datos está conformado por registros mensuales correspondientes al año 2015, organizados cronológicamente desde enero hasta diciembre. Cada
    fila representa un mes calendario y las columnas almacenan diferentes indicadores asociados al comportamiento de la tasa de cambio EUR/USD durante dicho
    período.

    Las variables contenidas en el conjunto de datos son:

    - **Open**: Valor de apertura de la tasa de cambio para el período mensual correspondiente. 
    - **High**: Valor máximo alcanzado por la tasa de cambio durante el mes.
    - **Low**: Valor mínimo registrado por la tasa de cambio durante el mes.
    - **Close**: Valor de cierre de la tasa de cambio para el período mensual correspondiente.
    - **Volume**: Volumen de operaciones registrado durante el período. Esta variable no es utilizada en el desarrollo del presente proyecto.
    

### 2. **loan-data.csv**

- Conjunto de datos que contiene información sobre préstamos personales otorgados por instituciones financieras de los Estados Unidos.
  
- Incluye variables relacionadas con las características del préstamo, el perfil del prestatario, el estado del crédito y el historial de pagos.
  
- Este conjunto de datos constituye la fuente principal de información del proyecto y sirve como base para la aplicación de diferentes técnicas de limpieza y preprocesamiento de datos.
  
- Durante el desarrollo del proyecto se emplean diversas estrategias para el tratamiento de valores faltantes, la transformación de variables, la integración de información externa y la preparación del conjunto de datos para etapas posteriores de análisis.

   * *Estructura del conjunto de datos*

   El conjunto de datos está compuesto por variables numéricas y categóricas que describen diferentes aspectos asociados a cada préstamo. Para el desarrollo de
   este proyecto se utilizan las siguientes variables:

   - **id**: Identificador único asignado a cada préstamo.
   - **issue_d**: Mes en el que el préstamo fue aprobado. 
   - **loan_amnt**: Monto solicitado por el prestatario.
   - **loan_status**: Estado actual del préstamo.
   - **funded_amnt**: Monto total aprobado y comprometido para el préstamo.
   - **term**: Plazo del préstamo, expresado en meses (36 o 60 meses).
   - **int_rate**: Tasa de interés anual aplicada al préstamo. 
   - **installment**: Pago mensual establecido para el prestatario.
   - **grade**: Clasificación general del nivel de riesgo del préstamo. 
   - **sub_grade**: Subclasificación del nivel de riesgo del préstamo.
   - **verification_status**: Estado de verificación de los ingresos declarados por el prestatario. 
   - **url**: Dirección web asociada al registro original del préstamo. 
   - **addr_state**: Estado de residencia declarado por el prestatario durante la solicitud del préstamo.   
   - **total_pymnt**: Monto total recibido por la institución financiera hasta la fecha del registro.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Operaciones numéricas
- **Matplotlib / Seaborn** - Visualización de datos
- **Jupyter Notebook** - Desarrollo interactivo

---

📌 Metodología del proyecto

El proceso de limpieza y preprocesamiento de los datos se desarrolla siguiendo las siguientes etapas:

   1. *Carga e inspección de los datos*📂
      - Importación de los conjuntos de datos desde archivos CSV.
      - Verificación de la estructura, dimensiones y tipos de datos.
      - Identificación de las variables de interés para el desarrollo del proyecto.
        
   2. *Análisis exploratorio de los datos (EDA)*🔍
      - Obtención de estadísticas descriptivas.
      - Evaluación de la distribución de las variables.
      - Identificación de valores faltantes e inconsistencias.
      - Análisis preliminar de las variables empleadas en el proyecto.
        
   3. *Integración de datos*🔗
      - Incorporación del conjunto de datos de tasas de cambio EUR/USD.
      - Conversión de los importes financieros expresados en euros a dólares estadounidenses.
      - Homogeneización de las variables monetarias del conjunto de datos principal.
        
   4. *Limpieza y preprocesamiento*🛠️
      - Tratamiento e imputación de valores faltantes.
      - Corrección de inconsistencias en variables categóricas.
      - Transformación y recodificación de variables.
      - Adecuación de los tipos de datos cuando es necesario.
      - Generación de nuevas variables auxiliares para facilitar el análisis.
        
   5. *Validación de los resultados*✔️
      - Verificación de la consistencia del conjunto de datos procesado.
      - Comprobación de la integridad de las variables transformadas.
      - Obtención del conjunto de datos final preparado para su utilización en etapas posteriores de análisis y modelado.

---

📈 Resultados del proyecto

Al finalizar el proceso de limpieza y preprocesamiento se obtiene:

📄 Un conjunto de datos con mayor nivel de integridad, consistencia y calidad, preparado para su utilización en etapas posteriores de análisis y modelado.
🧹 Un tratamiento sistemático de valores faltantes, inconsistencias y variables que requerían transformación.
🔗 Un conjunto de datos enriquecido mediante la integración de información externa correspondiente a las tasas de cambio EUR/USD.
📊 Visualizaciones comparativas que evidencian el impacto de las técnicas de limpieza y preprocesamiento aplicadas.
📚 Una documentación detallada que describe cada una de las etapas desarrolladas, favoreciendo la reproducibilidad y comprensión del proyecto.
💡 Un análisis de la calidad inicial del conjunto de datos y de las mejoras obtenidas tras el proceso de preparación de los datos.

---

## 🚀 Cómo Ejecutar

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Ernesto9734/Data-Analyst-Projects.git
   cd Data-Analyst-Projects
   ```

2. **Instalar dependencias:**
   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

3. **Ejecutar el notebook:**
   ```bash
   jupyter notebook "Project 01 - Data Cleaning and Preprocessing/"
   ```

---

## 📚 Referencias y Recursos

- [Documentación de Pandas](https://pandas.pydata.org/docs/)
- [Guía de Limpieza de Datos](https://towardsdatascience.com/the-ultimate-guide-to-data-cleaning-3969843991d4)
- [Best Practices en Preprocesamiento](https://scikit-learn.org/stable/modules/preprocessing.html)

---

## 📝 Notas Personales

Este proyecto es fundamental para desarrollar habilidades sólidas en manipulación de datos, ya que la **calidad de los datos preprocesados** determina la confiabilidad de cualquier análisis subsecuente.

---

## 👤 Autor

**Ernesto9734**  
Portafolio de Análisis de Datos

---

## 📄 Licencia

Este proyecto es parte de un portafolio educativo.

---

**Última actualización:** Junio 2026
