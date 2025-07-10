import tkinter as tk
from tkinter import messagebox
from logica_interfaz import LogicaTareas


class AplicacionTareas:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Mi Lista de Tareas")
        self.ventana.geometry("500x600")
        self.ventana.configure(bg="#f0f0f0")

        self.logica = LogicaTareas()
        self.vista_actual = tk.StringVar(value="pendientes")

        self.crear_elementos()
        self.mostrar_tareas()

    def crear_elementos(self):
        tk.Label(
            self.ventana,
            text="Mi Lista de Tareas",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
        ).pack(pady=10)

        marco_entrada = tk.Frame(self.ventana, bg="#f0f0f0")
        marco_entrada.pack(pady=10)

        tk.Label(
            marco_entrada, text="Nueva tarea:", font=("Arial", 10), bg="#f0f0f0"
        ).pack(anchor="w")

        self.caja_texto = tk.Entry(marco_entrada, width=40, font=("Arial", 10))
        self.caja_texto.pack(side="left", padx=5)
        self.caja_texto.bind("<Return>", lambda evento: self.agregar_tarea())

        tk.Button(
            marco_entrada,
            text="Agregar Tarea",
            command=self.agregar_tarea,
            bg="#4CAF50",
            fg="white",
        ).pack(side="left", padx=5)

        marco_botones = tk.Frame(self.ventana, bg="#f0f0f0")
        marco_botones.pack(pady=10)

        tk.Radiobutton(
            marco_botones,
            text="Tareas por Hacer",
            variable=self.vista_actual,
            value="pendientes",
            command=self.mostrar_tareas,
            bg="#f0f0f0",
            font=("Arial", 10),
        ).pack(side="left", padx=10)

        tk.Radiobutton(
            marco_botones,
            text="Tareas Completadas",
            variable=self.vista_actual,
            value="completadas",
            command=self.mostrar_tareas,
            bg="#f0f0f0",
            font=("Arial", 10),
        ).pack(side="left", padx=10)

        # self.marco_tareas = tk.Frame(self.ventana, bg='white', relief='sunken', bd=2)
        self.marco_tareas = tk.Frame(self.ventana, bg="#f0f0f0", bd=0, relief="flat")

        self.marco_tareas.pack(padx=20, pady=10, fill="both", expand=True)

    def agregar_tarea(self):
        texto = self.caja_texto.get()
        if self.logica.agregar_nueva_tarea(texto):
            self.caja_texto.delete(0, tk.END)
            self.mostrar_tareas()
        else:
            messagebox.showwarning("¡Atención!", "Por favor escribe una tarea válida")

    def mostrar_tareas(self):
        for widget in self.marco_tareas.winfo_children():
            widget.destroy()

        if self.vista_actual.get() == "pendientes":
            self.mostrar_tareas_pendientes()
        else:
            self.mostrar_tareas_completadas()

    def mostrar_tareas_pendientes(self):
        tareas = self.logica.tareas_por_hacer
        if not tareas:
            tk.Label(
                self.marco_tareas, text="¡No hay tareas pendientes!", font=("Arial", 12)
            ).pack(pady=20)
            # tk.Label(self.marco_tareas, text="¡No hay tareas pendientes!",font=("Arial", 12)).pack(pady=20)
            return

        for tarea in tareas:
            fila = tk.Frame(self.marco_tareas, bg="white")
            fila.pack(fill="x", padx=10, pady=5)

            tk.Checkbutton(
                fila, bg="white", command=lambda t=tarea: self.completar_tarea(t)
            ).pack(side="left")
            tk.Label(fila, text=tarea, font=("Arial", 10), bg="white", anchor="w").pack(
                side="left", padx=5, fill="x", expand=True
            )
            tk.Button(
                fila,
                text="X",
                command=lambda t=tarea: self.borrar_tarea_pendiente(t),
                bg="#ffcccc",
                font=("Arial", 8),
            ).pack(side="right")

    def mostrar_tareas_completadas(self):
        tareas = self.logica.tareas_completadas
        if not tareas:
            tk.Label(
                self.marco_tareas,
                text="Aún no has completado ninguna tarea",
                font=("Arial", 12),
            ).pack(pady=20)
            return

        for tarea in tareas:
            fila = tk.Frame(self.marco_tareas, bg="white")
            fila.pack(fill="x", padx=10, pady=5)

            tk.Label(fila, font=("Arial", 12), bg="white").pack(side="left")
            tk.Label(
                fila, text=tarea, font=("Arial", 10), bg="white", anchor="w", fg="gray"
            ).pack(side="left", padx=5, fill="x", expand=True)
            tk.Button(
                fila,
                text="x",
                command=lambda t=tarea: self.borrar_tarea_completada(t),
                bg="#ffcccc",
                font=("Arial", 8),
            ).pack(side="right")

    def completar_tarea(self, tarea):
        self.logica.marcar_como_completada(tarea)
        self.mostrar_tareas()

    def borrar_tarea_pendiente(self, tarea):
        self.logica.eliminar_tarea_pendiente(tarea)
        self.mostrar_tareas()

    def borrar_tarea_completada(self, tarea):
        self.logica.eliminar_tarea_completada(tarea)
        self.mostrar_tareas()

    def iniciar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = AplicacionTareas()
    app.iniciar()
