print('Pedir el día, mes y año de una fecha correcta y mostrar la fecha del día siguiente. \n Suponer que todos los meses tienen 30 días. ')

dia = int(input('Ingrese el día: '))
mes = int(input('Ingrese el mes: '))
year = int(input('Ingrese el año: '))

if (dia >= 1 & dia <= 30) & (mes >= 1 & mes <= 12) & (year > 0):
    dia = dia +  1
    if dia > 30:
        dia = 1
        mes = mes + 1
    if mes > 12:
        mes = 1
        year = year + 1
    print('La fecha del día siguiente es: ', dia, '/', mes, '/', year)
else:
    print('Fecha incorrecta')
