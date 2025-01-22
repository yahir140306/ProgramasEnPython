print('Pedir el día, mes y año de una fecha correcta y mostrar la fecha del día siguiente. Suponer que todos los meses tienen 30 días. ')

dia = int(input('Ingrese el día: '))
mes = int(input('Ingrese el mes: '))
year = int(input('Ingrese el año: '))

if dia == 30 and mes == 12:
    dia = 1
    mes = 1
    year += 1
elif dia == 30:
    dia = 1
    mes += 1
else:
    dia += 1

print('La fecha del día siguiente es: ', dia, '/', mes, '/', year)
