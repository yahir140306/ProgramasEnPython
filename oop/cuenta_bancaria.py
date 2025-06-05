import datetime

class CuentaBancaria:
    def __init__(self, propietario: str, monto_inicial=0):
        self.__propietario = propietario
        self.__monto = monto_inicial
        self.__numAcciones = 0
        self.__fecha_apertura = datetime.date.today()

    def depositar(self, cantidad: float):
        if cantidad <= 0:
            print("La cantidad a depositar debe ser positiva.")
            return
        if cantidad > 5000:
            print("No se puede depositar más de 5000 en una sola operación.")
            return
        self.__monto += cantidad
        self.__numAcciones += 1
        print(f"Depósito realizado. Nuevo saldo: {self.__monto}")

    def retirar(self, cantidad: float):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser positiva.")
            return
        if cantidad > self.__monto:
            print("Saldo insuficiente para realizar el retiro.")
            return
        self.__monto -= cantidad
        self.__numAcciones += 1
        print(f"Retiro realizado. Nuevo saldo: {self.__monto}")

    def consultar_saldo(self):
        self.__numAcciones += 1
        print(f"Saldo actual: {self.__monto}")

    def mostrar_info(self):
        print(f"Propietario: {self.__propietario}")
        print(f"Fecha de apertura: {self.__fecha_apertura}")    
        print(f"Número de acciones realizadas: {self.__numAcciones}")

def menu():
    print("\n--- MENÚ ---")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Consultar saldo")
    print("4. Mostrar información de la cuenta")
    print("5. Salir")

def main():
    propietario = input("Ingrese el nombre del propietario de la cuenta: ")
    cuenta = CuentaBancaria(propietario)

    while True:
        menu()
        opcion = input("Elija una opción: ")

        if opcion == '1':
            try:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta.depositar(cantidad)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == '2':
            try:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == '3':
            cuenta.consultar_saldo()
        elif opcion == '4':
            cuenta.mostrar_info()
        elif opcion == '5':
            print("Gracias por usar el programa. ¡Adiós!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
