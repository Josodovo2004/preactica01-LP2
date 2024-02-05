productos = [] #lista donde guardaremos los productos
#generara automaticamente el id del producto

def agregar_producto():
    nombre = input("Elija el nombre del producto: ")
    cantidad = int(input("Cuanto stock del producto hay: "))
    precio = int(input("Cuanto es el precio del producto: "))
    if len(productos) == 0:
        productos.append([1, nombre, cantidad, precio])
    else:
        a = productos[-1][0]
        productos.append([a+1, nombre, cantidad, precio])
    print(productos)
     #Esto hara que cada ves que se registre 1 producto el numero del id cambie
    
def eliminar_producto():
    id_eliminado = int(input("Ingrese el Id del producto que desea eliminar: "))
    
    for i in range(len(productos)):
        if productos[i][0] == id_eliminado:
            productos.pop(i)
def actualizar_producto():
    idActualizado = int(input("Ingrese el Id del producto que desea actualizar: "))
    
    for i in range(len(productos)):
        if productos[i][0] == idActualizado:
            productos[i][1] = input("Como sera el nombre: ")
            productos[i][2] = int(input("Cuanta cantidad hay: "))
            productos[i][3] = int(input("Cuanto cuesta ahora: "))
            break
            
def buscar_por_id():
    idBuscado = int(input("Escriba el id del producto que desea ver: "))
    
    for i in range(len(productos)):
        if productos[i][0] == idBuscado:
            print(f"El producto: {productos[i][1]}, cantidad: {productos[i][2]}, precio {productos[i][3]}")
            print(1)
            break
        else:
            print("nada")
def buscar_por_nombre():
    nombreBuscado = int(input("Escriba el nombre del producto que desea ver: "))
    
    for i in range(len(productos)):
        if productos[i][1] == nombreBuscado:
            print(f"El producto: {productos[i][1]}, cantidad: {productos[i][2]}, precio {productos[i][3]}")
            print(1)
def calcular_c_total():
    valorTotal = 0
    for producto in productos:
        valorTotal += producto[2] * producto[3]
    print(f"El valor total de los productos es {valorTotal}")

def main():
    while True:
        
        print("""Opciones:
              1-Agregar productos
              2-Eliminar Productos
              3-Actualizar producto
              4-Buscar Producto
              5-Calcular valor total valor del inventario
              6- Salir""")
        
        eleccion = int(input("Ingrese la opcion que desea ejecutar: "))
        
        if eleccion == 1:
            agregar_producto()
        elif eleccion == 2:
            eliminar_producto()
        elif eleccion == 3:
            actualizar_producto()
        elif eleccion == 4:
            print("""Opciones:
                    1) Buscar por nombre
                    2)Buscar por Id""")
            elecciones = [1,2]
            eleccion2 = int(input("Elija una de las opciones: "))
            while eleccion2 not in elecciones:
                print("Opcion no valida")
            if eleccion2 == 1:
                buscar_por_nombre()
            elif eleccion2 == 2:
                buscar_por_id()   
        elif eleccion == 5:
            calcular_c_total()
        elif eleccion == 6:
            break
        else:
            print("Eliccion no valida")
            
main()