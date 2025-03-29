print('Crear una aplicación y diagrama de flujo que el usuario introduzca ‘F’ o ‘M’ y que imprima Masculino si es ‘M’ de lo contrario mostrará el mensaje de Femenino.')

sexo = input('Ingrese su sexo (F/M): ')

sexo = sexo.upper()

if sexo == 'M':
    print('Masculino')

elif sexo == 'F':
    print('Femenino')

else:
    print('Sexo no válido')
