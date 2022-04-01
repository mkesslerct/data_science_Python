# Concatenar DataFrames con pandas
Cargar el archivo `mompean.csv` en un DataFrame llamado `mompean`. Indicar que la columna `FechaHora` es de tipo `Datetime` y usarla como `index` del DataFrame.



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



Añadir a `mompean` dos columnas que contengan el día de la semana y la hora correspondiente a cada medición. Para ello, podréis usar las dos propiedades `dayofweek` y `hour` que se pueden aplicar a un `Datetimeindex`. 


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
      <th>O3</th>
      <th>NOX</th>
      <th>PM10</th>
      <th>Ruido</th>
      <th>dia_semana</th>
      <th>hora</th>
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
      <td>4</td>
      <td>0</td>
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
      <td>4</td>
      <td>1</td>
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
      <td>4</td>
      <td>2</td>
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
      <td>4</td>
      <td>3</td>
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
      <td>4</td>
      <td>4</td>
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
      <td>1</td>
      <td>19</td>
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
      <td>1</td>
      <td>20</td>
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
      <td>1</td>
      <td>21</td>
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
      <td>1</td>
      <td>22</td>
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
      <td>1</td>
      <td>23</td>
    </tr>
  </tbody>
</table>
<p>96408 rows × 9 columns</p>
</div>



Seleccionar los valores correspondientes a Domingo a las 12 de la mañana en un dataframe y calcular las medias de sus columnas


```python
# Completar aquí

# --------------------

```




    NO             6.971319
    NO2           17.288719
    SO2            7.856874
    O3            70.305556
    NOX           27.862333
    PM10          22.290566
    Ruido         60.154696
    dia_semana     6.000000
    hora          12.000000
    dtype: float64



Qué tipo de objeto es el resultado? Transformadlo en un DataFrame de una fila y 10 columnas. 


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
      <th>O3</th>
      <th>NOX</th>
      <th>PM10</th>
      <th>Ruido</th>
      <th>dia_semana</th>
      <th>hora</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6.971319</td>
      <td>17.288719</td>
      <td>7.856874</td>
      <td>70.305556</td>
      <td>27.862333</td>
      <td>22.290566</td>
      <td>60.154696</td>
      <td>6.0</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>



Escribid un bucle que calcule para cada hora y día de la semana, el valor promedio de los distintos niveles de los indicadores de calidad del aire de `mompean` y que los vaya uniendo en un DataFrame


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
      <th>O3</th>
      <th>NOX</th>
      <th>PM10</th>
      <th>Ruido</th>
      <th>dia_semana</th>
      <th>hora</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.562380</td>
      <td>25.581574</td>
      <td>7.512287</td>
      <td>55.924303</td>
      <td>37.084453</td>
      <td>22.472486</td>
      <td>57.027624</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>6.180077</td>
      <td>23.312261</td>
      <td>7.435606</td>
      <td>53.521912</td>
      <td>32.668582</td>
      <td>20.853890</td>
      <td>55.419890</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>5.517241</td>
      <td>21.136015</td>
      <td>7.361742</td>
      <td>51.169323</td>
      <td>29.501916</td>
      <td>20.206831</td>
      <td>53.508287</td>
      <td>0.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>4.126437</td>
      <td>17.105364</td>
      <td>7.229167</td>
      <td>50.878486</td>
      <td>23.373563</td>
      <td>18.842505</td>
      <td>52.569061</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>3.624521</td>
      <td>14.111111</td>
      <td>7.143939</td>
      <td>50.537849</td>
      <td>19.616858</td>
      <td>17.838710</td>
      <td>51.806630</td>
      <td>0.0</td>
      <td>4.0</td>
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
    </tr>
    <tr>
      <th>0</th>
      <td>5.676245</td>
      <td>18.860153</td>
      <td>8.581132</td>
      <td>77.117296</td>
      <td>27.421456</td>
      <td>22.644612</td>
      <td>60.044199</td>
      <td>6.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>6.545977</td>
      <td>20.641762</td>
      <td>8.330189</td>
      <td>73.753479</td>
      <td>30.588123</td>
      <td>22.718336</td>
      <td>60.364641</td>
      <td>6.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.767754</td>
      <td>23.921305</td>
      <td>7.835539</td>
      <td>68.711155</td>
      <td>35.700576</td>
      <td>23.905303</td>
      <td>60.569061</td>
      <td>6.0</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.694818</td>
      <td>26.278311</td>
      <td>7.667297</td>
      <td>63.896414</td>
      <td>39.462572</td>
      <td>23.990512</td>
      <td>59.972376</td>
      <td>6.0</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>9.168906</td>
      <td>27.220729</td>
      <td>7.655955</td>
      <td>59.272908</td>
      <td>41.084453</td>
      <td>23.339658</td>
      <td>58.375691</td>
      <td>6.0</td>
      <td>23.0</td>
    </tr>
  </tbody>
</table>
<p>168 rows × 9 columns</p>
</div>



El realizar un bucle que lleva a cabo un `concat` en cada iteración tal como se ha hecho anteriormente no es recomendable porque `concat` crea cada vez una copia nueva del DataFrame lo que no es nada óptimo en cuanto a rendimiento. Es mejor construir un iterable con todos los DataFrames, y luego usar `concat` solo una vez sobre el iterable. 

Usando una "list comprehension", construir una lista que contenga todos los DataFrame relevantes del apartado anterior (medias para cada hora y día de la semana). A continuación concatenarlos para obtener el DataFrame del apartado anterior


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
      <th>O3</th>
      <th>NOX</th>
      <th>PM10</th>
      <th>Ruido</th>
      <th>dia_semana</th>
      <th>hora</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>7.562380</td>
      <td>25.581574</td>
      <td>7.512287</td>
      <td>55.924303</td>
      <td>37.084453</td>
      <td>22.472486</td>
      <td>57.027624</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>6.180077</td>
      <td>23.312261</td>
      <td>7.435606</td>
      <td>53.521912</td>
      <td>32.668582</td>
      <td>20.853890</td>
      <td>55.419890</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>5.517241</td>
      <td>21.136015</td>
      <td>7.361742</td>
      <td>51.169323</td>
      <td>29.501916</td>
      <td>20.206831</td>
      <td>53.508287</td>
      <td>0.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>4.126437</td>
      <td>17.105364</td>
      <td>7.229167</td>
      <td>50.878486</td>
      <td>23.373563</td>
      <td>18.842505</td>
      <td>52.569061</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>3.624521</td>
      <td>14.111111</td>
      <td>7.143939</td>
      <td>50.537849</td>
      <td>19.616858</td>
      <td>17.838710</td>
      <td>51.806630</td>
      <td>0.0</td>
      <td>4.0</td>
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
    </tr>
    <tr>
      <th>0</th>
      <td>5.676245</td>
      <td>18.860153</td>
      <td>8.581132</td>
      <td>77.117296</td>
      <td>27.421456</td>
      <td>22.644612</td>
      <td>60.044199</td>
      <td>6.0</td>
      <td>19.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>6.545977</td>
      <td>20.641762</td>
      <td>8.330189</td>
      <td>73.753479</td>
      <td>30.588123</td>
      <td>22.718336</td>
      <td>60.364641</td>
      <td>6.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>7.767754</td>
      <td>23.921305</td>
      <td>7.835539</td>
      <td>68.711155</td>
      <td>35.700576</td>
      <td>23.905303</td>
      <td>60.569061</td>
      <td>6.0</td>
      <td>21.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>8.694818</td>
      <td>26.278311</td>
      <td>7.667297</td>
      <td>63.896414</td>
      <td>39.462572</td>
      <td>23.990512</td>
      <td>59.972376</td>
      <td>6.0</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>9.168906</td>
      <td>27.220729</td>
      <td>7.655955</td>
      <td>59.272908</td>
      <td>41.084453</td>
      <td>23.339658</td>
      <td>58.375691</td>
      <td>6.0</td>
      <td>23.0</td>
    </tr>
  </tbody>
</table>
<p>168 rows × 9 columns</p>
</div>


