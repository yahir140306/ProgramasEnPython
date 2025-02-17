def calcular_cambio(monto_pagado, monto_total):
    cambio = monto_pagado - monto_total

    if cambio < 0:
        return "El monto pagado es insuficiente para cubrir el total."

    denominaciones = [500, 200, 100, 50, 20, 10, 5, 2, 1]

    desglose = {}

    for denom in denominaciones:
        cantidad = cambio // denom
        if cantidad > 0:
            desglose[denom] = cantidad
            cambio -= cantidad * denom

    return desglose, cambio

monto_total = int(input("¿Cuánto debe pagar?: "))
monto_pagado = int(input("¿Con cuánto va a pagar?: "))

desglose, cambio = calcular_cambio(monto_pagado, monto_total)

if isinstance(desglose, str):
    print(desglose)

else:
    print(f"\nCambio a devolver: {monto_pagado - monto_total} pesos")
    print("Desglose del cambio:")

    for denom, cantidad in desglose.items():
        print(f"{cantidad} billetes o monedas de {denom} pesos")

tipo = type(desglose)
print(tipo)
