DESCUENTO_ESTUDIANTE = 0.75

edad_0 = -1
edad_12 = 12
edad_59 = 59
edad_60 = 60

boleto_menor = 40
boleto_adulto = 100
boleto_adulto_mayor = 60

edad_visitante = int(input("Escribe tu edad: "))

if edad_visitante <= edad_0:
  print("Su boleto es nulo")

elif edad_visitante <= edad_12:
  precio = boleto_menor
  print("Su boleto es menor")
  estado = input("Eres estudiante (Si o No): ")

  if estado == "Si"or estado == "si":
    print("Tienes descuento")
    descuento = (boleto_menor * DESCUENTO_ESTUDIANTE)
    print ("Tu boleto es de: $", descuento)
  elif edad_visitante > edad_0:
    print("No es un boleto oficial")
  else:
    print("Tu boleto es de: $", boleto_menor)


elif edad_visitante <= edad_59:
  precio = boleto_adulto
  print("Su boleto es adulto")
  estado = input("Eres estudiante (Si o No): ")

  if estado == "Si" or estado == "si":
    print("Tienes descuento")
    descuento = (boleto_adulto * DESCUENTO_ESTUDIANTE)
    print ("Tu boleto es de: $", (descuento))
  else:
    print("Tu boleto es de: $", boleto_adulto)

else:
  edad_visitante >= edad_60
  precio = boleto_adulto_mayor
  print("Su boleto es adulto mayor")
  print("Tu boleto es de:$", boleto_adulto_mayor)