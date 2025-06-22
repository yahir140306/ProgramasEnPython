class Calculadora:
    def __init__(self):
        pass 

    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador de una fracción no puede ser cero.")
        self.numerador = numerador
        self.denominador = denominador
        self._simplificar() 

    def _mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    # def _simplificar(self):
    #     comun = self._mcd(abs(self.numerador), abs(self.denominador))
    #     self.numerador //= comun
    #     self.denominador //= comun

    #     if self.denominador < 0:
    #         self.numerador *= -1
    #         self.denominador *= -1

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def sumar(self, otra_fraccion):
        # Suma de fracciones
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def resta(self, otra_fraccion):
        # Resta de fracciones
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) - (otra_fraccion.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def multiplicar(self, otra_fraccion):
        # Multiplicación de fracciones
        nuevo_numerador = self.numerador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def dividir(self, otra_fraccion):
        # División de fracciones
        if otra_fraccion.numerador == 0:
            raise ValueError("No se puede dividir por una fracción con numerador cero.")
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)

def obtener_numero_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def obtener_fraccion(mensaje):
    while True:
        try:
            partes = input(mensaje + " (ej. 1/2): ").split('/')
            if len(partes) != 2:
                raise ValueError("Formato de fracción incorrecto.")
            numerador = int(partes[0])
            denominador = int(partes[1])
            return Fraccion(numerador, denominador)
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingresa la fracción en el formato correcto (ej. 1/2).")

def mostrar_menu_principal():
    print("\n--- CALCULADORA ---")
    print("1. Operaciones con números enteros")
    print("2. Operaciones con fracciones")
    print("3. Salir")

def mostrar_menu_operaciones():
    print("\n--- SELECCIONA UNA OPERACIÓN ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Volver al menú principal")

def main():
    calc = Calculadora()

    while True:
        mostrar_menu_principal()
        opcion_principal = input("Elige una opción: ")

        if opcion_principal == '1':
            while True:
                mostrar_menu_operaciones()
                opcion_operacion = input("Elige una operación: ")

                if opcion_operacion == '1':
                    num1 = obtener_numero_entero("Ingresa el primer número: ")
                    num2 = obtener_numero_entero("Ingresa el segundo número: ")
                    resultado = calc.sumar(num1, num2)
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                elif opcion_operacion == '2':
                    num1 = obtener_numero_entero("Ingresa el primer número: ")
                    num2 = obtener_numero_entero("Ingresa el segundo número: ")
                    resultado = calc.restar(num1, num2)
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                elif opcion_operacion == '3':
                    num1 = obtener_numero_entero("Ingresa el primer número: ")
                    num2 = obtener_numero_entero("Ingresa el segundo número: ")
                    resultado = calc.multiplicar(num1, num2)
                    print(f"Resultado: {num1} * {num2} = {resultado}")
                elif opcion_operacion == '4':
                    num1 = obtener_numero_entero("Ingresa el dividendo: ")
                    num2 = obtener_numero_entero("Ingresa el divisor: ")
                    try:
                        resultado = calc.dividir(num1, num2)
                        print(f"Resultado: {num1} / {num2} = {resultado}")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif opcion_operacion == '5':
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")

        elif opcion_principal == '2':
            while True:
                mostrar_menu_operaciones()
                opcion_operacion = input("Elige una operación: ")

                if opcion_operacion == '1':
                    frac1 = obtener_fraccion("Ingresa la primera fracción")
                    frac2 = obtener_fraccion("Ingresa la segunda fracción")
                    resultado = frac1 + frac2
                    print(f"Resultado: {frac1} + {frac2} = {resultado}")
                elif opcion_operacion == '2':
                    frac1 = obtener_fraccion("Ingresa la primera fracción")
                    frac2 = obtener_fraccion("Ingresa la segunda fracción")
                    resultado = frac1 - frac2
                    print(f"Resultado: {frac1} - {frac2} = {resultado}")
                elif opcion_operacion == '3':
                    frac1 = obtener_fraccion("Ingresa la primera fracción")
                    frac2 = obtener_fraccion("Ingresa la segunda fracción")
                    resultado = frac1 * frac2
                    print(f"Resultado: {frac1} * {frac2} = {resultado}")
                elif opcion_operacion == '4':
                    frac1 = obtener_fraccion("Ingresa el dividendo (fracción):")
                    frac2 = obtener_fraccion("Ingresa el divisor (fracción):")
                    try:
                        resultado = frac1 / frac2
                        print(f"Resultado: {frac1} / {frac2} = {resultado}")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif opcion_operacion == '5':
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")

        elif opcion_principal == '3':
            print("¡Gracias por usar la calculadora! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 3.")

if __name__ == "__main__":
    main()