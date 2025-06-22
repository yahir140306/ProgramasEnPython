print(
    "El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de $65.00; de 50 a 99 alumnos, el costo es de $70.00, de 30 a 49, de $95.00, y si son menos de 30, el costo de la renta del autobús es de $4000.00, sin importar el número de alumnos. Crear la aplicación y diagrama de flujo para este fin."
)

numeroAlumnos = int(input("Ingrese el número de alumnos: "))
costoAlumno = 0
costoTotal = 0

if numeroAlumnos >= 100:
    costoAlumno = 65

elif numeroAlumnos >= 50:
    costoAlumno = 70

elif numeroAlumnos >= 30:
    costoAlumno = 95
    
else:
    costoTotal = 4000
    costoAlumno = 4000 / numeroAlumnos

costoTotal = numeroAlumnos * costoAlumno

print(f"El costo por alumno es de ${costoAlumno} y el costo total es de ${costoTotal}")
