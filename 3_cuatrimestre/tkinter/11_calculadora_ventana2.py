import tkinter as tk

def obtener_valores():
    entrada1 = txtCaja1.get()
    entrada2 = txtCaja2.get()
    try:
        valor1 = float(entrada1)
        txtCaja1.configure(bg="white")
    except ValueError:
        txtCaja1.configure(bg="red")
        valor1 = None

    try:
        valor2 = float(entrada2)
        txtCaja2.configure(bg="white")
    except ValueError:
        txtCaja2.configure(bg="red")
        valor2 = None

    if valor1 is None or valor2 is None:
        etiqueta_resultado.config(text="¡Solo ingrese números!", fg="red")
        return None, None
    return valor1, valor2

def sumar():
    valor1, valor2 = obtener_valores()
    if valor1 is not None:
        etiqueta_resultado.config(text=str(valor1 + valor2), fg="black")

def restar():
    valor1, valor2 = obtener_valores()
    if valor1 is not None:
        etiqueta_resultado.config(text=str(valor1 - valor2), fg="black")

def multiplicar():
    valor1, valor2 = obtener_valores()
    if valor1 is not None:
        etiqueta_resultado.config(text=str(valor1 * valor2), fg="black")

def dividir():
    valor1, valor2 = obtener_valores()
    if valor1 is not None:
        if valor2 == 0:
            etiqueta_resultado.config(text="Error: División por cero", fg="red")
            txtCaja2.configure(bg="red")
        else:
            etiqueta_resultado.config(text=str(valor1 / valor2), fg="black")

# Interfaz
ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("500x500")

etiqueta1 = tk.Label(ventana, text="Número 1:", font=("arial", 20, "bold"))
etiqueta2 = tk.Label(ventana, text="Número 2:", font=("arial", 20, "bold"))
etiqueta_mensaje = tk.Label(ventana, text="El resultado es:", font=("arial", 20, "bold"))
etiqueta_resultado = tk.Label(ventana, text="", font=("arial", 20, "bold"))

txtCaja1 = tk.Entry(ventana, font=("arial", 20, "bold"))
txtCaja2 = tk.Entry(ventana, font=("arial", 20, "bold"))

boton_sumar = tk.Button(ventana, text="+", command=sumar)
boton_restar = tk.Button(ventana, text="-", command=restar)
boton_multiplicar = tk.Button(ventana, text="x", command=multiplicar)
boton_dividir = tk.Button(ventana, text="/", command=dividir)

# Posiciones
etiqueta1.pack()
txtCaja1.pack()
etiqueta2.pack()
txtCaja2.pack()

boton_sumar.place(x=100, y=250)
boton_restar.place(x=150, y=250)
boton_multiplicar.place(x=200, y=250)
boton_dividir.place(x=250, y=250)

etiqueta_mensaje.pack()
etiqueta_resultado.pack()

ventana.mainloop()
