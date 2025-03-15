# emplar ciclos, condicionales, acumaldores y contadores

print('Crear una aplicacion que simule las funciones basicas de un cajero automatico, retiros, depositos, ver saldo y salir')

saldo = 0
opcion = 0

while opcion != 4:
    print('1. Depositar')
    print('2. Retirar')
    print('3. Ver saldo')
    print('4. Salir')
    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        deposito = int(input('Ingrese la cantidad a depositar: '))
        saldo += deposito
        print(f'Su saldo actual es: {saldo}')
    elif opcion == 2:
        retiro = int(input('Ingrese la cantidad a retirar: '))
        if retiro > saldo:
            print('Fondos insuficientes')
        else:
            saldo -= retiro
            print(f'Su saldo actual es: {saldo}')
    elif opcion == 3:
        print(f'Su saldo actual es: {saldo}')
    elif opcion == 4:
        print('Gracias por usar nuestros servicios')
    else:
        print('Opcion invalida')

