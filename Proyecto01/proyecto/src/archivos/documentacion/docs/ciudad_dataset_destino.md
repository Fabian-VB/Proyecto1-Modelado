# Programa para proporcionar el clima de diferentes ciudades

Este programa utiliza la API de OpenWeather para proporcionar información sobre el clima de diversas ciudades. El usuario puede ingresar una ciudad de destino y obtener datos como temperatura, presión, humedad, descripción del clima, amanecer y puesta de sol.

## Configuración de la clave API

El programa primero verifica si existe un archivo `llave_api.txt` para obtener la clave API de OpenWeather. Si el archivo no existe, se utiliza una clave API predeterminada.

## Uso

Para utilizar el programa, sigue estos pasos:

1. Ejecuta el programa en tu terminal.
2. Si existe el archivo `llave_api.txt`, la clave API se leerá desde ese archivo. De lo contrario, se utilizará la clave API predeterminada.
3. Ingresa la ciudad de destino cuando se te solicite.
4. El programa consultará la API de OpenWeather y mostrará los datos del clima de la ciudad.

## Funciones

### `clima_ciudades_destino()`

Esta función se encarga de obtener y mostrar los datos del clima de la ciudad de destino ingresada por el usuario. Los datos incluyen temperatura, presión, humedad, descripción del clima, amanecer y puesta de sol.

```python
def clima_ciudades_destino():
    # ...
    # Código de la función clima_ciudades_destino
    # ...


### Ejemplo de Uso

```python
# Importar los módulos
import requests
import hora
import os 
from leer_csv import *
from time import timezone

# Definir api_key, url y ciudad_dest
if os.path.isfile("llave_api.txt"):
    with open("llave_api.txt", "r") as archivo:
        api_key = archivo.read().strip()
else:
    api_key = 'TU_LLAVE_API'
url = "http://api.openweathermap.org/data/2.5/weather?"
ciudad_dest = input("Ingresa la ciudad de destino: ")

# Realizar una solicitud HTTP para obtener los datos del clima
res1 = requests.get(url + "appid=" + api_key + "&q=" + ciudad_dest)
datos_ciudad2 = res1.json()

# Llamar a la función para mostrar el clima de la ciudad de destino
clima_ciudades_destino()
