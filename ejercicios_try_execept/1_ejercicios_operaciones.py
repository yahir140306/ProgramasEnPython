def suma(a: float, b: float):
    try:
        return a + b
    except TypeError:
        print("Error: Los valores deben ser números.")

def resta(a: float, b: float):
    try:
        return a - b
    except TypeError:
        print("Error: Los valores deben ser números.")

def multiplicacion(a: float, b: float):
    try:
        return a * b
    except TypeError:
        print("Error: Los valores deben ser números.")

def division(a: float, b: float):
    try:
        resultado = a / b
        return resultado
    except TypeError:
        print("Error: Los valores deben ser números.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

def elevar_al_cuadrado(a: float):
    try:
        return a**2
    except TypeError:
        print("Error: El valor debe ser un número.")

def elevar_a_n(a: float, n: float):
    try:
        return a**n
    except TypeError:
        print("Error: Los valores deben ser números.")

def obtener_factorial(n: float):
    try:
        if n < 0:
            raise ValueError("El número debe ser no negativo.")
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
    except TypeError:
        print("Error: El valor debe ser un número.")
    except ValueError as ve:
        print(f"Error: {ve}")

def obtener_raiz_cuadrada(a: float):
    try:
        if a < 0:
            raise ValueError("El número debe ser no negativo.")
        return a**0.5
    except TypeError:
        print("Error: El valor debe ser un número.")
    except ValueError as ve:
        print(f"Error: {ve}")

#TODO: ⬆️ todas las funciones que pidio 
#TODO: ⬇️ Inicia el programa con el menu

def menu_operaciones_basicas():
    while True:
        print("\nMENÚ OPERACIONES BÁSICAS")
        print("1.- SUMA")
        print("2.- RESTA")
        print("3.- MULTIPLICACIÓN")
        print("4.- DIVISIÓN")
        print("5.- VOLVER AL MENÚ PRINCIPAL")

        try:
            opcion = int(input("Introduce el número de la operación: "))
            if opcion == 5:
                break
            if opcion < 1 or opcion > 5:
                raise ValueError("Opción no válida.")

            valor1 = float(input("Introduce el valor 1: "))
            valor2 = float(input("Introduce el valor 2: "))

            if opcion == 1:
                resultado = suma(valor1, valor2)
                print(f"La suma es: {resultado}")
            elif opcion == 2:
                resultado = resta(valor1, valor2)
                print(f"La diferencia es: {resultado}")
            elif opcion == 3:
                resultado = multiplicacion(valor1, valor2)
                print(f"El producto es: {resultado}")
            elif opcion == 4:
                resultado = division(valor1, valor2)
                if resultado is not None:
                    print('No se puede dividir entre cero')
                else:    
                    print(f"El cociente es: {resultado}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")

def menu_operaciones_exponenciales():
    while True:
        print("\nMENÚ OPERACIONES EXPONENCIALES")
        print("1.- ELEVAR AL CUADRADO")
        print("2.- ELEVAR A LA N POTENCIA")
        print("3.- VOLVER AL MENÚ PRINCIPAL")
        try:
            opcion = int(input("Introduce el número de la operación: "))
            if opcion == 3:
                break
            if opcion < 1 or opcion > 3:
                print(ValueError("Opción no válida.")) 

            valor = float(input("Introduce el valor: "))

            if opcion == 1:
                resultado = elevar_al_cuadrado(valor)
                print(f"El cuadrado de {valor} es: {resultado}")
            elif opcion == 2:
                n = float(input("Introduce el exponente: "))
                resultado = elevar_a_n(valor, n)
                print(f"{valor} elevado a {n} es: {resultado}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")

def menu_operaciones_factoriales():
    while True:
        print("\nMENÚ OPERACIONES FACTORIALES")
        print("1.- OBTENER FACTORIAL")
        print("2.- VOLVER AL MENÚ PRINCIPAL")
        try:
            opcion = int(input("Introduce el número de la operación: "))
            if opcion == 2:
                break
            if opcion < 1 or opcion > 2:
                raise ValueError("Opción no válida.")

            valor = int(input("Introduce el valor: "))

            if opcion == 1:
                resultado = obtener_factorial(valor)
                print(f"El factorial de {valor} es: {resultado}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")

def menu_operaciones_raices():
    while True:
        print("\nMENÚ OPERACIONES RAICES")
        print("1.- OBTENER RAIZ CUADRADA")
        print("2.- VOLVER AL MENÚ PRINCIPAL")
        try:
            opcion = int(input("Introduce el número de la operación: "))
            if opcion == 2:
                break
            if opcion < 1 or opcion > 2:
                raise ValueError("Opción no válida.")

            valor = float(input("Introduce el valor: "))

            if opcion == 1:
                resultado: float = obtener_raiz_cuadrada(valor)
                print(f"La raíz cuadrada de {valor} es: {resultado}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")

# TODO: ⬇️ Inicia el programa con el menu

def menu_principal():
    while True:
        print("\nMENÚ DE OPERACIONES")
        print("1.- OPERACIONES BÁSICAS")
        print("2.- OPERACIONES EXPONENCIALES")
        print("3.- OPERACIONES FACTORIALES")
        print("4.- OPERACIONES RAICES")
        print("5.- SALIR")

        try:
            opcion = int(input("Introduce una opción: "))
            if opcion == 5:
                break
            if opcion < 1 or opcion > 5:
                raise ValueError("Opción no válida.")

            if opcion == 1:
                menu_operaciones_basicas()
            elif opcion == 2:
                menu_operaciones_exponenciales()
            elif opcion == 3:
                menu_operaciones_factoriales()
            elif opcion == 4:
                menu_operaciones_raices()

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    menu_principal()
