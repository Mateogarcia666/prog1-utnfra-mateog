inventario = []

#definimos el menu con prints
def menu():
    print('''Bienvenidos al quiosco Yoda's Snack.
        1. Agregar producto al inventario
        2. Realizar una venta
        3. Mostrar productos disponibles
        4. Salir de Yoda's Snack''' )

#definimos la funcion para agregar productos al inventario
def agregar_al_inventario():
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input(f"Ingrese la cantidad disponible de {nombre}: "))
    precio = float(input(f"Ingrese el precio por unidad de {nombre}: "))
    
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado al inventario.")

#realizamos venta de productos con el bucle for para recorrer la lista, elegir el producto y su cantidad
def realizar_venta():
    if len(inventario) == 0:
        print("El inventario se encuentra sin productos")
    else:
        nombre_producto = input("Ingrese el nombre del producto: ")
        producto_elegido = None
        for producto in inventario:
            if producto["nombre"] == nombre_producto:
                producto_elegido = producto
                break
            
        if producto_elegido == None:
                print("Opcion invalida")
        else: 
            cantidad_producto = int(input("Ingrese la cantidad del producto elegido: "))

            if cantidad_producto > producto_elegido ['cantidad']:
                print("No hay suficiente stock")
            else:
                producto_elegido ['cantidad'] -= cantidad_producto
                total = cantidad_producto * producto_elegido ['precio']
                print(f"Usted acaba de comprar {cantidad_producto} de {producto_elegido ['nombre']}, todo a un total de {total}")

#Mostramos el contenido de la lista si hay algo o no
def mostrar_productos():
    if inventario == False:
        print("El inventario se encuentra sin productos")
    else: 
        for producto in inventario:
            print(f"{producto ['nombre']}, con un precio de {producto ['precio']}, cantidad disponible {producto ['cantidad']}")

