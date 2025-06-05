class Contador:
    def __init__(self, valor: int):
        self.__valor = valor 

    def getContador(self):
        return self.__valor

    def setContador(self, contar: int):
        self.__valor = contar

mi_contador = Contador(10)

while True:
    print("Escoja una opción: ")
    print("1.- Incrementar")
    print("2.- Decrementar")

    opcion = int(input("Escoja uno: "))

    if opcion == 1:
        cantidad = float(input("Ingrese la cantidad: "))
        nuevo_valor = mi_contador.getContador() + cantidad
        mi_contador.setContador(nuevo_valor)
        print(f"Total después del incremento: {mi_contador.getContador()}")

    elif opcion == 2:
        cantidad = float(input("Ingrese la cantidad: "))
        nuevo_valor = mi_contador.getContador() - cantidad
        mi_contador.setContador(nuevo_valor)
        print(f"Total después del decremento: {mi_contador.getContador()}")

    else:
        print("Error: ingrese solamente 1 o 2.")
