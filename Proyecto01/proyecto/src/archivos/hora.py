from datetime import datetime

def tiempo_de_puesta_de_sol_amanecer(da_horas):
  'Se crea un metodo para poder crear la hora en que saldra el amanecer o la puesta de sol en la ciudad de destino'
  tiempo_local=datetime.utcfromtimestamp(da_horas) #Se crea una variable para guardar la hora
  return tiempo_local.time() #Regresa el tiempo