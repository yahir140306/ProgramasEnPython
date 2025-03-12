print("Crear una aplicacion el cual presente un menu con los siguientes productos: \n")
print(
    "El programa debe de permitir elegir el producto y la cantidad a comprar, el programa debe imprimir la cantidad, el producto, precio unitario y total a pagar."
)

print("Refresco --------------- $12.00 \n Agua Mineral ---- $8.00 ")
print("Galletas Emperador ----- $12.00 \n Maruchan -------- $10.00 ")

producto = input("Elija el producto a comprar: ")
producto = producto.lower()

cantidad = int(input("Cantidad a comprar: "))

match producto:
    case "refresco":
        precio = 12
        total = precio * cantidad
        print(
            f"Producto: {producto.capitalize()} \n Cantidad: {cantidad} \n Precio unitario: ${precio} \n Total a pagar: ${total}"
        )
    case "agua mineral":
        precio = 8
        total = precio * cantidad
        print(
            f"Producto: {producto.capitalize()} \n Cantidad: {cantidad} \n Precio unitario: ${precio} \n Total a pagar: ${total}"
        )
    case "galletas emperador":
        precio = 12
        total = precio * cantidad
        print(
            f"Producto: {producto.capitalize()} \n Cantidad: {cantidad} \n Precio unitario: ${precio} \n Total a pagar: ${total}"
        )
    case "maruchan":
        precio = 10
        total = precio * cantidad
        print(
            f"Producto: {producto.capitalize()} \n Cantidad: {cantidad} \n Precio unitario: ${precio} \n Total a pagar: ${total}"
        )
    case _:
        print("Producto no valido")
