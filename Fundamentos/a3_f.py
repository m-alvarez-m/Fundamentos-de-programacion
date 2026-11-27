# ACTIVIDAD 3 FACTORIAL

numero = int(input("Escribe un numero entero: "))
resultado = 1
for contador in range(1, numero +1):
  resultado = resultado * contador
print("El factorial es:", resultado)