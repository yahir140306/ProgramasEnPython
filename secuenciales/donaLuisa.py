print('Cuantos metros mide su hijo.')

PIES = 0.3048
PULGADAS = 0.0254

pies = float(input('Ingrese la cantidad en pies: '))
pulgadas = float(input('Ingrese la cantidad en pulgadas: '))

# metrosPies = pies * PIES
# metrosPulgadas = pulgadas * PULGADAS

pies += pies * PIES
pulgadas += pulgadas - PULGADAS

mide = pies + pulgadas

print(f'Mide: {mide} metros.')
