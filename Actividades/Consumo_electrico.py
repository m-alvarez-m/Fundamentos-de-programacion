TARIFA = 2.50
CUOTA_FIJA = 40

def calcular_consumo(anterior, actual):
    consumo = actual - anterior
    return consumo

def calcular_importe(consumo):
    importe = consumo * TARIFA + CUOTA_FIJA
    return importe

def mostrar_recibo(anterior, actual, consumo, importe):
    print("Lectura anterior:", anterior)
    print("Lectura actual:", actual)
    print("Consumo:", consumo)
    print("Total: $", importe)

def clasificar_consumo(consumo, limite_bajo, limite_medio):
    if consumo <= limite_bajo:
        return "Bajo"
    elif consumo <= limite_medio:
        return "Medio"
    else:
        return "Alto"

anterior = float(input("Lectura anterior: "))
actual = float(input("Lectura actual: "))

if actual < anterior:
    print("Error")
else:
    consumo = calcular_consumo(anterior, actual)
    importe = calcular_importe(consumo)

    mostrar_recibo(anterior, actual, consumo, importe)

    limite_bajo = float(input("Límite bajo: "))
    limite_medio = float(input("Límite medio: "))

    if limite_bajo < 0 or limite_medio <= limite_bajo:
        print("Error")
    else:
        clasificacion = clasificar_consumo(consumo, limite_bajo, limite_medio)
        print("Clasificación:", clasificacion)