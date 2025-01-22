print (' Crear una aplicación que tras leer 2 valores cumpla las siguientes condiciones. \n 1.- Si son los números iguales que los sume. \n 2.- Si el primer valor es mayor al segundo que realice una resta. \n 3.- Si el segundo es mayor al primer valor que realice una multiplicación. Realiza el pseudocódigo o algoritmo y diagrama de flujo para su solución.')

valor1 = int(input('Ingrese el primer valor: '))
valor2 = int(input('Ingrese el segundo valor: '))
if valor1 == valor2:
    print('La suma de los valores es: ', valor1 + valor2)
elif valor1 > valor2:
    print('La resta de los valores es: ', valor1 - valor2)
else:
    print('La multiplicación de los valores es: ', valor1 * valor2)

