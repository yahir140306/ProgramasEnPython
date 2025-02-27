print('P**3 Q**4 - 2 * P < 680 \n')

valorP = float(input('Ingrese valor P: '))
valorQ = float(input('Ingrese valor Q: '))

resultado = (valorP ** 3) * (valorQ ** 4) - 2 * valorP

if resultado < 680: 
    print(f'Valor P: {valorP} \nValor Q: {valorQ}')
