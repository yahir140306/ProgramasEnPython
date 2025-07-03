import tkinter as tk

class todo_list_interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tareas")
        self.master.geometry("300x400")
        
        self.tasks = []
        
        self.task_label = tk.Label(master, text="Tarea:")
        self.task_label.pack(pady=10)
        
        self.task_entry = tk.Entry(master)
        self.task_entry.pack(pady=5)
        
        self.add_button = tk.Button(master, text="Agregar Tarea", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.remove_button = tk.Button(master, text="Eliminar Tarea", command=self.remove_task)
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_indices = list(self.task_listbox.curselection())
        for index in reversed(selected_indices):
            del self.tasks[index]
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
    
if __name__ == "__main__":
    root = tk.Tk()
    app = todo_list_interface(root)
    root.mainloop()
