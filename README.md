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
3. Introducción a Pandas
4. Combinar dataframes
5. Aplicar transformaciones y calcular resúmenes por grupos
6. Visualizar datos con gráficas en Matplotlib
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


