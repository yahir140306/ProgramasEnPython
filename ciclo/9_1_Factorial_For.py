print('Pedir un numero y calcular su factorial.')

numero = int(input('Introduce un número: '))
factorial = 1

for i in range(1, numero + 1):
    factorial *= i

print(f'El factorial de {numero} es: {factorial}')