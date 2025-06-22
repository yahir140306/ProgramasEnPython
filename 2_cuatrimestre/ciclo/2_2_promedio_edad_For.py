print(
    "Se requiere una aplicación para obtener la edad promedio de un grupo de N alumnos."
)

print("Con ciclo for: ")

numeroAlumnos = int(input("Ingrese el número de alumnos: "))
suma = 0

for i in range(numeroAlumnos):
    suma = suma + int(input(f"Ingrese la edad del alumno {i + 1}: "))

promedio = suma / numeroAlumnos
print(f"El promedio de las edades de los {numeroAlumnos} alumnos es: {promedio}")
