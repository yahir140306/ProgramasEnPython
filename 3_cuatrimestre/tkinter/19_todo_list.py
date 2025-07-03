import tkinter as tk
from tkinter import ttk, messagebox

class TodoLogic:
    def __init__(self):
        self.tareas_pendientes = []
        self.tareas_terminadas = []

    def agregar_tarea(self, tarea):
        tarea = tarea.strip()
        if tarea:
            self.tareas_pendientes.append(tarea)
            return True
        return False

    def completar_tarea(self, tarea):
        if tarea in self.tareas_pendientes:
            self.tareas_pendientes.remove(tarea)
            self.tareas_terminadas.append(tarea)
            return True
        return False

    def borrar_pendiente(self, tarea):
        if tarea in self.tareas_pendientes:
            self.tareas_pendientes.remove(tarea)
            return True
        return False

    def borrar_terminada(self, tarea):
        if tarea in self.tareas_terminadas:
            self.tareas_terminadas.remove(tarea)
            return True
        return False


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x600")
        self.logic = TodoLogic()
        self.vista = tk.StringVar(value="pendientes")

        self.crear_widgets()
        self.actualizar_vista()

    def crear_widgets(self):
        tk.Label(self.root, text="Mi Lista de Tareas", font=("Arial", 16, "bold")).pack(pady=10)

        # Entrada
        entrada_frame = tk.Frame(self.root)
        entrada_frame.pack(pady=10)

        self.entrada = tk.Entry(entrada_frame, width=40, font=("Arial", 10))
        self.entrada.pack(side="left", padx=5)
        self.entrada.bind("<Return>", lambda e: self.agregar_tarea())

        tk.Button(entrada_frame, text="Agregar", command=self.agregar_tarea, bg="#4CAF50", fg="white").pack(side="left")

        # Radiobuttons
        radio_frame = tk.Frame(self.root)
        radio_frame.pack()

        tk.Radiobutton(radio_frame, text="Tareas Pendientes", variable=self.vista, value="pendientes", command=self.actualizar_vista).pack(side="left", padx=10)
        tk.Radiobutton(radio_frame, text="Tareas Terminadas", variable=self.vista, value="terminadas", command=self.actualizar_vista).pack(side="left", padx=10)

        # Frame lista
        self.lista_frame = tk.Frame(self.root, bg="white", relief="sunken", bd=1)
        self.lista_frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.canvas = tk.Canvas(self.lista_frame, bg="white")
        self.scrollbar = ttk.Scrollbar(self.lista_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def agregar_tarea(self):
        tarea = self.entrada.get()
        if self.logic.agregar_tarea(tarea):
            self.entrada.delete(0, tk.END)
            self.actualizar_vista()
        else:
            messagebox.showwarning("Campo vacío", "Por favor ingresa una tarea válida.")

    def actualizar_vista(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if self.vista.get() == "pendientes":
            self.mostrar_pendientes()
        else:
            self.mostrar_terminadas()

    def mostrar_pendientes(self):
        tareas = self.logic.tareas_pendientes
        if not tareas:
            tk.Label(self.scrollable_frame, text="No hay tareas pendientes", bg="white", fg="gray").pack(pady=10)
            return

        for tarea in tareas:
            frame = tk.Frame(self.scrollable_frame, bg="white")
            frame.pack(fill="x", padx=10, pady=5)

            tk.Checkbutton(frame, command=lambda t=tarea: self.completar_tarea(t), bg="white").pack(side="left")
            tk.Label(frame, text=tarea, bg="white").pack(side="left", padx=5, fill="x", expand=True)
            tk.Button(frame, text="❌", command=lambda t=tarea: self.borrar_pendiente(t), bg="#ffcccc").pack(side="right")

    def mostrar_terminadas(self):
        tareas = self.logic.tareas_terminadas
        if not tareas:
            tk.Label(self.scrollable_frame, text="No hay tareas terminadas", bg="white", fg="gray").pack(pady=10)
            return

        for tarea in tareas:
            frame = tk.Frame(self.scrollable_frame, bg="white")
            frame.pack(fill="x", padx=10, pady=5)

            tk.Label(frame, text="✓", fg="green", bg="white").pack(side="left")
            tk.Label(frame, text=tarea, font=("Arial", 10, "overstrike"), fg="gray", bg="white").pack(side="left", padx=5, fill="x", expand=True)
            tk.Button(frame, text="❌", command=lambda t=tarea: self.borrar_terminada(t), bg="#ffcccc").pack(side="right")

    def completar_tarea(self, tarea):
        self.logic.completar_tarea(tarea)
        self.actualizar_vista()

    def borrar_pendiente(self, tarea):
        self.logic.borrar_pendiente(tarea)
        self.actualizar_vista()

    def borrar_terminada(self, tarea):
        self.logic.borrar_terminada(tarea)
        self.actualizar_vista()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
