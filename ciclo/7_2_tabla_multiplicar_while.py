print('Crear un programa el cual imprima las tablas de multiplicar del 1 al 10.')

tabla = 1
while tabla < 11:
    print(f'\nTabla del {tabla}')
    multiplicador = 1
    while multiplicador < 11:
        print(f'{tabla} x {multiplicador} = {tabla * multiplicador}')
        multiplicador += 1
    tabla += 1


