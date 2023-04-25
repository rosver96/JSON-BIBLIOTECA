# EVALUACIÓN CICLO 1
# Elabore un programa Python para gestionar el CRUD del archivo de datos PetShopping.json con las siguientes funcionalidades:

# 1. Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios
# 2. Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio
# 3. Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios
# 4. Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por índice)
# 5. Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice)

import json

print("\n\n")


def verMenu():
    print("1).Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios\n2).Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio\n3).Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios\n4).Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por índice)\n5).Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice)\n")
    

def mostrarIndice():
    with open("./PetShopping.json","r") as archivo:
        lista = json.load(archivo)
    archivo.close()
    print('\n****************** LISTA ******************\n')
    y = len(lista["petstore"]["pet"])
    listaPET='INDICE'+'\t'+'\t'+'TIPO'+'\t'+'RAZA\t\t'+'TALLA\t'+'PRECIO\t\t'+'SERVICIOS\n'
    for i in range(y):
        listaPET+=str(i+1)+'\t'+'\t'+lista["petstore"]["pet"][i]["tipo"]+"\n"
    print(listaPET)
    

def listarMascotas():
    print("********* LISTADO DE MASCOTAS *********\n")
    print("tipo\t\t\traza\t\t\tprecio\t\t\t\tservicios\t\t\t")
    with open("./PetShopping.json" ,"r") as archivo :
        mascotas = json.load(archivo)
    for mascota in mascotas["petstore"]["pet"]: 
        print(mascota["tipo"],"\t",mascota["raza"],"\t",mascota["precio"],"\t",mascota["servicios"])
        

def crearMascota():
        with open("./PetShopping.json" ,"r") as archivo :
            mascotas = json.load(archivo)
        tipo = input("ingrese el tipo: ")
        raza = input("ingrese la raza: ")
        talla = input("ingrese la talla: ")
        precio = int(input("ingrese el precio: "))
        servicios = (input("ingrese los servicios: "))
        mascotas["petstore"]["pet"].append({"tipo": tipo, "raza" : raza, "talla":talla, "precio":precio,"servicios":servicios})
        print("********** MASCOTA CREADA EXITOSAMENTE *****************\n")
        with open ("./PetShopping.json" ,"w") as archivo:
            json.dump(mascotas,archivo)


def mostarPorTipo():
    with open ("./PetShopping.json","r") as archivo:
        mascotas = json.load(archivo)
    tipo = input("ingrese el tipo de mascota: ")
    print("RAZA\t\t\tPRECIO\t\t\tSERVICIOS\t\t\t")
    for mascota in mascotas["petstore"]["pet"]:
        if mascota ["tipo"] == tipo:
            print("\n",mascota["raza"],mascota["precio"],mascota["servicios"])
            
            
def actulizarMascota():

    mostrarIndice()
    with open("./PetShopping.json",'r') as archivo:
        mascotas = json.load(archivo)
    indice = input("ingrese el indice a actualizar: ")
    print("¿QUE DATO DESEAS ACTUALIZAR?\n")
    print("1. tipo")
    print("2. raza")
    print("3. talla")
    print("4. precio")
    print("5. servicios")
    opcion = input()
    if opcion == "1":
        tipo = input("ingrese un nuevo tipo: \n")
        mascotas["petstore"]["pet"][indice]["tipo"] = tipo
        print(f"el dato de tipo {tipo} se han actualizado\n")
    elif opcion == "2":
        raza = input("ingrese la raza de la mascota \n")
        mascotas["petstore"]["pet"][indice]["raza"] = raza
        print(f"el dato de raza {raza} se han actualizado\n")
    elif opcion == "3":
        talla = input("ingrese la talla de la mascota \n")
        mascotas["petstore"]["pet"][indice]["talla"] = talla
        print(f"el dato de la talla {talla} se han actualizado\n")
    elif opcion == "4":
        precio = int(input("ingrese la precio de la mascota \n"))
        mascotas["petstore"]["pet"][indice]["precio"] = precio
        print(f"el dato del precio {precio} se han actualizado\n")
    elif opcion == "5":
        servicios = input("ingrese los nuevos servicios de la mascota \n")
        mascotas["petstore"]["pet"][indice]["servicios"] = servicios
        print(f"el dato de los servicios {servicios} se han actualizado\n")
        
    with open("./PetShopping.json",'w') as archivo:
        json.dump(mascotas, archivo,)

    
def eliminarMascota():
    mostrarIndice()
    print("INGRESE EL INDICE QUE DESEAS ELIMINAR")
    mascot = int(input())
    with open("./PetShopping.json",'r') as archivo:
        mascotas = json.load(archivo)
        mascotas["petstore"]["pet"].pop(mascot-1)
        print("***** LA MASCOTA HA SIDO ELIMINADA *****")
    with open("./PetShopping.json",'w') as archivo:
        json.dump(mascotas, archivo,)


       
verMenu()


opc = int(input())

while opc != 0:
    if opc == 1:
        listarMascotas()
    elif opc == 2:
        crearMascota()
    elif opc == 3:
        mostarPorTipo()
    elif opc == 4:
        actulizarMascota()
    elif opc == 5:
        eliminarMascota()
    else:
        print("ingrese una opcion valida: ")
    verMenu()
    opc = int(input())