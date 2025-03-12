# usando switch - match 
print('Pedir un numero de 1 al 10 y mostrando escrito. \n')

numero = int(input('Ingrese un numero de 1 al 10: '))

match numero:
    case 1:
        print('Uno')
    case 2:
        print('Dos')
    case 3:
        print('Tres')
    case 4:
        print('Cuatro')
    case 5:
        print('Cinco')
    case 6:
        print('Seis')
    case 7:
        print('Siete')
    case 8:
        print('Ocho')
    case 9:
        print('Nueve')
    case 10:
        print('Diez')
    case _:
        print('Numero no valido')