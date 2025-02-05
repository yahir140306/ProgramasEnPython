print('Se requiere una aplicación para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita variables cantidades de dinero; además, se requiere saber cuánto lleva ahorrado cada mes.')

# while
print('Con ciclo while: ')
ahorroTotal = 0
i = 0
while i < 12:
    ahorro = float(input(f'Ingrese la cantidad de dinero ahorrada en el mes {i + 1}: '))
    ahorroTotal = ahorroTotal + ahorro
    print(f'El ahorro total hasta el mes {i + 1} es: {ahorroTotal}')
    i = i + 1
print(f'El ahorro total al final del año es: {ahorroTotal}')
