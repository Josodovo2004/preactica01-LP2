tareas = [] #lista donde guardaremos los productos
#generara automaticamente el id del producto

def agregar_producto():
    descripcion = input("Elija el nombre del producto: ")
    estado = input("Cuanto stock del producto hay: ")
    if len(tareas) == 0:
        tareas.append([1, descripcion, estado])
    else:
        a = tareas[-1][0]
        tareas.append([a+1, descripcion, estado, precio])
     #Esto hara que cada ves que se registre 1 producto el numero del id cambie
    
def eliminar_producto():
    id_eliminado = int(input("Ingrese el Id del producto que desea eliminar: "))
    
    for i in range(len(productos)):
        if tareas[i][0] == id_eliminado:
            tareas.pop(i)

def mostrar_empleados():
    for empleado in tareas:
        print(f"Empleado: {tareas[1]}, salario: {tareas[2]}")
