print('Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas. \n')

horas_trabajadas = 0
sueldo = 0

for dia in range(1, 7):
    horas = int(input(f'Ingrese las horas trabajadas el día {dia}: '))
    horas_trabajadas += horas
    sueldo += horas * 10

print(f'El total de horas trabajadas en la semana es: {horas_trabajadas}')
print(f'El sueldo a recibir es: {sueldo}')

