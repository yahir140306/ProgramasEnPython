lado1 = float(input("Ingrese lado 1: "))
lado2 = float(input("Ingrese lado 2: "))
lado3 = float(input("Ingrese lado 3: "))

if lado1 == lado2 and lado1 == lado3:
    print("Es un triangulo es equilatero.")

elif (
    lado1 == lado2
    or lado1 == lado3
    or lado2 == lado1
    or lado2 == lado3
    or lado3 == lado1
    or lado3 == lado2
):
    print("Es un triangulo isoseles.")

else:
    print("Es un triangulo escaleno.")
