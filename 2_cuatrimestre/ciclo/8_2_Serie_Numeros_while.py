print(
    "Pedir numeros hasta que se te de uno negativo y mostrar cuantos numeros se han introducido."
)

numeros = 0
while True:
    numero = int(input("Introduce un número: "))
    if numero < 0:
        break
    numeros += 1

print(f"Se han introducido {numeros} números.")

