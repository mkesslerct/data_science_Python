# Introducción a Data Science con Python

## Presentación

He impartido a lo largo de varios años en la Escuela Técnica Superior de Ingeniería de Telecomunicaciones en la Universidad Politécnica de Cartagena, una asignatura optativa de introducción a Data science. Durante muchos años el lenguage de programación usado era R, pero desde el curso 2020/21, decidí pasar a Python con las librerías `pandas`, `matplotlib` y `scikit-learn`. 

Este repositorio contiene todo el material de la asignatura, para su estudio autónomo. Encontraréis los enlaces a las unidades de aprendizaje así como trabajos propuestos para practicar los conceptos de cada tema.

> Nota: las unidades digitales fueron elaboradas con UPCTforma, la herramienta de autor creada por el [Centro de Producción de Contenidos Digitales](http://cpcd.upct.es/) de la Universidad Politécnica de Cartagena, en el seno de dos proyectos Erasmus Plus, INDIe 2018-1-ES01-KA201-050924 y INDIe4All  2020-1-ES01-KA201-083177, cofinanciados por la Comisión Europea.

> Para profesores: en este repositorio podréis encontrar también los ficheros fuentes de los documentos. En el directorio [utilidades](utilidades/readme.md), están algunos scripts útiles para generar entregables etc...

> Licencia: los materiales de este curso están distribuidos con la licencia Atribución-CompartirIgual 4.0 Internacional de Creative Commons. [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es). 

## Contenidos

1. [Preliminares: preparación Python para el curso](#preliminares-instalaci%C3%B3n-de-python-y-visual-studio-code-para-el-curso).
2. [Introducción a Python](#Introducci%C3%B3n-a-Python).
3. [Introducción a Pandas](#Introducci%C3%B3n-a-Pandas).
4. [Combinar dataframes](#combinar-dataframes)
5. [Aplicar transformaciones y calcular resúmenes por grupos](#aplicar-transformaciones-y-calcular-res%C3%BAmenes-por-grupos)
6. [Visualizar datos con gráficas en Matplotlib](#visualizar-datos-con-gr%C3%A1ficas-en-matplotlib)
7. Regresión
8. Aprendizaje máquina con Scikit-learn
9. Clasificación con regresión logística
10. Regularización de la función coste
11. Reducción de dimensión: análisis en componentes principales


## Datos necesarios para los trabajos y algunos ejemplos

En el siguiente enlace, podéis encontrar los ficheros de datos necesarios para los trabajos y los ejemplos. Podéis descargarlos a medida que los vayáis necesitando y guardar en una carpeta `data` en vuestro directorio de trabajo. También podéis indicar la url del conjunto a la hora de cargar el conjunto de datos con `read_csv`de `pandas`. Si optáis por esta segunda opción, tenéis que usar la url correspondiente a la versión "raw" del fichero en Github.

[Carpeta data](data/)

## Preliminares: instalación de Python y Visual Studio Code para el curso.

[Unidad con instrucciones sobre preparación de Python, Anaconda y Visual Studio Code](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/962daf11bddf469a94882d702aa95b17/)

Para facilitar la creación del entorno virtual `ids` en conda, podéis usar el siguiente fichero `yml` [ids_environment.yml](transparencias/00-preliminares_python_vscode/ids_environment.yml)


## Introducción a Python

### Unidades de aprendizaje
- [Unidad de introducción a Python, primeros pasos](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/4a6d472072f8484891005cad326a8f34/)
- [Funciones y métodos en Python](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/8e24b1604bbd4599b06111374c6ad2d0/)
- [Más sobre listas y diccionarios](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/7ac3caf462e34991beab4eb50393f0ea/)

### Transparencias asociadas a las unidades:
- [Introducción a Python, primeros pasos & funciones y métodos](transparencias/03-introduccion_python/01-python_introduccion.pdf)
- [Más sobre listas y dicccionarios](transparencias/03-introduccion_python/02-mas_sobre_listas_diccionarios.pdf)

### Para practicar:
- [Ejercicios para practicar](trabajos/03-introduccion_python/01-ejercicios.pdf)

## Introducción a Pandas

### Unidades de aprendizaje
- [Unidad de introducción a Pandas](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/8b009111011e41cdbfee3c94485b1069/)

### Transparencias asociadas a las unidades:
- [Introducción a Pandas](transparencias/04-introduccion_pandas/01-introduccion_pandas.pdf)
- [Seleccionar filas y/o columnas en dataframes](transparencias/04-introduccion_pandas/02-acceso_columnas_filas.pdf)

### Para practicar:
- Introducción a Pandas:
  - [Bloc de notas](trabajos/04-introduccion_pandas/01-introduccion_pandas_handout.ipynb)
  - [Salidas esperadas](trabajos/04-introduccion_pandas/01-introduccion_pandas_output.md)
- Seleccionar filas y columnas:
  - [Bloc de notas](trabajos/04-introduccion_pandas/02-seleccionar_filas_columnas_handout.ipynb)
  - [Salidas esperadas](trabajos/04-introduccion_pandas/02-seleccionar_filas_columnas_output.md)

## Combinar dataframes

### Unidades de aprendizaje
- [Combinar dataframes: concat y merge](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/390f81126dc746358ba53f61a65e8015/)

### Transparencias asociadas a las unidades:
- [Concatenar dataframes](transparencias/05-concat_merge/01-concat-slides_handout.pdf)
- [Combinar dataframes usando merge](transparencias/05-concat_merge/02-merge-slides_handout.pdf)

### Para practicar:
- Concatenar dataframes:
  - [Bloc de notas](trabajos/05-concat_merge/01-concat_handout.ipynb)
  - [Salidas esperadas](trabajos/05-concat_merge/01-concat_output.md)
- Combinar dataframes con merge:
  - [Bloc de notas](trabajos/05-concat_merge/01-merge_handout.ipynb)
  - [Salidas esperadas](trabajos/05-concat_merge/01-merge_output.md)

## Aplicar transformaciones y calcular resúmenes por grupos:

### Unidades de aprendizaje
- [Aplicar funciones a dataframes o series en Pandas](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/c907f028659e46b08f3f8ffde9eebaf2/)
- [Trabajar con datos agrupados en Pandas](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/7d77217add624843bc2f1b086519904e/)

### Transparencias asociadas a las unidades:
- [Aplicar funciones](transparencias/06-apply/01-apply-slides_handout.pdf)
- [Definir datos agrupados y calcular resúmenes](transparencias/07-groupby/01-groupby-slides_handout.pdf)

### Para practicar:
- Consumo eléctrico de una vivienda, resúmenes e indicadores:
  - [Bloc de notas](trabajos/07-groupby/01-trabajo_consumo_vivienda_handout.ipynb)
  - [Salidas esperadas](trabajos/07-groupby/01-trabajo_consumo_vivienda_output.md)


## Visualizar datos con gráficas en Matplotlib

### Unidades de aprendizaje
- [Visualizar datos con Matplotlib](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/74ae28a23bcd48b0bad8c444e700758b/)

### Transparencias asociadas a las unidades:
- [Visualizar datos con Matplotlib](transparencias/08-plotting/01-visualizacion_matplotlib_handout.pdf)

### Para practicar:
- Consumo eléctrico de una vivienda, representaciones gráficas:
  - [Bloc de notas](trabajos/08-plotting/02-visualizacion_consumo_vivienda_handout.ipynb)
  - [Salidas esperadas](trabajos/08-plotting/02-visualizacion_consumo_vivienda_output.md)


## Regresión

### Unidades de aprendizaje
- [Regresión y algoritmo del gradiente](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/558ab527c4464ab58897e5537bb46876/)

### Transparencias asociadas a las unidades:
- [Regresión y algoritmo del gradiente](transparencias/09-regresion/01-regresion.pdf)

### Para practicar:
- Predicción de la nota media alumnos de grado:
  - [Bloc de notas](trabajos/09-regresion/01-regresion_lineal_handout.ipynb)
  - [Salidas esperadas](trabajos/09-regresion/01-regresion_lineal_output.md)

## Aprendizaje máquina con `Scikit-learn`

### Unidades de aprendizaje
- [Aprendizaje máquina con `Scikit-learn`](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/4e1d9b0c53df4a9f964719e18afe8789/)

### Transparencias asociadas a las unidades:
- [Aprendizaje máquina con `Scikit-learn`](transparencias/10-scikit-learn/01-scikit-learn_handout.pdf)

### Para practicar:
- Predicción de la nota media alumnos de grado:
  - [Bloc de notas](trabajos/10-scikit-learn/01-sklearn_handout.ipynb)
  - [Salidas esperadas](trabajos/10-scikit-learn/01-sklearn_output.md)

## Clasificación con regresión logística

### Unidades de aprendizaje
- [Clasificación](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/733ff1c8182e4211b10b5e4f1d6b8e75/)

### Transparencias asociadas a las unidades:
- [Clasificación](transparencias/11-clasificacion/01-clasificacion.pdf)

### Para practicar:
- Clasificación con regresión logística:
  - [Bloc de notas](trabajos/11-clasificacion/01-clasificacion_handout.ipynb)
  - [Salidas esperadas](trabajos/11-clasificacion/01-clasificacion_output.md)

## Regularización de la función coste

### Unidades de aprendizaje
- [Regularización para evitar sobreajuste](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/55a2356a72b44ef2817f10e6ad963cc0/)

### Transparencias asociadas a las unidades:
- [Regularización](transparencias/12-regularizacion/01-regularizacion.pdf)

### Para practicar:
- Regularización con regresión y clasificación:
  - [Bloc de notas](trabajos/12-regularizacion/01-regularizacion_handout.ipynb)
  - [Salidas esperadas](trabajos/12-regularizacion/01-regularizacion_output.md)

## Reducción de dimensión: análisis en componentes principales

### Unidades de aprendizaje
- [Análisis en componentes principales](https://opencontent.upct.es/3240eb3933be43129adf7ccb23f1fcda/e7e0dd89ba1c43e1907257216e734957/)

### Transparencias asociadas a las unidades:
- [Análisis en componentes principales](transparencias/13-acp/01-acp.pdf)

### Para practicar:
- Reducción de la dimensión de un conjunto de imágenes.
  - [Bloc de notas](trabajos/13-acp/01-acp_handout.ipynb)
  - [Salidas esperadas](trabajos/13-acp/01-acp_output.md)

