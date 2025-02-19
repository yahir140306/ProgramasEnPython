import threading
import time
import sched
import timeit


## !Timer con threading.Timer (Temporizador simple)
def mostrar_mensaje():
    print("¡Tiempo cumplido!")


## Crear un temporizador que ejecuta `mostrar_mensaje` después de 5 segundos
temporizador = threading.Timer(5.0, mostrar_mensaje)

## Iniciar el temporizador
temporizador.start()


## !Timer con time.sleep() (Pausas en la ejecución)
print("Esperando 3 segundos...")
time.sleep(3)
print("¡Tiempo cumplido!")

##! Timer con sched.scheduler (Tareas programadas)
# Crear un programador
scheduler = sched.scheduler(time.time, time.sleep)


def tarea():
    print("¡Ejecutando tarea programada!")


# Programar tarea después de 4 segundos
scheduler.enter(4, 1, tarea)
scheduler.run()

##! Timer con timeit (Para medir tiempos de ejecución)

codigo = """
suma = 0
for i in range(1000000):
    suma += i
"""

# Medir el tiempo de ejecución del código
tiempo = timeit.timeit(codigo, number=1)
print(f"Tiempo de ejecución: {tiempo:.5f} segundos")
