print('Crear un programa el cual imprima las tablas de multiplicar del 1 al 10.')

for tabla in range(1, 11):
    print(f'\nTabla del {tabla}')
    for multiplicador in range(1, 11):
        print(f'{tabla} x {multiplicador} = {tabla * multiplicador}')
    
print('\nFin del programa')
