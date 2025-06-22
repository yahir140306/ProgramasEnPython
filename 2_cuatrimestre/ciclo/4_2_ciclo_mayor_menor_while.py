print(
    "Se requiere una aplicacion para determinar, de N cantidades, cuantas son menores o iguales a cero y cuantas mayores a cero. \n"
)

numero_cantidad = int(input("Dame un numero: "))

menoresIgual = 0
mayores = 0
i = 0

while i < numero_cantidad:
    numero = float(input("Ingrese un numero: "))
    if numero > 0:
        mayores += 1
    
    elif numero <= 0:
        menoresIgual += 1
    
    else:
        print("No es un digito")
    
    i += 1

print(f"\nNumeros menores o iguales a 0 son: {menoresIgual}")
print(f"Numeros mayores a 0 son: {mayores}")
