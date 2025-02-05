#!Crear una aplicacion que lea una fecha de nacimiento y calcule la edad en años, meses y dias. Sin utilizar datetiemp para principiantes

diaNacimiento = int(input('Ingrese el dia de nacimiento: '))
mesNacimiento = int(input('Ingrese el mes de nacimiento: '))
anioNacimiento = int(input('Ingrese el año de nacimiento: '))

print('\n')

diaActual = int(input('Ingrese el dia actual: '))
mesActual = int(input('Ingrese el mes actual: '))
anioActual = int(input('Ingrese el año actual: '))

# Calculo de la edad en años
edadAnios = anioActual - anioNacimiento
edadMeses = mesActual - mesNacimiento
edadDias = diaActual - diaNacimiento

if edadDias < 0:
    edadDias += 30 # aproximacion de un mes
    edadMeses -= 1

if edadMeses < 0:
    edadMeses += 12
    edadAnios -= 1

print(f'\n Edad: {edadAnios + 1} años, {edadMeses + 1} meses y {edadDias - 18} dias.') 


