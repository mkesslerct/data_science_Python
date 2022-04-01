# Manipular filas y columnas de DataFrame en pandas


## Pesos de bebes al nacer, EEUU.

Inspirado por el libro "The art of Statistics, learning from data" by David Spiegelhalter (Pelican, 2020), usaremos datos del "National Center for Health Statistics, USA", que publica conjuntos de datos enormes sobre los pesos al nacer de los bebes en EEUU durante muchos años: https://www.cdc.gov/nchs/data_access/Vitalstatsonline.htm. El conjunto correspondiente a 2019 es un fichero de texto de 5GB que contiene muchas características (columns) potencialmente relevantes para identificar los factores que influyen en el peso al nacer de un bebe en EEUU..

Con el objetivo de facilitar la manipulación de estos datos, se ha preparado un conjunto de datos más simple, con solamente dos columnas:

- `OEGest_R3`, que es el "Obstetric Estimate Recode 3" con tres valores posibles: 1 (Menor de 37 semanas), 2 (37 semanas o más), 3 (Sin registrar) 
- `DBWT`, que es "Birth Weight – Detail in Grams". Un valor de 9999 indica que no se registró el peso al nacer
El fichero es nat2019.csv, que puede encontrar en la carpeta "data" del Aula Virtual. 



Empezad por importar `pandas`, el submódulo `path` de `os` y definir `DATA_DIRECTORY`



```python
# Completar aquí

# --------------------

```

Después de cargar el fichero en un DataFrame llamado `pesos`, contestad a las siguientes preguntas:

1. Cuántas filas tiene el conjunto? 
2. Cuántos bebes nacieron antes de las 37 semanas?
3. Cuántos datos faltantes de peso presenta el conjunto?

Calculad el peso medio de los bebes al nacer en 2019


```python
# Completar aquí

# --------------------

```

    El peso medio de los bebes al nacer en 2019 en EEUU fue 3254.3g.


Calculad el peso medio de los bebes, descartando los que nacieron antes de las 37 semanas.


```python
# Completar aquí

# --------------------

```

    El peso medio de los bebes que nacieron con 37 semanas o más de gestación fue 3361.2g.


Calculad el peso medio de los bebes prematuros (que nacieron antes de las 37 semanas)


```python
# Completar aquí

# --------------------

```

    El peso medio de los bebes prematuros fue 2312.5g.


## Datos de Calidad del Aire, Mompean, Cartagena
Vimos en una práctica anterior el conjunto de datos sobre calidad del aire registrados en la estación de la calle Mompean, a unos metros del Campus de la Muralla de la UPCT. Empezad por cargar los datos en un DataFrame llamado `mompean`, indicando que la columna `FechaHora` es un objeto de tipo DateTime y que la usaremos como `index`.


```python
# Completar aquí

# --------------------
mompean
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
      <th>NO</th>
      <th>NO2</th>
      <th>SO2</th>
      <th>O3</th>
      <th>NOX</th>
      <th>PM10</th>
      <th>Ruido</th>
    </tr>
    <tr>
      <th>FechaHora</th>
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
      <th>2010-01-01 00:00:00</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>5.0</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>2010-01-01 01:00:00</th>
      <td>6.0</td>
      <td>12.0</td>
      <td>18.0</td>
      <td>NaN</td>
      <td>21.0</td>
      <td>15.0</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>2010-01-01 02:00:00</th>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>NaN</td>
      <td>26.0</td>
      <td>12.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>2010-01-01 03:00:00</th>
      <td>5.0</td>
      <td>10.0</td>
      <td>18.0</td>
      <td>NaN</td>
      <td>18.0</td>
      <td>2.0</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>2010-01-01 04:00:00</th>
      <td>4.0</td>
      <td>8.0</td>
      <td>19.0</td>
      <td>NaN</td>
      <td>14.0</td>
      <td>5.0</td>
      <td>55.0</td>
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
    </tr>
    <tr>
      <th>2019-12-31 19:00:00</th>
      <td>9.0</td>
      <td>35.0</td>
      <td>8.0</td>
      <td>47.0</td>
      <td>49.0</td>
      <td>19.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-31 20:00:00</th>
      <td>29.0</td>
      <td>59.0</td>
      <td>9.0</td>
      <td>24.0</td>
      <td>102.0</td>
      <td>41.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-31 21:00:00</th>
      <td>59.0</td>
      <td>65.0</td>
      <td>8.0</td>
      <td>10.0</td>
      <td>155.0</td>
      <td>48.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-31 22:00:00</th>
      <td>51.0</td>
      <td>51.0</td>
      <td>9.0</td>
      <td>11.0</td>
      <td>130.0</td>
      <td>45.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2019-12-31 23:00:00</th>
      <td>32.0</td>
      <td>42.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>90.0</td>
      <td>44.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>96408 rows × 7 columns</p>
</div>



Quedaos con las columnas que tienen como mínimo 88000 valores no faltantes. Llamad el DataFrame resultante `mompean_88K`


```python
# Completar aquí

# --------------------
mompean_88K

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
      <th>NO</th>
      <th>NO2</th>
      <th>SO2</th>
      <th>NOX</th>
      <th>PM10</th>
    </tr>
    <tr>
      <th>FechaHora</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-01 00:00:00</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>17.0</td>
      <td>14.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2010-01-01 01:00:00</th>
      <td>6.0</td>
      <td>12.0</td>
      <td>18.0</td>
      <td>21.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>2010-01-01 02:00:00</th>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>26.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2010-01-01 03:00:00</th>
      <td>5.0</td>
      <td>10.0</td>
      <td>18.0</td>
      <td>18.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-01-01 04:00:00</th>
      <td>4.0</td>
      <td>8.0</td>
      <td>19.0</td>
      <td>14.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2019-12-31 19:00:00</th>
      <td>9.0</td>
      <td>35.0</td>
      <td>8.0</td>
      <td>49.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>2019-12-31 20:00:00</th>
      <td>29.0</td>
      <td>59.0</td>
      <td>9.0</td>
      <td>102.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>2019-12-31 21:00:00</th>
      <td>59.0</td>
      <td>65.0</td>
      <td>8.0</td>
      <td>155.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>2019-12-31 22:00:00</th>
      <td>51.0</td>
      <td>51.0</td>
      <td>9.0</td>
      <td>130.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>2019-12-31 23:00:00</th>
      <td>32.0</td>
      <td>42.0</td>
      <td>9.0</td>
      <td>90.0</td>
      <td>44.0</td>
    </tr>
  </tbody>
</table>
<p>96408 rows × 5 columns</p>
</div>



De este DataFrame, seleccionad, usando `loc`, las filas que no tienen ningún valor faltante


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
      <th>NO</th>
      <th>NO2</th>
      <th>SO2</th>
      <th>NOX</th>
      <th>PM10</th>
    </tr>
    <tr>
      <th>FechaHora</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-01 00:00:00</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>17.0</td>
      <td>14.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2010-01-01 01:00:00</th>
      <td>6.0</td>
      <td>12.0</td>
      <td>18.0</td>
      <td>21.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>2010-01-01 02:00:00</th>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>26.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2010-01-01 03:00:00</th>
      <td>5.0</td>
      <td>10.0</td>
      <td>18.0</td>
      <td>18.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-01-01 04:00:00</th>
      <td>4.0</td>
      <td>8.0</td>
      <td>19.0</td>
      <td>14.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2019-12-31 19:00:00</th>
      <td>9.0</td>
      <td>35.0</td>
      <td>8.0</td>
      <td>49.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>2019-12-31 20:00:00</th>
      <td>29.0</td>
      <td>59.0</td>
      <td>9.0</td>
      <td>102.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>2019-12-31 21:00:00</th>
      <td>59.0</td>
      <td>65.0</td>
      <td>8.0</td>
      <td>155.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>2019-12-31 22:00:00</th>
      <td>51.0</td>
      <td>51.0</td>
      <td>9.0</td>
      <td>130.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>2019-12-31 23:00:00</th>
      <td>32.0</td>
      <td>42.0</td>
      <td>9.0</td>
      <td>90.0</td>
      <td>44.0</td>
    </tr>
  </tbody>
</table>
<p>83888 rows × 5 columns</p>
</div>



Obtener el mismo resultado usando el método `dropna`.


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
      <th>NO</th>
      <th>NO2</th>
      <th>SO2</th>
      <th>NOX</th>
      <th>PM10</th>
    </tr>
    <tr>
      <th>FechaHora</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-01 00:00:00</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>17.0</td>
      <td>14.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>2010-01-01 01:00:00</th>
      <td>6.0</td>
      <td>12.0</td>
      <td>18.0</td>
      <td>21.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>2010-01-01 02:00:00</th>
      <td>6.0</td>
      <td>17.0</td>
      <td>17.0</td>
      <td>26.0</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2010-01-01 03:00:00</th>
      <td>5.0</td>
      <td>10.0</td>
      <td>18.0</td>
      <td>18.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2010-01-01 04:00:00</th>
      <td>4.0</td>
      <td>8.0</td>
      <td>19.0</td>
      <td>14.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2019-12-31 19:00:00</th>
      <td>9.0</td>
      <td>35.0</td>
      <td>8.0</td>
      <td>49.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>2019-12-31 20:00:00</th>
      <td>29.0</td>
      <td>59.0</td>
      <td>9.0</td>
      <td>102.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>2019-12-31 21:00:00</th>
      <td>59.0</td>
      <td>65.0</td>
      <td>8.0</td>
      <td>155.0</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>2019-12-31 22:00:00</th>
      <td>51.0</td>
      <td>51.0</td>
      <td>9.0</td>
      <td>130.0</td>
      <td>45.0</td>
    </tr>
    <tr>
      <th>2019-12-31 23:00:00</th>
      <td>32.0</td>
      <td>42.0</td>
      <td>9.0</td>
      <td>90.0</td>
      <td>44.0</td>
    </tr>
  </tbody>
</table>
<p>83888 rows × 5 columns</p>
</div>



Introducid el DataFrame datos con los siguientes valores


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
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>f1</th>
      <td>1.0</td>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>f2</th>
      <td>NaN</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>f3</th>
      <td>7.0</td>
      <td>-1.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>f4</th>
      <td>2.0</td>
      <td>-5.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>f5</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Sustituid los valores faltantes de la columna `x` por la mediana de sus valores


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
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>f1</th>
      <td>1.0</td>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>f2</th>
      <td>2.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>f3</th>
      <td>7.0</td>
      <td>-1.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>f4</th>
      <td>2.0</td>
      <td>-5.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>f5</th>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Escribid una función `sustituye_NaN` que coja un Series como argumento y sustituya sus valores faltantes por la mediana de sus valores


```python
# Completar aquí

# --------------------
sustituye_NaN(datos['y'])
```




    f1   -1.0
    f2    0.0
    f3   -1.0
    f4   -5.0
    f5   -1.0
    Name: y, dtype: float64



Usad el método  `apply` (ver [referencia](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)), para sustituir en cada columna de datos los valores faltantes por la mediana de los valores de esa columna.


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
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>f1</th>
      <td>1.0</td>
      <td>-1.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>f2</th>
      <td>2.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>f3</th>
      <td>7.0</td>
      <td>-1.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>f4</th>
      <td>2.0</td>
      <td>-5.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>f5</th>
      <td>2.0</td>
      <td>-1.0</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>



Sustituid los valores del cuadrado superior izquierda de tamaño 2x2 por 10, 11, 12, 13:


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
      <th>x</th>
      <th>y</th>
      <th>z</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>f1</th>
      <td>10.0</td>
      <td>11.0</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>f2</th>
      <td>12.0</td>
      <td>13.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>f3</th>
      <td>7.0</td>
      <td>-1.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>f4</th>
      <td>2.0</td>
      <td>-5.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>f5</th>
      <td>2.0</td>
      <td>-1.0</td>
      <td>6.0</td>
    </tr>
  </tbody>
</table>
</div>


