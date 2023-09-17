import csv
ruta='/Users/Fa/Desktop/Proyecto01/proyecto/src/archivos/datos_ciudades/dataset1.csv' #ruta donde esta ubicado el archivo
with open(ruta, newline='') as archivo:
  #Permite obtener los datos del archivo csv línea por línea.
  csv_leer= csv.DictReader(archivo)
  """
  Se crean las siguientes varibles para guardar las longitudes y latitudes de los lugares de
  origen y destino, ademas de que este va a funcionar para que lea linea por linea e imprima solo lo que necesite
  """
  for row in csv_leer:
    origen=row['origin']
    destino=row['destination']
    origen_latitud=row['origin_latitude']
    origen_longitud=row['origin_longitude']
    destino_latitud= row['destination_latitude']
    destino_longitud=row['destination_longitude']