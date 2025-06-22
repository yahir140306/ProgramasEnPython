from fractions import Fraction

class calculadora_operaciones:
    def sumar(self,valor_a: float, valor_b: float):
        return valor_a + valor_b

    def restar(self,valor_a: float, valor_b: float):
        return valor_a - valor_b

    def multiplicar(self,valor_a: float, valor_b: float):
        return valor_a * valor_b

    def dividir(self,valor_a: float, valor_b: float):
        try:
            return valor_a / valor_b
        except ZeroDivisionError:
            return "\n Error: Division por cero no esta permitida."
            
# class calculadora_fracciones:
#     def sumar(self, valor_a: float, valor_b: float):
#         return valor_a + valor_b    
    
#     def restar(self, valor_a: float, valor_b: float):
#         return valor_a - valor_b    
    
#     def multiplicar(self, valor_a: float, valor_b: float):
#         return valor_a * valor_b    
    
#     def dividir(self, valor_a: float, valor_b: float):
#         try:
#             return valor_a / valor_b
#         except ZeroDivisionError:
#             return "\n Error: Division por cero no esta permitida."
             
def pedir_numero():
    while True:
        try:
            num = float(input("\n Ingrese su numero: "))
            return num
        except ValueError:
            print("\n Error: Por favor, ingrese un numero valido.")
            
def pedir_fraccion():
    while True:
        try:
            num = input("\n Ingrese la fraccion (ejemplo 1/2): ")
            fraccion = Fraction(num)
            return fraccion
        except ValueError:
            print("\n Error: Por favor, ingrese una fraccion valida.")
            
def menu():
    print("\n--- Calculadora básica ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("\n--- Calculadora Fracciones ---")
    print("5. Suma con fracciones")
    print("6. Resta con fracciones")
    print("7. Multiplicación con fracciones")
    print("8. División con fracciones")
    print("\n9. Salir")
    
calculadora_metodos = calculadora_operaciones()
# calculadora_fracciones_metodos = calculadora_basica()
# calculadora_fracciones_metodos = calculadora_fracciones()

while True:
    menu()
    opcion = input("\nElija una opcion: ")
    resultado = "\n Resultado: "

# operaciones basicas normales
    
    if opcion == '1':
        valor_a = pedir_numero()
        valor_b = pedir_numero()
        print(resultado, calculadora_metodos.sumar(valor_a, valor_b))
    
    elif opcion == '2':
        valor_a = pedir_numero()
        valor_b = pedir_numero()
        print(resultado, calculadora_metodos.restar(valor_a, valor_b))            
    
    elif opcion == '3':
        valor_a = pedir_numero()
        valor_b = pedir_numero()
        print(resultado, calculadora_metodos.multiplicar(valor_a, valor_b))            
    
    elif opcion == '4':
        valor_a = pedir_numero()
        valor_b = pedir_numero()
        print(resultado, calculadora_metodos.dividir(valor_a, valor_b))            

# operaciones con fracciones 
    
    elif opcion == '5':
        valor_a = pedir_fraccion()
        valor_b = pedir_fraccion()
        print(resultado, calculadora_metodos.sumar(valor_a, valor_b))
    
    elif opcion == '6':
        valor_a = pedir_fraccion()
        valor_b = pedir_fraccion()
        print(resultado, calculadora_metodos.restar(valor_a, valor_b))            
    
    elif opcion == '7':
        valor_a = pedir_fraccion()
        valor_b = pedir_fraccion()
        print(resultado, calculadora_metodos.multiplicar(valor_a, valor_b))            
    
    elif opcion == '8':
        valor_a = pedir_fraccion()
        valor_b = pedir_fraccion()
        print(resultado, calculadora_metodos.dividir(valor_a, valor_b))            
    
    elif opcion == '9':
        print("\n Gracias ... saliendo ...")
        break
    
    else:
        print("\n Error - Opcion no valida, intente de nuevo.")