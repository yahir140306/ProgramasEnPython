class Perro:  # se define la clase con class Nombre
    def __init__(self, Nombre, Raza, Color, Edad):
        self.nombre = Nombre
        self.raza = Raza
        self.color = Color
        self.edad = Edad


    def ladrar(self):
        print("Esta ladrando")


    def comer(self):
        print("Esta comiendo")


perro1 = Perro("Solovino", "Callejero premiun", "Cafe con leche", 5)
print(f"El nombre del perro1 es {perro1.nombre}")

perro2 = Perro("Firulais", "chihuahua", "rosa", 3)
print(f"El {perro2.nombre} es de color {perro1.color}")

perro3 = Perro("Golondrino", "Bulldog", "verde limon", 30)
print(f"El {perro3.nombre} es de la raza {perro3.raza}")

perro3.ladrar()



