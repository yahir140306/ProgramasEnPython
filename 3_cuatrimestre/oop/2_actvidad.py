# 1
class ave:
    def __init__(self, nombre, color, plumaje, pico, alas):
        self.nombre = nombre
        self.color = color
        self.plumaje = plumaje
        self.pico = pico
        self.alas = alas

    def cantar(self):
        print("Esta cantando")
    def comer(self):
        print("Esta comiendo")
    def volar(self):
        print("Esta volando")

ave1 = ave("Lola", "blanco", "suave", "Corto", "anchas")
ave2 = ave("Tito", "Azul", "liso", "Fino", "largas")
ave3 = ave("Pua", "rojo", "grueso", "mediano", "cortas")
ave4 = ave("Zazu", "amarillo", "delgado", "Largo", "anchas")
ave5 = ave("Milo", "verde", "esponjoso", "corto", "pequeñas")

print(f'El nombre de ave es: {ave1.nombre}')
print(f'El nombre de ave es: {ave2.nombre}')
print(f'El nombre de ave es: {ave3.nombre}')
print(f'El nombre de ave es: {ave4.nombre}')
print(f'El nombre de ave es: {ave5.nombre}')
ave1.cantar()
ave2.comer()
ave3.volar()
print("\n")

# 2
class pez:
    def __init__(self, nombre, color, especie, tamaño, tipo_agua):
        self.nombre = nombre
        self.color = color
        self.especie = especie
        self.tamaño = tamaño
        self.tipo_agua = tipo_agua

    def reproduccion(self):
            print("Esta reproduciendose")
    def nadar(self):
            print("Esta nadando")
    def comer(self):
            print("Esta comiendo")


pez1 = pez("Nemo", "naranja", "payaso", "pequeño", "salada")
pez2 = pez("Dory", "azul", "cirujano", "mediano", "salada")
pez3 = pez("Bubbles", "amarillo", "gobio", "pequeño", "dulce")
pez4 = pez("Goldie", "dorado", "carpa", "grande", "dulce")
pez5 = pez("Bubbles", "azul", "betta", "pequeño", "dulce")
print(f'El nombre del pez es: {pez1.nombre}')
print(f'El nombre del pez es: {pez2.nombre}')
print(f'El nombre del pez es: {pez3.nombre}')
print(f'El nombre del pez es: {pez4.nombre}')
print(f'El nombre del pez es: {pez5.nombre}')
pez4.reproduccion()
pez5.nadar()
pez1.comer()
print("\n")

#3
class flor:
    def __init__(self, nombre, color, tipo, altura, aroma):
        self.nombre = nombre
        self.color = color
        self.tipo = tipo
        self.altura = altura
        self.aroma = aroma

    def florecer(self):
        print("Esta floreciendo")
    def marchitar(self):
        print("Esta marchitandose")
    def crecer(self):
        print("Esta creciendo")

flor1 = flor("Rosa", "rojo", "perenne", "alta", "fuerte")
flor2 = flor("Tulipán", "amarillo", "anual", "media", "suave")
flor3 = flor("Lirio", "blanco", "perenne", "alta", "fresca")
flor4 = flor("Margarita", "blanco", "anual", "baja", "ligero")
flor5 = flor("Girasol", "amarillo", "anual", "alta", "intenso")
print(f'El nombre de la flor es: {flor1.nombre}')
print(f'El nombre de la flor es: {flor2.nombre}')
print(f'El nombre de la flor es: {flor3.nombre}')
print(f'El nombre de la flor es: {flor4.nombre}')
print(f'El nombre de la flor es: {flor5.nombre}')
flor2.florecer()
flor3.marchitar()
flor4.crecer()
print("\n")

# 4
class aviones:
    def __init__(self, nombre, color, tipo, capacidad, velocidad):
        self.nombre = nombre
        self.color = color
        self.tipo = tipo
        self.capacidad = capacidad
        self.velocidad = velocidad

    def despegar(self):
        print("Esta despegando")
    def aterrizar(self):
        print("Esta aterrizando")
    def volar(self):
        print("Esta volando")

avion1 = aviones("f-22 Raptor", "gris", "caza", 2, 2410)
avion2 = aviones("Eviofigther typhoon", "gris claro", "caza", 2, 2495)
avion3 = aviones("su-57", "gris oscuro", "caza", 2, 2000)
avion4 = aviones("Boeing 747", "blanco", "comercial", 660, 920)
avion5 = aviones("Airbus A380", "blanco y azul", "comercial", 850, 1020)
print(f'El nombre del avion es: {avion1.nombre}')
print(f'El nombre del avion es: {avion2.nombre}')
print(f'El nombre del avion es: {avion3.nombre}')
print(f'El nombre del avion es: {avion4.nombre}')
print(f'El nombre del avion es: {avion5.nombre}')
avion5.despegar()
avion1.aterrizar()
avion2.volar()
print("\n")

# 5 
class felinos:
    def __init__(self, nombre, color, raza, tamaño, habitat):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.tamaño = tamaño
        self.habitat = habitat

    def cazar(self):
        print("Esta cazando")
    def dormir(self):
        print("Esta durmiendo")
    def jugar(self):
        print("Esta jugando")

felino1 = felinos("Leo", "amarillo", "león", "grande", "sabana")
felino2 = felinos("Mia", "blanco", "gato persa", "pequeño", "hogar")
felino3 = felinos("Tigre", "naranja con rayas negras", "tigre de bengala", "grande", "selva")
felino4 = felinos("Pantera", 'negro', "pantera negra", "grande", "selva")
felino5 = felinos('Jaguar', 'Amarillo con manchas negras', 'jaguar', 'Mediano', 'Selva tropical')
print(f'El nombre del felino es: {felino1.nombre}')
print(f'El nombre del felino es: {felino2.nombre}')
print(f'El nombre del felino es: {felino3.nombre}')
print(f'El nombre del felino es: {felino4.nombre}')
print(f'El nombre del felino es: {felino5.nombre}')
felino3.cazar()
felino4.dormir()
felino5.jugar()