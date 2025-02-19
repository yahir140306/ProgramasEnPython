import time

print('Simulacion de un reloj, usando el ciclo while y for. Usando timer')

while True:
    horaActual = time.strftime("%H:%M:%S")

    print(f'\r{horaActual}', end='', flush=True)

    time.sleep(1)
