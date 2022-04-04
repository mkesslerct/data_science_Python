# Trabajo, flujo de trabajo en machine learning con `scikit-learn`
Para ilustar el flujo de trabajo frente a un conjunto de datos usando scikit-learn, vamos a considerar la predicción de la nota media de los alumnos de grados de la ETSIT que ya se abordó en el trabajo anterior.

El fichero que contiene los datos es `notas_DURM_media_ETSIT.csv` que se puede descargar del Aula Virtual y guardar en la carpeta data del directorio asociado a nuestro workspace. 

Después de cargar las librerías `pandas`, `numpy` y `matplotlib`, cargar los datos en un dataframe llamado `grados`.



```python
# Completar aquí

# --------------------

```


```python
# Completar aquí

# --------------------

```

## Empezamos por definir la matriz `X` de características y el vector `y` de respuestas

Vamos a empezar por definir la matriz `X` de características. Queremos incluir todas las características numéricas desde `NOTA_PAU_FISICA` que tienen que ver con la PAU, así como las de notas y las convocatorias de las asignaturas de las carrera consideradas. (No vamos a incluir las matrículas) Podréis usar loc, pasando un vector booleano en la dimensión de las columnas. Para crear este vector booleano, podréis usar el método `str.contains` que se puede aplicar a  `grados.columns`. Admite una expresión regular como argumento. Concretamente, para quedarnos con las columnas cuyos nombres contienen "NOTA" o "CONVOCS", escribimos `str.contains("NOTA|CONVOCS")`


```python
# Completar aquí: Definimos primero el DataFrame X.df que contenga las columnas que nos interesen

# --------------------
print(X_df.columns)

```

    Index(['NOTA_PAU_FISICA', 'NOTA_PAU_MATEMATICAS II', 'NOTA_PAU_CALIFICACION',
           'NOTA_FUNDAMENTOS DE PROGRAMACIÓN', 'NOTA_ONDAS ELECTROMAGNÉTICAS',
           'NOTA_SISTEMAS Y CIRCUITOS', 'NOTA_TEORÍA DE LA COMUNICACIÓN',
           'CONVOCS_HASTA_PRESENTARSE_1RA_VEZ_FUNDAMENTOS DE PROGRAMACIÓN',
           'CONVOCS_HASTA_PRESENTARSE_1RA_VEZ_ONDAS ELECTROMAGNÉTICAS',
           'CONVOCS_HASTA_PRESENTARSE_1RA_VEZ_SISTEMAS Y CIRCUITOS',
           'CONVOCS_HASTA_PRESENTARSE_1RA_VEZ_TEORÍA DE LA COMUNICACIÓN',
           'CONVOCS_TOTALES_FUNDAMENTOS DE PROGRAMACIÓN',
           'CONVOCS_TOTALES_ONDAS ELECTROMAGNÉTICAS',
           'CONVOCS_TOTALES_SISTEMAS Y CIRCUITOS',
           'CONVOCS_TOTALES_TEORÍA DE LA COMUNICACIÓN'],
          dtype='object')


Podemos transformar `X_df` a `X`, que será un `ndarray` de `numpy`usando su atributo `values`


```python
# Completar aquí

# --------------------
print(f'X es un objeto de tipo {type(X)} con tamaño {X.shape}')
```

    X es un objeto de tipo <class 'numpy.ndarray'> con tamaño (318, 15)


Definimos ahora el vector `y` de respuestas


```python
# Completar aquí

# --------------------
print(y[:10])
```

    [8.81089744 7.47297297 8.05131579 8.67364865 7.425      8.04539474
     6.53690476 9.07039474 6.87152778 9.08881579]



```python
import sklearn
```

# Primer bloque en la cadena de manipulación: imputación de valores faltantes
Empezad por obtener el número de valores faltantes de cada columna, desglosando por grado.


```python
# Completar aquí

# --------------------

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PLAN_ID</th>
      <th>CREDITOS</th>
      <th>MEDIA</th>
      <th>CURSO_INICIO</th>
      <th>NOTA_PAU_FISICA</th>
      <th>NOTA_PAU_MATEMATICAS II</th>
      <th>NOTA_PAU_CALIFICACION</th>
      <th>PLAN_DESC</th>
      <th>NOTA_FUNDAMENTOS DE PROGRAMACIÓN</th>
      <th>NOTA_ONDAS ELECTROMAGNÉTICAS</th>
      <th>...</th>
      <th>MATRICS_TOTALES_SISTEMAS Y CIRCUITOS</th>
      <th>MATRICS_TOTALES_TEORÍA DE LA COMUNICACIÓN</th>
      <th>CONVOCS_HASTA_PRESENTARSE_1RA_VEZ_FUNDAMENTOS DE PROGRAMACIÓN</th>
      <th>CONVOCS_HASTA_PRESENTARSE_1RA_VEZ_ONDAS ELECTROMAGNÉTICAS</th>
      <th>CONVOCS_HASTA_PRESENTARSE_1RA_VEZ_SISTEMAS Y CIRCUITOS</th>
      <th>CONVOCS_HASTA_PRESENTARSE_1RA_VEZ_TEORÍA DE LA COMUNICACIÓN</th>
      <th>CONVOCS_TOTALES_FUNDAMENTOS DE PROGRAMACIÓN</th>
      <th>CONVOCS_TOTALES_ONDAS ELECTROMAGNÉTICAS</th>
      <th>CONVOCS_TOTALES_SISTEMAS Y CIRCUITOS</th>
      <th>CONVOCS_TOTALES_TEORÍA DE LA COMUNICACIÓN</th>
    </tr>
    <tr>
      <th>PLAN_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>5041</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>21</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>9</td>
      <td>5</td>
      <td>...</td>
      <td>3</td>
      <td>3</td>
      <td>9</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>9</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>5051</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>22</td>
      <td>12</td>
      <td>3</td>
      <td>0</td>
      <td>32</td>
      <td>23</td>
      <td>...</td>
      <td>31</td>
      <td>24</td>
      <td>32</td>
      <td>23</td>
      <td>31</td>
      <td>24</td>
      <td>32</td>
      <td>23</td>
      <td>31</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 28 columns</p>
</div>



Podemos decidir asignar a los valores faltantes el valor de la mediana de su columna. Para ello, podemos usar la clase `SimpleImputer` del submódulo `impute` de `sklearn`. `SimpleImputer` es un objeto de la clase `Transformer`. para más información, ver la [referencia](https://scikit-learn.org/stable/modules/impute.html#impute)

Para ello, vamos a seguir los pasos vistos en las transparencias:
1. Instanciamos el objeto que llamaremos `imp`, especificando el parámetro `strategy='median'` indicando así que queremos que sustituya los valores faltantes (codificados como `np.nan`) por la mediana de su columna:


```python
# Completar aquí: 

# --------------------
imp

```




    SimpleImputer(strategy='median')



2. Ahora podemos realizar la estimación de los parámetros necesarios para el transformador, en el caso de nuestro conjunto de datos. Se realiza con el método `fit`.


```python
# Completar aquí

# --------------------
# Comprobamos los valores que ha calculado para poder posteriormente hacer la sustitución de los valores faltantes  
imp.statistics_
```




    array([6.28, 6.53, 7.54, 7.5 , 5.95, 5.9 , 6.4 , 1.  , 2.  , 1.  , 1.  ,
           1.  , 3.  , 1.  , 2.  ])



Entendéis cómo se ha calculado el valor 6.28 por ejemplo? Explicad lo aquí:




3. Podemos ahora aplicar el transformador con sus parámetros ya preparados a la matrix `X` y asignar el resultado a una nueva matriz `X_completada`. Se realiza con el método `transform`.


```python
# Completar aquí

# --------------------
pd.DataFrame(X_completada).count()
```




    0     318
    1     318
    2     318
    3     318
    4     318
    5     318
    6     318
    7     318
    8     318
    9     318
    10    318
    11    318
    12    318
    13    318
    14    318
    dtype: int64



## Creación del flujo con un `pipe`
Vamos ahora a unir tres etapas del procesamiento de los datos:
- imputación de valores faltantes
- estanderización: aunque las columnas no sean de ordenes de magnitud muy diferentes, para ilustrar el procedimiento, vamos a usar del submodulo `preprocessing` el transformador `StandardScaler`
- estimación por regresión lineal. Para ello, vamos el usar el estimador `LinearRegression` del submódulo `linear_model` de `sklearn`

Además los combinaremos en un único flujo usando `Pipeline` del submódulo `pipeline`. Lo hacemos creando el objeto que llamaremos `procesado_regresion`. Llamaremos los steps 'imputacion', 'estanderizacion', 'regresion'.


```python
# Completar aquí

# --------------------
procesado_regresion
```




    Pipeline(steps=[('imputacion', SimpleImputer(strategy='median')),
                    ('estanderizacion', StandardScaler()),
                    ('regresion', LinearRegression())])



## Separación del conjunto de aprendizaje y el de test
Usando `train_test_split` del submódulo `model_selection`, vamos a separar un conjunto de aprendizaje, que llamaremos `X_train` e `y_train` y el conjunto de test `X_test` e `y_test`. 
Lo realizamos reservando el 20% de los casos para `test` y, para que podáis comparar vuestros resultados con los míos, usando el parámetro `random_state=314`. 


```python
# Completar aquí

# --------------------
print(f'Tamaño de X_train: {X_train.shape}, tamaño de y_train {y_train.shape}')
print(f'Tamaño de X_test: {X_test.shape}, tamaño de y_test {y_test.shape}')
```

    Tamaño de X_train: (254, 15), tamaño de y_train (254,)
    Tamaño de X_test: (64, 15), tamaño de y_test (64,)


## Ajuste del modelo sobre el conjunto de aprendizaje y comprobación sobre conjunto de test
Vamos ahora a aplicar la combinación de transformadores y estimador que definimos como pipeline con las tres etapas ('imputacion', 'estanderizacion', 'regresion') sobre los datos de aprendizaje. El objeto pipeline se aplica con los mismos pasos de instanciación, ajuste. 


```python
# Completar aquí

# --------------------

```




    Pipeline(steps=[('imputacion', SimpleImputer(strategy='median')),
                    ('estanderizacion', StandardScaler()),
                    ('regresion', LinearRegression())])



Ahora vamos a realizar la predicción sobre el conjunto de test, creando el vector `y_test_pred`.


```python
# Completar aquí

# --------------------
y_test_pred[:10]
```




    array([6.77031107, 8.18766229, 7.61139718, 7.05030893, 7.07489737,
           6.7973194 , 7.0785764 , 6.27664063, 7.75293029, 7.08045576])



Nos queda evaluar la calidad de la predicción sobre el conjunto de test, calculando el RMSE. Lo guardamos en un objeto que llamamos `RMSE`.


```python
# Completar aquí

# --------------------
print(f'El valor del RMSE sobre el conjunto test es {RMSE}')
```

    El valor del RMSE sobre el conjunto test es 0.500608147168195


## Probamos con un subconjunto de características
Queremos probar con sólo las notas, tanto de la parte de acceso a la universidad como en la UPCT. Creamos una matriz `X_train_notas` que contenga sólo las columnas de `X_train` correspondientes a las características de notas (son las 7 primeras).


```python
# Completar aquí

# --------------------
# imprimimos las tres primeras filas:
print(X_train_notas[:3,])
```

    [[1.2   nan 7.92 5.4   nan 6.2  5.  ]
     [5.05 6.87 7.57 8.1  5.5  5.   5.3 ]
     [6.3  7.5  7.31 8.    nan 5.9   nan]]


Repetid el análisis usando `X_train_notas` y considerando `X_test_notas`



```python
# Completar aquí

# --------------------
print(f'El valor del RMSE sobre el conjunto test es {RMSE}')
# Fin Completar aquí
```

    El valor del RMSE sobre el conjunto test es 0.5060101842487271


# Ajuste con RandomForestRegressor
`scikit-learn` implementa otros muchos algoritmos para la predicción. En este apartado vamos a probar una regresión "Random Forest" que está basada en muchos árboles de decisión cuya predicción promedio es el resultado de nuestro algoritmo. 
Se trata de la clase `RandomForestRegressor` del submodulo `ensemble`. Depende de varios hiperparámetros, de los cuáles destacaremos:
- El número de estimadores `n_estimators`, que es el número de árboles de decisión en el "bosque", a priori cuanto más mejor, pero hay un momento en el que ya no mejora el ajuste y el coste computacional es grande.
- El número de características, que es el número máximo de características que debe considerar el modelo. Sobre todo útil si tenemos muchas. Si no especificamos nada para este hiperpárametro, su defecto es `None` que contempla todas las características.

Puesto que tenemos que fijar los valores de los hiperparámetros, lo vamos a hacer con el procedimiento de `GridSearchCV` que aplica validación cruzada sobre el conjunto de training, para determinar qué combinación de los hiperparámetros proporciona el mejor ajuste.

## Creación del flujo (pipe)
Al igual que en el apartado anterior, vamos a crear un flujo que incluya las tres etapas de imputación de valores faltantes, estanderización y regresión usando randomforests en este caso. Lo llamaremos `procesado_rfr`.


```python
# Completar aquí

# --------------------
procesado_rfr
```




    Pipeline(steps=[('imputacion', SimpleImputer(strategy='median')),
                    ('standerizacion', StandardScaler()),
                    ('rfr', RandomForestRegressor())])



## Ajuste de los hiperparámetros
Vamos ahora a llevar a cabo la búsqueda de los  mejores hiperparamétros entre las combinaciones de los siguientes valores:
- `n_estimators` toma los valores 3, 10, 30
- `max_features` toma los valores 2, 8, 15

Siguiendo las transparencias, llevar a cabo el `GridSearchCV`, instanciando el objeto necesario para empezar (lo llamamos `grid_search`)


```python
# Completar aquí

# --------------------
grid_search
```




    GridSearchCV(cv=5,
                 estimator=Pipeline(steps=[('imputacion',
                                            SimpleImputer(strategy='median')),
                                           ('standerizacion', StandardScaler()),
                                           ('rfr', RandomForestRegressor())]),
                 param_grid={'rfr__max_features': [2, 8, None],
                             'rfr__n_estimators': [3, 10, 30]},
                 scoring='neg_mean_squared_error')



Podemos ahora aplicar el método `fit` sobre `grid_search`.


```python
# Completar aquí

# --------------------
grid_search
```




    GridSearchCV(cv=5,
                 estimator=Pipeline(steps=[('imputacion',
                                            SimpleImputer(strategy='median')),
                                           ('standerizacion', StandardScaler()),
                                           ('rfr', RandomForestRegressor())]),
                 param_grid={'rfr__max_features': [2, 8, None],
                             'rfr__n_estimators': [3, 10, 30]},
                 scoring='neg_mean_squared_error')



Y aplicamos el resultado (que es el mejor estimador entre las combinaciones) sobre el conjunto de test, calculando su RMSE


```python
# Completar aquí

# --------------------
print(f'El valor de RMSE para la mejor combinación de hiperparámetros es: {RMSE}')
```

    El valor de RMSE para la mejor combinación de hiperparámetros es: 0.4688343350073512


Obtened los mejores parámetros:


```python
# Completar aquí

# --------------------

```




    {'rfr__max_features': 2, 'rfr__n_estimators': 30}



Y recorremos todos los algoritmos que se probaron, imprimiendo su puntuación



```python
resultados = grid_search.cv_results_
for mean_score, params in zip(resultados['mean_test_score'], resultados['params']):
    print(np.sqrt(-mean_score), params)
```

    0.41996348417081525 {'rfr__max_features': 2, 'rfr__n_estimators': 3}
    0.3975052145321989 {'rfr__max_features': 2, 'rfr__n_estimators': 10}
    0.3730965796274537 {'rfr__max_features': 2, 'rfr__n_estimators': 30}
    0.4383489209713492 {'rfr__max_features': 8, 'rfr__n_estimators': 3}
    0.3786647079596916 {'rfr__max_features': 8, 'rfr__n_estimators': 10}
    0.37316883315993765 {'rfr__max_features': 8, 'rfr__n_estimators': 30}
    0.41968007861054335 {'rfr__max_features': None, 'rfr__n_estimators': 3}
    0.4038804589265984 {'rfr__max_features': None, 'rfr__n_estimators': 10}
    0.3923576364222825 {'rfr__max_features': None, 'rfr__n_estimators': 30}


## Importancia de cada característica en la predicción
`RandomForestRegressor` proporciona la importancia relativa de cada característica en la predicción. Se obtiene con el atributo `feature_importances_` del estimador ajustado. En este caso, lo aplicamos al tercer paso de `best_estimator_`, que corresponde a random forest regression de `grid_search`. 


```python
grid_search.best_estimator_.steps[2][1].feature_importances_
```




    array([0.07023098, 0.05192649, 0.11331106, 0.09156294, 0.09339768,
           0.12101729, 0.12287604, 0.01310286, 0.03521873, 0.00901062,
           0.02267826, 0.02907091, 0.08664401, 0.04113167, 0.09882047])



Podemos identificar qué variables tienen mayor importancia en la predicción usando RandomForestRegressor.

## Opcional: representación gráfica
Procurad replicar esta gráfica que compara valores observados y predichos sobre el conjunto test.


```python
# Completar aquí

# --------------------

```


    
![png](01-sklearn_output_files/01-sklearn_output_50_0.png)
    


# Opcional. Ajuste incluyendo características polinomiales en la regresión de RandomForest.
Es posible incluir las características que corresponden a potencias y productos de características existentes en el conjunto. Se puede hacer de manera muy sencilla usando el `transformer` `PolynomialFeatures` del submódulo `preprocessing`. 
Añadid un paso en el flujo `procesado_rfr` que consista en el transformer  `PolynomialFeatures`.
Una vez añadido, realizad el `GridSearchCV` incluyendo también el hiperparámetro `degree` de `PolynomialFeatures` que pueda tomar el valor 2 o 3.
Comprobad la bondad del ajuste del mejor modelo sobre el conjunto de test.


```python
# Completar aquí

# --------------------
print(f'El valor de RMSE para la mejor combinación de hiperparámetros es: {RMSE}')
```

    El valor de RMSE para la mejor combinación de hiperparámetros es: 0.4784933419561473



```python
# Completar aquí: mejor combinación de hiperparámetros

# --------------------

```




    {'polinomial__degree': 1, 'rfr__max_features': 2, 'rfr__n_estimators': 30}




```python
# Completar aquí: valores de la puntuación de todos los modelos probados

# --------------------

```

    0.46672132885174283 {'polinomial__degree': 1, 'rfr__max_features': 2, 'rfr__n_estimators': 3}
    0.40035304668925975 {'polinomial__degree': 1, 'rfr__max_features': 2, 'rfr__n_estimators': 10}
    0.36360787320926985 {'polinomial__degree': 1, 'rfr__max_features': 2, 'rfr__n_estimators': 30}
    0.4398712979096358 {'polinomial__degree': 1, 'rfr__max_features': 8, 'rfr__n_estimators': 3}
    0.39276433470366023 {'polinomial__degree': 1, 'rfr__max_features': 8, 'rfr__n_estimators': 10}
    0.37577229926149336 {'polinomial__degree': 1, 'rfr__max_features': 8, 'rfr__n_estimators': 30}
    0.43092524685017497 {'polinomial__degree': 1, 'rfr__max_features': None, 'rfr__n_estimators': 3}
    0.3927617023333028 {'polinomial__degree': 1, 'rfr__max_features': None, 'rfr__n_estimators': 10}
    0.3947990717560434 {'polinomial__degree': 1, 'rfr__max_features': None, 'rfr__n_estimators': 30}
    0.4680392826543959 {'polinomial__degree': 2, 'rfr__max_features': 2, 'rfr__n_estimators': 3}
    0.4522866256290427 {'polinomial__degree': 2, 'rfr__max_features': 2, 'rfr__n_estimators': 10}
    0.41335609671827583 {'polinomial__degree': 2, 'rfr__max_features': 2, 'rfr__n_estimators': 30}
    0.444915132112396 {'polinomial__degree': 2, 'rfr__max_features': 8, 'rfr__n_estimators': 3}
    0.4015782136373722 {'polinomial__degree': 2, 'rfr__max_features': 8, 'rfr__n_estimators': 10}
    0.39454390041834786 {'polinomial__degree': 2, 'rfr__max_features': 8, 'rfr__n_estimators': 30}
    0.42188820977086605 {'polinomial__degree': 2, 'rfr__max_features': None, 'rfr__n_estimators': 3}
    0.400185724253491 {'polinomial__degree': 2, 'rfr__max_features': None, 'rfr__n_estimators': 10}
    0.38098425269112784 {'polinomial__degree': 2, 'rfr__max_features': None, 'rfr__n_estimators': 30}
    0.45763304484064266 {'polinomial__degree': 3, 'rfr__max_features': 2, 'rfr__n_estimators': 3}
    0.41854427167906366 {'polinomial__degree': 3, 'rfr__max_features': 2, 'rfr__n_estimators': 10}
    0.38853734818627234 {'polinomial__degree': 3, 'rfr__max_features': 2, 'rfr__n_estimators': 30}
    0.4196122837304968 {'polinomial__degree': 3, 'rfr__max_features': 8, 'rfr__n_estimators': 3}
    0.40778953269765567 {'polinomial__degree': 3, 'rfr__max_features': 8, 'rfr__n_estimators': 10}
    0.3776821267152501 {'polinomial__degree': 3, 'rfr__max_features': 8, 'rfr__n_estimators': 30}
    0.43898359080073335 {'polinomial__degree': 3, 'rfr__max_features': None, 'rfr__n_estimators': 3}
    0.39498489464135605 {'polinomial__degree': 3, 'rfr__max_features': None, 'rfr__n_estimators': 10}
    0.38194377134710294 {'polinomial__degree': 3, 'rfr__max_features': None, 'rfr__n_estimators': 30}

