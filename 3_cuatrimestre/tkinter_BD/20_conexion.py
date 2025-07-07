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


def insertar_datos():
    cn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="farmacia_juan_yahir",
    )
    cursor1 = cn.cursor()
    sql = "insert into productos_farmacia (id_producto, nombre, precio) values(%s, %s, %s)"
    datos = (12343, "Ibuprofeno", 50.00)
    cursor1.execute(sql, datos)
    cursor1.close()
    cn.commit()
    print("Datos registrados")


def eliminar_registro():
    cn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="farmacia_juan_yahir",
    )
    cursor1 = cn.cursor()
    sql = "delete from productos_farmacia where id_producto = %s"
    datos = (12343,)
    cursor1.execute(sql, datos)
    cursor1.close()
    cn.commit()
    print("Registro eliminado")


btnConection = tk.Button(frameConection, text="Conectar BD", command=conecctionBD)
btnConection.pack(pady=15)
btnConection = tk.Button(frameConection, text="Seleccionar", command=mostrar_datos)
btnConection.pack(pady=15)

btnConection = tk.Button(frameConection, text="Registrar", command=insertar_datos)
btnConection.pack(pady=15)

# conecctionBD()
frameConection.pack()
root.mainloop()
