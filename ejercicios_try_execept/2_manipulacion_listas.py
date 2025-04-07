listas = []


def agregar_elemento():
    cantidad = input("Cantidad de elementos a agregar: ")
    try:
        cantidad = int(cantidad)
        if cantidad < 0:
            print("\nError: La cantidad debe ser un número entero positivo.")
        else:
            for i in range(cantidad):
                lista = input("Ingrese el dato a agregar: ")
                if lista in listas:
                    print(
                        "\nError: El dato ya existe en la lista. No se permiten duplicados."
                    )
                    print("Reiniciando proceso...\n")
                    return agregar_elemento()
                listas.append(lista)

            print(f"\nSe agregaron {cantidad} elemento(s) a la lista.")
            print(f"Lista actual: {listas}\n")
    except ValueError:
        print("\nError: Debes ingresar un número entero.\n")


def eliminar_elemento():
    lista = input("Ingrese el dato a eliminar: ")

    try:
        if lista in listas:
            while lista in listas:
                listas.remove(lista)
            print(f"\nTodos los elementos '{lista}' han sido eliminados de la lista.\n")
            print(f"Lista actual: {listas}")
        else:
            print(f"\n{lista} no se encuentra en la lista.\n")
    except ValueError:
        print("Error.")


def ordenar_lista():
    listas.sort()
    print(f"\nLista ordenada: {listas}\n")


def mostrar_lista():
    if listas:
        print(f"\nLista actual: {listas}\n")
    else:
        print("\nLa lista está vacía.\n")


def menu():
    while True:
        print("\n--- Menu de opciones: ---")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Ordenar lista")
        print("4. Mostrar lista")
        print("5. Salir")

        try:
            opcion = int(input("\nSeleccione una opción: "))

            if opcion == 1:
                agregar_elemento()
            elif opcion == 2:
                eliminar_elemento()
            elif opcion == 3:
                ordenar_lista()
            elif opcion == 4:
                mostrar_lista()
            elif opcion == 5:
                break
            else:
                print("\nOpción inválida, intente nuevamente.\n")

        except ValueError:
            print("\nError: Entrada inválida. Por favor, ingrese un número entero.\n")


if __name__ == "__main__":
    menu()
