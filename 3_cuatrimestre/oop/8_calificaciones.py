class Estudiante:
    def __init__(self, numero):
        self.numero = numero  
        self.calificaciones = []

    def ingresar_calificaciones(self):
        print(f"\nIngresando calificaciones para Estudiante {self.numero}")
        for i in range(5):
            while True:
                try:
                    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
                    if 0 <= calificacion <= 10:
                        self.calificaciones.append(calificacion)
                        break
                    else:
                        print("La calificación debe estar entre 0 y 10.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def obtener_promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)


class AplicacionCalificaciones:
    def __init__(self):
        self.estudiantes = []

    def ejecutar(self):
        n = int(input("¿Cuántos estudiantes deseas ingresar? "))
        for i in range(n):
            estudiante = Estudiante(i + 1)
            estudiante.ingresar_calificaciones()
            self.estudiantes.append(estudiante)

        self.mostrar_resultados()

    def mostrar_resultados(self):
        print("\n--- Resultados ---")
        promedios = []
        for estudiante in self.estudiantes:
            promedio = estudiante.obtener_promedio()
            promedios.append(promedio)
            print(f"Estudiante {estudiante.numero} tiene un promedio de: {promedio:.2f}")

        promedio_general = sum(promedios) / len(promedios)
        print(f"\nPromedio general de todos los estudiantes: {promedio_general:.2f}")
        print(f"Promedio más alto: {max(promedios):.2f}")
        print(f"Promedio más bajo: {min(promedios):.2f}")


app = AplicacionCalificaciones()
app.ejecutar()
