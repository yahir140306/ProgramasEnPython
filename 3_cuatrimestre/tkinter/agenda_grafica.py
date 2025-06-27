import tkinter as tk 
import tkinter.messagebox

class agenda:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("170x250")
        self.ventana.title("Agenda de contactos")
        self.contactos = []
        self.imagen_boton = None
    
    def boton_salir(self, ventana_a_cerrar):
        """Crea un botón de salir que cierra la ventana especificada"""
        salir = tk.Button(ventana_a_cerrar, text="Salir", command=ventana_a_cerrar.destroy)
        return salir
    
    def Menu_principal(self):
        # Limpiar la ventana principal
        for widget in self.ventana.winfo_children():
            widget.destroy()
            
        menu = ["Agregar", "Eliminar", "Editar_contacto", "Contactos"]
        
        for i, texto in enumerate(menu):
            # Crear botones sin imágenes por simplicidad (puedes agregar las imágenes después)
            if texto == "Agregar":
                boton = tk.Button(self.ventana, text=texto, command=self.estructura_de_la_agenda, width=15)
            elif texto == "Eliminar":
                boton = tk.Button(self.ventana, text=texto, command=self.eliminar_contacto, width=15)
            elif texto == "Editar_contacto":
                boton = tk.Button(self.ventana, text="Editar", command=self.editar_contacto, width=15)
            elif texto == "Contactos":
                boton = tk.Button(self.ventana, text=texto, command=self.ver_contactos, width=15)
            
            boton.grid(row=i, column=0, padx=10, pady=5)
        
        # Botón de salir de la aplicación
        salir_app = tk.Button(self.ventana, text="Salir", command=self.ventana.quit, width=15)
        salir_app.grid(row=len(menu), column=0, padx=10, pady=10)

    def eliminar_contacto(self):
        self.ventana2 = tk.Toplevel(self.ventana)
        self.ventana2.title("Eliminar contacto")
        self.ventana2.geometry("300x150")
        
        eliminar = tk.Label(self.ventana2, text="Ingrese el nombre a eliminar:")
        eliminar.grid(row=0, column=0, padx=10, pady=10)
        
        self.nombre_a_eliminar = tk.Entry(self.ventana2, width=20)
        self.nombre_a_eliminar.grid(row=0, column=1, padx=10, pady=10)
        
        def confirmar_eliminacion():
            nombre = self.nombre_a_eliminar.get().strip()
            if nombre:
                # Buscar y eliminar el contacto
                for i, contacto in enumerate(self.contactos):
                    if contacto['nombre'].lower() == nombre.lower():
                        self.contactos.pop(i)
                        tk.messagebox.showinfo("Éxito", f"Contacto '{nombre}' eliminado correctamente")
                        self.ventana2.destroy()
                        return
                tk.messagebox.showwarning("Error", f"No se encontró el contacto '{nombre}'")
            else:
                tk.messagebox.showwarning("Error", "Por favor ingrese un nombre")
        
        boton_eliminar = tk.Button(self.ventana2, text="Eliminar", command=confirmar_eliminacion)
        boton_eliminar.grid(row=1, column=0, padx=10, pady=10)
        
        # Botón de salir
        boton_salir = self.boton_salir(self.ventana2)
        boton_salir.grid(row=1, column=1, padx=10, pady=10)

    def estructura_de_la_agenda(self):
        self.ventana3 = tk.Toplevel(self.ventana)
        self.ventana3.title("Agregar contacto")
        self.ventana3.geometry("400x200")
        
        etiquetas = ["Nombre:", "Teléfono:", "Dirección:"]
        campos = []
        
        for i, texto in enumerate(etiquetas):
            label = tk.Label(self.ventana3, text=texto)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.ventana3, width=30)
            entry.grid(row=i, column=1, padx=10, pady=5)
            campos.append(entry)

        def guardar_contacto():
            nombre = campos[0].get().strip()
            telefono = campos[1].get().strip()
            direccion = campos[2].get().strip()
            
            if nombre and telefono:  # Validar que al menos nombre y teléfono estén llenos
                contacto = {
                    "nombre": nombre,
                    "telefono": telefono,
                    "direccion": direccion
                }
                self.contactos.append(contacto)
                tk.messagebox.showinfo("Éxito", "Contacto guardado correctamente")
                self.ventana3.destroy()
            else:
                tk.messagebox.showwarning("Error", "Por favor complete al menos el nombre y teléfono")
        
        if self.imagen_boton:
            boton_guardar = tk.Button(self.ventana3, text="Guardar", image=self.imagen_boton, 
                                    compound="left", command=guardar_contacto)
        else:
            boton_guardar = tk.Button(self.ventana3, text="Guardar", command=guardar_contacto)
        boton_guardar.grid(row=3, column=0, padx=10, pady=10)
        
        boton_salir = self.boton_salir(self.ventana3)
        boton_salir.grid(row=3, column=1, padx=10, pady=10)

    def editar_contacto(self):
        if not self.contactos:
            tk.messagebox.showinfo("Información", "No hay contactos para editar")
            return
            
        self.ventana4 = tk.Toplevel(self.ventana)
        self.ventana4.title("Editar contacto")
        self.ventana4.geometry("400x250")
        
        # Lista de contactos para seleccionar
        tk.Label(self.ventana4, text="Seleccione el contacto a editar:").grid(row=0, column=0, columnspan=2, pady=10)
        
        self.lista_contactos = tk.Listbox(self.ventana4, width=50, height=5)
        for i, contacto in enumerate(self.contactos):
            self.lista_contactos.insert(i, f"{contacto['nombre']} - {contacto['telefono']}")
        self.lista_contactos.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        
        def seleccionar_contacto():
            seleccion = self.lista_contactos.curselection()
            if seleccion:
                indice = seleccion[0]
                contacto = self.contactos[indice]
                self.abrir_formulario_edicion(contacto, indice)
            else:
                tk.messagebox.showwarning("Error", "Por favor seleccione un contacto")
        
        boton_seleccionar = tk.Button(self.ventana4, text="Editar", command=seleccionar_contacto)
        boton_seleccionar.grid(row=2, column=0, padx=10, pady=10)
        
        # Botón de salir
        boton_salir = self.boton_salir(self.ventana4)
        boton_salir.grid(row=2, column=1, padx=10, pady=10)

    def abrir_formulario_edicion(self, contacto, indice):
        self.ventana5 = tk.Toplevel(self.ventana)
        self.ventana5.title("Editar contacto")
        self.ventana5.geometry("400x200")
        
        etiquetas = ["Nombre:", "Teléfono:", "Dirección:"]
        campos = []
        valores = [contacto['nombre'], contacto['telefono'], contacto['direccion']]
        
        for i, (texto, valor) in enumerate(zip(etiquetas, valores)):
            label = tk.Label(self.ventana5, text=texto)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(self.ventana5, width=30)
            entry.insert(0, valor)
            entry.grid(row=i, column=1, padx=10, pady=5)
            campos.append(entry)

        def actualizar_contacto():
            nombre = campos[0].get().strip()
            telefono = campos[1].get().strip()
            direccion = campos[2].get().strip()
            
            if nombre and telefono:
                self.contactos[indice] = {
                    "nombre": nombre,
                    "telefono": telefono,
                    "direccion": direccion
                }
                tk.messagebox.showinfo("Éxito", "Contacto actualizado correctamente")
                self.ventana5.destroy()
            else:
                tk.messagebox.showwarning("Error", "Por favor complete al menos el nombre y teléfono")
        
        boton_actualizar = tk.Button(self.ventana5, text="Actualizar", command=actualizar_contacto)
        boton_actualizar.grid(row=3, column=0, padx=10, pady=10)
        
        # Botón de salir
        boton_salir = self.boton_salir(self.ventana5)
        boton_salir.grid(row=3, column=1, padx=10, pady=10)

    def ver_contactos(self):
        ventana_contactos = tk.Toplevel(self.ventana)
        ventana_contactos.title("Contactos guardados")
        ventana_contactos.geometry("500x400")

        if not self.contactos:
            tk.Label(ventana_contactos, text="No hay contactos guardados.", 
                    font=("Arial", 12)).pack(padx=10, pady=20)
        else:
            # Crear un frame con scrollbar
            frame = tk.Frame(ventana_contactos)
            frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            scrollbar = tk.Scrollbar(frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            text_widget = tk.Text(frame, yscrollcommand=scrollbar.set, wrap=tk.WORD)
            text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            
            scrollbar.config(command=text_widget.yview)
            
            # Mostrar todos los contactos
            for i, contacto in enumerate(self.contactos):
                texto = f"{i + 1}. Nombre: {contacto['nombre']}\n"
                texto += f"   Teléfono: {contacto['telefono']}\n"
                texto += f"   Dirección: {contacto['direccion']}\n\n"
                text_widget.insert(tk.END, texto)
            
            text_widget.config(state=tk.DISABLED)  # Hacer el texto de solo lectura
        
        # Botón de salir
        boton_salir = self.boton_salir(ventana_contactos)
        boton_salir.pack(pady=10)

import tkinter.messagebox

ventana = tk.Tk()
agen = agenda(ventana)
agen.Menu_principal()
ventana.mainloop()