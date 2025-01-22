print('Pedir una hora de la forma hora, minutos ysegundos, y mostrar la hora en el segundo siguiente. ')

hora = int(input('Ingrese la hora: '))
minutos = int(input('Ingrese los minutos: '))
segundos = int(input('Ingrese los segundos: '))

if (hora >= 0 & hora <= 23) & (minutos >= 0 & minutos <= 59) & (segundos >= 0 & segundos <= 59):
    segundos = segundos + 1
    if segundos == 60:
        segundos = 0
        minutos = minutos + 1
    if minutos == 60:
        minutos = 0
        hora = hora + 1
    if hora == 24:
        hora = 0
    print('La hora en el segundo siguiente es: ', hora, ':', minutos, ':', segundos)