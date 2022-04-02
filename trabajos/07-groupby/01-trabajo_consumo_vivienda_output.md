# Trabajo. Análisis exploratorio del consumo eléctrico de una casa

El conjunto de datos que analizaremos en este trabajo  coresponden a mediciones del consumo eléctrico de una vivienda, obtenido de [https://archive.ics.uci.edu/ml/datasets/Individual+household+electric+power+consumption#], el UCI Machine Learning Repository (Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.)

El conjunto de datos inicial es mucho más grande, se ha agregado los valores por hora haciendo promedios, para hacerlo más manejable.

## Primer paso: cargamos los datos
Después de importar los módulos necesarios y definir `DATA_DIRECTORY`, cargar el fichero `household_hourly_power_consumption.txt` en un DataFrame llamado `vivienda`. 


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
      <th>global_active_power</th>
      <th>global_reactive_power</th>
      <th>voltage</th>
      <th>global_intensity</th>
      <th>sub_metering_1</th>
      <th>sub_metering_2</th>
      <th>sub_metering_3</th>
    </tr>
    <tr>
      <th>date_hour</th>
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
      <th>2006-12-16 17:00:00</th>
      <td>4.222889</td>
      <td>0.229000</td>
      <td>234.643889</td>
      <td>18.100000</td>
      <td>0.0</td>
      <td>0.527778</td>
      <td>16.861111</td>
    </tr>
    <tr>
      <th>2006-12-16 18:00:00</th>
      <td>3.632200</td>
      <td>0.080033</td>
      <td>234.580167</td>
      <td>15.600000</td>
      <td>0.0</td>
      <td>6.716667</td>
      <td>16.866667</td>
    </tr>
    <tr>
      <th>2006-12-16 19:00:00</th>
      <td>3.400233</td>
      <td>0.085233</td>
      <td>233.232500</td>
      <td>14.503333</td>
      <td>0.0</td>
      <td>1.433333</td>
      <td>16.683333</td>
    </tr>
    <tr>
      <th>2006-12-16 20:00:00</th>
      <td>3.268567</td>
      <td>0.075100</td>
      <td>234.071500</td>
      <td>13.916667</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>16.783333</td>
    </tr>
    <tr>
      <th>2006-12-16 21:00:00</th>
      <td>3.056467</td>
      <td>0.076667</td>
      <td>237.158667</td>
      <td>13.046667</td>
      <td>0.0</td>
      <td>0.416667</td>
      <td>17.216667</td>
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
      <th>2010-11-26 17:00:00</th>
      <td>1.725900</td>
      <td>0.061400</td>
      <td>237.069667</td>
      <td>7.216667</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>12.866667</td>
    </tr>
    <tr>
      <th>2010-11-26 18:00:00</th>
      <td>1.573467</td>
      <td>0.053700</td>
      <td>237.531833</td>
      <td>6.620000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2010-11-26 19:00:00</th>
      <td>1.659333</td>
      <td>0.060033</td>
      <td>236.741000</td>
      <td>7.056667</td>
      <td>0.0</td>
      <td>0.066667</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2010-11-26 20:00:00</th>
      <td>1.163700</td>
      <td>0.061167</td>
      <td>239.396000</td>
      <td>4.913333</td>
      <td>0.0</td>
      <td>1.066667</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2010-11-26 21:00:00</th>
      <td>0.934667</td>
      <td>0.000000</td>
      <td>239.690000</td>
      <td>3.800000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
  </tbody>
</table>
<p>34589 rows × 7 columns</p>
</div>




```python
vivienda.isna().sum(axis=1).value_counts()
```




    0    34168
    7      421
    dtype: int64



> En el conjunto, las zonas de medición correspondientes a "sub_metering_n" son las siguientes:
- sub_metering_1: cocina
- sub_metering_2: lavadero que tiene lavadora y secadora aparte de un frigorífico
- sub_metering_3: termo eléctrico de ACS y un aire condicionado.

2. Cuál el valor mínimo de la potencia global activa que se puede encontrar en el conjunto?  ¿Cuál es el valor máximo? ¿En qué fechas y hora se dieron?  (Indicación: echad un vistazo a [idxmin](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin) y su hermano `idxmax`.)




```python
# Completar aquí

# --------------------

```

    El valor mínimo de global_active_power es 0.124 en la fecha hora: 2008-08-23 21:00:00
    El valor máximo de global_active_power es 6.56053333333333 en la fecha hora:  2008-11-23 18:00:00


3. Cuál es el valor promedio de la intensidad global en el conjunto?



```python
# Completar aquí

# --------------------

```




    4.628238362989026



## Manipulaciones

### Añadimos una columna *sub_metering_resto*

Las columnas sub_metering_1, sub_metering_2 y sub_metering_3 miden la energía activa en tres zonas de la vivienda. Para calcular la energía activa en el resto de la vivienda, debemos substraerlas de la columna global_active_power, (despúes de multiplicar está última por 60/1000 para pasar de kW por minuto  a W por hora), según la fórmula

> (global_active_power*1000/60 - sub_metering_1 - sub_metering_2 - sub_metering_3) 

Tenéis que añadir esta columna que llamaréis sub_metering_resto al dataframe *vivienda*


```python
# Completar aquí

# --------------------

```

## Explorando el número de datos.




Usando los atributos `year`, `month` del  índice de `vivienda`, y el método `value_counts`, obtened cuántas mediciones tenemos para cada año



```python
# Completar aquí

# --------------------

```




    2006     367
    2007    8760
    2008    8784
    2009    8760
    2010    7918
    Name: date_hour, dtype: int64



Para obtener una tabla de frecuencias del número de datos por año y por mes, podemos usar la función `crosstab` de pandas.


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
      <th>mes</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>11</th>
      <th>12</th>
    </tr>
    <tr>
      <th>año</th>
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
      <th>2006</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>367</td>
    </tr>
    <tr>
      <th>2007</th>
      <td>744</td>
      <td>672</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
    </tr>
    <tr>
      <th>2008</th>
      <td>744</td>
      <td>696</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
    </tr>
    <tr>
      <th>2009</th>
      <td>744</td>
      <td>672</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
    </tr>
    <tr>
      <th>2010</th>
      <td>744</td>
      <td>672</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>744</td>
      <td>720</td>
      <td>744</td>
      <td>622</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## Resumimos por grupos
En esta sección usaremos `groupby` aplicado al índice del DataFrame `vivienda` para obtener distintos resúmenes del consumo energético de la vivienda.

### Perfil de potencia a lo largo del día

Queremos ver para empezar el perfil de potencia global activa medio por hora, es decir para cada hora del día (0 a 23), cuál es el valor promedio de la potencia global activa.


```python
# Completar aquí

# --------------------

```




    date_hour
    0     0.659562
    1     0.539325
    2     0.480618
    3     0.444850
    4     0.443844
    5     0.453674
    6     0.791606
    7     1.502373
    8     1.460940
    9     1.331642
    10    1.260913
    11    1.246408
    12    1.207061
    13    1.144471
    14    1.082750
    15    0.990806
    16    0.948805
    17    1.056164
    18    1.326433
    19    1.733428
    20    1.899073
    21    1.876063
    22    1.412681
    23    0.902142
    Name: global_active_power, dtype: float64



Repetir la instrucción anterior para añadir a la vez la potencia global máxima por hora, el número de datos que han entrado en el cálculo, y la potencia mínima. Guardaréis el resultado en un DataFrame  llamado `perfil_horario_vivienda`.

**NOTA** Para especificar los nombres de las columnas del DataFrame resultado, podéis usar tuplas en `agg` de la forma (nombre_deseado, nombre_de_la_función). Por ejemplo ("potencia_media", "mean")


```python
# Completar aquí

# --------------------
perfil_horario_potencia
 
       
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">global_active_power</th>
    </tr>
    <tr>
      <th></th>
      <th>potencia_media</th>
      <th>potencia_máxima</th>
      <th>número</th>
      <th>potencia_minima</th>
    </tr>
    <tr>
      <th>date_hour</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.659562</td>
      <td>5.155500</td>
      <td>1426</td>
      <td>0.127600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.539325</td>
      <td>5.759067</td>
      <td>1424</td>
      <td>0.144100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.480618</td>
      <td>3.498267</td>
      <td>1424</td>
      <td>0.131500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.444850</td>
      <td>2.847333</td>
      <td>1424</td>
      <td>0.135067</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.443844</td>
      <td>2.992500</td>
      <td>1422</td>
      <td>0.127533</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.453674</td>
      <td>2.910300</td>
      <td>1421</td>
      <td>0.130467</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.791606</td>
      <td>3.590267</td>
      <td>1421</td>
      <td>0.151067</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.502373</td>
      <td>4.416600</td>
      <td>1422</td>
      <td>0.131633</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.460940</td>
      <td>4.418900</td>
      <td>1422</td>
      <td>0.144567</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.331642</td>
      <td>3.716267</td>
      <td>1422</td>
      <td>0.129233</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.260913</td>
      <td>5.161067</td>
      <td>1422</td>
      <td>0.150167</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1.246408</td>
      <td>5.090800</td>
      <td>1422</td>
      <td>0.126600</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1.207061</td>
      <td>5.237267</td>
      <td>1422</td>
      <td>0.138067</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.144471</td>
      <td>4.661500</td>
      <td>1423</td>
      <td>0.137067</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.082750</td>
      <td>4.638200</td>
      <td>1424</td>
      <td>0.134133</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.990806</td>
      <td>5.025133</td>
      <td>1423</td>
      <td>0.132967</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.948805</td>
      <td>5.137800</td>
      <td>1423</td>
      <td>0.126800</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.056164</td>
      <td>6.333667</td>
      <td>1423</td>
      <td>0.127500</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1.326433</td>
      <td>6.560533</td>
      <td>1424</td>
      <td>0.134200</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.733428</td>
      <td>6.496033</td>
      <td>1427</td>
      <td>0.152333</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1.899073</td>
      <td>6.519633</td>
      <td>1427</td>
      <td>0.130967</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1.876063</td>
      <td>6.363867</td>
      <td>1428</td>
      <td>0.124000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1.412681</td>
      <td>5.814267</td>
      <td>1426</td>
      <td>0.145633</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.902142</td>
      <td>5.562467</td>
      <td>1426</td>
      <td>0.132500</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Completar aquí

# --------------------
perfil_horario_potencia
 
       
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
      <th>potencia_media</th>
      <th>potencia_máxima</th>
      <th>número</th>
      <th>potencia_minima</th>
    </tr>
    <tr>
      <th>date_hour</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.659562</td>
      <td>5.155500</td>
      <td>1426</td>
      <td>0.127600</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.539325</td>
      <td>5.759067</td>
      <td>1424</td>
      <td>0.144100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.480618</td>
      <td>3.498267</td>
      <td>1424</td>
      <td>0.131500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.444850</td>
      <td>2.847333</td>
      <td>1424</td>
      <td>0.135067</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.443844</td>
      <td>2.992500</td>
      <td>1422</td>
      <td>0.127533</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.453674</td>
      <td>2.910300</td>
      <td>1421</td>
      <td>0.130467</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.791606</td>
      <td>3.590267</td>
      <td>1421</td>
      <td>0.151067</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1.502373</td>
      <td>4.416600</td>
      <td>1422</td>
      <td>0.131633</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.460940</td>
      <td>4.418900</td>
      <td>1422</td>
      <td>0.144567</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.331642</td>
      <td>3.716267</td>
      <td>1422</td>
      <td>0.129233</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.260913</td>
      <td>5.161067</td>
      <td>1422</td>
      <td>0.150167</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1.246408</td>
      <td>5.090800</td>
      <td>1422</td>
      <td>0.126600</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1.207061</td>
      <td>5.237267</td>
      <td>1422</td>
      <td>0.138067</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1.144471</td>
      <td>4.661500</td>
      <td>1423</td>
      <td>0.137067</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1.082750</td>
      <td>4.638200</td>
      <td>1424</td>
      <td>0.134133</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.990806</td>
      <td>5.025133</td>
      <td>1423</td>
      <td>0.132967</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.948805</td>
      <td>5.137800</td>
      <td>1423</td>
      <td>0.126800</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.056164</td>
      <td>6.333667</td>
      <td>1423</td>
      <td>0.127500</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1.326433</td>
      <td>6.560533</td>
      <td>1424</td>
      <td>0.134200</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1.733428</td>
      <td>6.496033</td>
      <td>1427</td>
      <td>0.152333</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1.899073</td>
      <td>6.519633</td>
      <td>1427</td>
      <td>0.130967</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1.876063</td>
      <td>6.363867</td>
      <td>1428</td>
      <td>0.124000</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1.412681</td>
      <td>5.814267</td>
      <td>1426</td>
      <td>0.145633</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.902142</td>
      <td>5.562467</td>
      <td>1426</td>
      <td>0.132500</td>
    </tr>
  </tbody>
</table>
</div>



## Proporción de potencia correspondiente a la cocina

Empezamos por calcular la suma, por cada fila, de las columnas desde `sub_metering_1` hasta `sub_metering_resto`.


```python
# Completar aquí

# --------------------

```




    date_hour
    2006-12-16 17:00:00    70.381481
    2006-12-16 18:00:00    60.536667
    2006-12-16 19:00:00    56.670556
    2006-12-16 20:00:00    54.476111
    2006-12-16 21:00:00    50.941111
                             ...    
    2010-11-26 17:00:00    28.765000
    2010-11-26 18:00:00    26.224444
    2010-11-26 19:00:00    27.655556
    2010-11-26 20:00:00    19.395000
    2010-11-26 21:00:00    15.577778
    Length: 34589, dtype: float64



A continuación, añadimos al conjunto `vivienda` la columna calculada `prop_cocina` que contenga en porcentaje la proporción de `sub_metering_1` respecto a la suma de las columnas `sub_metering`.



```python
# Completar aquí

# --------------------
vivienda
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
      <th>global_active_power</th>
      <th>global_reactive_power</th>
      <th>voltage</th>
      <th>global_intensity</th>
      <th>sub_metering_1</th>
      <th>sub_metering_2</th>
      <th>sub_metering_3</th>
      <th>sub_metering_resto</th>
      <th>prop_cocina</th>
    </tr>
    <tr>
      <th>date_hour</th>
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
      <th>2006-12-16 17:00:00</th>
      <td>4.222889</td>
      <td>0.229000</td>
      <td>234.643889</td>
      <td>18.100000</td>
      <td>0.0</td>
      <td>0.527778</td>
      <td>16.861111</td>
      <td>52.992593</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-12-16 18:00:00</th>
      <td>3.632200</td>
      <td>0.080033</td>
      <td>234.580167</td>
      <td>15.600000</td>
      <td>0.0</td>
      <td>6.716667</td>
      <td>16.866667</td>
      <td>36.953333</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-12-16 19:00:00</th>
      <td>3.400233</td>
      <td>0.085233</td>
      <td>233.232500</td>
      <td>14.503333</td>
      <td>0.0</td>
      <td>1.433333</td>
      <td>16.683333</td>
      <td>38.553889</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-12-16 20:00:00</th>
      <td>3.268567</td>
      <td>0.075100</td>
      <td>234.071500</td>
      <td>13.916667</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>16.783333</td>
      <td>37.692778</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2006-12-16 21:00:00</th>
      <td>3.056467</td>
      <td>0.076667</td>
      <td>237.158667</td>
      <td>13.046667</td>
      <td>0.0</td>
      <td>0.416667</td>
      <td>17.216667</td>
      <td>33.307778</td>
      <td>0.0</td>
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
      <th>2010-11-26 17:00:00</th>
      <td>1.725900</td>
      <td>0.061400</td>
      <td>237.069667</td>
      <td>7.216667</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>12.866667</td>
      <td>15.898333</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-11-26 18:00:00</th>
      <td>1.573467</td>
      <td>0.053700</td>
      <td>237.531833</td>
      <td>6.620000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>26.224444</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-11-26 19:00:00</th>
      <td>1.659333</td>
      <td>0.060033</td>
      <td>236.741000</td>
      <td>7.056667</td>
      <td>0.0</td>
      <td>0.066667</td>
      <td>0.000000</td>
      <td>27.588889</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-11-26 20:00:00</th>
      <td>1.163700</td>
      <td>0.061167</td>
      <td>239.396000</td>
      <td>4.913333</td>
      <td>0.0</td>
      <td>1.066667</td>
      <td>0.000000</td>
      <td>18.328333</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-11-26 21:00:00</th>
      <td>0.934667</td>
      <td>0.000000</td>
      <td>239.690000</td>
      <td>3.800000</td>
      <td>0.0</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>15.577778</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>34589 rows × 9 columns</p>
</div>



Podemos obtener ahora la evolución horario de la proporción correspondiente a la cocina, con los mismos indicadores que para la potencia global.


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

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="4" halign="left">prop_cocina</th>
    </tr>
    <tr>
      <th></th>
      <th>prop_media</th>
      <th>prop_máxima</th>
      <th>número</th>
      <th>prop_mínima</th>
    </tr>
    <tr>
      <th>date_hour</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.547905</td>
      <td>71.124576</td>
      <td>1426</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.080553</td>
      <td>68.412045</td>
      <td>1424</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.683529</td>
      <td>65.839160</td>
      <td>1424</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.350238</td>
      <td>64.637306</td>
      <td>1424</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.256954</td>
      <td>64.203017</td>
      <td>1422</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.169877</td>
      <td>53.975143</td>
      <td>1421</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.133651</td>
      <td>56.187602</td>
      <td>1421</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.779337</td>
      <td>29.547224</td>
      <td>1422</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3.992971</td>
      <td>66.780186</td>
      <td>1422</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>4.974586</td>
      <td>73.693355</td>
      <td>1422</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3.516382</td>
      <td>79.598486</td>
      <td>1422</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4.078810</td>
      <td>71.855187</td>
      <td>1422</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>4.318073</td>
      <td>72.143172</td>
      <td>1422</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>4.262482</td>
      <td>72.929995</td>
      <td>1423</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>5.048005</td>
      <td>69.486733</td>
      <td>1424</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>5.162795</td>
      <td>74.221737</td>
      <td>1423</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>3.069429</td>
      <td>73.573937</td>
      <td>1423</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1.971908</td>
      <td>73.655449</td>
      <td>1423</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>3.593565</td>
      <td>81.557872</td>
      <td>1424</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>6.106618</td>
      <td>79.113924</td>
      <td>1427</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>6.344438</td>
      <td>73.827255</td>
      <td>1427</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>6.739150</td>
      <td>64.853027</td>
      <td>1428</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>22</th>
      <td>7.374024</td>
      <td>64.523311</td>
      <td>1426</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>4.222714</td>
      <td>76.623910</td>
      <td>1426</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



Queremos añadir como factor de agrupamiento el día de la semana (atributo `weekday` de un objeto `datetime`). Calcular para el agrupamiento, día de la semana, hora, el valor promedio de la proporción correspondiente a la cocina y ordenarlos de mayor a menor. Weekday toma el valor 0 para Lunes y 6 para Domingo. Cuándo se hace más uso de la cocina en esta familia? 



```python
# Completar aquí

# --------------------

```




    date_hour  date_hour
    5          15           12.068463
    6          12           11.794802
               15           10.361347
    5          14           10.335298
    6          11            9.900869
                              ...    
    1          4             0.000000
               5             0.000000
    2          6             0.000000
    4          2             0.000000
    2          5             0.000000
    Name: prop_cocina, Length: 168, dtype: float64


