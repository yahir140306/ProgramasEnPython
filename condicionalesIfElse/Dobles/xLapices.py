print(
    "Realice la aplicación y diagrama de flujo para determinar cuánto se debe pagar por equis cantidad de lápices considerando que si son 1000 o más el costo es de 85¢; de lo contrario, el precio es de 90¢. "
)

lapices = int(input("Ingrese la cantidad de lápices: "))
costo = 0

if lapices >= 1000:
    costo = 0.85
    
else:
    costo = 0.95

print(f"El costo total es de ${lapices * costo}")
