
#Se crea la lista vacia
listaRegistros = []
clientes = 0
limite = clientes + 1
cTotal=0

while clientes <limite:
    #Ingresar datos Usuarios
    nombre = input("Ingrese el nombre: ")
    producto = input("Ingrese su producto: ")
    costo = float(input("Ingrese el costo: "))   
    
    #Se crea el diccionario
    registro = dict(nombre=nombre, producto=producto, costo=costo)
    listaRegistros.append(registro)
    
    cTotal += registro["costo"]

    terminar = input("Deseas terminar el programa? (Presiona '0' si es así o '1' si no lo deseas): ")
    
    #Condicional que evalua la finalizacion del programa
    if terminar== "0":
        for registro in listaRegistros:
            print(registro)
        print("Costo Final:", cTotal)
        clientes= limite +1
    elif terminar == "1":
        clientes +=1 
        limite +=1
    else:
        print("Presiona un número válido")
        clientes +=1 
        limite +=1




