import tkinter as tk

ventana = tk.Tk()
ventana.title("Contador")
ventana.geometry("300x300")

lbltitulo = tk.Label(ventana, text="Contador", font=("arial", 20, "bold"))
lblcontador = tk.Label(ventana, text="0", font=("arial", 20, "bold"))
btnClick = tk.Button(ventana, text="Click")

def DarClick(event): 
    contador = int(lblcontador.cget("text"))   
    contador += 1
    lblcontador.config(text=str(contador))

btnClick.bind("<Button-1>", DarClick)

lbltitulo.pack()
lblcontador.pack()
btnClick.pack()

ventana.mainloop()

