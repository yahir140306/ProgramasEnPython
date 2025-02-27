print(
    "El consultorio del Dr. Lorenzo T. Mata Lozano tiene como política cobrar la consulta con base en el número de cita, de la siguiente forma: \nLas tres primeras citas a $200.00 c/u. \nLas siguientes dos citas a $150.00 c/u. \nLas tres siguientes citas a $100.00 c/u. \nLas restantes a $50.00 c/u, mientras dure el tratamiento. \nSe requiere un algoritmo para determinar: \nCuánto pagará el paciente por la cita. \nEl monto de lo que ha pagado el paciente por el tratamiento. \n"
)

citas = int(input("Ingrese el número de cita: "))

if citas <= 3:
    print("El costo de la cita es: $200.00")
    print("El monto total pagado es: $", 200 * citas)

elif citas <= 5:
    print("El costo de la cita es: $150.00")
    print("El monto total pagado es: $", 200 * 3 + 150 * (citas - 3))

elif citas <= 8:
    print("El costo de la cita es: $100.00")
    print("El monto total pagado es: $", 200 * 3 + 150 * 2 + 100 * (citas - 5))
    
else:
    print("El costo de la cita es: $50.00")
    print("El monto total pagado es: $", 200 * 3 + 150 * 2 + 100 * 3 + 50 * (citas - 8))
