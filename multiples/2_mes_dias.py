print('Crear una aplicacion tras pedir el nombre del mes, imprima cuantos dias tiene dicho mes. \n')

mes = input('Ingrese el nombre del mes: ')
mes = mes.lower()

match mes:
    case 'enero' | 'marzo' | 'mayo' | 'julio' | 'agosto' | 'octubre' | 'diciembre':
        print(f'{mes.capitalize()} tiene 31 dias.')
    case 'abril' | 'junio' | 'septiembre' | 'noviembre':
        print(f'{mes.capitalize()} tiene 30 dias.')
    case 'febrero':
        print(f'{mes.capitalize()} tiene 28 o 29 dias.')
    case _:
        print('Mes no valido')