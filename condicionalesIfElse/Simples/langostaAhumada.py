print('. “La langosta ahumada” es una empresa dedicada a ofrecer banquetes; sus tarifas son las siguientes: el costo de platillo por persona es de $95.00, pero si el número de personas es mayor a 200 pero menor o igual a 300, el costo es de $85.00. Para más de 300 personas el costo por platillo es de $75.00. Se requiere un Pseudocódigo que ayude a determinar el presupuesto que se debe presentar a los clientes que deseen realizar un evento.')

numeroPersonas = int(input('Ingrese el número de personas: '))
costo = 0

if numeroPersonas > 300:
    costo = 75
elif numeroPersonas > 200:
    costo = 85
else:
    costo = 95

presupuesto = numeroPersonas * costo
print(f'El presupuesto es de ${presupuesto}')