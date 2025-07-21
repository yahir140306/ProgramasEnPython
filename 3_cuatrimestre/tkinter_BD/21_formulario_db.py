import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from insertar_datos_formulario_db import (
    insertar_alumno,
    obtener_alumnos,
    verificar_matricula_existe,
    obtener_alumno_por_matricula,
    actualizar_alumno,
    eliminar_alumno,
    verificar_matricula_existe_excepto,
)

root = tk.Tk()
root.title("Registro de Alumnos")
root.geometry("1100x600")

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
