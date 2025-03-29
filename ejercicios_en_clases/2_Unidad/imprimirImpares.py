print(
    "Crear una aplicacion que imprima todos los numeros impares que existen entre un rango de numeros proporiconados por el usuario, usandp el ciclo while"
)

numeroInicial = int(input("Ingrese el número inicial: "))
numeroFinal = int(input("Ingrese el número final: "))

print(f"Los números impares entre {numeroInicial} y {numeroFinal} son: ")

while numeroInicial <= numeroFinal:
    numerosImpares = numeroInicial % 2
    if numerosImpares != 0:
        print(numeroInicial)
    numeroInicial = numeroInicial + 1
