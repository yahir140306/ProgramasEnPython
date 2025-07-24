import io
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

import mysql.connector
from PIL import Image, ImageTk

ruta_imagen = None


def conectar_bd():
    cn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="registro_alumnos_poo",
    )
    return cn


def seleccionar_imagen():
    global ruta_imagen
    ruta_imagen = filedialog.askopenfilename(
        initialdir="C:/Users/Juan Vahir/Downloads/",
        title="Buscar Imagen",
        filetypes=(("Archivos de Imagen", "*.jpg *.jpeg *.png *.gif "),),
    )

    print("Imagen seleccionada:", ruta_imagen)
    if ruta_imagen:
        try:
            imagen_pil = Image.open(ruta_imagen)
            imagen_pil.thumbnail((200, 200))
            nuevo_imagen = ImageTk.PhotoImage(imagen_pil)
            label_imagen.config(image=nuevo_imagen)
            label_imagen.image = nuevo_imagen
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
            print(f"Tamaño de imagen: {len(imagen_bytes)} bytes")

            cn = conectar_bd()
            print("Conexión exitosa a la base de datos")

            miCursor = cn.cursor()
            sql = "INSERT INTO images (nombre, imagen) VALUES (%s, %s)"
            nombre_archivo = (
                ruta_imagen.split("/")[-1]
                if "/" in ruta_imagen
                else ruta_imagen.split("\\")[-1]
            )

            print(f"Insertando archivo: {nombre_archivo}")
            valores = (nombre_archivo, imagen_bytes)
            miCursor.execute(sql, valores)
            cn.commit()
            cargar_imagenes_bd()

            print(f"Filas afectadas: {miCursor.rowcount}")
            cn.close()

            messagebox.showinfo(
                "Éxito",
                f"Imagen '{nombre_archivo}' guardada correctamente en la base de datos",
            )
    except mysql.connector.Error as db_error:
        print(f"Error de MySQL: {db_error}")
        messagebox.showerror("Error de Base de Datos", f"Error de MySQL: {db_error}")
    except Exception as e:
        print(f"Error general: {e}")
        messagebox.showerror("Error", f"Error al guardar en la base de datos: {e}")


def cargar_imagenes_bd():
    eliminar_datos()
    cn = conectar_bd()
    miCursor = cn.cursor()
    sql = "SELECT  nombre from images"
    miCursor.execute(sql)
    for nombre in miCursor:
        lstImage.insert("", tk.END, text=nombre)
        print(nombre)


def eliminar_datos():
    for item in lstImage.get_children():
        lstImage.delete(item)


def item_seleccionado(event):
    item = lstImage.selection()
    nombre = lstImage.item(item, "text")
    print(nombre)
    buscar_ver_imagen(nombre)


def buscar_ver_imagen(nombre):
    cn = conectar_bd()
    miCursor = cn.cursor()
    sql = "SELECT imagen FROM images WHERE nombre = %s"
    valores = (nombre,)
    miCursor.execute(sql, valores)
    img = miCursor.fetchone()[0]
    miimagen = Image.open(io.BytesIO(img))
    miimagen = miimagen.resize((300, 200))
    foto = ImageTk.PhotoImage(miimagen)
    lblImagenPrevia.config(image=foto)
    lblImagenPrevia.image = foto


ventana = tk.Tk()
ventana.title("Guardar Imagen en MySQL")
ventana.geometry("600x800")

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

frmImage = tk.LabelFrame(ventana, text="Lista de imagenes")
frmImage.pack(fill="x")

lstImage = ttk.Treeview(frmImage)
lstImage.column("#0")
lstImage.heading("#0", text="Nombre")
lstImage.pack(fill="both")

lblImagenPrevia = tk.Label(frmImage, text="Imagen aqui ...")
lblImagenPrevia.pack(fill="both")

cargar_imagenes_bd()

lstImage.bind("<Double-Button-1>", item_seleccionado)

ventana.mainloop()
