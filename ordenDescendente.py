print(
    "\n Ordenar 3 numeros dados de manera descendente, utilizando solo condicionales. \n "
)

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
numero3 = int(input("Numero 3: "))

if numero1 >= numero2 and numero1 >= numero3:
    if numero2 >= numero3:
        # print(f'Orden: {numero1}, {numero2}, {numero3}')
        # print(f'Orden: {numero3}, {numero2}, {numero1}')
        menor, medio, mayor = numero3, numero2, numero1

    else:
        # print(f'Orden: {numero1}, {numero3}, {numero2}') mayor a menor
        # print(f'Orden: {numero2}, {numero3}, {numero1}') menor a mayor
        menor, medio, mayor = numero2, numero3, numero1

elif numero2 >= numero1 and numero2 >= numero3:
    if numero1 >= numero3:
        # print(f'Orden: {numero2}, {numero1}, {numero3}')
        # print(f'Orden: {numero3}, {numero1}, {numero2}')
        menor, medio, mayor = numero3, numero1, numero2

    else:
        # print(f'Orden: {numero2}, {numero3}, {numero1}')
        # print(f'Orden: {numero1}, {numero3}, {numero2}')
        menor, medio, mayor = numero1, numero3, numero2


else:
    if numero1 >= numero2:
        # print(f'Orden: {numero3}, {numero1}, {numero2}')
        # print(f'Orden: {numero2}, {numero1}, {numero3}')
        menor, medio, mayor = numero2, numero1, numero3

    else:
        # print(f'Orden: {numero3}, {numero2}, {numero1}')
        # print(f'Orden: {numero1}, {numero2}, {numero3}')
        menor, medio, mayor = numero1, numero2, numero3


print(f"\n Orden: {menor}, {medio}, {mayor}")
