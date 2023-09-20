import requests, hora, os 
from leer_csv import *
from time import timezone
'Programa para proporcionar el clima de diferentes ciudades'

if os.path.isfile("llave_api.txt"):
    with open("llave_api.txt", "r") as archivo: #Llave proporcionada de OpenWeather.
        api_key = archivo.read().strip() #Lee la llave y elimina espacios en blanco
else:
    api_key = 'TU_LLAVE_API' #Si no se encuentra el archivo, usa la llave predeterminada

url="http://api.openweathermap.org/data/2.5/weather?" #url de OpenWeather para ingresar a los climas.
#El usuario ingresa las ciudades que desea ver a traves de una API que se encuentra en la pagina anterior.
"Toma la ciudad proporcionada por el usuario y con ayuda de la api y url busca los datos pedidos."
ciudad_dest = input("Ingresa la ciudad de destino: ")
completa_url2 = url + "appid=" + api_key + "&q=" + ciudad_dest
res1 = requests.get(completa_url2)
datos_ciudad2 = res1.json()

def clima_ciudades_destino():
        'Método que va a funcionar a traves de la condicional para que pueda imprimir en la pantalla las ciudades de destino'
        if datos_ciudad2["cod"] != "404":
                kelvin=273.15 #Se cres una variable para convertir kelvin a celsius
                guarda_datos = datos_ciudad2["main"] #Se crea una variable para guardar los datos de la ciudad que se escribió en la terminal
                temperatura1 = int(guarda_datos["temp"]-kelvin) #Se crea una variable donde realiza la conversion a grados
                presion1 = guarda_datos["pressure"] #Se crea una variable para guardar la presion atmosferica de la ciudad
                humedad1 = guarda_datos["humidity"] #Se crea una variable para guardar la humedad de la ciudad
                amanecer1=datos_ciudad2['sys']['sunrise'] #Se crea una variable para guardar los datos sobre el amanacer de la ciudad
                puesta1=datos_ciudad2['sys']['sunset'] #Se crea una variable para guardar la puesta de sol de la ciudad
                timezone1=datos_ciudad2['timezone'] #Se crea una variable para guardar la hora sobre las dos anteriores variables
                datos_clima = datos_ciudad2["weather"] #Se crea una variable para guardar el clima que hay en esa ciudad
                descripcion1 = datos_clima[0]["description"] #Se crea una variable para guardar los descripcion del clima
                amanecer_tiempo= hora.tiempo_de_puesta_de_sol_amanecer(amanecer1+timezone1) #Se crea una variable para guardar la hora en el tiempo que saldra el amanecer
                puesta_tiempo= hora.tiempo_de_puesta_de_sol_amanecer(puesta1+timezone1) #Se crea una variable para guardar la hora del puesto de sol
                #Muestra en consola los datos de la ciudad de destino ingresada por el usuario e imprime las variables anteriores
                print("Ciudad de destino:")
                print(" Temperatura(Celsius) = " + str(temperatura1) + "\n Presion atmosferica= " +
                      str(presion1) + "\n Humedad(en porcentaje) = " + str(humedad1) +
                      "\n Descripcion = " + str(descripcion1) + "\n Latitud = " + destino_latitud+ "\n Longitud = " + destino_longitud)
                print(f" Amanecer a las {amanecer_tiempo} y la puesta de sol a las {puesta_tiempo}")
        else:
                print(" No se encontro la ciudad ")