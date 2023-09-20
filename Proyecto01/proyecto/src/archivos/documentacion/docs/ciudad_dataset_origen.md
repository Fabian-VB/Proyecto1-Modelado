# Documentación del Programa para Obtener el Clima de Ciudades

Este programa permite a los usuarios obtener información sobre el clima de una ciudad de origen. Utiliza la API de OpenWeather para obtener los datos climáticos.

## Configuración de la Clave API

El programa verifica si existe un archivo llamado "llave_api.txt" que contiene una clave API para OpenWeather. Si el archivo existe, se lee la clave API desde el archivo. Si no existe, se utiliza una clave API predeterminada.

## Uso

1. Ejecute el programa en su terminal.
2. Si existe el archivo "llave_api.txt", la clave API se leerá desde ese archivo.
3. Ingrese la ciudad de origen cuando se le solicite.
4. El programa consultará la API de OpenWeather y mostrará los datos climáticos de la ciudad de origen en la consola.

## Función `clima_ciudades_origen()`

Esta función se encarga de procesar los datos climáticos recibidos de la API de OpenWeather y mostrar la información en la consola.

```python
def clima_ciudades_origen():
    # ...
    # Código de la función clima_ciudades_origen
    # ...


### Ejemplo de Uso

```python
# Importar los módulos
import requests
import csv
import os 
from leer_csv import *

# Definir api_key, url y ciudad
if os.path.isfile("llave_api.txt"):
    with open("llave_api.txt", "r") as archivo:
        api_key = archivo.read().strip()
else:
    api_key = 'TU_LLAVE_API'
url = "http://api.openweathermap.org/data/2.5/weather?"
ciudad = input("Ingresa la ciudad de origen: ")

# Realizar una solicitud HTTP para obtener los datos del clima
res = requests.get(url + "appid=" + api_key + "&q=" + ciudad)
datos_ciudad1 = res.json()

# Llamar a la función para mostrar el clima
clima_ciudades_origen()
