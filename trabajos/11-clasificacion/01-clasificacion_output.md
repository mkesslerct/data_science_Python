# Clasificación con regresión logística
## Primer conjunto de datos: frontera de decisión lineal.

Vamos a empezar con un primer conjunto. El fichero que contiene los datos es ejemplo-logistica-1.csv que se puede descargar del Aula Virtual y guardar en la carpeta data del directorio asociado a nuestro nuevo proyecto.


```python
# Completar aquí

# --------------------
datos
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
      <th>x1</th>
      <th>x2</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.33</td>
      <td>2.65</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.86</td>
      <td>3.42</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.86</td>
      <td>1.92</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.54</td>
      <td>4.77</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.01</td>
      <td>0.59</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>3.88</td>
      <td>3.88</td>
      <td>0</td>
    </tr>
    <tr>
      <th>996</th>
      <td>3.18</td>
      <td>0.35</td>
      <td>0</td>
    </tr>
    <tr>
      <th>997</th>
      <td>1.41</td>
      <td>1.20</td>
      <td>0</td>
    </tr>
    <tr>
      <th>998</th>
      <td>0.96</td>
      <td>1.21</td>
      <td>0</td>
    </tr>
    <tr>
      <th>999</th>
      <td>1.33</td>
      <td>1.94</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 3 columns</p>
</div>



El conjunto presenta dos características x1 y x2, que queremos usar para poder predecir la variable binaria y.


Llevad a cabo la representación gráfica del conjunto, usando un color distinto para distinguir entre los valores de y.


```python
# Completar aquí 

# --------------------

```


    
![svg](01-clasificacion_output_files/01-clasificacion_output_3_0.svg)
    


Cúantos etiquetas de 0 y de 1 hay en el conjunto?



```python
# Completar aquí

# --------------------

```




    0    907
    1     93
    Name: y, dtype: int64



## Ajuste paso a paso de una regresión logística.


En esta parte, vamos a aprender a ajustar una regresión logística a nuestros datos.
Lo hacemos usando en `sklearn` la clase `LogisticRegression` del súbmodulo `linear_model`


```python
# Completar aquí: importar LogisticRegression

# --------------------

```

Para ilustrar, vamos a ajustarlo sobre todo el conjunto. Después de definir `X` e `y`, instanciar el estimador dándole el nombre `log_reg`, y ajustarlo a los datos


```python
# Completar aquí

# --------------------

```




    LogisticRegression()



Podemos consultar los coeficientes y la ordenada con los atributos `coef_` y `intercept_`, al igual que lo hicimos para `LinearRegression`.


```python
# Completar aquí:

# --------------------

```

    Coeficientes: [[-3.85884303  3.68888482]]
    Ordenada: [-10.53561775]


Deducir de estos valores la ecuación explícita de la recta que sirve de frontera de decisión para nuestro algoritmo


```python
# Completar aquí

# --------------------
print(f'La pendiente es {pendiente:.3f} mientras que la ordenada al origen es {ordenada:.3f}.')
```

    La pendiente es 1.046 mientras que la ordenada al origen es 2.856.


Usando `axline`, añadid a la gráfica la frontera de decisión


```python
# Completar aquí

# --------------------

```


    
![svg](01-clasificacion_output_files/01-clasificacion_output_15_0.svg)
    


## Medidas de calidad del ajuste
Para medir la calidad de nuestro algoritmo, tal como lo vimos en la unidad anterior, podemos usar la validación cruzada, correspondiente a `cross_val_scores` del súbmodulo `model_selection`, pero esta vez, al ser el problema de clasificación, vamos a usar `scoring='accuracy'` que calcula el proporción de veces que la clasificación acierta.

Aplicar validación cruzada con 5 "folds" al conjunto, usando nuestro estimador `log_reg`, y guardar las puntuaciones en un objecto llamado `scores`.


```python
# Completar aquí

# --------------------
scores
```




    array([0.985, 0.975, 0.975, 0.99 , 0.975])



Los resultados son buenísimos, pero estos indicadores son demasiado sumarios. 
Imaginad que hubiéramos escogido como regla de clasificación que todos los datos son 0. Habríamos tenido un tasa de acierto de más del 90% que, a priori es muy buena!

Por ello, lo que se hace es, para empezar, comprobar la matriz de confusión, que nos dice cuántas veces hemos clasificado un 0 como un 1, un 0 como un 1, un 1 como un 0 y un 1 como un 1. En inglés corresponde a 

- TP: True Positive, los 1 clasificados como 1
- TN: True Negative, los 0 clasificados como 0
- FP: False Positivo, los 0 que hemos clasificado erróneamente como 1
- FN: False Negative, los 1 que hemos clasificado erróneamente como 0.

Para construir esta matriz, necesitamos las predicciones de cada individuo. Si queremos hacerlo con validación cruzada (lo recomendable), usamos `cross_val_predict` del súbmodulo `model_selection`. 
En la validación cruzada, por ejemplo con 5 folds, cada individuo entra 4 veces en un subconjunto de aprendizaje y sólo una vez en un subconjunto de tipo test, en el que se realiza la predicción. `cross_val_predict` devuelve el vector de los valores predichos durante el proceso de validación cruzada

Después de importar `cross_val_predict`, construir el vector `y_pred` que contenga los valores predichos durante el proceso de validación cruzada. [Referencia](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html) de `cross_val_predict`.


```python
# Completar aquí

# --------------------

```

Podemos ahora calcular la matriz de confusión, importando `confusion_matrix` del submódulo `metrics`. [Referencia](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)


```python
# Completar aquí

# --------------------

```




    array([[900,   7],
           [ 13,  80]], dtype=int64)



Deducid de esta matrix la precisión, es decir la tasa de Verdaderos Positivos (TP) respecto a todos los predichos como positivos, (TP + FP). Asignadla a un objeto que llamaremos `precision`


```python
# Completar aquí

# --------------------
print(f'La precisión es : {precision:.3f}')
```

    La precisión es : 0.920


Calculad la sensibilidad, es decir la tasa de individuos clasificados como Positivos (TP) respecto a auténticos positivos en el conjunto, (TP + FN). Asignadla a un objeto que llamaremos `sensibilidad`


```python
# Completar aquí

# --------------------
print(f'La sensibilidad es : {sensibilidad:.3f}')
```

    La sensibilidad es : 0.860


Se pueden calcular automáticamente con `scikit-learn` usando `precision_score` y `recall_score` del submódulo `metrics`. Le pasamos como argumentos `y_pred` e `y`. Asignamos sus valores a `puntuacion_precision` y `puntuacion_recall`.


```python
# Completar aquí

# --------------------
print(f'Los valores calculados usando precision_score y recall_score son: {puntuacion_precision:.2f} y {puntuacion_recall:.2f} respectivamente.')
```

    Los valores calculados usando precision_score y recall_score son: 0.92 y 0.86 respectivamente.


## Clasificación de un nuevo individuo
Supongamos que tenemos un nuevo individuo cuyas características son `x1=3` y `x2=2`. Predecir la etiqueta de `y`, y calcular la probabilidad estimada asociada  que se obtiene con el método `predict_proba` que se aplica a nuestro estimador.


```python
# Completar aquí

# --------------------

```

    La predicción es 0 con una probabilidad de 1.0000


## Representación de la probabilidad predicha en función de los valores de `x1` y `x2`
Vamos a usar el método `predict_proba` para calcular la probabilidad asigna por nuestro modelo a los valores de la región y visualizarlos usando un mapa de calor.
Vamos a construir una rejilla de `n_puntos` por `n_puntos` en el rango de valores de `x1` y `x2`, y calcularemos para cada par de valores en la rejilla la probabilidad predicha por nuestro estimador. A continuación los representaremos usando el color para distinguir los valores de la probabilidad.
Situamos el código necesario en una función:


```python
# Nada que completar
def visualizar_proba_pred(estimador, X, n_puntos=200):
    # Creamos la rejilla, usando mínimo y máximo de las columnas de X
    l_x1=X[:,0].min()
    r_x1=X[:,0].max()
    l_x2=X[:,1].min()
    r_x2=X[:,1].max()
    x1, x2 = np.meshgrid(
        np.linspace(l_x1, r_x1, n_puntos),
        np.linspace(l_x2, r_x2, n_puntos)
    )
    X_rejilla = np.array([x1.ravel(), x2.ravel()]).reshape(2, -1).T
    y_rejilla = estimador.predict_proba(X_rejilla)[:, 1]
    c = y_rejilla.reshape(n_puntos, n_puntos)
    l_c,r_c  = np.abs(c).min(), np.abs(c).max()
    figure, axes = plt.subplots()
    c = axes.pcolormesh(x1, x2, c, cmap='coolwarm', vmin=l_c, vmax=r_c, shading='auto')
    axes.set_title('Probabilidad estimada de que la etiqueta sea 1')
    axes.axis([l_x1, r_x1, l_x2, r_x2])
    figure.colorbar(c);
```

Representamos la visualización para nuestro modelo `log_reg` usando esta función


```python
# Completar aquí

# --------------------

```


    
![svg](01-clasificacion_output_files/01-clasificacion_output_33_0.svg)
    


# Segundo ejemplo, frontera de decisión cuadrática
Descargad el fichero ejemplo-logistica-2.csv y cargadlo en un DataFrame llamado datos.
Representad `x2` frente a `x1`, distinguiendo según el valor de `y`.


```python
# Completar aquí

# --------------------

```


    
![svg](01-clasificacion_output_files/01-clasificacion_output_35_0.svg)
    


## Ajuste de una regresión logística con características polinomiales de grado 2.
Usando el transformador `PolynomialFeatures` del súbmodulo `preprocessing`, cread un pipeline que calcule los términos polinomiales de grado 2 y a continuación aplique una regresión lógistica.
> Usaremos el argumento `include_bias=False` en `PolynomialFeatures`, para que no añada una columna de 1 a nuestra matriz de características, puesto que la regresión logística ya se encarga de ello.


```python
# Completar aquí

# --------------------

```

Aplicadlo al conjunto de datos, definiendo `X` e `y`. Escribid la ecuación implícita de la frontera de la región de decisión.


```python
# Completar aquí

# --------------------

```

    La ecuación de la frontera de decisión es 8.69-5.68x1-4.55x2+1.23x1^2-0.21x1x2+1.28x2^2



```python

```

Obtened la matriz de confusión, después de usar validación cruzada para predecir los valores en el conjunto



```python
# Completar aquí

# --------------------

```




    array([[219,  65],
           [ 51, 665]], dtype=int64)



Finalmente, usad la función `visualizar_proba_pred` para visualizar la probabilidad predicha


```python
# Completar aquí

# --------------------

```


    
![svg](01-clasificacion_output_files/01-clasificacion_output_44_0.svg)
    

