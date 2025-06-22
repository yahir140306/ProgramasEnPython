print('Productor de leche.')

litros = float(input('Ingrese los litros: '))
precioGalon = float(input('Ingrese el precio por galon: '))

conversion = litros / 3.785
produccion = conversion * precioGalon

print (f'Produccion de un dia: {produccion}')