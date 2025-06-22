print('Realice un diagrama de flujo y el programa que calcule \n pagara finalmente una persona por articulo equis, \n considerando que tiene un descuento de 20%, y debe pagar 15% de \n IVA (debe mostrar el precio con descuento y el precio final)?')

precio = float(input('Ingrese el precio del articulo: '))
descuento = precio * 0.20
precioDescuento = precio - descuento
iva = precioDescuento * 0.15
precioFinal = precioDescuento + iva

print(f'Descuento: {descuento}, Precio final: {precioFinal}')