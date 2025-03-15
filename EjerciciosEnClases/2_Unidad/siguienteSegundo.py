print(
    "Pedir una hora de la forma hora, minutos y segundos, y mostrar la hora siguiente"
)

hora = int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

if (
    hora < 0
    or hora > 23
    or minutos < 0
    or minutos > 59
    or segundos < 0
    or segundos > 59
):
    print("Hora inválida.")

else:
    segundos += 1

    if segundos == 60:
        segundos = 0
        minutos += 1

        if minutos == 60:
            minutos = 0
            hora += 1

            if hora == 24:
                hora = 0

    print(f"La hora siguiente es: {hora}:{minutos}:{segundos}")
