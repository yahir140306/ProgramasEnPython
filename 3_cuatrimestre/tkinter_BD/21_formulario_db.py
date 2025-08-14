import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import os
from insertar_datos_formulario_db import (
    insertar_alumno,
    obtener_alumnos,
    verificar_matricula_existe,
    obtener_alumno_por_matricula,
    actualizar_alumno,
    eliminar_alumno,
    verificar_matricula_existe_excepto,
)

# Imports para PDF
try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
        Image as ReportLabImage,
    )
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib import colors
    from reportlab.lib.units import inch
    from PIL import Image as PILImage  # Para obtener dimensiones de imágenes

    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print(
        "ReportLab no está instalado. Para usar la función PDF, instala con: pip install reportlab"
    )

root = tk.Tk()
root.title("Registro de Alumnos")
root.geometry("1100x600")

# Crear directorios necesarios para imágenes
current_dir = os.path.dirname(__file__)
fotos_dir = os.path.join(current_dir, "fotos")
if not os.path.exists(fotos_dir):
    os.makedirs(fotos_dir)

frame = tk.Frame(root)
frame.grid(padx=10, pady=10)

# Variable para controlar si estamos editando
editando = False
matricula_original = None


def solo_numeros(texto):
    return texto.isdigit() or texto == ""


tk.Label(frame, text="Registro de Alumnos", font=("Arial", 18, "bold")).grid(
    row=0, column=0, columnspan=4, pady=(0, 10)
)

hoy = datetime.now()
fecha_formato = hoy.strftime("%d/%m/%Y")

tk.Label(frame, text=f"Fecha: {fecha_formato}").grid(row=0, column=4, sticky="e")

tk.Label(frame, text="Matricula:").grid(row=1, column=0, sticky="w")
vcmd = (root.register(solo_numeros), "%P")  # Validación: solo números
entry_matricula = tk.Entry(frame, validate="key", validatecommand=vcmd)
entry_matricula.grid(row=1, column=1)

tk.Label(frame, text="Nombre:").grid(row=2, column=0, sticky="w")
entry_nombre = tk.Entry(frame)
entry_nombre.grid(row=2, column=1)

tk.Label(frame, text="Apellido:").grid(row=2, column=2, sticky="w")
entry_apellido = tk.Entry(frame)
entry_apellido.grid(row=2, column=3)

tk.Label(frame, text="Fecha Nacimiento (YYYY-MM-DD):").grid(row=4, column=0, sticky="w")
entry_fecha_nac = tk.Entry(frame)
entry_fecha_nac.grid(row=4, column=1)

tk.Label(frame, text="Sexo:").grid(row=4, column=2, sticky="w")
sexo_var = tk.StringVar()
tk.Radiobutton(frame, text="Mujer", variable=sexo_var, value="Mujer").grid(
    row=4, column=3, sticky="w"
)
tk.Radiobutton(frame, text="Hombre", variable=sexo_var, value="Hombre").grid(
    row=4, column=4, sticky="w"
)

tk.Label(frame, text="Dirección:").grid(row=6, column=0, sticky="w")

carreras_por_direccion = {
    "Ciencias Económico Administrativas": [
        "Maestría en Innovación y Negocios",
        "Licenciatura en Administración",
        "Licenciatura en Contaduría",
        "Licenciatura en Negocios y Mercadotecnia",
    ],
    "Ciencias Naturales e Ingeniería": [
        "Maestría en Sistemas de Gestión Ambiental",
        "Licenciatura en Ingeniería en Manejo de Recursos Naturales",
        "Licenciatura en Ingeniería en Mantenimiento Industrial",
        "Licenciatura en Ingeniería Civil",
    ],
    "Tecnologias de la Información": [
        "Licenciatura en Ingeniería en Tecnologías de la Información e Innovación Digital",
        "Licenciatura en Ingeniería Mecatrónica",
    ],
    "Ciencias Exactas": [
        "Licenciatura en Ingeniería Mecánica",
        "Licenciatura en Ingeniería Industrial",
        "Licenciatura en Ingeniería en Diseño Textil y Moda",
    ],
    "Ciencias de la Salud": [
        "Licenciatura en Terapia Física",
        "Licenciatura en Enfermería",
        "Licenciatura en Médico Cirujano y Partero",
    ],
}


def actualizar_carreras(event):
    direccion_seleccionada = cbb_direccion.get()
    if direccion_seleccionada in carreras_por_direccion:
        cbb_carrera["values"] = carreras_por_direccion[direccion_seleccionada]
        cbb_carrera.set("Seleccione carrera...")
    else:
        cbb_carrera["values"] = []
        cbb_carrera.set("")


cbb_direccion = ttk.Combobox(
    frame, state="readonly", values=list(carreras_por_direccion.keys()), width="30"
)
cbb_direccion.grid(row=6, column=1, padx=20, pady=20, sticky="w")
cbb_direccion.set("Seleccione...")
cbb_direccion.bind("<<ComboboxSelected>>", actualizar_carreras)

tk.Label(frame, text="Carrera:").grid(row=6, column=2, sticky="w", padx=20, pady=20)
cbb_carrera = ttk.Combobox(frame, state="readonly", width="50")
cbb_carrera.grid(row=6, column=3, padx=20, pady=20, sticky="w")
cbb_carrera.set("Seleccione carrera...")


def validar_fecha(fecha_str):
    try:
        from datetime import datetime

        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def cargar_alumnos():
    try:
        alumnos = obtener_alumnos()
        for item in tabla.get_children():
            tabla.delete(item)

        for alumno in alumnos:
            tabla.insert("", "end", values=alumno)
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar alumnos: {str(e)}")


def limpiar_campos():
    """Limpia todos los campos del formulario"""
    entry_matricula.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_apellido.delete(0, tk.END)
    entry_fecha_nac.delete(0, tk.END)
    sexo_var.set("")
    cbb_direccion.set("Seleccione...")
    cbb_carrera.set("Seleccione carrera...")


def agregar_alumno():
    global editando, matricula_original

    matricula = entry_matricula.get().strip()
    nombre = entry_nombre.get().strip()
    apellido = entry_apellido.get().strip()
    fecha_nac = entry_fecha_nac.get().strip()
    sexo = sexo_var.get()
    direccion = cbb_direccion.get()
    carrera = cbb_carrera.get()

    if not (
        matricula
        and nombre
        and apellido
        and fecha_nac
        and sexo
        and direccion
        and carrera
    ):
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return

    if not validar_fecha(fecha_nac):
        messagebox.showerror(
            "Error", "La fecha debe tener el formato YYYY-MM-DD (ejemplo: 2000-01-15)"
        )
        return

    try:
        if editando:
            if matricula != matricula_original and verificar_matricula_existe_excepto(
                matricula, matricula_original
            ):
                messagebox.showerror("Error", f"La matrícula {matricula} ya existe.")
                return

            actualizar_alumno(
                matricula_original,
                matricula,
                nombre,
                apellido,
                fecha_nac,
                sexo,
                direccion,
                carrera,
            )
            messagebox.showinfo("Éxito", "Alumno actualizado correctamente.")

            editando = False
            matricula_original = None
            btn_agregar.config(text="Agregar Alumno")
            btn_cancelar.pack_forget()

        else:
            if verificar_matricula_existe(matricula):
                messagebox.showerror("Error", f"La matrícula {matricula} ya existe.")
                return

            insertar_alumno(
                matricula, nombre, apellido, fecha_nac, sexo, direccion, carrera
            )
            messagebox.showinfo("Éxito", "Alumno agregado correctamente.")

        cargar_alumnos()
        limpiar_campos()

    except Exception as e:
        messagebox.showerror("Error de base de datos", str(e))


def editar_alumno():
    global editando, matricula_original

    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione un alumno para editar.")
        return

    item = tabla.item(seleccion[0])
    valores = item["values"]
    matricula = valores[0]

    try:
        alumno = obtener_alumno_por_matricula(matricula)
        if alumno:
            limpiar_campos()
            entry_matricula.insert(0, alumno[0])
            entry_nombre.insert(0, alumno[1])
            entry_apellido.insert(0, alumno[2])
            entry_fecha_nac.insert(0, alumno[3])
            sexo_var.set(alumno[4])
            cbb_direccion.set(alumno[5])

            if alumno[5] in carreras_por_direccion:
                cbb_carrera["values"] = carreras_por_direccion[alumno[5]]
                cbb_carrera.set(alumno[6])

            editando = True
            matricula_original = alumno[0]
            btn_agregar.config(text="Actualizar Alumno")
            btn_cancelar.pack(side="left", padx=5)

    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar datos del alumno: {str(e)}")


def eliminar_alumno_seleccionado():
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Seleccione un alumno para eliminar.")
        return

    item = tabla.item(seleccion[0])
    valores = item["values"]
    matricula = valores[0]
    nombre = valores[1]
    apellido = valores[2]

    respuesta = messagebox.askyesno(
        "Confirmar eliminación",
        f"¿Está seguro de que desea eliminar al alumno {nombre} {apellido} con matrícula {matricula}?",
    )

    if respuesta:
        try:
            eliminar_alumno(matricula)
            messagebox.showinfo("Éxito", "Alumno eliminado correctamente.")
            cargar_alumnos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar alumno: {str(e)}")


def cancelar_edicion():
    global editando, matricula_original

    editando = False
    matricula_original = None
    btn_agregar.config(text="Agregar Alumno")
    btn_cancelar.pack_forget()
    limpiar_campos()


def generar_historial_academico():
    """Genera el historial académico en PDF del alumno seleccionado"""
    if not REPORTLAB_AVAILABLE:
        messagebox.showerror(
            "Error", "ReportLab no está instalado.\nInstala con: pip install reportlab"
        )
        return

    # Verificar que hay un alumno seleccionado
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning(
            "Advertencia", "Selecciona un alumno para generar su historial académico"
        )
        return

    item = tabla.item(seleccion[0])
    valores = item["values"]
    matricula = valores[0]

    try:
        # Obtener datos del alumno
        alumno = obtener_alumno_por_matricula(matricula)
        if not alumno:
            messagebox.showerror("Error", "No se encontró el alumno seleccionado")
            return

        # Datos del alumno
        datos_alumno = {
            "nombre": f"{alumno[1]} {alumno[2]}",  # nombre + apellido
            "curp": "CURP123456789",  # Ejemplo, debes agregarlo a tu BD
            "matricula": alumno[0],
            "sexo": alumno[4],
            "carrera": alumno[6],
            "direccion": alumno[5],
        }

        # Obtener calificaciones reales de la base de datos
        try:
            from insertar_datos_formulario_db import obtener_calificaciones_alumno

            calificaciones_bd = obtener_calificaciones_alumno(matricula)

            # Convertir a formato de tuplas (materia, calificacion)
            if calificaciones_bd:
                materias = [
                    (materia, float(calificacion))
                    for materia, calificacion, _ in calificaciones_bd
                ]
            else:
                # Si no hay calificaciones, usar materias sin calificaciones
                materias = [
                    ("Bases de datos", None),
                    ("Desarrollo y pensamientos y toma de decisiones", None),
                    ("Inglés 3", None),
                    ("Programación orientada a objetos", None),
                    ("Proyecto integrador I", None),
                    ("Tópicos de calidad para el diseño de software", None),
                ]
        except Exception as e:
            print(f"Error al obtener calificaciones: {e}")
            # Usar datos por defecto en caso de error
            materias = [
                ("Bases de datos", None),
                ("Desarrollo y pensamientos y toma de decisiones", None),
                ("Inglés 3", None),
                ("Programación orientada a objetos", None),
                ("Proyecto integrador I", None),
                ("Tópicos de calidad para el diseño de software", None),
            ]

        # Calcular promedio solo si hay calificaciones
        calificaciones_validas = [
            calificacion for _, calificacion in materias if calificacion is not None
        ]
        if calificaciones_validas:
            promedio = sum(calificaciones_validas) / len(calificaciones_validas)
        else:
            promedio = 0.0

        # Generar PDF con fecha en español
        # Diccionario de meses en español
        meses_es = {
            "January": "enero",
            "February": "febrero",
            "March": "marzo",
            "April": "abril",
            "May": "mayo",
            "June": "junio",
            "July": "julio",
            "August": "agosto",
            "September": "septiembre",
            "October": "octubre",
            "November": "noviembre",
            "December": "diciembre",
        }

        fecha_obj = datetime.now()
        dia = fecha_obj.strftime("%d")
        mes_en = fecha_obj.strftime("%B")  # Mes en inglés
        mes_es = meses_es.get(mes_en, mes_en.lower())  # Convertir a español
        año = fecha_obj.strftime("%Y")

        # Formatear fecha con día y mes en negritas
        fecha_formateada = f"<b>{dia} de</b> <b>{mes_es}</b> de {año}"

        nombre_archivo = f"historial_academico_{datos_alumno['matricula']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        ruta_descargas = os.path.join(os.path.expanduser("~"), "Downloads")
        ruta_archivo = os.path.join(ruta_descargas, nombre_archivo)

        doc = SimpleDocTemplate(ruta_archivo, pagesize=letter, topMargin=0.5 * inch)
        elements = []
        styles = getSampleStyleSheet()

        # Estilo centrado
        centered_style = ParagraphStyle(
            "Centered", parent=styles["Normal"], alignment=1, fontSize=12
        )

        # Estilo para fecha (alineado a la derecha)
        right_style = ParagraphStyle(
            "Right", parent=styles["Normal"], alignment=2, fontSize=10
        )

        # Estilo para títulos
        title_style = ParagraphStyle(
            "Title",
            parent=styles["Heading1"],
            alignment=1,
            fontSize=16,
            textColor=colors.darkblue,
        )

        # Logo centrado (usar logos.png existente)
        logo_path = os.path.join(os.path.dirname(__file__), "logos.png")
        if os.path.exists(logo_path):
            try:
                # Obtener dimensiones originales del logo para mantener proporciones
                with PILImage.open(logo_path) as img:
                    original_width, original_height = img.size

                # Configurar ancho deseado (más ancho para que se extienda horizontalmente)
                desired_width = 6.5 * inch  # Ancho más grande - aumentado de 5 a 6.5

                # Calcular altura proporcional
                aspect_ratio = original_height / original_width
                calculated_height = desired_width * aspect_ratio

                # Limitar altura máxima para que no sea demasiado alta
                max_height = 2.5 * inch  # También aumenté un poco la altura máxima
                if calculated_height > max_height:
                    calculated_height = max_height
                    desired_width = calculated_height / aspect_ratio

                elements.append(
                    ReportLabImage(
                        logo_path, width=desired_width, height=calculated_height
                    )
                )
                elements.append(Spacer(1, 12))
            except Exception:
                # Si hay error con las dimensiones, usar tamaño fijo más ancho
                elements.append(
                    ReportLabImage(logo_path, width=6.5 * inch, height=2 * inch)
                )
                elements.append(Spacer(1, 12))
        else:
            # Si no hay logo, agregar título de la institución
            elements.append(
                Paragraph(
                    "UNIVERSIDAD TECNOLÓGICA DE LA SIERRA HIDALGUENSE", title_style
                )
            )
            elements.append(Spacer(1, 12))

        # Fecha alineada a la derecha
        elements.append(
            Paragraph(f"Zacualtipán de Ángeles Hgo., a {fecha_formateada}", right_style)
        )
        elements.append(Spacer(1, 20))

        # Foto del estudiante centrada (opcional)
        foto_path = os.path.join(
            os.path.dirname(__file__), f"fotos/{datos_alumno['matricula']}.jpg"
        )
        if os.path.exists(foto_path):
            elements.append(
                ReportLabImage(foto_path, width=1.5 * inch, height=2 * inch)
            )
            elements.append(Spacer(1, 15))

        # Subtítulo "DATOS DEL ESTUDIANTE"
        subtitle_style = ParagraphStyle(
            "Subtitle",
            parent=styles["Heading2"],
            alignment=1,
            fontSize=12,  # Reducido de 14 a 12
            textColor=colors.black,  # Cambiado de darkblue a black
            fontName="Helvetica-Bold",  # Agregado para negritas
        )
        elements.append(Paragraph("Datos del estudiante", subtitle_style))
        elements.append(Spacer(1, 15))

        # Tabla de datos del estudiante con 2 columnas (etiqueta | valor)
        # Estilo para textos largos que se ajusten automáticamente
        texto_style = ParagraphStyle(
            "TextoTabla",
            parent=styles["Normal"],
            fontSize=10,
            fontName="Helvetica-Bold",
            alignment=0,  # Alineación izquierda
            # leading=12,  # Espaciado entre líneas
        )

        # Preparar datos usando Paragraph para textos largos

        # Estilo especial para la fila de Matrícula y Sexo
        matricula_sexo_style = ParagraphStyle(
            "MatriculaSexo",
            parent=styles["Normal"],
            fontSize=10,
            fontName="Helvetica",  # Sin negritas por defecto
            alignment=0,
        )

        datos_filas = [
            ["Nombre:", Paragraph(datos_alumno["nombre"], texto_style)],
            ["CURP:", Paragraph(datos_alumno["curp"], texto_style)],
            # Matrícula y Sexo en la misma fila
            [
                "Matrícula:",
                Paragraph(
                    f"<b>{datos_alumno['matricula']}</b>                    Sexo: <b>{datos_alumno['sexo']}</b>",
                    matricula_sexo_style,
                ),
            ],
            [
                "Carrera:",
                Paragraph(datos_alumno["carrera"], texto_style),
            ],  # Se ajustará automáticamente
            [
                "Dirección:",
                Paragraph(datos_alumno["direccion"], texto_style),
            ],  # Se ajustará automáticamente
        ]

        tabla_datos = Table(
            datos_filas,
            colWidths=[1.8 * inch, 4.2 * inch],  # Mantenemos anchos
        )
        tabla_datos.setStyle(
            TableStyle(
                [
                    # Columna izquierda (etiquetas) - sin negrita
                    ("FONTNAME", (0, 0), (0, -1), "Helvetica"),
                    ("FONTSIZE", (0, 0), (0, -1), 11),
                    ("ALIGN", (0, 0), (0, -1), "LEFT"),  # Cambio de RIGHT a LEFT
                    # Columna derecha - los Paragraph ya tienen su estilo
                    ("ALIGN", (1, 0), (1, -1), "LEFT"),
                    # Estilo general
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),  # TOP para textos largos
                    ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
                    # SIN GRID - para que no se vean las líneas
                    ("LEFTPADDING", (0, 0), (-1, -1), 10),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),  # REDUCIDO: de 8 a 3
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),  # REDUCIDO: de 8 a 3
                ]
            )
        )

        elements.append(tabla_datos)
        elements.append(Spacer(1, 20))

        # Título de calificaciones
        elements.append(Paragraph("<b>Calificaciones</b>", centered_style))
        elements.append(Spacer(1, 15))

        # Tabla de calificaciones
        tabla_data = [["Materia", "Calificación"]]
        for materia, calificacion in materias:
            if calificacion is not None:
                tabla_data.append([materia, f"{calificacion:.1f}"])
            else:
                tabla_data.append([materia, "Sin calificación"])

        tabla_calificaciones = Table(tabla_data, colWidths=[4 * inch, 1.5 * inch])
        tabla_calificaciones.setStyle(
            TableStyle(
                [
                    # Encabezado - SIN FONDO DE COLOR
                    ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),  # Todo en negro
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, 0),
                        "LEFT",
                    ),  # Encabezados alineados a la IZQUIERDA
                    (
                        "ALIGN",
                        (0, 1),
                        (0, -1),
                        "LEFT",
                    ),  # Materias alineadas a la IZQUIERDA
                    ("ALIGN", (1, 1), (1, -1), "CENTER"),  # Calificaciones centradas
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold",
                    ),  # Solo encabezado en negrita
                    ("FONTSIZE", (0, 0), (-1, 0), 12),
                    # Contenido
                    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                    ("FONTSIZE", (0, 1), (-1, -1), 10),
                    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                    # LÍNEAS ESPECÍFICAS - Solo encabezado y separación de columnas en las filas de materias
                    (
                        "LINEBELOW",
                        (0, 0),
                        (-1, 0),
                        1,
                        colors.black,
                    ),  # Línea debajo del encabezado
                    (
                        "LINEBEFORE",
                        (1, 1),
                        (1, -1),
                        1,
                        colors.black,
                    ),  # Línea vertical entre columnas solo para las materias (no en el encabezado)
                    # SIN ROWBACKGROUNDS - Sin colores alternados
                ]
            )
        )

        elements.append(tabla_calificaciones)
        elements.append(Spacer(1, 20))

        # Promedio general
        promedio_style = ParagraphStyle(
            "Promedio",
            parent=styles["Normal"],
            alignment=2,  # Cambiado de 1 (centro) a 2 (derecha)
            fontSize=11,  # Reducido de 14 a 11
        )
        elements.append(
            Paragraph(f"<b>Promedio General: <u>{promedio:.2f}</u></b>", promedio_style)
        )

        # Generar el PDF
        doc.build(elements)

        messagebox.showinfo(
            "Éxito", f"Historial académico generado correctamente:\n{ruta_archivo}"
        )

        # Preguntar si quiere abrir el archivo
        respuesta = messagebox.askyesno(
            "Abrir PDF", "¿Desea abrir el historial académico generado?"
        )
        if respuesta:
            os.startfile(ruta_archivo)  # Windows

    except Exception as e:
        messagebox.showerror(
            "Error", f"Error al generar el historial académico: {str(e)}"
        )


def gestionar_calificaciones():
    """Abre ventana para gestionar calificaciones del alumno seleccionado"""
    # Verificar que hay un alumno seleccionado
    seleccion = tabla.selection()
    if not seleccion:
        messagebox.showwarning(
            "Advertencia", "Selecciona un alumno para gestionar sus calificaciones"
        )
        return

    item = tabla.item(seleccion[0])
    valores = item["values"]
    matricula = valores[0]
    nombre_completo = f"{valores[1]} {valores[2]}"

    # Crear ventana para gestionar calificaciones
    ventana_calif = tk.Toplevel(root)
    ventana_calif.title(f"Gestionar Calificaciones - {nombre_completo}")
    ventana_calif.geometry("600x500")
    ventana_calif.resizable(False, False)

    # Frame principal
    frame_calif = tk.Frame(ventana_calif, bg="lightblue")
    frame_calif.pack(fill="both", expand=True, padx=10, pady=10)

    # Título
    tk.Label(
        frame_calif,
        text=f"Calificaciones de: {nombre_completo}",
        font=("Arial", 14, "bold"),
        bg="lightblue",
    ).pack(pady=(0, 10))

    tk.Label(
        frame_calif, text=f"Matrícula: {matricula}", font=("Arial", 10), bg="lightblue"
    ).pack(pady=(0, 20))

    # Materias del 3er cuatrimestre
    materias = [
        "Bases de datos",
        "Desarrollo y pensamientos y toma de decisiones",
        "Inglés 3",
        "Programación orientada a objetos",
        "Proyecto integrador I",
        "Tópicos de calidad para el diseño de software",
    ]

    # Diccionario para almacenar los Entry de calificaciones
    entries_calificaciones = {}

    # Frame para las materias y calificaciones
    frame_materias = tk.Frame(frame_calif, bg="lightblue")
    frame_materias.pack(fill="x", padx=20)

    # Crear campos para cada materia
    for i, materia in enumerate(materias):
        # Frame para cada materia
        frame_materia = tk.Frame(frame_materias, bg="lightblue")
        frame_materia.pack(fill="x", pady=5)

        # Label de la materia
        tk.Label(
            frame_materia,
            text=materia + ":",
            font=("Arial", 10),
            bg="lightblue",
            width=40,
            anchor="w",
        ).pack(side="left")

        # Entry para la calificación
        vcmd_calif = (
            ventana_calif.register(lambda x: x.replace(".", "").isdigit() or x == ""),
            "%P",
        )
        entry_calif = tk.Entry(
            frame_materia, width=10, validate="key", validatecommand=vcmd_calif
        )
        entry_calif.pack(side="right", padx=(10, 0))

        entries_calificaciones[materia] = entry_calif

    # Cargar calificaciones existentes
    def cargar_calificaciones_existentes():
        try:
            from insertar_datos_formulario_db import obtener_calificaciones_alumno

            calificaciones = obtener_calificaciones_alumno(matricula)

            # Limpiar campos
            for entry in entries_calificaciones.values():
                entry.delete(0, tk.END)

            # Llenar con calificaciones existentes
            for materia, calificacion, _ in calificaciones:
                if materia in entries_calificaciones:
                    entries_calificaciones[materia].insert(0, str(calificacion))

        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar calificaciones: {str(e)}")

    # Función para guardar calificaciones
    def guardar_calificaciones():
        try:
            from insertar_datos_formulario_db import insertar_calificacion

            calificaciones_guardadas = 0
            errores = []

            for materia, entry in entries_calificaciones.items():
                calificacion_str = entry.get().strip()

                if calificacion_str:  # Si hay valor
                    try:
                        calificacion = float(calificacion_str)

                        # Validar rango de calificación (0-100)
                        if 0 <= calificacion <= 100:
                            if insertar_calificacion(matricula, materia, calificacion):
                                calificaciones_guardadas += 1
                            else:
                                errores.append(f"Error al guardar {materia}")
                        else:
                            errores.append(
                                f"{materia}: La calificación debe estar entre 0 y 100"
                            )

                    except ValueError:
                        errores.append(f"{materia}: Calificación inválida")

            # Mostrar resultado
            if calificaciones_guardadas > 0:
                if errores:
                    messagebox.showwarning(
                        "Parcialmente guardado",
                        f"Se guardaron {calificaciones_guardadas} calificaciones.\n\nErrores:\n"
                        + "\n".join(errores),
                    )
                else:
                    messagebox.showinfo(
                        "Éxito",
                        f"Se guardaron {calificaciones_guardadas} calificaciones correctamente.",
                    )
            elif errores:
                messagebox.showerror(
                    "Errores",
                    "No se pudo guardar ninguna calificación:\n" + "\n".join(errores),
                )
            else:
                messagebox.showwarning(
                    "Sin datos", "No hay calificaciones para guardar."
                )

        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar calificaciones: {str(e)}")

    # Función para calcular promedio
    def calcular_mostrar_promedio():
        try:
            total = 0
            materias_con_calif = 0

            for entry in entries_calificaciones.values():
                calificacion_str = entry.get().strip()
                if calificacion_str:
                    try:
                        calificacion = float(calificacion_str)
                        if 0 <= calificacion <= 100:
                            total += calificacion
                            materias_con_calif += 1
                    except ValueError:
                        pass

            if materias_con_calif > 0:
                promedio = total / materias_con_calif
                messagebox.showinfo(
                    "Promedio",
                    f"Promedio actual: {promedio:.2f}\nMaterias con calificación: {materias_con_calif}",
                )
            else:
                messagebox.showwarning(
                    "Sin datos", "No hay calificaciones válidas para calcular promedio."
                )

        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular promedio: {str(e)}")

    # Frame para botones
    frame_botones_calif = tk.Frame(frame_calif, bg="lightblue")
    frame_botones_calif.pack(fill="x", padx=20, pady=20)

    # Botones
    tk.Button(
        frame_botones_calif,
        text="Guardar Calificaciones",
        command=guardar_calificaciones,
        bg="green",
        fg="white",
        font=("Arial", 10, "bold"),
    ).pack(side="left", padx=5)

    tk.Button(
        frame_botones_calif,
        text="Calcular Promedio",
        command=calcular_mostrar_promedio,
        bg="blue",
        fg="white",
        font=("Arial", 10),
    ).pack(side="left", padx=5)

    tk.Button(
        frame_botones_calif,
        text="Cerrar",
        command=ventana_calif.destroy,
        bg="red",
        fg="white",
        font=("Arial", 10),
    ).pack(side="right", padx=5)

    # Cargar calificaciones al abrir la ventana
    cargar_calificaciones_existentes()


frame_botones = tk.Frame(frame)
frame_botones.grid(row=8, column=0, columnspan=5, pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Alumno", command=agregar_alumno)
btn_agregar.pack(side="left", padx=5)

btn_cancelar = tk.Button(frame_botones, text="Cancelar", command=cancelar_edicion)

btn_editar = tk.Button(frame_botones, text="Editar Alumno", command=editar_alumno)
btn_editar.pack(side="left", padx=5)

btn_eliminar = tk.Button(
    frame_botones, text="Eliminar Alumno", command=eliminar_alumno_seleccionado
)
btn_eliminar.pack(side="left", padx=5)

btn_historial = tk.Button(
    frame_botones,
    text="Descargar Historial Académico",
    command=generar_historial_academico,
    bg="#2e8b57",
    fg="white",
    font=("Arial", 9, "bold"),
)
btn_historial.pack(side="left", padx=5)

btn_calificaciones = tk.Button(
    frame_botones,
    text="Gestionar Calificaciones",
    command=gestionar_calificaciones,
    bg="orange",
    fg="white",
    font=("Arial", 9, "bold"),
)
btn_calificaciones.pack(side="left", padx=5)

frm_tabla = tk.Frame(root)
frm_tabla.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")

root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(0, weight=1)

tabla = ttk.Treeview(
    frm_tabla,
    columns=(
        "Matricula",
        "Nombre",
        "Apellido",
        "Fecha_Nac",
        "Sexo",
        "Direccion",
        "Carrera",
    ),
    show="headings",
)
tabla.heading("Matricula", text="Matrícula")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Apellido", text="Apellido")
tabla.heading("Fecha_Nac", text="Fecha Nac.")
tabla.heading("Sexo", text="Sexo")
tabla.heading("Direccion", text="Dirección")
tabla.heading("Carrera", text="Carrera")

tabla.column("Matricula", width=100)
tabla.column("Nombre", width=120)
tabla.column("Apellido", width=120)
tabla.column("Fecha_Nac", width=100)
tabla.column("Sexo", width=80)
tabla.column("Direccion", width=200)
tabla.column("Carrera", width=300)

scrollbar = ttk.Scrollbar(frm_tabla, orient="vertical", command=tabla.yview)
tabla.configure(yscrollcommand=scrollbar.set)

tabla.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

cargar_alumnos()

root.mainloop()
