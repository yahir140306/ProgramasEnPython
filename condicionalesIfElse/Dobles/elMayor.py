print(
    "Crear una aplicación que lea dos números y que muestre un mensaje indicando cual es el mayor. "
)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercero número: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"El número {numero1} es mayor que el número {numero2}")

elif numero2 > numero1:
    print(f"El número {numero2} es mayor que el número {numero1}")
    
else:
    print(f"Los números {numero1} y {numero2} son iguales")
