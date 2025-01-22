print('Crear una aplicación que tras leer un número determine si es positivo o negativo')

numero = int(input('Ingrese un número: '))
if numero > 0:
    print('El número es positivo')
elif numero < 0:
    print('El número es negativo')
else:
    print('El número es cero')
