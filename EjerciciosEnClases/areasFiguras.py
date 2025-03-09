print(
    "Crear una aplicacion con funciones que calcule el area de las siguientes figuras: Trapecio, Pentagono, Triangulo, Circulo, Cuadrado. \nQue muestre un menu el cual permita seleccionar la figura a calcular el area y solicite los valores requeridas. \n"
)


def areaTrapecio(baseMayor, baseMenor, altura):
    return ((baseMayor + baseMenor) * altura) / 2


def areaPentagono(perimetro, apotema):
    return (perimetro * apotema) / 2


def areaTriangulo(base, altura):
    return (base * altura) / 2


def areaCirculo(radio):
    return 3.1416 * (radio ** 2)


def areaCuadrado(lado):
    return lado ** 2


def menu():
    while True:
        print('\nSeleccione la figura a calcular el area: \n1. Trapecio \n2. Pentagono \n3. Triangulo \n4. Circulo \n5. Cuadrado \n6. Salir')
        opcion = int(input('Opcion: '))

        if opcion == 1:
            print('\nArea de un Trapecio.')
            baseMayor = float(input('Ingrese la base mayor: '))
            baseMenor = float(input('Ingrese la base menor: '))
            altura = float(input('Ingrese la altura: '))
            print(f'El area del Trapecio es: {areaTrapecio(baseMayor, baseMenor, altura)}')
        
        elif opcion == 2:
            print('\nArea de un Pentagono.')
            perimetro = float(input('Ingrese el perimetro: '))
            apotema = float(input('Ingrese la apotema: '))
            print(f'El area del Pentagono es: {areaPentagono(perimetro, apotema)}')
        
        elif opcion == 3:
            print('\nArea de un Triangulo.')
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            print(f'El area del Triangulo es: {areaTriangulo(base, altura)}')
        
        elif opcion == 4:
            print('\nArea de un Circulo.')
            radio = float(input("Ingrese el radio: "))
            print(f"El area del Circulo es: {areaCirculo(radio)}")
        
        elif opcion == 5:
            print('\nArea de un Cuadrado.')
            lado = float(input('Ingrese el lado: '))
            print(f'El area del Cuadrado es: {areaCuadrado(lado)}')
        
        elif opcion == 6:
            break

        else:
            print('\nOpcion no valida')

menu()