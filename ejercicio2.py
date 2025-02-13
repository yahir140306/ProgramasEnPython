print('El profesor de la materia de programación desea saber cuántos alumnos tienen calificación de 10, cuántos de 9 y cuántos de 8, además cuántos no aprobaron. Cantidad de calificaciones a leer 30 Usar --> Ciclo While ')

calificacion = 0
diez = 0
nueve = 0
ocho = 0
reprobados = 0
i = 0

while i < 30:
    calificacion = float(input(f'Ingrese la calificación del alumno {i + 1}: '))
    
    if calificacion == 10:
        diez = diez + 1

    elif calificacion == 9:
        nueve = nueve + 1
    
    elif calificacion == 8:
        ocho = ocho + 1
    
    else:
        reprobados = reprobados + 1
    
    i = i + 1

print(f'La cantidad de alumnos con calificación de 10 es: {diez}')
print(f'La cantidad de alumnos con calificación de 9 es: {nueve}')
print(f'La cantidad de alumnos con calificación de 8 es: {ocho}')
print(f'La cantidad de alumnos reprobados es: {reprobados}')
