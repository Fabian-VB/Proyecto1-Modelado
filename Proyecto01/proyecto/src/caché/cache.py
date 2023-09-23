import time
from functools import lru_cache
@lru_cache
def tiempo(var=0, var2=0):
    'Metodo para crear el tiempo en el que se va a realizar una tarea y va a imprimir el tiempo'
    time.sleep(2)
    return var+var2

comienza =time.time()
print(tiempo(10,20))
print(tiempo(10,20))
tiempo.cache_clear()
print(tiempo(10,20))
print(tiempo.cache_info())
print(f'Tiempo total {time.time()-comienza}')