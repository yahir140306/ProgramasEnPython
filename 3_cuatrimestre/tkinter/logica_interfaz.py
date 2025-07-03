class LogicaTareas:    
    def __init__(self):
        self.tareas_por_hacer = []
        self.tareas_completadas = []
    
    def agregar_nueva_tarea(self, texto_tarea):
        texto_tarea = texto_tarea.strip()
        if texto_tarea:
            self.tareas_por_hacer.append(texto_tarea)
            return True
        return False
    
    def marcar_como_completada(self, tarea):
        if tarea in self.tareas_por_hacer:
            self.tareas_por_hacer.remove(tarea)
            self.tareas_completadas.append(tarea)
            return True
        return False
    
    def eliminar_tarea_pendiente(self, tarea):
        if tarea in self.tareas_por_hacer:
            self.tareas_por_hacer.remove(tarea)
            return True
        return False
    
    def eliminar_tarea_completada(self, tarea):
        if tarea in self.tareas_completadas:
            self.tareas_completadas.remove(tarea)
            return True
        return False
