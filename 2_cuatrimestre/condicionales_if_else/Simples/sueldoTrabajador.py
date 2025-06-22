print ('Dado el sueldo de un trabajador, aplicar aumento del 15% si su sueldo es inferior a 3000, e imprimir el nuevo sueldo, elaborar la aplicación y el diagrama de flujo correspondiente.')

sueldo = float(input('Ingrese el sueldo del trabajador: '))

if sueldo < 3000:
    sueldo = sueldo * 1.15
else:
    sueldo = sueldo

print (f'El nuevo sueldo es de ${sueldo}')