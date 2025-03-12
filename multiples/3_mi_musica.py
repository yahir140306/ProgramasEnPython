print('Crear un menu en el que muestre por lo menos 5 generos musicales que te agraden, el usuario debe poder elegir uno de ellos y este debe mostrar como minimo 3 interpretes de dicho genero. \n')

genero = input('Ingrese el genero musical que le guste: ')
genero = genero.lower()

match genero:
    case 'rock':
        print('Interpretes de rock:')
        print('1. Led Zeppelin')
        print('2. The Rolling Stones')
        print('3. Pink Floyd')
    case 'pop':
        print('Interpretes de pop:')
        print('1. Michael Jackson')
        print('2. Madonna')
        print('3. Britney Spears')
    case 'electronica':
        print('Interpretes de electronica:')
        print('1. Daft Punk')
        print('2. The Chemical Brothers')
        print('3. Kraftwerk')
    case 'metal':
        print('Interpretes de metal:')
        print('1. Metallica')
        print('2. Iron Maiden')
        print('3. Black Sabbath')
    case 'reggae':
        print('Interpretes de reggae:')
        print('1. Bob Marley')
        print('2. Peter Tosh')
        print('3. Jimmy Cliff')
    case _:
        print('Genero no valido')