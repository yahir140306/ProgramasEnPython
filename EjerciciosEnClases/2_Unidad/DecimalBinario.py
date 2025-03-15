print("Crear una aplicacion que lea x numero y que lo convierta a binario")

# numero = 10
# binario = 0

# while numero != 0:
#     mod = numero % 2
#     print(mod)
#     binario = (binario + mod)
#     numero = numero / 2
# print(numero)

decimal = int(input("Ingrese: "))
binario = ""

while decimal > 0:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2
print(binario)

# 10 / 2 = 0 - 5
# 5 / 2 = 1 - 2
# 2 / 2 = 0 - 1
# 1 / 2 = 1 -
