print('Costo del boleto, basado en kilometros y costo por kilometro.')

kilometros = float(input('Ingrese los kilometros: '))
costoKilometro = float(input('Ingrese el valor por kilometro: '))

costoBoleto = kilometros * costoKilometro

print(f'El boleto cuesta: {costoBoleto}')