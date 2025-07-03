import tkinter as tk
from tkinter import ttk, messagebox

class TodoLogic:
    """Clase que maneja toda la lógica de las tareas"""
    
    def __init__(self):
        self.tareas_pendientes = []
        self.tareas_terminadas = []
    
    def agregar_tarea(self, tarea):
        """Agrega una nueva tarea a la lista de pendientes"""
        if tarea.strip():  # Verifica que no esté vacía
            self.tareas_pendientes.append(tarea.strip())
            return True
        return False
    
    def completar_tarea(self, indice):
        """Mueve una tarea de pendientes a terminadas"""
        if 0 <= indice < len(self.tareas_pendientes):
            tarea = self.tareas_pendientes.pop(indice)
            self.tareas_terminadas.append(tarea)
            return True
        return False
    
    def borrar_tarea_pendiente(self, indice):
        """Elimina una tarea de la lista de pendientes"""
        if 0 <= indice < len(self.tareas_pendientes):
            self.tareas_pendientes.pop(indice)
            return True
        return False
    
    def borrar_tarea_terminada(self, indice):
        """Elimina una tarea de la lista de terminadas"""
        if 0 <= indice < len(self.tareas_terminadas):
            self.tareas_terminadas.pop(indice)
            return True
        return False

class TodoVisual:
    """Clase que maneja la interfaz visual"""
    
    def __init__(self):
        self.logica = TodoLogic()
        self.setup_ventana()
        self.setup_widgets()
        self.vista_actual = tk.StringVar(value="pendientes")
        self.actualizar_vista()
    
    def setup_ventana(self):
        """Configura la ventana principal"""
        self.root = tk.Tk()
        self.root.title("Mi Lista de Tareas")
        self.root.geometry("500x600")
        self.root.configure(bg='#f0f0f0')
    
    def setup_widgets(self):
        """Configura todos los widgets de la interfaz"""
        # Título principal
        titulo = tk.Label(self.root, text="Mi Lista de Tareas", 
                         font=("Arial", 16, "bold"), bg='#f0f0f0')
        titulo.pack(pady=10)
        
        # Frame para agregar tareas
        frame_agregar = tk.Frame(self.root, bg='#f0f0f0')
        frame_agregar.pack(pady=10, padx=20, fill='x')
        
        tk.Label(frame_agregar, text="Tarea:", font=("Arial", 10), bg='#f0f0f0').pack(anchor='w')
        
        self.entrada_tarea = tk.Entry(frame_agregar, font=("Arial", 10), width=40)
        self.entrada_tarea.pack(side='left', padx=(0, 10))
        self.entrada_tarea.bind('<Return>', lambda e: self.agregar_tarea())
        
        btn_agregar = tk.Button(frame_agregar, text="Agregar Tarea", 
                               command=self.agregar_tarea, bg='#4CAF50', fg='white')
        btn_agregar.pack(side='left')
        
        # Frame para los radiobuttons
        frame_radio = tk.Frame(self.root, bg='#f0f0f0')
        frame_radio.pack(pady=10)
        
        self.vista_actual = tk.StringVar(value="pendientes")
        
        rb_pendientes = tk.Radiobutton(frame_radio, text="Tareas Pendientes", 
                                      variable=self.vista_actual, value="pendientes",
                                      command=self.cambiar_vista, bg='#f0f0f0')
        rb_pendientes.pack(side='left', padx=10)
        
        rb_terminadas = tk.Radiobutton(frame_radio, text="Tareas Terminadas", 
                                      variable=self.vista_actual, value="terminadas",
                                      command=self.cambiar_vista, bg='#f0f0f0')
        rb_terminadas.pack(side='left', padx=10)
        
        # Frame para la lista de tareas
        self.frame_lista = tk.Frame(self.root, bg='white', relief='sunken', bd=2)
        self.frame_lista.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Scrollbar para la lista
        canvas = tk.Canvas(self.frame_lista, bg='white')
        scrollbar = ttk.Scrollbar(self.frame_lista, orient="vertical", command=canvas.yview)
        self.frame_tareas = tk.Frame(canvas, bg='white')
        
        self.frame_tareas.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.frame_tareas, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        self.canvas = canvas
    
    def agregar_tarea(self):
        """Agrega una nueva tarea"""
        tarea = self.entrada_tarea.get()
        if self.logica.agregar_tarea(tarea):
            self.entrada_tarea.delete(0, tk.END)
            if self.vista_actual.get() == "pendientes":
                self.actualizar_vista()
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea válida")
    
    def cambiar_vista(self):
        """Cambia entre vista de pendientes y terminadas"""
        self.actualizar_vista()
    
    def actualizar_vista(self):
        """Actualiza la vista según el radiobutton seleccionado"""
        # Limpiar frame actual
        for widget in self.frame_tareas.winfo_children():
            widget.destroy()
        
        if self.vista_actual.get() == "pendientes":
            self.mostrar_tareas_pendientes()
        else:
            self.mostrar_tareas_terminadas()
        
        # Actualizar scroll region
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def mostrar_tareas_pendientes(self):
        """Muestra las tareas pendientes con checkboxes"""
        if not self.logica.tareas_pendientes:
            tk.Label(self.frame_tareas, text="No hay tareas pendientes", 
                    font=("Arial", 12), bg='white', fg='gray').pack(pady=20)
            return
        
        for i, tarea in enumerate(self.logica.tareas_pendientes):
            frame_tarea = tk.Frame(self.frame_tareas, bg='white', pady=5)
            frame_tarea.pack(fill='x', padx=10, pady=2)
            
            # Checkbox para completar - crear una función específica para cada tarea
            def crear_comando_completar(indice):
                return lambda: self.completar_tarea_por_indice(indice)
            
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(frame_tarea, variable=var, bg='white',
                                    command=crear_comando_completar(i))
            checkbox.pack(side='left')
            
            # Texto de la tarea
            tk.Label(frame_tarea, text=tarea, font=("Arial", 10), 
                    bg='white', anchor='w').pack(side='left', padx=5, fill='x', expand=True)
            
            # Botón para borrar
            def crear_comando_borrar(indice):
                return lambda: self.borrar_pendiente_por_indice(indice)
            
            btn_borrar = tk.Button(frame_tarea, text="❌", font=("Arial", 8),
                                 command=crear_comando_borrar(i),
                                 bg='#ffcccc')
            btn_borrar.pack(side='right')
    
    def mostrar_tareas_terminadas(self):
        """Muestra las tareas terminadas"""
        if not self.logica.tareas_terminadas:
            tk.Label(self.frame_tareas, text="No hay tareas terminadas", 
                    font=("Arial", 12), bg='white', fg='gray').pack(pady=20)
            return
        
        for i, tarea in enumerate(self.logica.tareas_terminadas):
            frame_tarea = tk.Frame(self.frame_tareas, bg='white', pady=5)
            frame_tarea.pack(fill='x', padx=10, pady=2)
            
            # Símbolo de completado
            tk.Label(frame_tarea, text="✓", font=("Arial", 12), 
                    bg='white', fg='green').pack(side='left')
            
            # Texto de la tarea (tachado)
            tk.Label(frame_tarea, text=tarea, font=("Arial", 10, "overstrike"), 
                    bg='white', anchor='w', fg='gray').pack(side='left', padx=5, fill='x', expand=True)
            
            # Botón para borrar
            def crear_comando_borrar_terminada(indice):
                return lambda: self.borrar_terminada_por_indice(indice)
            
            btn_borrar = tk.Button(frame_tarea, text="❌", font=("Arial", 8),
                                 command=crear_comando_borrar_terminada(i),
                                 bg='#ffcccc')
            btn_borrar.pack(side='right')
    
    def completar_tarea_por_indice(self, indice):
        """Completa una tarea específica por su índice"""
        if self.logica.completar_tarea(indice):
            self.actualizar_vista()
    
    def borrar_pendiente_por_indice(self, indice):
        """Borra una tarea pendiente específica"""
        if self.logica.borrar_tarea_pendiente(indice):
            self.actualizar_vista()
    
    def borrar_terminada_por_indice(self, indice):
        """Borra una tarea terminada específica"""
        if self.logica.borrar_tarea_terminada(indice):
            self.actualizar_vista()
    
    def completar_tarea(self, indice):
        """Completa una tarea y actualiza la vista"""
        if self.logica.completar_tarea(indice):
            self.actualizar_vista()
    
    def borrar_pendiente(self, indice):
        """Borra una tarea pendiente"""
        if self.logica.borrar_tarea_pendiente(indice):
            self.actualizar_vista()
    
    def borrar_terminada(self, indice):
        """Borra una tarea terminada"""
        if self.logica.borrar_tarea_terminada(indice):
            self.actualizar_vista()
    
    def ejecutar(self):
        """Inicia la aplicación"""
        self.root.mainloop()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = TodoVisual()
    app.ejecutar()