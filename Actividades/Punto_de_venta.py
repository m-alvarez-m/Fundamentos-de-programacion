for dia in range(1, 6):
    cuenta = 0
    total = 0
    extraordinarias = 0
    total_extraordinario = 0
    caja = True
    
    while caja == True:
        venta = float(input("Ingresa la venta: "))

        if venta == 0:
            caja = False
        else:
            cuenta = cuenta + 1
            total = total + venta

            if venta > 1000:
                extraordinarias = extraordinarias + 1
                total_extraordinario = total_extraordinario + venta

    if cuenta > 0:
        promedio = total / cuenta
    else:
        promedio = 0

    print("Total de ventas:", cuenta)
    print("Total vendido:", total)
    print("Promedio:", promedio)
    print("Ventas extraordinarias:", extraordinarias)
    print("Importe extraordinario:", total_extraordinario)