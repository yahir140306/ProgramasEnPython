print('Calcuar la edad actual.')

nombre = (input('Ingrese su nombre: '))
nacimiento = int(input('Ingrese el año de nacimiento: ')) 
actual = int(input('Ingrese el año actual: '))

edad = actual - nacimiento

print(f'{nombre} tiene {edad} años de edad.')