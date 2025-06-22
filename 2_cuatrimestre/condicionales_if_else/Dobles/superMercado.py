print('Si en un supermercado el cliente a la hora de pagar muestra una tarjeta cliente le dan un descuento del 5% de lo que compro y si el cliente no tiene tarjeta cliente le dan un descuento del 2%.')

compra = float(input('Ingrese el monto de la compra: '))
tarjeta = input('¿Tiene tarjeta cliente? (S/N): ')

if tarjeta == 'S':
    descuento = compra * 0.05
    total = compra - descuento
    print('El descuento es de: ', descuento)
    print('El total a pagar es: ', total)

elif tarjeta == 'N':
    descuento = compra * 0.02
    total = compra - descuento
    print('El descuento es de: ', descuento)
    print('El total a pagar es: ', total)

else:
    print('Opción incorrecta')

