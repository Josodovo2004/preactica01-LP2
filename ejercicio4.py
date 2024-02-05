tareas = [] #lista donde guardaremos los productos
#generara automaticamente el id del producto

def agregar_tarea():
    descripcion = input("Elija el nombre del producto: ")
    estado = input("Cuanto stock del producto hay: ")
    if len(tareas) == 0:
        tareas.append([1, descripcion, estado])
    else:
        a = tareas[-1][0]
        tareas.append([a+1, descripcion, estado])
     #Esto hara que cada ves que se registre 1 producto el numero del id cambie
    
def eliminar_tarea():
    id_eliminado = int(input("Ingrese el Id del producto que desea eliminar: "))
    
    for i in range(len(tareas)):
        if tareas[i][0] == id_eliminado:
            tareas.pop(i)

def mostrar_tareas():
    for tarea in tareas:
        print(f"Descripcion: {tarea[1]}, estado: {tarea[2]}")

def marcar_completado():
    id_completado = int(input("Ingrese la tarea que desea marcar como completada: "))
    for i in range(len(tareas)):
        if tareas[i][0] == id_completado:
            tareas[i][2] == "Completado" 
    

def main():
    while True:
        eleccion = int(input("Elija una de las opciones (1,2,3,4,5)"))
    
        if eleccion == 1:
            agregar_tarea()
        elif eleccion == 2:
            eliminar_tarea()
        elif eleccion == 3:
            mostrar_tareas()
        elif eleccion == 4:
            marcar_completado()
        elif eleccion == 5:
            break
        else:
            print("Eliccion no valida")

main()
