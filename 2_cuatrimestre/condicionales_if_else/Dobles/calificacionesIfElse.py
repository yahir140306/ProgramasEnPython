print(
    "Crear la aplicación y el diagrama de flujo que permita lea 8 calificaciones y genere el promedio y este es mayor a 8 muestre el mensaje aprobado de lo contrario indicar reprobado. "
)

calificaciones1 = float(input("Ingrese la calificación 1: "))
calificaciones2 = float(input("Ingrese la calificación 2: "))
calificaciones3 = float(input("Ingrese la calificación 3: "))
calificaciones4 = float(input("Ingrese la calificación 4: "))
calificaciones5 = float(input("Ingrese la calificación 5: "))
calificaciones6 = float(input("Ingrese la calificación 6: "))
calificaciones7 = float(input("Ingrese la calificación 7: "))
calificaciones8 = float(input("Ingrese la calificación 8: "))

sumar = (
    calificaciones1
    + calificaciones2
    + calificaciones3
    + calificaciones4
    + calificaciones5
    + calificaciones6
    + calificaciones7
    + calificaciones8
)

promedio = sumar / 8

if promedio > 8:
    print("Aprobado")
else:
    print("Reprobado")
