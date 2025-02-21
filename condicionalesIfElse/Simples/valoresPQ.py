print('p**3 q**4 - 2 * p < 680')

valorP = float(input('Ingrese valor P: '))
valorQ = float(input('Ingrese valor Q: '))

resultado = (valorP ** 3) * (valorQ ** 4) - 2 * valorP

if resultado < 680: 
    print(f'Valor P: {valorP} \n ValorQ: {valorQ}')
