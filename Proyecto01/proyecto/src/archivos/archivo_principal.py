import climage, csv, ciudad_dataset_destino, ciudades_dataset_origen
from hora import *

def imagen_terminal():
    'Metodo que va a imprimir la imagen en la terminal'
    ruta='/Users/Fa/Downloads/Proyecto1-Modelado/Proyecto01/proyecto/src/archivos/imagen_pantalla/imagenes.jpg' #ruta donde esta ubicada la foto
    imagen =climage.convert(ruta) #Se crea una variable para la imagen que va a imprimir
    print(imagen) #imprime la imagen

'Clase que va imprimir todos los datos de los archivos anteriores'
imagen_terminal() #metodo que va aimprimir la imagen
ciudades_dataset_origen.clima_ciudades_origen() #metodo que esta ubicado en la carpeta ciudades_dataset_origen
print('--------------------------------------------------') #imprime una linea para que no se confunda el texto
ciudad_dataset_destino.clima_ciudades_destino() #metodo que esta ubicado en la carpeta ciudades_dataset_destino