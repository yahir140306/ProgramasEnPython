import tkinter as tk
import time

miVentana = tk.Tk()
miVentana.title("Ventana")
miVentana.geometry("400x400")
miVentana.minsize(600,600)
miVentana.configure(bg="lightblue")


etiqueta = tk.Label(miVentana, text="Hola, soy una etiqueta")
etiqueta2 = tk.Label(miVentana, text="")
etiqueta.pack()
etiqueta.configure(fg="blue", bg="yellow", text="Nacimos pobres pero morimos ricos", font=("Arial", "0", "bold"))

miButton = tk.Button(miVentana, text="Dar click")
txtCaja = tk.Entry()
txtCaja.configure(font=("arial", "20", "bold"))

txtCaja.pack()
# etiqueta.pack()
miButton.pack()
etiqueta2.pack()

def obtenerDatos():
    mensaje = f"Bienvenid@ {txtCaja.get()}"
    # etiqueta2.configure(text=txtCaja.get(), font=("arial", "20", "bold"))
    etiqueta2.configure(text=mensaje, font=("arial", "20", "bold"))
    # print(txtCaja.get())

miButton.configure(command=obtenerDatos)


def actualizarHora(color = "yellow"):
    # color = "yellow"
    if color == "yellow":
        color = "red"
    else:
        color = "yellow"          
    etiqueta.configure(fg="blue", bg=color, text=time.strftime("%H:%M:%S"), font=("Arial", "60", "bold"))
    miVentana.after(1000, actualizarHora, color)


actualizarHora()
miVentana.mainloop()




