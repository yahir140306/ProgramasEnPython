import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import mysql.connector
from PIL import Image, ImageTk
import io

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import os
from datetime import datetime


def generar_pdf():
    # Verificar que haya una mascota seleccionada
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning(
            "Advertencia", "Selecciona una mascota para generar el PDF"
        )
        return

    try:
        # Obtener ID de la mascota seleccionada
        item = tabla.item(seleccion[0])
        id_mascota = item["values"][0]
        print(f"DEBUG: ID mascota seleccionada: {id_mascota}")

        conn = conectar_bd()
        if not conn:
            print("DEBUG: No se pudo conectar a la base de datos")
            return

        cursor = conn.cursor()
        cursor.execute(
            "SELECT nombre, edad, raza, dueno, imagen FROM mascotas WHERE id = %s",
            (id_mascota,),
        )
        mascota = cursor.fetchone()
        conn.close()

        print(f"DEBUG: Datos de mascota obtenidos: {mascota is not None}")

        if not mascota:
            messagebox.showerror("Error", "No se encontró la mascota seleccionada")
            return

        nombre, edad, raza, dueno, imagen_bytes = mascota
        print(f"DEBUG: Mascota - Nombre: {nombre}, Edad: {edad}, Raza: {raza}")

        # Crear archivo PDF en la carpeta de Descargas
        fecha_actual = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"mascota_{nombre}_{fecha_actual}.pdf"
        ruta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")

        # Verificar que la carpeta Downloads existe
        if not os.path.exists(ruta_descargas):
            messagebox.showerror(
                "Error", f"No se encontró la carpeta Downloads: {ruta_descargas}"
            )
            return

        ruta_archivo = os.path.join(ruta_descargas, nombre_archivo)
        print(f"DEBUG: Ruta del archivo PDF: {ruta_archivo}")

        doc = SimpleDocTemplate(ruta_archivo, pagesize=letter)
        elements = []

        # Estilos
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            "CustomTitle",
            parent=styles["Heading1"],
            fontSize=18,
            spaceAfter=20,
            alignment=1,  # Centrado
            textColor=colors.darkblue,
        )

        # Título
        title = Paragraph("Veterinaria Peluditos al Rescate", title_style)
        elements.append(title)

        # Subtítulo
        subtitle = Paragraph("Información de Mascota", styles["Heading2"])
        elements.append(subtitle)
        elements.append(Spacer(1, 20))

        # Información de la mascota
        info_text = f"""
        <b>Nombre:</b> {nombre}<br/>
        <b>Edad:</b> {edad} años<br/>
        <b>Raza:</b> {raza}<br/>
        <b>Dueño:</b> {dueno}<br/>
        <b>Fecha de generación:</b> {datetime.now().strftime("%d/%m/%Y %H:%M")}
        """

        info_paragraph = Paragraph(info_text, styles["Normal"])
        elements.append(info_paragraph)
        elements.append(Spacer(1, 30))

        # Agregar imagen si existe
        temp_path = None  # Variable para rastrear archivo temporal
        if imagen_bytes:
            try:
                # Crear imagen temporal
                import tempfile

                with tempfile.NamedTemporaryFile(
                    delete=False, suffix=".jpg"
                ) as temp_file:
                    temp_file.write(imagen_bytes)
                    temp_path = temp_file.name

                # Agregar imagen al PDF
                from reportlab.platypus import Image as ReportLabImage

                # Verificar que el archivo temporal existe
                if not os.path.exists(temp_path):
                    raise FileNotFoundError(
                        "No se pudo crear el archivo temporal de imagen"
                    )

                img = ReportLabImage(temp_path, width=3 * inch, height=3 * inch)
                elements.append(Paragraph("Fotografía:", styles["Heading3"]))
                elements.append(Spacer(1, 10))
                elements.append(img)

                # NO eliminar archivo temporal aquí - se hará después del build

            except Exception as img_error:
                error_text = Paragraph(
                    f"Error al cargar imagen: {img_error}", styles["Normal"]
                )
                elements.append(error_text)
                # Limpiar archivo temporal si hay error
                if temp_path and os.path.exists(temp_path):
                    os.unlink(temp_path)
                    temp_path = None
        else:
            no_img_text = Paragraph(
                "Esta mascota no tiene imagen registrada.", styles["Normal"]
            )
            elements.append(no_img_text)

        # Generar PDF
        print("DEBUG: Generando PDF...")
        doc.build(elements)
        print("DEBUG: PDF generado exitosamente")

        # Eliminar archivo temporal después de generar el PDF
        if temp_path and os.path.exists(temp_path):
            os.unlink(temp_path)
            print("DEBUG: Archivo temporal eliminado")

        # Verificar que el archivo se creó
        if os.path.exists(ruta_archivo):
            print(
                f"DEBUG: Archivo confirmado. Tamaño: {os.path.getsize(ruta_archivo)} bytes"
            )
        else:
            messagebox.showerror("Error", "El archivo PDF no se creó correctamente")
            return

        # Mensaje de éxito
        messagebox.showinfo("Éxito", f"PDF generado correctamente:\n{ruta_archivo}")

        # Preguntar si quiere abrir el archivo
        respuesta = messagebox.askyesno(
            "Abrir PDF", "¿Desea abrir el archivo PDF generado?"
        )
        if respuesta:
            os.startfile(ruta_archivo)  # Windows

    except Exception as e:
        print(f"DEBUG: Error completo: {str(e)}")
        import traceback

        traceback.print_exc()

        # Limpiar archivo temporal si existe en caso de error general
        if "temp_path" in locals() and temp_path and os.path.exists(temp_path):
            os.unlink(temp_path)
            print("DEBUG: Archivo temporal eliminado por error")

        messagebox.showerror("Error", f"Error al generar PDF: {e}")


# Variables globales
ruta_imagen = None


def conectar_bd():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port=3306,
            database="veterinaria_peluditos",
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror(
            "Error de conexión", f"No se pudo conectar a la base de datos: {e}"
        )
        return None


def solo_numeros(texto):
    return texto.isdigit() or texto == ""


def seleccionar_imagen():
    global ruta_imagen
    ruta_imagen = filedialog.askopenfilename(
        initialdir="C:/Users/Juan Vahir/Downloads/",
        title="Seleccionar imagen de mascota",
        filetypes=(("Archivos de Imagen", "*.jpg *.jpeg *.png *.gif"),),
    )

    if ruta_imagen:
        try:
            imagen_pil = Image.open(ruta_imagen)
            imagen_pil.thumbnail((150, 150))
            imagen_tk = ImageTk.PhotoImage(imagen_pil)
            label_imagen.config(image=imagen_tk, text="")
            label_imagen.image = imagen_tk
            btn_cargar_imagen.config(text="Cambiar imagen")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")


def guardar_mascota():
    nombre = entry_nombre.get().strip()
    dueno = entry_dueno.get().strip()
    edad = entry_edad.get().strip()
    raza = entry_raza.get().strip()

    if not nombre or not dueno or not edad or not raza:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    try:
        conn = conectar_bd()
        if not conn:
            return

        cursor = conn.cursor()

        imagen_bytes = None
        if ruta_imagen:
            with open(ruta_imagen, "rb") as file:
                imagen_bytes = file.read()

        sql = "INSERT INTO mascotas (nombre, dueno, edad, raza, imagen) VALUES (%s, %s, %s, %s, %s)"
        valores = (nombre, dueno, int(edad), raza, imagen_bytes)

        cursor.execute(sql, valores)
        conn.commit()

        messagebox.showinfo("Éxito", "Mascota guardada correctamente")
        limpiar_campos()
        cargar_mascotas()

        conn.close()

    except mysql.connector.Error as e:
        messagebox.showerror("Error de BD", f"Error al guardar mascota: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Error inesperado: {e}")


def limpiar_campos():
    global ruta_imagen
    entry_nombre.delete(0, tk.END)
    entry_dueno.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    entry_raza.delete(0, tk.END)
    ruta_imagen = None
    label_imagen.config(image="", text="Sin imagen")
    label_imagen.image = None
    btn_cargar_imagen.config(text="Cargar imagen")


def cargar_mascotas():
    try:
        conn = conectar_bd()
        if not conn:
            return

        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, nombre, edad, raza, dueno, imagen FROM mascotas ORDER BY id DESC"
        )
        mascotas = cursor.fetchall()

        for item in tabla.get_children():
            tabla.delete(item)

        for mascota in mascotas:
            id_mascota, nombre, edad, raza, dueno, imagen = mascota
            estado_imagen = "Sí" if imagen else "No"
            tabla.insert(
                "", "end", values=(id_mascota, nombre, edad, raza, dueno, estado_imagen)
            )

        conn.close()

    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"Error al cargar mascotas: {e}")


def ver_imagen_seleccionada():
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning(
            "Advertencia", "Selecciona una mascota para ver su imagen"
        )
        return

    item = tabla.item(seleccion[0])
    id_mascota = item["values"][0]

    try:
        conn = conectar_bd()
        if not conn:
            return

        cursor = conn.cursor()
        cursor.execute(
            "SELECT nombre, imagen FROM mascotas WHERE id = %s", (id_mascota,)
        )
        resultado = cursor.fetchone()

        if resultado and resultado[1]:
            nombre, imagen_bytes = resultado

            ventana_imagen = tk.Toplevel(root)
            ventana_imagen.title(f"Imagen de {nombre}")
            ventana_imagen.geometry("400x400")

            imagen_pil = Image.open(io.BytesIO(imagen_bytes))
            imagen_pil.thumbnail((350, 350))
            imagen_tk = ImageTk.PhotoImage(imagen_pil)

            label_img = tk.Label(ventana_imagen, image=imagen_tk)
            label_img.image = imagen_tk
            label_img.pack(pady=20)

        else:
            messagebox.showinfo("Info", "Esta mascota no tiene imagen")

        conn.close()

    except Exception as e:
        messagebox.showerror("Error", f"Error al mostrar imagen: {e}")


root = tk.Tk()
root.title("Veterinaria Peluditos al Rescate")
root.geometry("1000x700")
root.configure(bg="#f0f0f0")

titulo = tk.Label(
    root,
    text="Veterinaria Peluditos al Rescate",
    font=("Arial", 24, "bold"),
)
titulo.pack(pady=20)

frame_principal = tk.Frame(root, bg="#f0f0f0")
frame_principal.pack(padx=20, pady=10, fill="both", expand=True)

frame_datos = tk.LabelFrame(
    frame_principal,
    text="Datos de la Mascota",
    font=("Arial", 14, "bold"),
)
frame_datos.pack(fill="x", pady=(0, 10))

frame_interno = tk.Frame(frame_datos, bg="#f0f0f0")
frame_interno.pack(padx=10, pady=10, fill="both")

frame_campos = tk.Frame(frame_interno, bg="#f0f0f0")
frame_campos.pack(side="left", fill="both", expand=True)

tk.Label(frame_campos, text="Nombre:", font=("Arial", 10), bg="#f0f0f0").grid(
    row=0, column=0, sticky="w", pady=5
)
entry_nombre = tk.Entry(frame_campos, font=("Arial", 10), width=25)
entry_nombre.grid(row=0, column=1, padx=(10, 20), pady=5)

tk.Label(frame_campos, text="Dueño:", font=("Arial", 10), bg="#f0f0f0").grid(
    row=1, column=0, sticky="w", pady=5
)
entry_dueno = tk.Entry(frame_campos, font=("Arial", 10), width=25)
entry_dueno.grid(row=1, column=1, padx=(10, 20), pady=5)

tk.Label(frame_campos, text="Edad:", font=("Arial", 10), bg="#f0f0f0").grid(
    row=2, column=0, sticky="w", pady=5
)
vcmd = (root.register(solo_numeros), "%P")
entry_edad = tk.Entry(
    frame_campos, font=("Arial", 10), width=25, validate="key", validatecommand=vcmd
)
entry_edad.grid(row=2, column=1, padx=(10, 20), pady=5)

tk.Label(frame_campos, text="Raza:", font=("Arial", 10), bg="#f0f0f0").grid(
    row=3, column=0, sticky="w", pady=5
)
entry_raza = tk.Entry(frame_campos, font=("Arial", 10), width=25)
entry_raza.grid(row=3, column=1, padx=(10, 20), pady=5)

frame_imagen = tk.Frame(frame_interno, bg="#f0f0f0")
frame_imagen.pack(side="right", padx=(20, 0))

tk.Label(
    frame_imagen,
    text="Ver imagen de mascota",
    font=("Arial", 12, "bold"),
).pack(pady=(0, 10))

label_imagen = tk.Label(
    frame_imagen, text="Sin imagen", width=20, height=8, relief="solid", bg="white"
)
label_imagen.pack(pady=(0, 10))

btn_cargar_imagen = tk.Button(
    frame_imagen,
    text="Cargar imagen",
    command=seleccionar_imagen,
    font=("Arial", 10),
)
btn_cargar_imagen.pack()

btn_guardar = tk.Button(
    frame_principal,
    text="Guardar Mascota",
    command=guardar_mascota,
    font=("Arial", 12, "bold"),
    pady=5,
)
btn_guardar.pack(pady=10)

frame_listado = tk.LabelFrame(
    frame_principal,
    text="Listado de Mascotas",
    font=("Arial", 14, "bold"),
)
frame_listado.pack(fill="both", expand=True, pady=(10, 0))

tabla = ttk.Treeview(
    frame_listado,
    columns=("Nombre", "Edad", "Raza", "Dueño", "Imagen"),
    show="headings",
    height=10,
)

# Configurar encabezados
# tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.heading("Raza", text="Raza")
tabla.heading("Dueño", text="Dueño")
tabla.heading("Imagen", text="Imagen")

# Configurar anchos
# tabla.column("ID", width=50)
tabla.column("Nombre", width=120)
tabla.column("Edad", width=80)
tabla.column("Raza", width=120)
tabla.column("Dueño", width=120)
tabla.column("Imagen", width=80)


frame_botones = tk.Frame(frame_listado, bg="#f0f0f0")
frame_botones.pack(pady=(0, 10))

# Botón para ver imagen
btn_ver_imagen = tk.Button(
    frame_botones,
    text="Ver Imagen Seleccionada",
    command=ver_imagen_seleccionada,
    bg="#e74c3c",
    fg="white",
    font=("Arial", 10),
    padx=10,
)
btn_ver_imagen.pack(side="left", padx=(0, 10))

# Botón para generar PDF
btn_generar_pdf = tk.Button(
    frame_botones,
    text="Generar PDF",
    command=generar_pdf,
    bg="#9b59b6",
    fg="white",
    font=("Arial", 10),
    padx=20,
)
btn_generar_pdf.pack(side="left")
# Scrollbar para la tabla
scrollbar = ttk.Scrollbar(frame_listado, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)

tabla.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y", pady=10)

# # Botón para ver imagen
# btn_ver_imagen = tk.Button(
#     frame_listado,
#     text="Ver Imagen Seleccionada",
#     command=ver_imagen_seleccionada,
# )
# btn_ver_imagen.pack(pady=(0, 10))

# Cargar mascotas al iniciar
cargar_mascotas()

root.mainloop()
