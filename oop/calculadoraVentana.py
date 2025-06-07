import tkinter as tk

ventana = tk.Tk()
ventana.title("Calduora Basica")
ventana.geometry("500x500")

etiqueta1 = tk.Label(ventana, text="Numero 1: ")
etiqueta2 = tk.Label(ventana, text="Numero 2: ")
etiqueta_mensaje = tk.Label(ventana, text="El resultado es: ")

txtCaja1 = tk.Entry()
txtCaja1.configure(font=("arial", "20", "bold"))
txtCaja2 = tk.Entry()
txtCaja2.configure(font=("arial", "20", "bold"))
txt_resultado = tk.Entry()
txt_resultado.configure(font=("arial", "20", "bold"))

boton_sumar = tk.Button(ventana, text="+")
boton_restar = tk.Button(ventana, text="-")
boton_multiplicar = tk.Button(ventana, text="x")
boton_dividir = tk.Button(ventana, text="/")

# posiciones
boton_sumar.place(x=100,y=200)
boton_restar.place(x=200,y=300)
boton_multiplicar.place(x=300,y=400)
boton_dividir.place(x=400,y=500)

def sumar():
    valor1 = float(txtCaja1.get())
    valor2 = float(txtCaja2.get())
    resultado = valor1 + valor2
    etiqueta_mensaje.configure(text=str(resultado), font=("arial", "20", "bold"))
    
def restar():
    valor1 = float(txtCaja1.get())
    valor2 = float(txtCaja2.get())
    resultado = valor1 - valor2
    etiqueta_mensaje.configure(text=str(resultado), font=("arial", "20", "bold"))
    
def multiplicar():
    valor1 = float(txtCaja1.get())
    valor2 = float(txtCaja2.get())
    resultado = valor1 * valor2
    etiqueta_mensaje.configure(text=str(resultado), font=("arial", "20", "bold"))
    
def dividir():
    valor1 = float(txtCaja1.get())
    valor2 = float(txtCaja2.get())
    resultado = valor1 / valor2
    etiqueta_mensaje.configure(text=str(resultado), font=("arial", "20", "bold"))
    

boton_sumar.configure(command=sumar)
boton_restar.configure(command=restar)
boton_multiplicar.configure(command=multiplicar)
boton_dividir.configure(command=dividir)

# mostrar los elementos
etiqueta1.pack()
txtCaja1.pack()

etiqueta2.pack()
txtCaja2.pack()


boton_sumar.pack()
boton_restar.pack()
boton_multiplicar.pack()
boton_dividir.pack()

etiqueta_mensaje.pack()
txt_resultado.pack()

ventana.mainloop()