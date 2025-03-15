import time

print("Simulacion de un reloj, usando el ciclo while y for. Sin usar timer")
# Solicitar la hora al usuario
hora = int(input("Ingrese la hora (0-23): "))
minuto = int(input("Ingrese los minutos (0-59): "))
segundo = int(input("Ingrese los segundos (0-59): "))

while True:  # Bucle infinito para simular un reloj en funcionamiento
    for _ in range(60):  # Iterar los segundos
        print(f"\r{hora:02}:{minuto:02}:{segundo:02}", end="", flush=True)
        time.sleep(1)  # Espera 1 segundo
        segundo += 1
        
        if segundo == 60:
            segundo = 0
            minuto += 1
            
            if minuto == 60:
                minuto = 0
                hora += 1
                
                if hora == 24:
                    hora = 0
