import tkinter as tk
from tkinter import ttk
from datetime import date

root = tk.Tk()
root.title("Registro de Alumnos")
root.geometry("1225x500")

# Frame principal
frame = tk.Frame(root)
frame.grid(padx=10, pady=10)

# Título
tk.Label(frame, text="Registro de Alumnos", font=("Arial", 18, "bold")).grid(
    row=0, column=0, columnspan=4, pady=(0, 10)
)

# Fecha actual
tk.Label(frame, text=f"Fecha: {date.today()}").grid(row=0, column=4, sticky="e")

# Matricula
tk.Label(frame, text="Matricula:").grid(row=1, column=0, sticky="w")
entry_matricula = tk.Entry(frame)
entry_matricula.grid(row=1, column=1)

# Nombre
tk.Label(frame, text="Nombre:").grid(row=2, column=0, sticky="w")
entry_nombre = tk.Entry(frame)
entry_nombre.grid(row=2, column=1)

# Apellido
tk.Label(frame, text="Apellido:").grid(row=3, column=0, sticky="w")
entry_apellido = tk.Entry(frame)
entry_apellido.grid(row=3, column=1)

# Fecha de nacimiento
tk.Label(frame, text="Fecha Nacimiento:").grid(row=4, column=0, sticky="w")
entry_fecha_nac = tk.Entry(frame)
entry_fecha_nac.grid(row=4, column=1)

# Sexo (Radiobuttons)
tk.Label(frame, text="Sexo:").grid(row=5, column=0, sticky="w")
sexo_var = tk.StringVar()
tk.Radiobutton(frame, text="Mujer", variable=sexo_var, value="Mujer").grid(
    row=5, column=1, sticky="w"
)
tk.Radiobutton(frame, text="Hombre", variable=sexo_var, value="Hombre").grid(
    row=5, column=2, sticky="w"
)

# Ciencias Económico Administrativas -> Maestria en innovacion y negocios , licenciatura en administracion, licenciatura en contaduria, licenciatura en negocios y mercadotecnia
# Ciencias Naturales e Ingeniería -> Maestria en istemas de gestion ambiental, licenciatura en ingenieria en manejo de recursos naturales, licenciatura en ingenieria en mantenimiento industrial, licenciatura en ingenieria en ingenieria civil
# Tecnologias de la Información -> Licenciatura en ingenieria en tecnologias de la informacion e innovacion digital, licenciatura en ingenieria mecatronica
# Ciencias Exactas -> Licenciatura en ingenieria en mecanica, licenciaturia en ingenieria industrial, licenciatura en ingenieria en diseño textil y moda
# Ciencias de la Salud -> Licenciatura en terapia fisica, licenciatura en enfermeria, licenciatura en medico cirujano y partero


# Dirección (como Combobox)
tk.Label(frame, text="Dirección:").grid(row=6, column=0, sticky="w")

# Diccionario que mapea direcciones con sus carreras correspondientes
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


# Función para actualizar las carreras según la dirección seleccionada
def actualizar_carreras(event):
    direccion_seleccionada = cbb_direccion.get()
    if direccion_seleccionada in carreras_por_direccion:
        cbb_carrera["values"] = carreras_por_direccion[direccion_seleccionada]
        cbb_carrera.set("Seleccione carrera...")
    else:
        cbb_carrera["values"] = []
        cbb_carrera.set("")


cbb_direccion = ttk.Combobox(
    frame, state="readonly", values=list(carreras_por_direccion.keys())
)
cbb_direccion.grid(row=6, column=1, padx=5, pady=5)
cbb_direccion.set("Seleccione...")
cbb_direccion.bind("<<ComboboxSelected>>", actualizar_carreras)

# Eliminando los comentarios ya que ahora usamos el diccionario

# Carrera (como Combobox)
tk.Label(frame, text="Carrera:").grid(row=7, column=0, sticky="w", padx=5, pady=5)
cbb_carrera = ttk.Combobox(frame, state="readonly")
cbb_carrera.grid(row=7, column=1)
cbb_carrera.set("Seleccione carrera...")

# Botón agregar
btn_agregar = tk.Button(frame, text="Agregar Alumno")
btn_agregar.grid(row=8, column=0, columnspan=2, pady=10)

# Tabla para mostrar los alumnos
frm_tabla = tk.Frame(root)
frm_tabla.grid(row=9, column=0, padx=10, pady=10)

tabla = ttk.Treeview(
    frm_tabla,
    columns=("Matricula", "Nombre", "Apellido", "Sexo", "Direccion", "Carrera"),
    show="headings",
)
tabla.heading("Matricula", text="Matricula")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Apellido", text="Apellido")
tabla.heading("Sexo", text="Sexo")
tabla.heading("Direccion", text="Dirección")
tabla.heading("Carrera", text="Carrera")

tabla.pack(fill="both", expand=True)

root.mainloop()
