print(
    "Crear una aplicación que lea dos números y que muestre un mensaje indicando cual es el mayor. "
)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercero número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El número {numero1} es mayor que el número {numero2} y {numero3}")

elif numero2 > numero1 and numero2 > numero3:
    print(f"El número {numero2} es mayor que el número {numero1} y {numero3}")

elif numero3 > numero1 and numero3 > numero2:
    print(f"El número {numero3} es mayor que el número {numero1} y {numero2}")

else:
    print(f"Los números {numero1}, {numero2} y {numero3} son iguales")
