class operaciones:
    def __init__(self, valor1, valor2):
        self.num1 = valor1
        self.num2 = valor2
        
    def sumar(self,valor1, valor2):
        return(valor1+valor2)

    def restar(self,valor1, valor2):
        return(valor1-valor2)

    def multiplicar(self,valor1, valor2):
        return(valor1*valor2)

    def dividir(self,valor1, valor2):
        return(valor1/valor2)


oper= operaciones(4,5)
#resultado = oper.sumar()
print(oper.sumar())
valor1=input("Ingrese el valor: ")
valor2=input("Ingrese el valor: ")

print(oper.restar(valor1,valor2))