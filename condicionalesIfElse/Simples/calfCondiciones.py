print('7 califiaciones que calcule el promedio y si este es mayor a 8 imprima aprobado.')

calificacion1 = float(input('Ingrese calificacion: '))
calificacion2 = float(input('Ingrese calificacion: '))
calificacion3 = float(input('Ingrese calificacion: '))
calificacion4 = float(input('Ingrese calificacion: '))
calificacion5 = float(input('Ingrese calificacion: '))
calificacion6 = float(input('Ingrese calificacion: '))
calificacion7 = float(input('Ingrese calificacion: '))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4 + calificacion5 + calificacion6 + calificacion7) / 7

if promedio > 8: 
    print('Aprobado')