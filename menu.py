from funciones import *

#Importamos las funciones y armamos un bucle para el menu
inventario =  []
while True:
    menu()
    opcion = input("Seleccione una opcion (1,2,3,4): ")

    if opcion == '1':
        agregar_al_inventario()
    elif opcion == '2':
        realizar_venta()
    elif opcion == '3':
        mostrar_productos()
    elif opcion == '4':
        break
    else: 
        print("Opcion invalida")

