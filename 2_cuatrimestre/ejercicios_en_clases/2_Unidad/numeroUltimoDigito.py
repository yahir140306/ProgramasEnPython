print('Crear una aplicacion que lea un numero x e imprima el ultimo digito del numero proporcionado.')

numero = int(input("Ingrese un número: "))
ultimo_digito = numero % 10
print(f"El último dígito del número {numero} es: {ultimo_digito}")
