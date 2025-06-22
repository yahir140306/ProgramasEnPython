print('Pedir un numero y calcular su factorial.')

numero = int(input('Introduce un número: '))
factorial = 1

while numero > 0:
    factorial *= numero
    numero -= 1

print(f'El factorial es: {factorial}')