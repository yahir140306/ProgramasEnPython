import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Agenda:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("200x300")
        self.ventana.title("Agenda de Contactos")
        self.contactos = []
        
        # Variables para guardar referencias a los botones
        self.botones = {}

        imagen_original = Image.open("descarga (1).png")
        imagen_redimensionada = imagen_original.resize((100, 50))
        self.imagen_boton = ImageTk.PhotoImage(imagen_redimensionada)

    def actualizar_estado_botones(self):
        """Actualiza el estado de los botones según si hay contactos o no"""
        hay_contactos = len(self.contactos) > 0
        
        # Habilitar/deshabilitar botones que requieren contactos
        if "Eliminar" in self.botones:
            self.botones["Eliminar"]["state"] = "normal" if hay_contactos else "disabled"
        if "Editar_contacto" in self.botones:
            self.botones["Editar_contacto"]["state"] = "normal" if hay_contactos else "disabled"
        if "Contactos" in self.botones:
            self.botones["Contactos"]["state"] = "normal" if hay_contactos else "disabled"

    def boton_salir(self, ventana_padre):
        def regresar_al_menu():
            ventana_padre.destroy()
            self.Menu_principal()
        tk.Button(ventana_padre, text="Salir", command=regresar_al_menu).grid(row=5, column=1, pady=10)

    def Menu_principal(self):
        # Limpiar ventana principal si hay widgets
        for widget in self.ventana.winfo_children():
            widget.destroy()
            
        menu = ["Agregar", "Eliminar", "Editar_contacto", "Contactos"]
        for i, texto in enumerate(menu):
            if texto == "Agregar":
                ima = Image.open("agregarr.png").resize((50, 50))
                botonima = ImageTk.PhotoImage(ima)
                boton = tk.Button(self.ventana, image=botonima, text=texto, command=self.estructura_de_la_agenda,
                                  compound="left", width=150)
            elif texto == "Eliminar":
                ima = Image.open("borrar.png").resize((50, 50))
                botonima = ImageTk.PhotoImage(ima)
                boton = tk.Button(self.ventana, image=botonima, text=texto, command=self.eliminar_contacto,
                                  compound="left", width=150)
            elif texto == "Editar_contacto":
                ima = Image.open("edi.png").resize((50, 50))
                botonima = ImageTk.PhotoImage(ima)
                boton = tk.Button(self.ventana, image=botonima, text=texto, command=self.editar_contacto,
                                  compound="left", width=150)
            elif texto == "Contactos":
                ima = Image.open("contag.png").resize((50, 50))
                botonima = ImageTk.PhotoImage(ima)
                boton = tk.Button(self.ventana, image=botonima, text=texto, command=self.ver_contactos,
                                  compound="left", width=150)

            boton.image = botonima
            boton.grid(row=i, column=0, padx=10, pady=5)
            
            # Guardar referencia al botón
            self.botones[texto] = boton
        
        # Actualizar estado inicial de los botones
        self.actualizar_estado_botones()

    def estructura_de_la_agenda(self):
        self.ventana3 = tk.Toplevel(self.ventana)
        self.ventana3.title("Agregar Contacto")

        etiquetas = ["Nombre", "Teléfono", "Dirección"]
        campos = []

        for i, texto in enumerate(etiquetas):
            tk.Label(self.ventana3, text=texto).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.ventana3, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            campos.append(entry)

        def guardar_contacto():
            nombre = campos[0].get().strip()
            telefono = campos[1].get().strip()
            direccion = campos[2].get().strip()

            # Validar que todos los campos tengan datos
            if not nombre or not telefono or not direccion:
                messagebox.showwarning("Campos vacíos", "Por favor llena todos los campos.")
                return

            contacto = {
                "nombre": nombre,
                "telefono": telefono,
                "direccion": direccion
            }
            self.contactos.append(contacto)
            for campo in campos:
                campo.delete(0, tk.END)
            print("Contacto guardado:", contacto)
            
            # Actualizar estado de botones en el menú principal
            self.actualizar_estado_botones()

        tk.Button(self.ventana3, text="Guardar", command=guardar_contacto).grid(row=3, column=0, columnspan=2, pady=10)
        self.boton_salir(self.ventana3)

    def eliminar_contacto(self):
        ventana2 = tk.Toplevel(self.ventana)
        ventana2.title("Eliminar Contacto")

        tk.Label(ventana2, text="Nombre a eliminar:").grid(row=0, column=0, padx=5, pady=5)
        entrada = tk.Entry(ventana2)
        entrada.grid(row=0, column=1, padx=5, pady=5)

        def eliminar():
            nombre = entrada.get().strip()
            if not nombre:
                messagebox.showwarning("Campo vacío", "Por favor ingresa el nombre del contacto.")
                return
                
            for contacto in self.contactos:
                if contacto["nombre"] == nombre:
                    self.contactos.remove(contacto)
                    break
            entrada.delete(0, tk.END)
            
            # Actualizar estado de botones
            self.actualizar_estado_botones()

        tk.Button(ventana2, text="Eliminar", command=eliminar).grid(row=1, column=0, columnspan=2, pady=10)
        self.boton_salir(ventana2)

    def editar_contacto(self):
        ventana_editar = tk.Toplevel(self.ventana)
        ventana_editar.title("Editar Contacto")

        tk.Label(ventana_editar, text="Nombre del contacto a editar:").grid(row=0, column=0, padx=5, pady=5)
        entrada_nombre = tk.Entry(ventana_editar)
        entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

        def buscar_y_editar():
            nombre = entrada_nombre.get().strip()
            if not nombre:
                messagebox.showwarning("Campo vacío", "Por favor ingresa el nombre del contacto.")
                return
                
            for contacto in self.contactos:
                if contacto["nombre"] == nombre:
                    tk.Label(ventana_editar, text="Nuevo teléfono:").grid(row=2, column=0, padx=5, pady=5)
                    nuevo_tel = tk.Entry(ventana_editar)
                    nuevo_tel.insert(0, contacto["telefono"])
                    nuevo_tel.grid(row=2, column=1, padx=5, pady=5)

                    tk.Label(ventana_editar, text="Nueva dirección:").grid(row=3, column=0, padx=5, pady=5)
                    nueva_dir = tk.Entry(ventana_editar)
                    nueva_dir.insert(0, contacto["direccion"])
                    nueva_dir.grid(row=3, column=1, padx=5, pady=5)
                    
                    tk.Label(ventana_editar, text="Nuevo nombre:").grid(row=4, column=0, padx=5, pady=5)
                    nuevo_nom = tk.Entry(ventana_editar)
                    nuevo_nom.insert(0, contacto["nombre"])
                    nuevo_nom.grid(row=4, column=1, padx=5, pady=5)

                    def guardar_cambios():
                        nuevo_nombre = nuevo_nom.get().strip()
                        nuevo_telefono = nuevo_tel.get().strip()
                        nueva_direccion = nueva_dir.get().strip()
                        
                        # Validar que todos los campos tengan datos
                        if not nuevo_nombre or not nuevo_telefono or not nueva_direccion:
                            messagebox.showwarning("Campos vacíos", "Por favor llena todos los campos.")
                            return
                        
                        contacto["telefono"] = nuevo_telefono
                        contacto["direccion"] = nueva_direccion
                        contacto["nombre"] = nuevo_nombre
                        ventana_editar.destroy()
                        print("Contacto actualizado:", contacto)

                    tk.Button(ventana_editar, text="Guardar Cambios", command=guardar_cambios).grid(row=5, column=0, columnspan=2, pady=10)
                    break
            else:
                tk.Label(ventana_editar, text="Contacto no encontrado.").grid(row=5, column=0, columnspan=2)

        tk.Button(ventana_editar, text="Buscar", command=buscar_y_editar).grid(row=1, column=0, columnspan=2, pady=5)
        self.boton_salir(ventana_editar)

    def ver_contactos(self):
        ventana_contactos = tk.Toplevel(self.ventana)
        ventana_contactos.title("Contactos Guardados")

        if not self.contactos:
            tk.Label(ventana_contactos, text="No hay contactos guardados.").pack(padx=10, pady=10)
        else:
            for i, contacto in enumerate(self.contactos):
                texto = f"{i + 1}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Dirección: {contacto['direccion']}"
                tk.Label(ventana_contactos, text=texto).pack(anchor="w", padx=10)

        self.boton_salir(ventana_contactos)

ventana = tk.Tk()
agen = Agenda(ventana)
agen.Menu_principal()
ventana.mainloop()