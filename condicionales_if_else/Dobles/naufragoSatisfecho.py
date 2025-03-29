print(
    "“El náufrago satisfecho” ofrece hamburguesas sencillas, dobles y triples, las cuales tienen un costo de $20.00, $25.00 y $28.00 respectivamente. La empresa acepta tarjetas de crédito con un cargo de 5% sobre la compra. Suponiendo que los clientes adquieren sólo un tipo de hamburguesa, realice la aplicación y diagrama de flujo para determinar cuánto debe pagar una persona por N hamburguesas."
)

tipoHamburguesa = int(input("Ingrese el tipo de hamburguesa (1, 2 o 3): "))
hamburguesas = int(input("Ingrese el número de hamburguesas: "))
tarjeta = input("¿Desea pagar con tarjeta de crédito? (s/n): ")
precio = 0

if tipoHamburguesa == 1:
    precio = 20 * hamburguesas
elif tipoHamburguesa == 2:
    precio = 25 * hamburguesas
elif tipoHamburguesa == 3:
    precio = 28 * hamburguesas
else:
    print("Tipo de hamburguesa no válido")

if tarjeta == "s":
    precio += precio * 0.05

print(f"El total a pagar es de ${precio}")