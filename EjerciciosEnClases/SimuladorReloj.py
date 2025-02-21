print('Simulacion de un reloj, usando el ciclo while y for. Sin usar timer')


# Variables
horas = 0
minutos = 0
segundos = 0

# Ciclo infinito
while True:
    for horas in range(0, 24):
        for minutos in range(0, 60):
            for segundos in range(0, 60):
                print(f"{horas}:{minutos}:{segundos}")
                if horas == 23 and minutos == 59 and segundos == 59:
                    horas = 0
                    minutos = 0
                    segundos = 0
                if segundos == 59:
                    segundos = 0
                if minutos == 59 and segundos == 59:
                    minutos = 0
                if horas == 23 and minutos == 59 and segundos == 59:
                    horas = 0
                segundos += 1
            minutos += 1
        horas += 1
    break
print("Fin del programa")
