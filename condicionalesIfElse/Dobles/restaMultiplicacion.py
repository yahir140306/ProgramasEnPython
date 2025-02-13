print(
    " Crear la aplicación y diagrama de flujo que lea 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume."
)

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
resultado = 0

if numero1 == numero2:
    resultado = numero1 * numero2
    print(f"El resultado de la multiplicación es {resultado}")

elif numero1 > numero2:
    resultado = numero1 - numero2
    print(f"El resultado de la resta es {resultado}")
    
else:
    resultado = numero1 + numero2
    print(f"El resultado de la suma es {resultado}")
