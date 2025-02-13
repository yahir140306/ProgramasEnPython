print(
    " El consultorio del Dr. Lorenzo T. Mata Lozano tiene como política cobrar la consulta con base en el número de cita, de la siguiente forma: \n Las tres primeras citas a $200.00 c/u. \n Las siguientes dos citas a $150.00 c/u. \n Las tres siguientes citas a $100.00 c/u. \n Las restantes a $50.00 c/u, mientras dure el tratamiento. \n Se requiere un algoritmo para determinar: \n Cuánto pagará el paciente por la cita. \n El monto de lo que ha pagado el paciente por el tratamiento. "
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
