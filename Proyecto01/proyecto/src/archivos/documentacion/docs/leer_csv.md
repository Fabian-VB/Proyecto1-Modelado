# Documentación del Archivo CSV

Este módulo se encarga de leer un archivo CSV que contiene datos sobre lugares de origen y destino. Luego, procesa y almacena estos datos en variables.

## Función `leer_csv`

### Descripción

La función `leer_csv` se encarga de leer un archivo CSV y extraer información relevante de él, como lugares de origen y destino, y las coordenadas geográficas correspondientes.

### Parámetros

- `ruta` (str): La ruta del archivo CSV que se va a leer.

### Ejemplo de Uso

```python
import csv

ruta = '/ruta/al/archivo.csv'
leer_csv(ruta)

