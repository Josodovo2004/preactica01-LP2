empleados = [] #lista donde guardaremos los productos
#generara automaticamente el id del producto

def agregar_empleado():
    nombre = input("Cual es el nombre del empleado: ")
    salario = int(input("Cuanto es el salario del empleado: "))
    departamento = int(input("En que departamento trabaja: "))
    if len(empleados) == 0:
        empleados.append([1, nombre, salario, departamento])
    else:
        a = empleados[-1][0]
        empleados.append([a+1, nombre, salario, departamento])
    print(empleados)
     #Esto hara que cada ves que se registre 1 producto el numero del id cambie
    
def eliminar_empleado():
    id_eliminado = int(input("Ingrese el Id del producto que desea eliminar: "))
    
    for i in range(len(empleados)):
        if empleados[i][0] == id_eliminado:
            empleados.pop(i)

def buscar_por_id():
    idBuscado = int(input("Escriba el id del producto que desea ver: "))
    
    for i in range(len(empleados)):
        if empleados[i][0] == idBuscado:
            print(f"Empleado: {empleados[i][1]}, salario: {empleados[i][2]}, departamento {empleados[i][3]}")
            break
        else:
            print("nada")
def buscar_por_nombre():
    nombreBuscado = int(input("Escriba el nombre del producto que desea ver: "))
    
    for i in range(len(empleados)):
        if empleados[i][1] == nombreBuscado:
            print(f"Empleado: {empleados[i][1]}, salario: {empleados[i][2]}, departamento {empleados[i][3]}")
            
def mostrar_empleados():
    for empleado in empleados:
        print(f"Empleado: {empleado[1]}, salario: {empleado[2]}, departamento {empleado[3]}")
        
def salario_promedio_departamento():
    departamento = int(input("De que departamento quiere consultar: "))
    sumaSalarios = 0
    for empleado in empleados:
        if empleado[3] == departamento:
            sumaSalarios += empleado[3]
    print(sumaSalarios)
            
def salario_promedio():
    sumaSalarios = 0
    for empleado in empleados:
        sumaSalarios += empleado[3]        
    print(sumaSalarios)
            

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
            agregar_empleado()
        elif eleccion == 2:
            eliminar_empleado()
        elif eleccion == 3:
            pass
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
            salario_promedio_departamento()
        elif eleccion == 6:
            break
        else:
            print("Eliccion no valida")
            