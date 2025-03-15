print('Crear una aplicacion que lea un numero e indique si es un numero primo. \n ')

numero = int(input('Ingrese un numero: '))

if (numero <= 1):
    print (f'{numero} - No es primo')

for i in range(numero):
    if numero % i == 0:
        print(f'{numero} - No es primo')
    
    print(f'{numero} - Si es primo')