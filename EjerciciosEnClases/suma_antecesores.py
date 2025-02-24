print(
    "Crear una aplicacion que lea x numero e imprima la suma de los numeros antecesores siempre y cuando sea un numero positivo"
)

numero = int(input("Ingrese un numero: "))
suma = 0

if numero < 0:
    print("No es un numero valido")
else: 
    for i in range(numero):
        suma += i
    print(f"La suma de los numeros antecesores de {numero} es: {suma}")
