# Unir DataFrames con `merge` en pandas
En este trabajo nos basaremos en el ejemplo `nycflights13` del libro 'R for Data Science' de Gareth Grolemund y Hadley Wickham, disponible en línea en https://r4ds.had.co.nz/ o en soporte papel en la editorial O'Reilly (2017).

En su capítulo 13, 'Relational data', usa el [ejemplo](https://r4ds.had.co.nz/relational-data.html#nycflights13-relational) del conjunto de datos de los vuelos que salen de algún aeropuerto de Nueva York en 2013, junto con las condiciones atmosféricas del vuelo. Permiten por ejemplo investigar los retrasos y sus posibles causas.

Consideraremos los cuatros dataframes con relaciones descritas en el siguiente esquema: 



```python
from IPython import display
display.Image('https://multimediarepository.blob.core.windows.net/imagecontainer/caa2fe0f172f4e81abe11c3a52dcab6d.png')
# Imagen de 'R for Data science', capítulo 13, G. Grelemund y H. Wickham, https://r4ds.had.co.nz/
```




    
![png](02-merge_output_files/02-merge_output_1_0.png)
    



El objetivo es conseguir completar el DataFrame `flights` en un DataFrame llamado `flights_extended` que contenga todos las variables de las tablas de metainformación sobre aviones, compañias, condiciones meteorólicas, aeropuertos. 

Indicar en este bloque de texto qué tipo de `merge` usaréis para unir cada tabla con la tabla `flights` para completarla.

- `flights` con `airports`: 
- `flights` con `airplane`: 
- `flights` con `carrier`: 
- `flights` con  `weather`:

Cuál es el número de filas que esperáis para el DataFrame resultante `flights_extended`?

Cargar los ficheros en formato  `feather` con la instrucción `read_feather` de `pandas` correspondientes a `flights`, `airports`,  `planes`,  `airlines`, y `weather`.



```python
# Completar aquí

# --------------------

```

Construir el DataFrame `flights_extended` secuencialmente, cambiando los nombres de columnas cuando es oportuno, uniendo `flights` con  `airports`,  `planes`,  `airlines`, y `weather`.


```python
# Completar aquí: construir flights_aiports que contenga el merge de flights con airports tanto para origin como para destination

# --------------------
flights_airports
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
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>dep_time</th>
      <th>sched_dep_time</th>
      <th>dep_delay</th>
      <th>arr_time</th>
      <th>sched_arr_time</th>
      <th>arr_delay</th>
      <th>carrier</th>
      <th>...</th>
      <th>dst_origin</th>
      <th>tzone_origin</th>
      <th>faa_dest</th>
      <th>name_dest</th>
      <th>lat_dest</th>
      <th>lon_dest</th>
      <th>alt_dest</th>
      <th>tz_dest</th>
      <th>dst_dest</th>
      <th>tzone_dest</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>517.0</td>
      <td>515</td>
      <td>2.0</td>
      <td>830.0</td>
      <td>819</td>
      <td>11.0</td>
      <td>UA</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>IAH</td>
      <td>George Bush Intercontinental</td>
      <td>29.984433</td>
      <td>-95.341442</td>
      <td>97.0</td>
      <td>-6.0</td>
      <td>A</td>
      <td>America/Chicago</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>533.0</td>
      <td>529</td>
      <td>4.0</td>
      <td>850.0</td>
      <td>830</td>
      <td>20.0</td>
      <td>UA</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>IAH</td>
      <td>George Bush Intercontinental</td>
      <td>29.984433</td>
      <td>-95.341442</td>
      <td>97.0</td>
      <td>-6.0</td>
      <td>A</td>
      <td>America/Chicago</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>542.0</td>
      <td>540</td>
      <td>2.0</td>
      <td>923.0</td>
      <td>850</td>
      <td>33.0</td>
      <td>AA</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>MIA</td>
      <td>Miami Intl</td>
      <td>25.793250</td>
      <td>-80.290556</td>
      <td>8.0</td>
      <td>-5.0</td>
      <td>A</td>
      <td>America/New_York</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>544.0</td>
      <td>545</td>
      <td>-1.0</td>
      <td>1004.0</td>
      <td>1022</td>
      <td>-18.0</td>
      <td>B6</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>554.0</td>
      <td>600</td>
      <td>-6.0</td>
      <td>812.0</td>
      <td>837</td>
      <td>-25.0</td>
      <td>DL</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>ATL</td>
      <td>Hartsfield Jackson Atlanta Intl</td>
      <td>33.636719</td>
      <td>-84.428067</td>
      <td>1026.0</td>
      <td>-5.0</td>
      <td>A</td>
      <td>America/New_York</td>
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
      <th>336771</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>1455</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1634</td>
      <td>NaN</td>
      <td>9E</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>DCA</td>
      <td>Ronald Reagan Washington Natl</td>
      <td>38.852083</td>
      <td>-77.037722</td>
      <td>15.0</td>
      <td>-5.0</td>
      <td>A</td>
      <td>America/New_York</td>
    </tr>
    <tr>
      <th>336772</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>2200</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2312</td>
      <td>NaN</td>
      <td>9E</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>SYR</td>
      <td>Syracuse Hancock Intl</td>
      <td>43.111187</td>
      <td>-76.106311</td>
      <td>421.0</td>
      <td>-5.0</td>
      <td>A</td>
      <td>America/New_York</td>
    </tr>
    <tr>
      <th>336773</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>1210</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1330</td>
      <td>NaN</td>
      <td>MQ</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>BNA</td>
      <td>Nashville Intl</td>
      <td>36.124472</td>
      <td>-86.678194</td>
      <td>599.0</td>
      <td>-6.0</td>
      <td>A</td>
      <td>America/Chicago</td>
    </tr>
    <tr>
      <th>336774</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>1159</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1344</td>
      <td>NaN</td>
      <td>MQ</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>CLE</td>
      <td>Cleveland Hopkins Intl</td>
      <td>41.411689</td>
      <td>-81.849794</td>
      <td>791.0</td>
      <td>-5.0</td>
      <td>A</td>
      <td>America/New_York</td>
    </tr>
    <tr>
      <th>336775</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>840</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1020</td>
      <td>NaN</td>
      <td>MQ</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>RDU</td>
      <td>Raleigh Durham Intl</td>
      <td>35.877639</td>
      <td>-78.787472</td>
      <td>435.0</td>
      <td>-5.0</td>
      <td>A</td>
      <td>America/New_York</td>
    </tr>
  </tbody>
</table>
<p>336776 rows × 35 columns</p>
</div>




```python
# Completar aquí: comprobad las columnas de flights_airports

# --------------------

```

    Index(['year', 'month', 'day', 'dep_time', 'sched_dep_time', 'dep_delay',
           'arr_time', 'sched_arr_time', 'arr_delay', 'carrier', 'flight',
           'tailnum', 'origin', 'dest', 'air_time', 'distance', 'hour', 'minute',
           'time_hour', 'faa_origin', 'name_origin', 'lat_origin', 'lon_origin',
           'alt_origin', 'tz_origin', 'dst_origin', 'tzone_origin', 'faa_dest',
           'name_dest', 'lat_dest', 'lon_dest', 'alt_dest', 'tz_dest', 'dst_dest',
           'tzone_dest'],
          dtype='object')



```python
# Completar aquí: construir flights_aiports_planes_airlines que contenga el merge de flights_airports con planes y airlinesdestination

# --------------------
flights_airports_planes_airlines
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
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>dep_time</th>
      <th>sched_dep_time</th>
      <th>dep_delay</th>
      <th>arr_time</th>
      <th>sched_arr_time</th>
      <th>arr_delay</th>
      <th>carrier</th>
      <th>...</th>
      <th>dst_dest</th>
      <th>tzone_dest</th>
      <th>type</th>
      <th>manufacturer</th>
      <th>model</th>
      <th>engines</th>
      <th>seats</th>
      <th>speed</th>
      <th>engine</th>
      <th>name_carrier</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>517.0</td>
      <td>515</td>
      <td>2.0</td>
      <td>830.0</td>
      <td>819</td>
      <td>11.0</td>
      <td>UA</td>
      <td>...</td>
      <td>A</td>
      <td>America/Chicago</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Air Lines Inc.</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>533.0</td>
      <td>529</td>
      <td>4.0</td>
      <td>850.0</td>
      <td>830</td>
      <td>20.0</td>
      <td>UA</td>
      <td>...</td>
      <td>A</td>
      <td>America/Chicago</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>United Air Lines Inc.</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>542.0</td>
      <td>540</td>
      <td>2.0</td>
      <td>923.0</td>
      <td>850</td>
      <td>33.0</td>
      <td>AA</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>American Airlines Inc.</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>544.0</td>
      <td>545</td>
      <td>-1.0</td>
      <td>1004.0</td>
      <td>1022</td>
      <td>-18.0</td>
      <td>B6</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>JetBlue Airways</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>554.0</td>
      <td>600</td>
      <td>-6.0</td>
      <td>812.0</td>
      <td>837</td>
      <td>-25.0</td>
      <td>DL</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Delta Air Lines Inc.</td>
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
      <th>336771</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>1455</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1634</td>
      <td>NaN</td>
      <td>9E</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Endeavor Air Inc.</td>
    </tr>
    <tr>
      <th>336772</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>2200</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2312</td>
      <td>NaN</td>
      <td>9E</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Endeavor Air Inc.</td>
    </tr>
    <tr>
      <th>336773</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>1210</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1330</td>
      <td>NaN</td>
      <td>MQ</td>
      <td>...</td>
      <td>A</td>
      <td>America/Chicago</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Envoy Air</td>
    </tr>
    <tr>
      <th>336774</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>1159</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1344</td>
      <td>NaN</td>
      <td>MQ</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Envoy Air</td>
    </tr>
    <tr>
      <th>336775</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>840</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1020</td>
      <td>NaN</td>
      <td>MQ</td>
      <td>...</td>
      <td>A</td>
      <td>America/New_York</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Envoy Air</td>
    </tr>
  </tbody>
</table>
<p>336776 rows × 43 columns</p>
</div>




```python
# Completar aquí: comprobad las columnas de fligths_airports_planes_airlines

# --------------------

```

    Index(['year', 'month', 'day', 'dep_time', 'sched_dep_time', 'dep_delay',
           'arr_time', 'sched_arr_time', 'arr_delay', 'carrier', 'flight',
           'tailnum', 'origin', 'dest', 'air_time', 'distance', 'hour', 'minute',
           'time_hour', 'faa_origin', 'name_origin', 'lat_origin', 'lon_origin',
           'alt_origin', 'tz_origin', 'dst_origin', 'tzone_origin', 'faa_dest',
           'name_dest', 'lat_dest', 'lon_dest', 'alt_dest', 'tz_dest', 'dst_dest',
           'tzone_dest', 'type', 'manufacturer', 'model', 'engines', 'seats',
           'speed', 'engine', 'name_carrier'],
          dtype='object')


Finalmente, construid `flights_extended` que contenga también la información meteorológica en el aeropuerto de origen


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
      <th>year</th>
      <th>month</th>
      <th>day</th>
      <th>dep_time</th>
      <th>sched_dep_time</th>
      <th>dep_delay</th>
      <th>arr_time</th>
      <th>sched_arr_time</th>
      <th>arr_delay</th>
      <th>carrier</th>
      <th>...</th>
      <th>name_carrier</th>
      <th>temp</th>
      <th>dewp</th>
      <th>humid</th>
      <th>wind_dir</th>
      <th>wind_speed</th>
      <th>wind_gust</th>
      <th>precip</th>
      <th>pressure</th>
      <th>visib</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>517.0</td>
      <td>515</td>
      <td>2.0</td>
      <td>830.0</td>
      <td>819</td>
      <td>11.0</td>
      <td>UA</td>
      <td>...</td>
      <td>United Air Lines Inc.</td>
      <td>39.02</td>
      <td>28.04</td>
      <td>64.43</td>
      <td>260.0</td>
      <td>12.65858</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1011.9</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>533.0</td>
      <td>529</td>
      <td>4.0</td>
      <td>850.0</td>
      <td>830</td>
      <td>20.0</td>
      <td>UA</td>
      <td>...</td>
      <td>United Air Lines Inc.</td>
      <td>39.92</td>
      <td>24.98</td>
      <td>54.81</td>
      <td>250.0</td>
      <td>14.96014</td>
      <td>21.86482</td>
      <td>0.0</td>
      <td>1011.4</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>542.0</td>
      <td>540</td>
      <td>2.0</td>
      <td>923.0</td>
      <td>850</td>
      <td>33.0</td>
      <td>AA</td>
      <td>...</td>
      <td>American Airlines Inc.</td>
      <td>39.02</td>
      <td>26.96</td>
      <td>61.63</td>
      <td>260.0</td>
      <td>14.96014</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1012.1</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>544.0</td>
      <td>545</td>
      <td>-1.0</td>
      <td>1004.0</td>
      <td>1022</td>
      <td>-18.0</td>
      <td>B6</td>
      <td>...</td>
      <td>JetBlue Airways</td>
      <td>39.02</td>
      <td>26.96</td>
      <td>61.63</td>
      <td>260.0</td>
      <td>14.96014</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1012.1</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2013</td>
      <td>1</td>
      <td>1</td>
      <td>554.0</td>
      <td>600</td>
      <td>-6.0</td>
      <td>812.0</td>
      <td>837</td>
      <td>-25.0</td>
      <td>DL</td>
      <td>...</td>
      <td>Delta Air Lines Inc.</td>
      <td>39.92</td>
      <td>24.98</td>
      <td>54.81</td>
      <td>260.0</td>
      <td>16.11092</td>
      <td>23.01560</td>
      <td>0.0</td>
      <td>1011.7</td>
      <td>10.0</td>
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
      <th>336771</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>1455</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1634</td>
      <td>NaN</td>
      <td>9E</td>
      <td>...</td>
      <td>Endeavor Air Inc.</td>
      <td>68.00</td>
      <td>55.04</td>
      <td>63.21</td>
      <td>190.0</td>
      <td>11.50780</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1016.6</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>336772</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>2200</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2312</td>
      <td>NaN</td>
      <td>9E</td>
      <td>...</td>
      <td>Endeavor Air Inc.</td>
      <td>64.94</td>
      <td>53.06</td>
      <td>65.37</td>
      <td>200.0</td>
      <td>6.90468</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1015.8</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>336773</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>1210</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1330</td>
      <td>NaN</td>
      <td>MQ</td>
      <td>...</td>
      <td>Envoy Air</td>
      <td>69.08</td>
      <td>48.02</td>
      <td>46.99</td>
      <td>70.0</td>
      <td>5.75390</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1016.7</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>336774</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>1159</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1344</td>
      <td>NaN</td>
      <td>MQ</td>
      <td>...</td>
      <td>Envoy Air</td>
      <td>66.92</td>
      <td>48.92</td>
      <td>52.35</td>
      <td>70.0</td>
      <td>8.05546</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1017.5</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>336775</th>
      <td>2013</td>
      <td>9</td>
      <td>30</td>
      <td>NaN</td>
      <td>840</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1020</td>
      <td>NaN</td>
      <td>MQ</td>
      <td>...</td>
      <td>Envoy Air</td>
      <td>60.98</td>
      <td>51.08</td>
      <td>69.86</td>
      <td>NaN</td>
      <td>5.75390</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1018.6</td>
      <td>10.0</td>
    </tr>
  </tbody>
</table>
<p>336776 rows × 52 columns</p>
</div>




```python
# Completar aquí: comprobad las columnas

# --------------------

```

    Index(['year', 'month', 'day', 'dep_time', 'sched_dep_time', 'dep_delay',
           'arr_time', 'sched_arr_time', 'arr_delay', 'carrier', 'flight',
           'tailnum', 'origin', 'dest', 'air_time', 'distance', 'hour', 'minute',
           'time_hour', 'faa_origin', 'name_origin', 'lat_origin', 'lon_origin',
           'alt_origin', 'tz_origin', 'dst_origin', 'tzone_origin', 'faa_dest',
           'name_dest', 'lat_dest', 'lon_dest', 'alt_dest', 'tz_dest', 'dst_dest',
           'tzone_dest', 'type', 'manufacturer', 'model', 'engines', 'seats',
           'speed', 'engine', 'name_carrier', 'temp', 'dewp', 'humid', 'wind_dir',
           'wind_speed', 'wind_gust', 'precip', 'pressure', 'visib'],
          dtype='object')



```python
# Completar aquí: comprobad la dimensión de flights_extended

# --------------------

```




    (336776, 52)


