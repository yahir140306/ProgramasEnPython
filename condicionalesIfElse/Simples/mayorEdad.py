print("Pedir nombre, year de nacimiento y year actual.")

nombre = input("Ingrese su nombre: ")
yearNacimiento = int(input("Ingrese su año de nacimiento: "))
yearActual = int(input("Ingrese el año actual: "))

yourYear = yearActual - yearNacimiento

if yourYear >= 18:
    print(f"Tu nombre: {nombre}, eres mayor de edad.")
