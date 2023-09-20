import requests, csv, os
from leer_csv import *
'Programa para proporcionar el clima de diferentes ciudades'

if os.path.isfile("llave_api.txt"):
    with open("llave_api.txt", "r") as archivo: #Llave proporcionada de OpenWeather.
        api_key = archivo.read().strip() #Lee la llave y elimina espacios en blanco
else:
    api_key = 'TU_LLAVE_API' #Si no se encuentra el archivo, usa la llave predeterminada

url="http://api.openweathermap.org/data/2.5/weather?"   #url de OpenWeather para ingresar a los climas.
ciudad = input("Ingresa la ciudad de origen: ") #El usuario ingresa las ciudades que desea ver.
"Toma la ciudad proporcionada por el usuario y con ayuda de la api y url busca los datos pedidos."
completa_url = url + "appid=" + api_key + "&q=" + ciudad
res = requests.get(completa_url)
datos_ciudad1 = res.json()

def clima_ciudades_origen():
  'Método que va a funcionar a traves de la condicional para que pueda imprimir en la pantalla las ciudades de destino'
  if datos_ciudad1["cod"] != "404":
    kelvin=273.15 #Se cres una variable para convertir kelvin a celsius
    guarda_datos_ciudad1 = datos_ciudad1["main"] #Se crea una variable para guardar los datos de la ciudad que se escribió en la terminal
    temperatura = int(guarda_datos_ciudad1["temp"]-kelvin) #Se crea una variable donde realiza la conversion a grados
    presion = guarda_datos_ciudad1["pressure"] #Se crea una variable para guardar la presion atmosferica de la ciudad
    humedad = guarda_datos_ciudad1["humidity"] #Se crea una variable para guardar la humedad de la ciudad
    datos_clima_1 = datos_ciudad1["weather"] #Se crea una variable para guardar el clima que hay en esa ciudad
    descripcion = datos_clima_1[0]["description"] #Se crea una variable para guardar los descripcion del clima
    #Muestra en consola los datos de la ciudad de destino ingresada por el usuario e imprime las variables anteriores
    print("Ciudad de origen:")
    print(" Temperatura(Celsius) = " + str(temperatura) + "\n Presion atmosferica= " + str(presion) +
          "\n Humedad(en porcentaje) = " + str(humedad) + "\n Descripcion = " + str(descripcion) +
          "\n Latitud = " + origen_latitud + "\n Longitud = " +origen_longitud)
  else:
    print(" No se encontro la ciudad ")