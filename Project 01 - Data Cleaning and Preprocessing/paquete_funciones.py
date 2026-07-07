############################################################################################################################################
#######                                                LIBRERIAS                                                                     #######
############################################################################################################################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

############################################################################################################################################
#######                                       FUNCIONES DE IMPORTACIÓN DE DATOS                                                      #######
############################################################################################################################################

def importar_base_datos(
    nombre_archivo_datos: str, 
    indice_etiquetas: int, 
    indice_datos: int, 
    separador: str = ','
    ) -> tuple[np.ndarray, np.ndarray]:

    """
    Importa un archivo de texto plano, transpone la matriz para facilitar su 
    procesamiento y separa las etiquetas de los datos numéricos o categóricos.

    Args:
        nombre_archivo_datos (str): Ruta o nombre del archivo a importar (ej. 'data.csv').
        indice_etiquetas (int): Índice de la fila/columna donde se encuentran los nombres de las variables.
        indice_datos (int): Índice a partir del cual comienzan las filas/columnas de datos puros.
        separador (str, optional): Carácter que delimita los valores en el archivo. Por defecto es ','.

    Returns:
        tuple[np.ndarray, np.ndarray]: Una tupla que contiene:
            - etiquetas (np.ndarray): Arreglo unidimensional con los nombres de las columnas.
            - datos (np.ndarray): Arreglo bidimensional con el contenido de la base de datos.
    """
    
    # Carga de datos en formato 'str' para evitar errores de tipo antes de la clasificación y casteo
    datos_crudos_np = np.loadtxt(nombre_archivo_datos, delimiter=separador, dtype='str')
    
    # Conversión de columnas a filas para optimizar el procesamiento y la clasificación de los datos
    datos_crudos_np = datos_crudos_np.transpose()
    
    # Extracción de las etiquetas de las variables
    etiquetas = datos_crudos_np[:, indice_etiquetas]
    
    # Extracción de la matriz de datos a partir del índice especificado
    datos = datos_crudos_np[:, indice_datos:]
    
    # --- Bloque de visualización en consola ---
    print('Etiquetas contenidas en la base de datos:')
    for etiqueta in etiquetas:
        print(f'{etiqueta} \t')
    print()
    
    # Muestra solo las primeras 5 columnas/filas de datos para no saturar la consola
    print(f'Muestra de los datos extraídos: \n {datos[:, :5]}')
    print()
    
    return (etiquetas, datos)

############################################################################################################################################
#######                                     FUNCIONES DE VISUALIZACIÓN DE DATOS                                                      #######
############################################################################################################################################

def visualizacion_grafico_barras(
    datos: pd.DataFrame, 
    titulo: str, 
    etiquetas: list[str],
    porcentuales: bool,
    ancho: int = 7,
    alto: int = 4,
) -> None:
    
    """
    Genera y muestra un gráfico de barras estilizado bajo los estándares de la IEEE,
    permitiendo alternar dinámicamente entre formatos numéricos absolutos o porcentuales.

    Args:
        datos (pd.DataFrame): DataFrame que contiene los datos a graficar. 
                              Se asume que la columna 0 es el eje X y la columna 1 es el eje Y.
        titulo (str): Título principal del gráfico.
        etiquetas (list[str]): Lista con dos elementos tipo string para nombrar los ejes:
                               [etiqueta_eje_x, etiqueta_eje_y].
        porcentuales (bool): Si es True, añade el símbolo '%' a las etiquetas sobre las barras.
                             Si es False, renderiza los valores como números estándar con un decimal.
        ancho (int, optional): Ancho de la figura en pulgadas. Por defecto es 7.
        alto (int, optional): Alto de la figura en pulgadas. Por defecto es 4.

    Returns:
        None: La función no retorna ningún valor, solo despliega el gráfico en pantalla.
    """

    # --- CONFIGURACIÓN ESTILO IEEE ---

    # Usamos el estilo 'white' (fondo limpio sin cuadrículas por defecto)
    sns.set_theme(style="white")
    
    # Configuración de la tipografía global (Times New Roman) y estilos de los ejes
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
    plt.rcParams['axes.edgecolor'] = 'black'
    plt.rcParams['axes.linewidth'] = 1.0
    plt.rcParams['figure.dpi'] = 120
    
    # Obtención de los nombres de las columnas para indexación dinámica
    columnas = datos.columns.tolist()
    
    # Inicialización del lienzo y los ejes
    fig, ax = plt.subplots(figsize=(ancho, alto))
    
    # --- MAPEO DE COLOR NATIVO (DEGRADADO) ---
    # 1. Obtenemos el mapa de color de Matplotlib (Estilo 'Blues' para un look corporativo/formal)
    cmap = plt.colormaps.get_cmap('Blues')
    
    # 2. Normalizamos los valores numéricos del eje Y entre 0 y 1 para mapear la intensidad del color
    valores_y = datos[columnas[1]].values
    norm = mcolors.Normalize(vmin=valores_y.min(), vmax=valores_y.max())
    
    # 3. Construimos la lista de colores aplicando un rango controlado (0.3 a 0.8)
    # Esto previene que las barras con valores mínimos se mezclen de forma invisible con el fondo blanco
    colores_barras = [cmap(0.3 + 0.5 * norm(val)) for val in valores_y]

    # Creación del gráfico de barras con bordes definidos estilo publicación científica
    sns.barplot(
        x=columnas[0], 
        y=columnas[1], 
        data=datos, 
        palette=colores_barras,
        edgecolor='black',
        linewidth=0.8,
        hue=columnas[0]
    )

    # --- ETIQUETAS DE DATOS DINÁMICAS ---
    # Iteración sobre los contenedores del gráfico para inyectar los valores sobre cada barra
    for contenedor in ax.containers:
        if porcentuales:
            # Formato con un decimal acompañado del signo de porcentaje (ej: 45.2%)
            ax.bar_label(contenedor, padding=3, fmt='%.1f%%', fontsize=12, fontfamily='serif')
        else:
            # Formato numérico estándar con un decimal para valores absolutos o conteos (ej: 125.0)
            ax.bar_label(contenedor, padding=3, fmt='%.1f', fontsize=12, fontfamily='serif')
    
    # Ajuste dinámico del límite superior (añade un 10% de espacio libre para que no se corten los números)
    limite_superior_actual = ax.get_ylim()[1]
    ax.set_ylim(top=limite_superior_actual * 1.10)

    # Personalización formal de títulos y ejes
    plt.title(titulo, fontsize=14, fontweight='bold', pad=12)
    plt.xlabel(etiquetas[0], fontsize=12)
    plt.ylabel(etiquetas[1], fontsize=12)

    # Configuración de los ticks orientados hacia el interior del marco (Sello clásico de la IEEE)
    ax.tick_params(direction='in', which='both', top=True, right=True, labelsize=10)

    # Rotación y alineación de los textos en el eje X para evitar solapamientos
    plt.xticks(rotation=45, ha='right')
    
    # Optimización automática de márgenes y geometría de la imagen
    plt.tight_layout()
    
    # Despliegue del gráfico final
    plt.show()

############################################################################################################################################
#######                                    FUNCIONES DE CATEGORIZACIÓN DE DATOS                                                      #######
############################################################################################################################################

def categorizacion_casteo_datos(datos: np.ndarray) -> np.ndarray:

    """
    Intenta convertir todos los elementos de un arreglo bidimensional a valores de tipo flotante.
    Si un elemento no puede ser convertido (por ser texto o nulo), lo reemplaza por `np.nan`.

    Args:
        datos (np.ndarray): Arreglo bidimensional (matriz) con los datos originales en formato string.

    Returns:
        np.ndarray: Una nueva matriz de NumPy de tipo flotante donde los elementos no numéricos 
                    han sido transformados en valores faltantes (NaN).
    """

    datos_numericos = []

    # Iteración sobre cada fila de la matriz de datos
    for fila in datos:
        temporal = []
        
        # Iteración sobre cada elemento (columna) dentro de la fila actual
        for elemento in fila:
            try:
                # Intento de conversión a flotante (limpieza/casteo de datos numéricos)
                x = float(elemento)
            except (ValueError, TypeError):
                # Si el elemento contiene texto o formatos incompatibles, se asigna como un valor nulo (NaN)
                x = np.nan
            finally:
                # Se añade el valor resultante (número o NaN) a la fila temporal
                temporal.append(x)
        
        # Se añade la fila procesada a la lista principal
        datos_numericos.append(temporal)
    
    # Conversión de la estructura de listas de Python a una matriz oficial de NumPy
    datos_numericos = np.array(datos_numericos)

    # --- Bloque de visualización en consola ---
    # Muestra una pequeña porción del resultado (primeras 5 columnas) para verificar el casteo
    print(f'Resultado del Casteo Inicial de los Datos: \n {datos_numericos[:, :5]}')
    print()

    return datos_numericos

############################################################################################################################################

def categorizacion_proporcion_datos_nulos(
    datos: np.ndarray, 
    etiquetas: list[str]
    ) -> dict[str, pd.DataFrame]:
    
    """
    Calcula el porcentaje de valores nulos (NaN) para cada variable y genera 
    reportes en formato DataFrame de Pandas, tanto en orden original como ordenados descendentemente.

    Args:
        datos (np.ndarray): Matriz bidimensional donde cada fila representa una variable 
                            (debido a la transposición previa en el flujo de importación).
        etiquetas (list[str]): Lista con los nombres de las variables correspondientes a cada fila de datos.

    Returns:
        dict[str, pd.DataFrame]: Un diccionario con dos reportes:
            - "tabla": DataFrame con las variables y sus porcentajes en el orden original.
            - "tabla_ordenada": DataFrame ordenado de mayor a menor porcentaje de nulos.
    """

    porcentaje_datos_nulos = []

    # Iteración sobre cada variable (fila de la matriz transpuesta)
    for columna in datos:
        # pd.isna(columna).sum() cuenta los True (valores nulos) en la variable actual
        calculo_porcentaje = pd.isna(columna).sum() / len(columna) * 100
        porcentaje_datos_nulos.append(calculo_porcentaje)

    # Creación del DataFrame consolidado relacionando cada variable con su porcentaje de nulos
    categoria_pandas = pd.DataFrame({
        'Categoria': etiquetas, 
        'Porcentaje': porcentaje_datos_nulos
    })

    # Generación de una copia ordenada de mayor a menor para identificar las variables más críticas
    categoria_pandas_ordenado = categoria_pandas.sort_values(by='Porcentaje', ascending=False)

    # --- Bloque de visualización en consola ---
    print(f'Proporción de Datos Nulos por Variable: \n {categoria_pandas}')
    print()
    
    return {
        "tabla": categoria_pandas,
        "tabla_ordenada": categoria_pandas_ordenado
    }

############################################################################################################################################

def categorizacion_inicial_datos(
    datos: np.ndarray, 
    etiquetas: np.ndarray
    ) -> list[float]:
    
    """
    Orquesta el flujo inicial de análisis de calidad de datos: realiza el casteo
    numérico, calcula la proporción de valores nulos por variable y genera una
    visualización gráfica del estado de la base de datos.

    Args:
        datos (np.ndarray): Matriz bidimensional con los datos crudos (strings).
        etiquetas (np.ndarray): Arreglo unidimensional con los nombres de las variables.

    Returns:
        list[float]: Una lista con los porcentajes de datos nulos de cada variable, 
                     en el orden original de las etiquetas.
    """

    # 1. Intento de conversión de todos los datos a flotantes (marcando textos/errores como NaN)
    datos_casteados = categorizacion_casteo_datos(
        datos=datos
    )
    
    # 2. Cálculo del porcentaje de valores nulos por cada variable individual
    valores_tabulados = categorizacion_proporcion_datos_nulos(
        datos=datos_casteados, 
        etiquetas=etiquetas
    )
    
    # 3. Generación del gráfico de barras ordenado de mayor a menor porcentaje de nulos
    # Nota: Se eliminó el argumento 'columnas' para coincidir con la definición de la función original
    visualizacion_grafico_barras(
        datos=valores_tabulados['tabla_ordenada'],
        titulo='Categorización - Porcentaje de Datos Nulos por Variable',
        etiquetas=['Variable', 'Porcentaje (%)'],
        porcentuales = True,
    )

    # 4. Extracción y retorno de los porcentajes de nulos en formato de lista nativa de Python
    return list(valores_tabulados['tabla']['Porcentaje'])

############################################################################################################################################
#######                                    FUNCIONES DE FORMATO INICIAL DE DATOS                                                     #######
############################################################################################################################################

def extraccion_columnas(indices: list[int], etiquetas: list[str]) -> list[str]:

    """
    Extrae los nombres de las columnas correspondientes a una lista de índices específicos.

    Args:
        indices (list[int]): Lista de posiciones indexadas que se desean extraer.
        etiquetas (list[str]): Lista global con los nombres de todas las variables.

    Returns:
        list[str]: Lista con los nombres de las columnas seleccionadas.
    """

    # Comprensión de listas: itera y extrae directamente en una sola operación
    return [etiquetas[i] for i in indices]

############################################################################################################################################

def renombrar_variables(etiquetas: list[str], diccionario_etiquetas: dict[str, str]) -> list[str]:

    """
    Renombra una lista de variables basándose en un diccionario de mapeo.
     Las variables que no estén presentes en el diccionario conservarán su nombre original.

    Args:
        etiquetas (list[str]): Lista original con los nombres de las variables.
        diccionario_etiquetas (dict[str, str]): Diccionario donde las llaves son los nombres 
                                                actuales y los valores son los nuevos nombres.

    Returns:
        list[str]: Nueva lista con las variables renombradas en el mismo orden original.
    """

    return [diccionario_etiquetas.get(etiqueta, etiqueta) for etiqueta in etiquetas]

############################################################################################################################################

def clasificacion_variables(
    porcentajes: list[float], 
    etiquetas: list[str], 
    excepciones: list[str] | None = None,
) -> dict[str, list[str]]:
    
    """
    Clasifica automáticamente las variables en numéricas y no numéricas basándose en
    el porcentaje de fallas de casteo, aislando excepciones.

    Args:
        porcentajes (list[float]): Lista con los porcentajes de conversiones fallidas por variable.
        etiquetas (list[str]): Lista con los nombres originales de las variables.
        excepciones (list[str] | None, optional): Lista de variables que deben ser excluidas de la 
                                                  clasificación numérica (ej: identificadores tipo 'id').

    Returns:
        dict[str, list[str]]: Diccionario con dos llaves: 'numericas' y 'no_numericas', 
                              cada una con la lista de sus respectivas variables.
    """

    if excepciones is None:
        excepciones = []

    indice_numericos, indice_no_numericos = [], []

    # 1. Clasificación basada en el umbral del 100% de fallas y la lista de exclusión
    for i in range(len(porcentajes)):
        if (etiquetas[i] not in excepciones) and (porcentajes[i] != 100):
            indice_numericos.append(i)
        else:
            indice_no_numericos.append(i)

    # 2. Extracción de los nombres utilizando tu función auxiliar
    variables_numericas = extraccion_columnas(indices=indice_numericos, etiquetas=etiquetas)
    variables_no_numericas = extraccion_columnas(indices=indice_no_numericos, etiquetas=etiquetas)

    return {
        'numericas': variables_numericas,
        'no_numericas': variables_no_numericas
    }

############################################################################################################################################

def conformar_base_datos(
    datos: np.ndarray, 
    porcentajes: list[float], 
    etiquetas: list[str], 
    excepciones: list[str] | None = None, 
    diccionario_renombrado: dict[str, str] | None = None
) -> dict[str, pd.DataFrame | dict[str, list[str]]]:
    
    """
    Construye el DataFrame de Pandas a partir de la matriz transpuesta de datos crudos,
    clasifica las variables, aplica un renombrado opcional, y homogeniza el tratamiento
    de datos faltantes (NaN) tanto para columnas numéricas como categóricas.

    Args:
        datos (np.ndarray): Matriz bidimensional de datos originales (NumPy).
        porcentajes (list[float]): Porcentajes de fallas de casteo por variable.
        etiquetas (list[str]): Nombres originales de las variables.
        excepciones (list[str] | None, optional): Variables a excluir de la clasificación numérica.
        diccionario_renombrado (dict[str, str] | None, optional): Diccionario de mapeo para cambiar 
                                                                  los nombres de las variables.

    Returns:
        dict[str, pd.DataFrame | dict[str, list[str]]]: Un diccionario con la siguiente estructura:
            - 'datos': El pd.DataFrame final procesado con sus tipos correspondientes.
            - 'variables': Un dict interno con las listas de columnas ['numericas'] y ['no_numericas'].
    """
    
    def imprimir_lista(titulo: str, elementos: list[str]) -> None:
        """Función helper interna para imprimir reportes limpios en consola."""
        print(titulo)
        for elemento in elementos:
            print(f"- {elemento}")
        print()

    # 1. Clasificación pura de variables (sin renombrar aún para no perder el rastro de las etiquetas originales)
    variables = clasificacion_variables(
        porcentajes=porcentajes, 
        etiquetas=etiquetas, 
        excepciones=excepciones
    )

    # 2. Gestión centralizada del renombrado
    if diccionario_renombrado is not None:
        variables_numericas = renombrar_variables(
            etiquetas=variables['numericas'],
            diccionario_etiquetas=diccionario_renombrado
        )
        variables_no_numericas = renombrar_variables(
            etiquetas=variables['no_numericas'],
            diccionario_etiquetas=diccionario_renombrado
        )
        etiquetas_finales = renombrar_variables(
            etiquetas=etiquetas,
            diccionario_etiquetas=diccionario_renombrado
        )
    else:
        variables_numericas = variables['numericas']
        variables_no_numericas = variables['no_numericas']
        etiquetas_finales = etiquetas

    # 3. Reporte en consola para el Jupyter Notebook
    imprimir_lista(
        titulo="Variables clasificadas como numéricas:",
        elementos=variables_numericas
    )
    imprimir_lista(
        titulo="Variables clasificadas como no numéricas:",
        elementos=variables_no_numericas
    )
    
    # 4. Construcción del DataFrame usando la matriz transpuesta y las etiquetas (renombradas o no)
    datos_pandas = pd.DataFrame(datos.transpose(), columns=etiquetas_finales)

    # 5. Conversión de tipos y homologación de valores nulos
    # Forzamos las numéricas a flotantes/enteros reales de Pandas (los errores se vuelven NaN)
    datos_pandas[variables_numericas] = datos_pandas[variables_numericas].apply(pd.to_numeric, errors='coerce')
    
    # Estandarizamos las cadenas vacías de las categóricas para que usen el mismo NaN de NumPy/Pandas
    datos_pandas[variables_no_numericas] = datos_pandas[variables_no_numericas].replace('', np.nan)

    return {
        'datos': datos_pandas,
        'variables': {
            'numericas': variables_numericas,
            'no_numericas': variables_no_numericas
        }
    }

############################################################################################################################################
#######                                FUNCIONES DE EXPLORACION INICIAL DE DATOS                                                     #######
############################################################################################################################################

def exploracion_inicial_datos_categoricos(datos: pd.DataFrame, columnas: list[str]) -> None:
    """
    Realiza un perfilamiento estadístico inicial de las variables categóricas, 
    calculando su cardinalidad exacta y omitiendo los valores nulos de forma local.

    Args:
        datos (pd.DataFrame): El DataFrame que contiene los datos a analizar.
        columnas (list[str]): Lista con los nombres de las columnas categóricas/no numéricas.

    Returns:
        None: Imprime directamente el reporte de diagnóstico en la consola.
    """
    # Corrección de sintaxis: Multiplicación de strings dentro de la función print
    print('=' * 60)
    print('Análisis Exploratorio Inicial de Datos No Numéricos')
    print('=' * 60)
    
    total_registros = datos.shape[0]
    print(f'Total de Registros en el Dataset: {total_registros}\n')
    
    for col in columnas:
        print('-' * 60)
        print(f'Análisis de la Variable: {col}')
        print('-' * 60)
        
        # .nunique() es más rápido y por defecto ignora los NaN automáticamente.
        # Contamos cuántos valores únicos reales y útiles existen en esta columna.
        valores_unicos = datos[col].nunique()
        
        # Calculamos también cuántos nulos tiene esta columna específica para dar más contexto
        total_nulos = datos[col].isna().sum()
        porcentaje_nulos = (total_nulos / total_registros) * 100
        
        print(f'Cantidad de Valores Únicos (Cardinalidad): {valores_unicos}')
        print(f'Índice de Unicidad: {valores_unicos/total_registros}')
        print(f'Valores Faltantes (NaN): {total_nulos} ({porcentaje_nulos:.2f}%)')
        print()