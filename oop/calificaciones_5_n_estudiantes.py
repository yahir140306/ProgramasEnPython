# class calificaciones:
#     def __init__(self):
#         pass
        


def pedir_calificaciones():
    calificacion_suma = 0
    for i in range(5):
        calificacion = float(input(f"Ingrese la calificacion {i+ 1}: "))
        calificacion_suma += calificacion 
        promedio = calificacion_suma / 5        
    print(f"Tu promedio general es: {promedio}")


pedir_calificaciones()

# def main():
#     # calificaciones.pedir_calificaciones()
#     pedir_calificaciones()

# if __name__ == "__main__":
#     main()