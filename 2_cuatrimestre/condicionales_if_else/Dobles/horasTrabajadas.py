print(
    "Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: Si trabaja 40 horas o menos se le paga a $16 por hora. Si trabaja más de 40 horas se le paga a 16 por cada una de las primeras 40 horas y $20 por cada hora extra. Crear la aplicación y diagrama de flujo para este fin. \n"
)

horasTrabajadas = int(input("Ingrese el número de horas trabajadas: "))

salario = 0

if horasTrabajadas <= 40:
    salario = horasTrabajadas * 16
    
else:
    salario = 40 * 16 + (horasTrabajadas - 40) * 20

print(f"El salario semanal es de ${salario}")
