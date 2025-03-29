print(
    "Almacenes “El harapiento distinguido” tiene una promoción: a todos los trajes que tienen un precio superior a $2500.00 se les aplicará un descuento de 15 %, a todos los demás se les aplicará sólo 8 %. Realice la aplicación y el diagrama de flujo para determinar el precio final que debe pagar una persona por comprar un traje y de cuánto es el descuento que obtendrá. \n"
)

precioTraje = float(input("Ingrese el precio del traje: "))
descuento = 0

if precioTraje > 2500:
    descuento = 0.15

else:
    descuento = 0.08

precioFinal = precioTraje - (precioTraje * descuento)
descuento = precioTraje * descuento

print(
    f"El precio final del traje es de ${precioFinal} y el descuento aplicado es de ${descuento}"
)
