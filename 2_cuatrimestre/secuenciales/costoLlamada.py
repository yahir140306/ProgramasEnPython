print('Costo de la llamada, tiempo por el costo por minuto.')

tiempoLlamada = float(input('Ingrese el tiempo de la llamada en minutos:' ))
costoMinuto = float(input('Ingrese el valor por minuto: '))
costoTotal = tiempoLlamada * costoMinuto

print(f'El costo de la llamada: {costoTotal}')