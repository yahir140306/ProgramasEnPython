import tkinter as tk
import mysql.connector


root = tk.Tk()
root.title("Conexion a BD")
root.geometry("600x600")
frameConection = tk.Frame()


def conecctionBD():
    cn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="farmacia_juan_yahir",
    )
    cursor1 = cn.cursor()
    cursor1.execute("show databases")

    for base in cursor1:
        print(base)
    print(cn)
    cursor1.close()


def mostrar_datos():
    cn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="farmacia_juan_yahir",
    )
    cursor1 = cn.cursor()
    cursor1.execute("select * from productos_farmacia")
    for fila in cursor1:
        lblDatos = tk.Label(frameConection, text=fila)
        lblDatos.pack()
        print(fila)


btnConection = tk.Button(frameConection, text="Conectar BD", command=conecctionBD)
btnConection.pack(pady=15)
btnConection = tk.Button(frameConection, text="Seleccionar", command=mostrar_datos)
btnConection.pack(pady=15)

# conecctionBD()
frameConection.pack()
root.mainloop()
