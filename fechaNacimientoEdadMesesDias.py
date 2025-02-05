from datetime import datetime

print('Crear una aplicacion que lea una fecha de nacimiento y calcule la edad en años, meses y dias. \n')

fechaNacimiento = input('Ingrese su fecha de nacimiento (dd/mm/yyyy): ')
fechaNacimiento = datetime.strptime(fechaNacimiento, '%d/%m/%Y')

fechaActual = datetime.now()

edad = fechaActual - fechaNacimiento
edad = edad.days

edadAnios = edad // 365
edadMeses = (edad % 365) // 30
edadDias = (edad % 365) % 30

print(f'\n Edad: {edadAnios} años, {edadMeses} meses y {edadDias} dias.')

