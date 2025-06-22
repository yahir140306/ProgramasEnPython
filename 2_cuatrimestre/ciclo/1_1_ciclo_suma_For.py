print('Se requiere una aplicación para obtener la suma de diez cantidades mediante la utilización de un ciclo.')

suma = 0

for i in range(10):
    suma = suma + int(input(f'Ingrese el número {i + 1}: '))

print(f'La suma de los números ingresados es: {suma}')
