# Trabajo Regresión lineal: predicción de la nota media de los alumnos de grado de la ETSIT, UPCT. Primera parte.
## Introducción


> En este trabajo, usamos datos asociados a todos los alumnos de Grado en Ingeniería Telemática y Grado en Ingeniería de Sistemas de Telecomunicación de la UPCT, que hayan superado 120 ECTS, que provengan de la Región de Murcia y que se hayan examinado de Física y Matemáticas_II en la Prueba de Acceso a la Universidad (PAU).

## Objetivo:

Nuestro objetivo es estudiar la posibilidad de predecir la nota media a partir de algunos datos en el ingreso del estudiante (calificación y ranking PAU, así como de Física y Matemáticas II) y de sus resultados en algunas de las asignaturas más exigentes de la titulación:

1. Fundamentos de programación.
2. Sistemas y circuitos
3. Sistemas lineales
4. Ondas electromagnéticas

El fichero que contiene los datos es `notas_DURM_media_ETSIT.csv` que se puede descargar del Aula Virtual y guardar en la carpeta data del directorio asociado a nuestro workspace. 

Después de cargar las librerías `pandas`, `numpy` y `matplotlib`, cargar los datos en un dataframe llamado `grados`.


```python
# Completar aquí

# --------------------

```


```python
# Completar aquí

# --------------------
grados
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5041</td>
      <td>234.0</td>
      <td>8.810897</td>
      <td>2010-11</td>
      <td>9.6</td>
      <td>9.80</td>
      <td>9.34</td>
      <td>GRADO EN INGENIERÍA EN SISTEMAS DE TELECOMUNIC...</td>
      <td>8.6</td>
      <td>7.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5041</td>
      <td>222.0</td>
      <td>7.472973</td>
      <td>2010-11</td>
      <td>2.3</td>
      <td>9.25</td>
      <td>7.43</td>
      <td>GRADO EN INGENIERÍA EN SISTEMAS DE TELECOMUNIC...</td>
      <td>5.0</td>
      <td>5.5</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5041</td>
      <td>228.0</td>
      <td>8.051316</td>
      <td>2010-11</td>
      <td>8.7</td>
      <td>7.25</td>
      <td>8.10</td>
      <td>GRADO EN INGENIERÍA EN SISTEMAS DE TELECOMUNIC...</td>
      <td>6.9</td>
      <td>5.5</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5041</td>
      <td>222.0</td>
      <td>8.673649</td>
      <td>2010-11</td>
      <td>9.8</td>
      <td>9.00</td>
      <td>9.15</td>
      <td>GRADO EN INGENIERÍA EN SISTEMAS DE TELECOMUNIC...</td>
      <td>9.0</td>
      <td>6.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5041</td>
      <td>240.0</td>
      <td>7.425000</td>
      <td>2010-11</td>
      <td>4.1</td>
      <td>9.00</td>
      <td>7.97</td>
      <td>GRADO EN INGENIERÍA EN SISTEMAS DE TELECOMUNIC...</td>
      <td>8.4</td>
      <td>6.3</td>
      <td>...</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>313</th>
      <td>5051</td>
      <td>120.0</td>
      <td>8.135000</td>
      <td>2018-19</td>
      <td>5.1</td>
      <td>10.00</td>
      <td>9.57</td>
      <td>GRADO EN INGENIERÍA TELEMÁTICA (BOE 20-04-2011)</td>
      <td>10.0</td>
      <td>7.3</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>314</th>
      <td>5051</td>
      <td>120.0</td>
      <td>9.040000</td>
      <td>2018-19</td>
      <td>10.0</td>
      <td>10.00</td>
      <td>9.68</td>
      <td>GRADO EN INGENIERÍA TELEMÁTICA (BOE 20-04-2011)</td>
      <td>10.0</td>
      <td>9.5</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>315</th>
      <td>5051</td>
      <td>120.0</td>
      <td>8.075000</td>
      <td>2018-19</td>
      <td>5.4</td>
      <td>8.75</td>
      <td>8.38</td>
      <td>GRADO EN INGENIERÍA TELEMÁTICA (BOE 20-04-2011)</td>
      <td>8.5</td>
      <td>8.0</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>316</th>
      <td>5051</td>
      <td>120.0</td>
      <td>8.500000</td>
      <td>2018-19</td>
      <td>8.0</td>
      <td>9.00</td>
      <td>8.54</td>
      <td>GRADO EN INGENIERÍA TELEMÁTICA (BOE 20-04-2011)</td>
      <td>9.0</td>
      <td>8.1</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>317</th>
      <td>5051</td>
      <td>138.0</td>
      <td>7.391304</td>
      <td>2018-19</td>
      <td>3.0</td>
      <td>7.40</td>
      <td>8.42</td>
      <td>GRADO EN INGENIERÍA TELEMÁTICA (BOE 20-04-2011)</td>
      <td>NaN</td>
      <td>5.7</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>318 rows × 28 columns</p>
</div>



- La variable `MEDIA` es la nota media sobre 10 del alumno, ponderada por los créditos de cada asignatura.
- Las variables que contienen `PAU` corresponden a lo obtenido por el alumno en el examen de acceso a la universidad, en particular `NOTA_PAU_CALIFICACION` es la nota media sobre 10.

Realizad una exploración del fichero de datos, obteniendo el número de registros para cada variable, si tienen datos faltantes, indicadores como su máximo, mínimo, etc.


```python
# Completar aquí, exploración del conjunto

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
      <th>NOTA_PAU_FISICA</th>
      <th>NOTA_PAU_MATEMATICAS II</th>
      <th>NOTA_PAU_CALIFICACION</th>
      <th>NOTA_FUNDAMENTOS DE PROGRAMACIÓN</th>
      <th>NOTA_ONDAS ELECTROMAGNÉTICAS</th>
      <th>NOTA_SISTEMAS Y CIRCUITOS</th>
      <th>NOTA_TEORÍA DE LA COMUNICACIÓN</th>
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
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>318.000000</td>
      <td>318.000000</td>
      <td>318.000000</td>
      <td>275.000000</td>
      <td>301.000000</td>
      <td>313.000000</td>
      <td>277.000000</td>
      <td>290.000000</td>
      <td>284.000000</td>
      <td>291.000000</td>
      <td>...</td>
      <td>284.000000</td>
      <td>291.000000</td>
      <td>277.000000</td>
      <td>290.000000</td>
      <td>284.000000</td>
      <td>291.000000</td>
      <td>277.000000</td>
      <td>290.000000</td>
      <td>284.000000</td>
      <td>291.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5045.937107</td>
      <td>186.251572</td>
      <td>7.170736</td>
      <td>5.907200</td>
      <td>6.494651</td>
      <td>7.456965</td>
      <td>7.453069</td>
      <td>6.094138</td>
      <td>6.253873</td>
      <td>6.589347</td>
      <td>...</td>
      <td>1.359155</td>
      <td>1.597938</td>
      <td>1.675090</td>
      <td>2.710345</td>
      <td>1.623239</td>
      <td>1.817869</td>
      <td>2.036101</td>
      <td>3.893103</td>
      <td>2.154930</td>
      <td>2.783505</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.007484</td>
      <td>36.566817</td>
      <td>0.649487</td>
      <td>2.245361</td>
      <td>2.346454</td>
      <td>1.090931</td>
      <td>1.561180</td>
      <td>0.958228</td>
      <td>1.230740</td>
      <td>1.138627</td>
      <td>...</td>
      <td>0.604360</td>
      <td>0.850879</td>
      <td>1.363018</td>
      <td>1.954207</td>
      <td>1.281406</td>
      <td>1.435206</td>
      <td>1.880139</td>
      <td>2.753850</td>
      <td>1.717899</td>
      <td>2.344002</td>
    </tr>
    <tr>
      <th>min</th>
      <td>5041.000000</td>
      <td>120.000000</td>
      <td>5.908046</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>5.180000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>...</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5041.000000</td>
      <td>156.000000</td>
      <td>6.705398</td>
      <td>4.100000</td>
      <td>5.000000</td>
      <td>6.610000</td>
      <td>6.100000</td>
      <td>5.425000</td>
      <td>5.200000</td>
      <td>5.700000</td>
      <td>...</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5041.000000</td>
      <td>192.000000</td>
      <td>7.037259</td>
      <td>6.280000</td>
      <td>6.530000</td>
      <td>7.540000</td>
      <td>7.500000</td>
      <td>5.950000</td>
      <td>5.900000</td>
      <td>6.400000</td>
      <td>...</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5051.000000</td>
      <td>221.000000</td>
      <td>7.487365</td>
      <td>7.600000</td>
      <td>8.500000</td>
      <td>8.210000</td>
      <td>8.800000</td>
      <td>6.500000</td>
      <td>7.000000</td>
      <td>7.300000</td>
      <td>...</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>5.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5051.000000</td>
      <td>244.000000</td>
      <td>9.559259</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>9.740000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>9.800000</td>
      <td>...</td>
      <td>4.000000</td>
      <td>5.000000</td>
      <td>11.000000</td>
      <td>10.000000</td>
      <td>11.000000</td>
      <td>10.000000</td>
      <td>12.000000</td>
      <td>15.000000</td>
      <td>11.000000</td>
      <td>13.000000</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 26 columns</p>
</div>



## Primer paso: modelo simplificado

Vamos a empezar con un modelo simplificado donde sólo consideramos en cuanto a perfiles de ingreso, la nota  PAU. 

### Representación gráfica
Obtened una gráfica de la nota media en el grado en función de la calificación PAU


```python
# Completar aquí

# --------------------

```




    (5.0, 10.0)




    
![png](01-regresion_lineal_output_files/01-regresion_lineal_output_6_1.png)
    


### Ajuste de una recta, usando el algoritmo de gradiente


En esta parte, vamos a ajustar una recta para intentar explicar la nota media en función del ranking del alumno en la  PAU. Aunque, sea mucho (muchísimo!) más sencillo usar `LinearRegression` de `scikit-learn` para realizar el ajuste, implementaremos el algoritmo del gradiente para ir encontrando el mínimo de la función coste. 

Lo haremos en varias etapas...

#### Implementación de la función coste.

Recordar que la función coste es (ver transparencias):
$$J(\theta)=\frac{1}{n}\sum_{i=1}^n\left(y_i-x_{i\bullet}^T\theta\right)^2=\frac{1}{n}\lvert\lvert \mathbf{y}-\mathbf{X}\theta\rvert\rvert^2=\frac{1}{n}\left(\mathbf{y}-\mathbf{X}\theta\right)^T\cdot \left(\mathbf{y}-\mathbf{X}\theta\right),$$
donde $\mathbf{y}$ es el vector que contiene todas las observaciones de la variable respuesta, y la matriz $\mathbf{X}$ la matriz de diseño. La matriz de diseño contiene los valores de las características que queremos tener en cuenta en nuestro modelo para todos los individuos y una columna de 1.

Definir el array de numpy `y` que contenga los valores de MEDIA, y el array `X` que sea la matriz de diseño asociada a la fórmula: 

$$MEDIA=\theta_0+\theta_1 NOTA\_PAU\_CALIFICACION$$
pero habiendo, en primer lugar, quitado las filas que tienen un dato faltante en alguna de estas dos columnas

Para definir `X`, habrá que usar `np.concatenate`, y `np.ones` tal como está explicado en las transparencias del tema.



```python
# Completar aquí

# --------------------
print(f'10 primeros valores de y: \n {y[:10]}')
print(f'10 primeras filas de X:\n {X[:10, :]}')
```

    10 primeros valores de y: 
     [8.81089744 7.47297297 8.05131579 8.67364865 7.425      8.04539474
     6.53690476 9.07039474 6.87152778 9.08881579]
    10 primeras filas de X:
     [[1.   9.34]
     [1.   7.43]
     [1.   8.1 ]
     [1.   9.15]
     [1.   7.97]
     [1.   9.27]
     [1.   7.92]
     [1.   9.66]
     [1.   7.83]
     [1.   9.09]]


Podemos ahora definir la función coste, que se llamará `J`  y que admita los parámetros `theta`, `X` e `y`.


```python
# Completar aquí

# --------------------
J(np.array([1, 1]), X, y)
```




    2.42367700597077



El gradiente de la función coste se puede escribir de manera compacta (ver transparencias) 
$$\nabla J(\theta)=\frac{2}{n} \mathbf{X}^T\cdot \left(\mathbf{X}\theta-y\right).$$
Pasamos a definirla también con el nombre `gradJ`


```python
# Completar aquí

# --------------------
gradJ(np.array([1, 1]), X, y)
```




    array([ 2.56988768, 20.70162311])



#### Implementación del algoritmo del gradiente

Una vez que tenemos implementada la función de coste y su gradiente, podemos escribir el código para el algoritmo iterativo del gradiente.

Empezamos por fijar un valor inicial de theta, el valor de $\alpha$, el learning rate y también el número máximo de iteraciones que autorizaremos para el algoritmo.





```python
theta_inicial = np.array([1, 1])
alpha = 0.001
iteraciones =  3000
```

Usando un bucle implementad el algoritmo del gradiente usando la fórmula de actualización, a cada etapa:
$$\theta\leftarrow \theta-\alpha \nabla J(\theta).$$



```python
# Completar aquí

# --------------------
theta
```




    array([1.39062093, 0.76660468])



### Debemos monitorizar el algoritmo del gradiente

Para comprobar cómo evoluciona el algoritmo del gradiente y en particular, si hemos escogido bien el valor de $\alpha$, es importante comprobar la evolución del valor de la función coste con las iteraciones.

Para ello vamos a introducir un DataFrame llamado monitor, que recoja los valores de `alpha`, `theta`, `J(theta, X, y)` y `gradJ(theta, X, y)` a medida que vamos iterando el algoritmo. 

Empezamos por definir dos funciones que faciliten el manipular el dataframe monitor:
- la primera función `inicializa_monitor` que devuelve un dataframe preparado con las columnas necesarias y con el tipo apropiado.
- la segunda función `inserta_en_monitor`, que añade a `monitor` una fila con los valores de iteracion, alpha, theta y el coste.


```python
# Nada que completar pero sí entender el código
def inicializa_monitor():
    monitor = pd.DataFrame(
        {
            'alpha': float(), 
            'theta_0': float(), 
            'theta_1': float(), 
            'coste': float()
        }, 
        index=[]
    )
    return monitor
# ------------------------------------------------------------------------------------------------------
def inserta_en_monitor(monitor, iteracion, alpha, theta, coste):
    fila = pd.DataFrame(
         {
             'alpha': alpha, 
             'theta_0': theta[0], 
             'theta_1': theta[1], 
             'coste': coste
        }, 
        index=[iteracion]
    )
    return pd.concat([monitor,fila])


```

Tenéis ahora que aprovechar vuestra implementación del algoritmo del gradiente para crear una nueva función `buscar_optimo_gradiente` que admita los siguientes parámetros:
- theta_inicial: un vector `numpy` de valores para los componentes de theta_inicial 
- coste: la función de coste definida, que tome como parámetro theta
- gradiente: la función que calcule el gradiente de la función de coste
- alpha: el paso escogido para cada iteración  
- iteraciones: el número total de iteraciones que se realiza hasta parar y devolver el óptimo
- monitor: el dataframe que contiene la evolución de las cantidades de interés durante la iteración.
Tendrá que devolver un tupla que contenga theta, el valor final de theta encontrado, y el dataframe monitor


```python
# Completar aquí: Definir buscar_optimo_gradiente

# --------------------
monitor = inicializa_monitor()
theta, monitor = buscar_optimo_gradiente(
    theta_inicial,
    coste=J,
    gradiente=gradJ,
    iteraciones=iteraciones,
    alpha=0.001,
    monitor=monitor
)
print(f'El valor final de theta es {theta}')
print(f'El dataframe monitor es: {monitor}')

```

    El valor final de theta es [1.39062093 0.76660468]
    El dataframe monitor es:       alpha   theta_0   theta_1     coste
    0     0.001  1.000000  1.000000  2.423677
    1     0.001  0.997430  0.979298  2.013654
    2     0.001  0.995174  0.960986  1.692905
    3     0.001  0.993196  0.944788  1.441989
    4     0.001  0.991463  0.930459  1.245703
    ...     ...       ...       ...       ...
    2995  0.001  1.389972  0.766690  0.482535
    2996  0.001  1.390102  0.766673  0.482518
    2997  0.001  1.390232  0.766656  0.482501
    2998  0.001  1.390361  0.766639  0.482484
    2999  0.001  1.390491  0.766622  0.482467
    
    [3000 rows x 4 columns]



Podemos ahora representar gráficamente la evolución de la función coste en función de la iteración del algoritmo:


```python
# Completar aquí

# --------------------

```




    [<matplotlib.lines.Line2D at 0x127aae770>]




    
![png](01-regresion_lineal_output_files/01-regresion_lineal_output_22_1.png)
    


Observamos un decrecimiento brusco de la función coste en las primeras iteraciones pero después parece decrecer muy lentamente. Quiere decir que hemos alcanzado el mínimo muy rápidamente?

Para comprobarlo, tenéis que representar la evolución del coste pero entre la iteración 50 y la iteración 3000:


```python
# Completar aquí

# --------------------

```


    
![png](01-regresion_lineal_output_files/01-regresion_lineal_output_24_0.png)
    


#### Variamos el learning rate.

Vimos que era recomendable probar con distintos valores de $\alpha$. Concretamente, vamos a probar para empezar los valores 
       $$\alpha=0.001\curvearrowright 0.003\curvearrowright0.01$$


Añadir a vuestro algoritmo de gradiente que registraba la evolución en el dataframe monitor, un bucle adicional para explorar estos valores de $\alpha$.


```python
# Completar aquí

# --------------------
monitor
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
      <th>alpha</th>
      <th>theta_0</th>
      <th>theta_1</th>
      <th>coste</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.001</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.423677</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.001</td>
      <td>0.997430</td>
      <td>0.979298</td>
      <td>2.013654</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.001</td>
      <td>0.995174</td>
      <td>0.960986</td>
      <td>1.692905</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.001</td>
      <td>0.993196</td>
      <td>0.944788</td>
      <td>1.441989</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.001</td>
      <td>0.991463</td>
      <td>0.930459</td>
      <td>1.245703</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2995</th>
      <td>0.010</td>
      <td>3.505063</td>
      <td>0.488875</td>
      <td>0.296841</td>
    </tr>
    <tr>
      <th>2996</th>
      <td>0.010</td>
      <td>3.505492</td>
      <td>0.488818</td>
      <td>0.296822</td>
    </tr>
    <tr>
      <th>2997</th>
      <td>0.010</td>
      <td>3.505920</td>
      <td>0.488762</td>
      <td>0.296804</td>
    </tr>
    <tr>
      <th>2998</th>
      <td>0.010</td>
      <td>3.506349</td>
      <td>0.488706</td>
      <td>0.296785</td>
    </tr>
    <tr>
      <th>2999</th>
      <td>0.010</td>
      <td>3.506777</td>
      <td>0.488650</td>
      <td>0.296767</td>
    </tr>
  </tbody>
</table>
<p>9000 rows × 4 columns</p>
</div>



Ahora vamos a representar solamente para iter superior a 50, tres líneas de evolución de J en función de la iteración, una para cada valor de $\alpha$.


```python
# Completar aquí

# --------------------

```


    
![png](01-regresion_lineal_output_files/01-regresion_lineal_output_28_0.png)
    


Nos queda probar con `alpha` igual a 0.03 por ejemplo, pero usaremos menos iteraciones, solamente 30.


```python
# Completar aquí

# --------------------
fig, ax = plt.subplots()
ax.plot(monitor.index, monitor['coste']);
```


    
![png](01-regresion_lineal_output_files/01-regresion_lineal_output_30_0.png)
    


#### Parámetros finales
Vamos por lo tanto a quedarnos con alpha=0.01, pero aumentamos el número de iteraciones, por ejemplo a 30000


```python
# Completar aquí

# --------------------
print(f'Nuestra estimación de la ordenada al origen es {theta[0]:.2f} mientras que la pendiente es {theta[1]:.2f}')
```

    Nuestra estimación de la ordenada al origen es 4.55 mientras que la pendiente es 0.35


Queremos representar la hipótesis, es decir el modelo con el que nos quedaríamos. Para ello, podréis usar `axline` de `matplotlib` (ver [referencia](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axline.html#matplotlib.axes.Axes.axline))


```python
# Completar aquí

# --------------------

```


    
![png](01-regresion_lineal_output_files/01-regresion_lineal_output_34_0.png)
    

