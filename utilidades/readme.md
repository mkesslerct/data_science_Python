# Diferentes utilidades para generar entregables, transparencias etc..
Esta carpeta contiene distintos scripts de utilidades, que uso para generar entregables, o las transparencias HTML a partir de un bloc de notas Jupyter.

## Generar un entregable de trabajo, a partir del bloc de notas Jupyter.

Los enunciados de trabajos entregables consisten siempre de dos elementos:
1. Un bloc de notas de nombre tipo `trabajo_handout.ipynb` donde los alumnos tienen celdas de código vacías o parcialmente vacías si hay alguna indicación. Tienen que entregar este bloc de notas completado.
2. Un fichero html con las salidas esperadas del trabajo, que se llama `trabajo_output.html`. Los alumnos pueden fijarse en estas salidas esperadas para comprobar que obtienen, con su código, lo que se espera.

Para generar estos dos elementos, tengo mi bloc de notas `trabajo.ipynb`, donde en las celdas pongo el código solución, pero precedido por una línea que empieza por `# Completar aquí` y seguido por una línea que empieza por `# Fin Completar aquí`. (Se deben respetar espacios, mayúsculas y tíldes) 
Por ejemplo:
En `trabajo.ipynb` tengo un bloque:
```
# Completar aquí
geyser = pd.read_csv("datos_geyser.csv")
# Fin Completar aquí
geyser
```

que se transformará en `trabajo_handout.ipynb` en
```
# Completar aquí

# ---------------------------
geyser
```

El script que se encarga de generar estos entregables es `generate_handout.py` que admite como argumento la ruta hasta el fichero `ipynb` que hay que procesar.

```
python3 generate_handout.py ../trabajos/trabajo.ipynb
```

> Nota: se debe ejecutar este comanda en un entorno donde esté instalado ipykernel, por ejemplo el base de conda, o el entorno `ids` del curso.
