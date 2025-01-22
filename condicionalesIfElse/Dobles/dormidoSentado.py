print('Una persona enferma, que pesa 70 kg., se encuentra en reposo y desea saber cuántas calorías consume su cuerpo durante todo el tiempo que realice una misma actividad. Las actividades que tiene permitido realizar son únicamente dormir o estar sentado en reposo. Los datos que tiene son que estando dormido consume 1.08 calorías por minuto y estando sentado en reposo consume 1.66 calorías por minuto.')

tiempo = int(input('Ingrese el tiempo en minutos: '))
caloriasDormido = 1.08
caloriasSentado = 1.66
calorias = 0

actividad = input('Ingrese la actividad (dormido/sentado): ')

if actividad == 'dormido':
    calorias = tiempo * caloriasDormido
elif actividad == 'sentado':
    calorias = tiempo * caloriasSentado
else: 
    print('Actividad no válida')

print(f'Calorías consumidas: {calorias}')