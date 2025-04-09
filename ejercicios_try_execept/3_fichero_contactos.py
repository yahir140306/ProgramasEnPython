import os
from tabulate import tabulate


def crear_contacto(nombre, direccion, telefono, email):
    archivo = f"{nombre}.txt"

    if os.path.exists(archivo):
        print(f"\nEl contacto '{nombre}' ya existe. No se puede duplicar.")
        return

    contacto = f"Nombre: {nombre}\nDireccion: {direccion}\nTelefono: {telefono}\nEmail: {email}"

    try:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(contacto)
        print(f"\nContacto '{nombre}' creado.")
        print(
            "\n"
            + tabulate(
                [
                    ["Nombre", "Direccion", "Telefono", "Email"],
                    [nombre, direccion, telefono, email],
                ],
                tablefmt="grid",
            )
        )
    except Exception as e:
        print(f"⚠️ Error al crear el contacto: {e}")


def ver_contactos():
    nombre = input("¿Qué contacto quieres ver? (Nombre): ")
    archivo = f"{nombre}.txt"

    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()
            datos = [linea.strip().split(": ", 1) for linea in lineas if ": " in linea]
            print("\n" + tabulate(datos, tablefmt="grid"))
    else:
        print(f"El contacto '{nombre}' no existe.")


def eliminar_contacto(nombre):
    archivo = f"{nombre}.txt"
    if os.path.exists(archivo):
        os.remove(archivo)
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"El contacto '{nombre}' no existe.")


def modificar_contacto(
    nombre, nuevo_direccion=None, nuevo_telefono=None, nuevo_email=None
):
    archivo = f"{nombre}.txt"
    if os.path.exists(archivo):
        with open(archivo, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        direccion = lineas[1].split(":", 1)[1].strip()
        telefono = lineas[2].split(":", 1)[1].strip()
        email = lineas[3].split(":", 1)[1].strip()

        direccion = nuevo_direccion if nuevo_direccion else direccion
        telefono = nuevo_telefono if nuevo_telefono else telefono
        email = nuevo_email if nuevo_email else email

        nuevo_contenido = f"Nombre: {nombre} \nDireccion: {direccion} \nTelefono: {telefono} \nEmail: {email}"
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)
        print(f"\nContacto '{nombre}' modificado.")
        print(
            tabulate(
                [
                    ["Nombre", "Direccion", "Telefono", "Email"],
                    [nombre, direccion, telefono, email],
                ],
                headers="firstrow",
                tablefmt="grid",
            )
        )
    else:
        print(f"El contacto '{nombre}' no existe.")


def menu():
    while True:
        print("\n   Menu:")
        print("1. Crear contacto")
        print("2. Ver contacto")
        print("3. Eliminar contacto")
        print("4. Modificar contacto")
        print("5. Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            nombre = input("\nNombre: ")
            direccion = input("Direccion: ")
            telefono = input("Telefono: ")
            email = input("Email: ")
            crear_contacto(nombre, direccion, telefono, email)
        elif opcion == "2":
            ver_contactos()
        elif opcion == "3":
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Nombre del contacto a modificar: ")
            nuevo_direccion = input(
                "Nueva Direccion (dejar en blanco para no modificar): "
            )
            nuevo_telefono = input(
                "Nuevo Telefono (dejar en blanco para no modificar): "
            )
            nuevo_email = input("Nuevo Email (dejar en blanco para no modificar): ")
            modificar_contacto(
                nombre,
                nuevo_direccion if nuevo_direccion else None,
                nuevo_telefono if nuevo_telefono else None,
                nuevo_email if nuevo_email else None,
            )
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu()
