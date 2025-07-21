import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

import mysql.connector
from PIL import Image, ImageTk

ruta_imagen = None  # Variable global para almacenar la ruta de la imagen


def seleccionar_imagen():
    global ruta_imagen
    ruta_imagen = filedialog.askopenfilename(
        initialdir="/Users/Juan Vahir/Downloads/",
        title="Buscar Imagen",
        filetypes=(("Archivos de Imagen", "*.jpg *.jpeg *.png *.gif "),),
    )

    print("Imagen seleccionada:", ruta_imagen)
    if ruta_imagen:
        try:
            # Usar una variable local para el objeto Image
            imagen_pil = Image.open(ruta_imagen)
            imagen_pil.thumbnail((200, 200))
            nuevo_imagen = ImageTk.PhotoImage(imagen_pil)
            label_imagen.config(image=nuevo_imagen)
            label_imagen.image = nuevo_imagen  # Mantener referencia
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")


def guardar_imagen_bd():
    if not ruta_imagen:
        messagebox.showerror(
            "Error de imagen", "Debes de seleccionar una imagen primero"
        )
        return

    try:
        with open(ruta_imagen, "rb") as file:
            imagen_bytes = file.read()
            cn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port=3306,
                database="registro_alumnos_poo",
            )
            miCursor = cn.cursor()
            sql = "INSERT INTO imagens (nombre, imagen) VALUES (%s, %s)"
            # Extraer solo el nombre del archivo de la ruta completa
            nombre_archivo = (
                ruta_imagen.split("/")[-1]
                if "/" in ruta_imagen
                else ruta_imagen.split("\\")[-1]
            )
            valores = (nombre_archivo, imagen_bytes)
            miCursor.execute(sql, valores)
            cn.commit()
            cn.close()  # Cerrar la conexión
            messagebox.showinfo(
                "Éxito", "Imagen guardada correctamente en la base de datos"
            )
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar en la base de datos: {e}")


ventana = tk.Tk()
ventana.title("Guardar Imagen en MySQL")
ventana.geometry("400x400")

boton_seleccionar = tk.Button(
    ventana, text="Seleccionar Imagen", command=seleccionar_imagen
)
boton_seleccionar.pack(pady=20)

label_imagen = tk.Label(ventana)
label_imagen.pack(pady=20)

boton_guardar = tk.Button(
    ventana, text="Guardar Imagen en BD", command=guardar_imagen_bd
)
boton_guardar.pack(pady=20)

ventana.mainloop()
