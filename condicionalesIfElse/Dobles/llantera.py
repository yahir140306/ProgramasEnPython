print('Calcular el total que una persona debe pagar en una llantera, si el precio de cada llanta es de $800 si se compran menos de 5 llantas y de $700 si se compran 5 o más. Crear la aplicación y el diagrama de flujo para este fin. ')

nuemeroLlantas = int(input('Ingrese el número de llantas: '))
precio = 0

if nuemeroLlantas >= 5:
    precio = 700
else:
    precio = 800

total = nuemeroLlantas * precio
print(f'El total a pagar es de ${total}')
