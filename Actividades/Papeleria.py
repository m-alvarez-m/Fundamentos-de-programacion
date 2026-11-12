IVA = 0.16
producto_a = input("Escribe el nombre del producto: ")
cantidad_a = int(input("Escribe la cantidad: "))
precio_a = float(input("Escribe el precio: "))

producto_b = input("Escribe el nombre del producto: ")
cantidad_b = int(input("Escribe la cantidad: "))
precio_b = float(input("Escribe el precio: "))

producto_c = input("Escribe el nombre del producto: ")
cantidad_c = int(input("Escribe la cantidad: "))
precio_c = float(input("Escribe el precio: "))

subtotal = float(cantidad_a * precio_a)+(cantidad_b * precio_b)+(cantidad_c * precio_c)
print("sin iva ", subtotal)

calcular_iva = subtotal * IVA
print("Iva", calcular_iva)

total = calcular_iva + subtotal
print("Total", total)