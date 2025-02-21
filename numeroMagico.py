import random

numeroMgaico = random.randint(1, 10)

print(
    "Crear una aplicacion que genere un numero magico y el usuario lo adivine, hasta el que usuario logre adivinar el numero magico y diga hasta los numeros de intentos."
)

cont = 0
numeroEscogido = int(input("Ingrese un número: "))

while numeroEscogido != numeroMgaico:
    print("Fallaste!!, intentalo de nuevo")
    numeroEscogido = int(input("Ingrese un número: "))
    cont += 1

print(f"Felicidades, lo lograste en {cont} intentos.")


# for i in range(True):
#     numeroEscogido = int(input("Ingrese un número: "))
#     if numeroEscogido == numeroMgaico:
#         print("Felicidades, has adivinado el número mágico.")
#         break
#     else:
#         print("Fallaste!!, intentalo de nuevo")
