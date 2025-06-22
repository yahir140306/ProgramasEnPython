print(
    "Crea una aplicacion que lea busque vocales en una palabra. Solicite la palabra y la vocal a buscar"
)

palabra = input("Ingresa una palabra: ")
vocal = input("Ingresa una vocal a buscar: ")
vocales = "aeiou"

if vocal not in vocales:
    print("La vocal no es valida")
    exit()

contador = 0

for i in palabra:
    if i == vocal:
        contador += 1

print(f"La palabra {palabra} tiene {contador} vocal {vocal}")
