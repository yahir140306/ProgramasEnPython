import tkinter as tk
from tkinter import ttk
import json 
import os

ventana = tk.Tk()
ventana.title("Agenda de Contactos")
ventana.geometry("800x400")

lbltitulo = tk.Label(ventana, text="Agenda de Contactos", font=("arial", 20, "bold"))
lblnombre = tk.Label(ventana, text="Nombre:")   
lblapellido = tk.Label(ventana, text="Apellido: ")
lbltelefono = tk.Label(ventana, text="Teléfono:")
cbbsexo = ttk.Combobox(state="readonly", values=["Hombre", "Mujer"])
cbbsexo.set("Seleccione su sexo:")

lblcontactos = tk.Label(ventana, text="", font=("arial", 15, "bold"))

txtnombre = tk.Entry(ventana)
txtapellido = tk.Entry(ventana)
txttelefono = tk.Entry(ventana)
# txtsexo = tk.Entry(ventana)

btnagregar = tk.Button(ventana, text="Agregar Contacto")

contactos = []

def guardar_contactos():
    with open("contactos.json", "w") as archivo:
        json.dump(contactos, archivo, indent=4)

def cargar_contactos():
    if os.path.exists("contactos.json"):
        with open("contactos.json", "r") as archivo:
            return json.load(archivo)
    return []

def actualizar_tabla():
    for fila in tabla.get_children():
        tabla.delete(fila)
    for contacto in contactos:
        tabla.insert("", "end", values=(contacto["nombre"], contacto["apellido"], contacto["telefono"], contacto["sexo"]))

def AgregarContacto(event):
    nombre = txtnombre.get()
    telefono = txttelefono.get()
    apellido = txtapellido.get()
    sexo = cbbsexo.get()
    if nombre and telefono and apellido and sexo != "Seleccione su sexo:":
        nuevo = {
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "sexo": sexo
        }
        # contactos.append(f"{nombre} - {apellido} - {telefono} - {sexo}")
        contactos.append(nuevo)
        guardar_contactos()
        actualizar_tabla()
        txtnombre.delete(0, tk.END)
        txtapellido.delete(0, tk.END)
        txttelefono.delete(0, tk.END)
        cbbsexo.set("Seleccione su sexo:")

def ActualizarContactos():
    lblcontactos.config(text="Contactos:\n" + "\n".join(contactos))
btnagregar.bind("<Button-1>", AgregarContacto)


frm_tabla = tk.Frame(ventana)
frm_tabla.pack(fill="both", expand=True)
tabla = ttk.Treeview(ventana, columns=("Nombre", "Apellido", "Telefono", "Sexo"), show="headings")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Apellido", text="Apellido")
tabla.heading("Telefono", text="Telefono")
tabla.heading("Sexo", text="Sexo")


lbltitulo.pack()

lblnombre.pack()
txtnombre.pack()

lblapellido.pack()
txtapellido.pack()

lbltelefono.pack()
txttelefono.pack()

cbbsexo.pack()
# txtsexo.pack()

btnagregar.pack()
lblcontactos.pack()
tabla.pack(fill="both", expand=True)

contactos = cargar_contactos()
actualizar_tabla()


ventana.mainloop()
