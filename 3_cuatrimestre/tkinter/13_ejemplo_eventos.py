import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Eventos")
ventana.geometry("300x300")

lbltitulo = tk.Label(ventana, text="Eventos", font=("arial", 20, "bold"))
btnAceptar = tk.Button(ventana, text="Aceptar")

def DarClick(event):
    messagebox.showinfo("Evento", "Has hecho click en el botón Aceptar")

btnAceptar.bind("<Button-1>", DarClick)

lbltitulo.pack()
btnAceptar.pack()

ventana.mainloop()
