import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora Básica")
ventana.geometry("400x600")

numero1 = ""
numero2 = ""
operacion = ""
escribiendo_primer_numero = True

pantalla = tk.Entry(ventana, font=("arial", 20, "bold"), width=20, justify="right")
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def actualizar_pantalla():
    texto = ""
    
    if numero1:
        texto += numero1
    
    if operacion:
        if operacion == "/":
            texto += " / "
        elif operacion == "*":
            texto += " x "
        else:
            texto += " " + operacion + " "
    
    if numero2:
        texto += numero2
    
    pantalla.delete(0, tk.END)
    if texto:
        pantalla.insert(0, texto)
    else:
        pantalla.insert(0, "0")

def agregar_numero(num):
    global numero1, numero2, escribiendo_primer_numero
    
    if escribiendo_primer_numero:
        numero1 = numero1 + str(num)
    else:
        numero2 = numero2 + str(num)
    
    actualizar_pantalla()

def agregar_punto():
    global numero1, numero2, escribiendo_primer_numero
    
    if escribiendo_primer_numero:
        if "." not in numero1:
            numero1 = numero1 + "."
    else:
        if "." not in numero2:
            numero2 = numero2 + "."
    
    actualizar_pantalla()

def elegir_operacion(op):
    global operacion, escribiendo_primer_numero, numero1
    
    if numero1 != "":
        operacion = op
        escribiendo_primer_numero = False
        actualizar_pantalla()

def calcular():
    global numero1, numero2, operacion, escribiendo_primer_numero
    
    if numero1 != "" and numero2 != "" and operacion != "":
        try:
            num1 = float(numero1)
            num2 = float(numero2)
            
            if operacion == "+":
                resultado = num1 + num2
            elif operacion == "-":
                resultado = num1 - num2
            elif operacion == "*":
                resultado = num1 * num2
            elif operacion == "/":
                if num2 == 0:
                    pantalla.delete(0, tk.END)
                    pantalla.insert(0, "Error: División por 0")
                    return
                else:
                    resultado = num1 / num2
            
            pantalla.delete(0, tk.END)
            if resultado == int(resultado):
                pantalla.insert(0, str(int(resultado)))
                numero1 = str(int(resultado))
            else:
                pantalla.insert(0, str(round(resultado, 4)))
                numero1 = str(round(resultado, 4))
            
            numero2 = ""
            operacion = ""
            escribiendo_primer_numero = True
            
        except ValueError:
            pantalla.delete(0, tk.END)
            pantalla.insert(0, "Error")

def limpiar():
    global numero1, numero2, operacion, escribiendo_primer_numero
    numero1 = ""
    numero2 = ""
    operacion = ""
    escribiendo_primer_numero = True
    actualizar_pantalla()

# def borrar_ultimo():
#     global numero1, numero2, escribiendo_primer_numero
    
#     if escribiendo_primer_numero and numero1:
#         numero1 = numero1[:-1]
#     elif not escribiendo_primer_numero and numero2:
#         numero2 = numero2[:-1]
    
    actualizar_pantalla()

tk.Button(ventana, text="7", command=lambda: agregar_numero(7), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=1, column=0, padx=2, pady=2)
tk.Button(ventana, text="8", command=lambda: agregar_numero(8), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=1, column=1, padx=2, pady=2)
tk.Button(ventana, text="9", command=lambda: agregar_numero(9), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=1, column=2, padx=2, pady=2)

tk.Button(ventana, text="4", command=lambda: agregar_numero(4), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=2, column=0, padx=2, pady=2)
tk.Button(ventana, text="5", command=lambda: agregar_numero(5), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=2, column=1, padx=2, pady=2)
tk.Button(ventana, text="6", command=lambda: agregar_numero(6), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=2, column=2, padx=2, pady=2)

tk.Button(ventana, text="1", command=lambda: agregar_numero(1), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=3, column=0, padx=2, pady=2)
tk.Button(ventana, text="2", command=lambda: agregar_numero(2), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=3, column=1, padx=2, pady=2)
tk.Button(ventana, text="3", command=lambda: agregar_numero(3), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=3, column=2, padx=2, pady=2)

tk.Button(ventana, text="0", command=lambda: agregar_numero(0), 
          font=("arial", 16, "bold"), width=11, height=2).grid(row=4, column=0, columnspan=2, padx=2, pady=2, sticky="ew")
tk.Button(ventana, text=".", command=agregar_punto, 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=4, column=2, padx=2, pady=2)

tk.Button(ventana, text="/", command=lambda: elegir_operacion("/"), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=1, column=3, padx=2, pady=2)
tk.Button(ventana, text="x", command=lambda: elegir_operacion("*"), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=2, column=3, padx=2, pady=2)
tk.Button(ventana, text="-", command=lambda: elegir_operacion("-"), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=3, column=3, padx=2, pady=2)
tk.Button(ventana, text="+", command=lambda: elegir_operacion("+"), 
          font=("arial", 16, "bold"), width=5, height=2).grid(row=4, column=3, padx=2, pady=2)

tk.Button(ventana, text="=", command=calcular, 
          font=("arial", 16, "bold"), width=23, height=2).grid(row=5, column=0, columnspan=4, padx=2, pady=2, sticky="ew")

tk.Button(ventana, text="Limpiar", command=limpiar, 
          font=("arial", 12, "bold")).grid(row=6, column=0, columnspan=2, padx=2, pady=2, sticky="ew")
# tk.Button(ventana, text="Borrar", command=borrar_ultimo, 
#           font=("arial", 12, "bold")).grid(row=6, column=2, columnspan=2, padx=2, pady=2, sticky="ew")

for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

actualizar_pantalla()

ventana.mainloop()