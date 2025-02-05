print('Se requiere una aplicación para obtener la suma de diez cantidades mediante la utilización de un ciclo.')

# ahora que sea con while

suma = 0
i = 0
while i < 10:
    suma = suma + int(input(f'Ingrese el número {i + 1}: '))
    i = i + 1
print(f'La suma de los números ingresados es: {suma}')

