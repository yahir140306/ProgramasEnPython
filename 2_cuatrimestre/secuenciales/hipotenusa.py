import math

print('Calcular la hipotenusa.')

catetoA = float(input('Ingrese cateto A: '))
catetoB = float(input('Ingrese cateto B: '))

hipotenusa = math.sqrt((catetoA ** 2 + catetoB ** 2 ))

print(f'Hipotenusa es: {hipotenusa}')