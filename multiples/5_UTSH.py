print('Crear una aplicación en la que se muestre un menú con el nombre de las carreras de la Universidad Tecnológica de la Sierra Hidalguense, el usuario podrá elegir una carrera y debe mostrar un mensaje que diga el nombre del director encargado de esa área \n')

carreras = ['Tecnologias de la Información y Comunicación areas Sistemas Informáticos', 'Tecnologias de la Información y Comunicación areas Redes y Telecomunicaciones', 'Mecatrónica', 'Terapia Física']

directores = ['Ing. José Luis Hernández Pérez', 'Ing. José Luis Hernández Pérez', 'Ing. José Luis Hernández Pérez', 'Ing. José Luis Hernández Pérez']

palaras = 'El director de la carrera de '

print('Carreras de la Universidad Tecnológica de la Sierra Hidalguense:')
print(f'1. {carreras[0]}')
print(f'2. {carreras[1]}')
print(f'3. {carreras[2]}')
print(f'4. {carreras[3]}')


carrera = int(input('\nElija una carrera de la Universidad Tecnológica de la Sierra Hidalguense: '))

match carrera:
    case 1:
        print(f'{palaras} {carreras[0]} es {directores[0]}')
    case 2:
        print(f'{palaras} {carreras[1]} es {directores[1]}')
    case 3:
        print(f'{palaras} {carreras[2]} es {directores[2]}')
    case 4:
        print(f'{palaras} {carreras[3]} es {directores[3]}')
    case _:
        print('Carrera no valida')