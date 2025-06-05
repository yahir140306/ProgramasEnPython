class Persona:
    def __init__(self, nombre: str, apellido: str, curp: str, edad: int, genero: str):
        self.__Nombre = nombre 
        # variable tipo privada se antepone a la variable 2 guiones najo __Nombre
        self.Apellido = apellido
        self.Curp = curp
        self.__Edad = edad
        self.__Genero = genero

    # Getter permite recuperar los valores de variables privadas
    def getNombre(self):
        return self.__Nombre
    
    # set permite asignar 
    def setGenero(self, genero):
        self.__Genero = genero

    def getGenero(self):
        self.__Genero 

    def getEdad(self):
        return self.__Edad 

    def setEdad(self, nuevaEdad):
        self.__Edad = nuevaEdad

    def verDatos(self):
        return (f" Nombre: {self.__Nombre} \n Apellido: {self.Apellido} \n Curp: {self.Curp} \n Edad: {self.__Edad}")

personita = Persona("German", "Guitierrez Gamero", "HBDVJHBVHBDV", 23, "Hombre")

print(personita.getNombre())
print(personita.getGenero())

print("Menu \n 1.-Ver Datos \n 2.-Asignar Genero \n 3.-Salir \n 4.-Cumpleaños")
opcion = int(input("Introduce el numero de la accion a realizar: "))

match(opcion):
    case 1:
        print(personita.verDatos())
    case 2:
        genero = input("Con que genero te identificar F | M | OTRO ? ")
        personita.setGenero(genero)
        print(personita.setGenero(genero))
        print(personita.verDatos())
        print(f"Genero: {personita.getGenero()}")
    case 3:
        pass
    case 4:
        edad = personita.getEdad()
        # personita.setEdad(personita.getEdad() + 1)
        personita.setEdad(edad + 1)
        print(f"Nueva edad: {personita.getEdad()}")