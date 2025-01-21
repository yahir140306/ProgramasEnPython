print(' “El náufrago satisfecho” ofrece hamburguesas sencillas, dobles y triples, las cuales tienen un costo de $20.00, $25.00 y $28.00 respectivamente. La empresa acepta tarjetas de crédito con un cargo de 5 % sobre la compra. Suponiendo que los clientes adquieren sólo un tipo de hamburguesa, realice la aplicación y diagrama de flujo para determinar cuánto debe pagar una persona por N hamburguesas.')

tiposHamburgesas = int(input('Ingrese el número de hamburguesas: '))
costo = 0

cantidadHambuguesas = int(input('Ingrese el número de hamburguesas: '))

tarjeta = input('¿Paga con tarjeta? (S/N): ')

if cantidadHambuguesas == 1:
    costo = 20
elif cantidadHambuguesas == 2:
    costo = 25
elif cantidadHambuguesas == 3:
    costo = 28
else:
    print('El número de hamburguesas no es válido')
    exit()

totalSinCargo = cantidadHambuguesas * costo
cargo = totalSinCargo * 0.05
total = totalSinCargo + cargo

Si tarjeta == 'S':
    print(f'El total a pagar es de ${total}')
else:
    print(f'El total a pagar es de ${totalSinCargo}')
