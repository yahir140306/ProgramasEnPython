class Operaciones:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumar(self):
        return self.valor1 + self.valor2

    def restar(self):
        return self.valor1 - self.valor2

    def multiplicar(self):
        return self.valor1 * self.valor2

    def dividir(self):
        if self.valor2 == 0:
            return "Error: no se puede dividir entre 0"
        return self.valor1 / self.valor2

class Fracciones:
    def __init__(self, numerador1: int, denominador1: int, numerador2: int, denominador2: int):
        self.numerador1 = numerador1
        self.denominador1 = denominador1
        self.numerador2 = numerador2
        self.denominador2 = denominador2

    def _simplificar_fraccion(self, num, den):
        """Método auxiliar para simplificar fracciones."""
        if den == 0:
            return "Error: El denominador no puede ser cero."
        if num == 0:
            return 0, 1 # Retorna 0/1 si el numerador es 0
        
        # Encuentra el máximo común divisor (MCD)
        def mcd(a, b):
            while b:
                a, b = b, a % b
            return a

        divisor_comun = mcd(abs(int(num)), abs(int(den)))
        numerador_simplificado = int(num / divisor_comun)
        denominador_simplificado = int(den / divisor_comun)
        
        # Asegurarse de que el signo esté en el numerador
        if denominador_simplificado < 0:
            numerador_simplificado *= -1
            denominador_simplificado *= -1
            
        return numerador_simplificado, denominador_simplificado

    def sumar_fracciones(self):
        if self.denominador1 == 0 or self.denominador2 == 0:
            return "Error: Uno de los denominadores es 0. No se puede realizar la operación."

        numerador_resultado = (self.numerador1 * self.denominador2) + (self.numerador2 * self.denominador1)
        denominador_resultado = self.denominador1 * self.denominador2

        num_simplificado, den_simplificado = self._simplificar_fraccion(numerador_resultado, denominador_resultado)

        if den_simplificado == 1:
            return f"{num_simplificado}"
        return f"{num_simplificado}/{den_simplificado}"

    def restar_fracciones(self):
        if self.denominador1 == 0 or self.denominador2 == 0:
            return "Error: Uno de los denominadores es 0. No se puede realizar la operación."

        numerador_resultado = (self.numerador1 * self.denominador2) - (self.numerador2 * self.denominador1)
        denominador_resultado = self.denominador1 * self.denominador2

        num_simplificado, den_simplificado = self._simplificar_fraccion(numerador_resultado, denominador_resultado)
        
        if den_simplificado == 1:
            return f"{num_simplificado}"
        return f"{num_simplificado}/{den_simplificado}"

    def multiplicar_fracciones(self):
        if self.denominador1 == 0 or self.denominador2 == 0:
            return "Error: Uno de los denominadores es 0. No se puede realizar la operación."

        numerador_resultado = self.numerador1 * self.numerador2
        denominador_resultado = self.denominador1 * self.denominador2

        num_simplificado, den_simplificado = self._simplificar_fraccion(numerador_resultado, denominador_resultado)
        
        if den_simplificado == 1:
            return f"{num_simplificado}"
        return f"{num_simplificado}/{den_simplificado}"

    def dividir_fracciones(self):
        if self.denominador1 == 0 or self.denominador2 == 0 or self.numerador2 == 0:
            return "Error: Uno de los denominadores es 0 o el numerador de la segunda fracción es 0 (división por cero)."

        numerador_resultado = self.numerador1 * self.denominador2
        denominador_resultado = self.denominador1 * self.numerador2
        
        num_simplificado, den_simplificado = self._simplificar_fraccion(numerador_resultado, denominador_resultado)
        
        if den_simplificado == 1:
            return f"{num_simplificado}"
        return f"{num_simplificado}/{den_simplificado}"


def obtener_entrada_numerica(mensaje):
    """Función auxiliar para obtener entrada numérica del usuario."""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, ingresa solo números. Intenta de nuevo.")

while True:
    print("\n--- Menú de Operaciones ---")
    print("0.- Salir")
    print("1.- Menú de Fracciones")
    print("2.- Sumar")
    print("3.- Restar")
    print("4.- Multiplicar")
    print("5.- Dividir")

    eleccion_usuario = input("Ingresa el número de tu elección: ")

    if eleccion_usuario == "0":
        break
    
    if eleccion_usuario not in ["1", "2", "3", "4", "5"]:
        print("Opción no válida. Por favor, elige un número del 0 al 5.")
        continue

    if eleccion_usuario == "1":
        print("\n--- Menú de Fracciones ---")
        print("Ingresa los 4 valores para las fracciones.")
        print("Recuerda: (numerador1 / denominador1) y (numerador2 / denominador2)")

        num1 = obtener_entrada_numerica("\n Ingresa el numerador de la primera fracción: ")
        den1 = obtener_entrada_numerica("\n Ingresa el denominador de la primera fracción: ")
        num2 = obtener_entrada_numerica("\n Ingresa el numerador de la segunda fracción: ")
        den2 = obtener_entrada_numerica("\n Ingresa el denominador de la segunda fracción: ")

        objeto_fraccion = Fracciones(num1, den1, num2, den2)

        print("\nElige la operación para fracciones:")
        print("1.- Sumar fracciones")
        print("2.- Restar fracciones")
        print("3.- Multiplicar fracciones")
        print("4.- Dividir fracciones")
        eleccion_operacion_fraccion = input("Ingresa el número de tu elección: ")

        print("Resultado:")
        if eleccion_operacion_fraccion == "1":
            print(objeto_fraccion.sumar_fracciones())
        elif eleccion_operacion_fraccion == "2":
            print(objeto_fraccion.restar_fracciones())
        elif eleccion_operacion_fraccion == "3":
            print(objeto_fraccion.multiplicar_fracciones())
        elif eleccion_operacion_fraccion == "4":
            print(objeto_fraccion.dividir_fracciones())
        else:
            print("Opción no válida para operaciones de fracciones.")

    else: # Esto cubre las opciones 2, 3, 4, 5
        print("\nIngresa dos valores para la operación:")
        val1 = obtener_entrada_numerica("\n Ingresa el primer número: ")
        val2 = obtener_entrada_numerica("\n Ingresa el segundo número: ")

        objeto_operacion = Operaciones(val1, val2)

        print("Resultado:")
        if eleccion_usuario == "2":
            print(objeto_operacion.sumar())
        elif eleccion_usuario == "3":
            print(objeto_operacion.restar())
        elif eleccion_usuario == "4":
            print(objeto_operacion.multiplicar())
        elif eleccion_usuario == "5":
            print(objeto_operacion.dividir())
    
    input("\nPulsa Enter para continuar...")

print("¡Gracias por usar nuestro menú! :)")