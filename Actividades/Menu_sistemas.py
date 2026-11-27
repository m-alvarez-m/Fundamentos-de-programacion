inventario = 1
boletera = 2
caja_registradora = 3
medidor = 4

while menu == 0:
        print("            MENU            ")
        menu = int(input("presiona (1, 4)  (0) para salir: "))

        if menu == 1:
                print("----inventario----")
                from Papeleria import inventario
                inventario()

        elif menu == 2:
                print("----boletera----")
                from Museo import boletera
                boletera()

        elif menu == 3:
                print("----caja registradora----")
                from Punto_de_venta import caja_registradora
                caja_registradora()

        elif menu == 4:
                print("----medidor electrico----")
                from Consumo_electrico import medidor
                medidor()

