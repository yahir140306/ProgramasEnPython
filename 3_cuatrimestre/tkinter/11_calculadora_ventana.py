import tkinter as tk
def validar_numero(valor):
    if valor == "":
        return True
    try:
        float(valor)
        return True
    except ValueError:
        return False

ventana = tk.Tk()
ventana.title("Calduora Basica")
ventana.geometry("500x500")

etiqueta1 = tk.Label(ventana, text="Numero 1: ", font=("arial", "20", "bold"))
etiqueta2 = tk.Label(ventana, text="Numero 2: ", font=("arial", "20", "bold"))
etiqueta_mensaje = tk.Label(ventana, text="El resultado es: ")
etiqueta_resultado = tk.Label(ventana, text="")

txtCaja1 = tk.Entry()
txtCaja1.configure(font=("arial", "20", "bold"))
txtCaja2 = tk.Entry()
txtCaja2.configure(font=("arial", "20", "bold"))
# txt_resultado = tk.Entry()
# txt_resultado.configure(font=("arial", "20", "bold"))
etiqueta_mensaje.configure(font=("arial", "20", "bold"))


boton_sumar = tk.Button(ventana, text="+")
boton_restar = tk.Button(ventana, text="-")
boton_multiplicar = tk.Button(ventana, text="x")
boton_dividir = tk.Button(ventana, text="/")

# posiciones
boton_sumar.place(x=100,y=250)
boton_restar.place(x=150,y=250)
boton_multiplicar.place(x=200,y=250)
boton_dividir.place(x=250,y=250)
# etiqueta_resultado.place(x=150, y=200)

def obtener_valores():
    entrada1 = txtCaja1.get()
    entrada2 = txtCaja2.get()
    try:
        valor1 = float(entrada1)
        # txtCaja1.configure(bg="white")
    except ValueError:
        txtCaja1.configure(bg="red")
        valor1 = None

    try:
        valor2 = float(entrada2)
        # txtCaja2.configure(bg="white")
    except ValueError:
        txtCaja2.configure(bg="red")
        valor2 = None

    if valor1 is None or valor2 is None:
        etiqueta_resultado.config(text="¡Solo ingrese números!", fg="red")
        return None, None
    return valor1, valor2


def sumar():
    valor1 = float(txtCaja1.get())
    valor2 = float(txtCaja2.get())
    resultado = valor1 + valor2
    etiqueta_resultado.configure(text=str(resultado), font=("arial", "20", "bold"))
    
def restar():
    valor1 = float(txtCaja1.get())
    valor2 = float(txtCaja2.get())
    resultado = valor1 - valor2
    etiqueta_resultado.configure(text=str(resultado), font=("arial", "20", "bold"))
    
def multiplicar():
    valor1 = float(txtCaja1.get())
    valor2 = float(txtCaja2.get())
    resultado = valor1 * valor2
    etiqueta_resultado.configure(text=str(resultado), font=("arial", "20", "bold"))
    
def dividir():
    valor1 = float(txtCaja1.get())
    valor2 = float(txtCaja2.get())
    if valor2 == 0:
        etiqueta_resultado.configure(text="Error: División por cero", font=("arial", "20", "bold"))
        txtCaja1.configure(bg="red")
        txtCaja2.configure(bg="red")
        return
    else:
        resultado = valor1 / valor2
    etiqueta_resultado.configure(text=str(resultado), font=("arial", "20", "bold"))
    

boton_sumar.configure(command=sumar)
boton_restar.configure(command=restar)
boton_multiplicar.configure(command=multiplicar)
boton_dividir.configure(command=dividir)

# mostrar los elementos
etiqueta1.pack()
txtCaja1.pack()

etiqueta2.pack()
txtCaja2.pack()


# boton_sumar.pack()
# boton_restar.pack()
# boton_multiplicar.pack()
# boton_dividir.pack()

etiqueta_mensaje.pack()
etiqueta_resultado.pack()
# txt_resultado.pack()

ventana.mainloop()