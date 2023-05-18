import json
from os import system


print("\n\n\n")

with open("./PetShopping.json", "r") as archivo:
    biblioteca = json.load(archivo)
    
#Menu principal
def menu_principal ():
            print('''
    **************** PetShopping ****************
    -----Ingrese la opcion que quiere realizar: -----
    1.Mostrar mascotas
    2.Añadir nueva mascota
    3.Mostrar datos de la mascota
    4.Editar datos de la mascota
    5.Eliminar mascota
    0.Salir
    ''')
    
#Listar mascotas con Tipo, Raza, Precio y Servicios
def mostar_mascotas (biblioteca):
    contador = 0
    print('ID',"\t\t",'TIPO',"\t\t",'RAZA',"\t\t\t",'PRECIO',"\t\t\t\t",'SERVICIOS')
    for i in biblioteca["petstore"]["pet"]:
        print(contador, "\t\t", i["tipo"],"\t\t", i["raza"],"\t\t\t", i["precio"],"\t\t\t", i["servicios"])
        contador += 1
        
#Crear Nueva mascota
        
def crear_nueva_mascota (biblioteca):
    tipo = input("Ingrese el tipo de mascota: ")
    raza = input("Ingrese la raza de la mascota: ")
    precio = input("Ingrese el precio de la mascota: ")
    numero_servicios = input("¿Va a ingresar mas de un servicio? S/N \n")
    if numero_servicios == "s" or numero_servicios == "S":
        cantidad_servi = int(input("Cuantos servicios va a ingresar: \n"))
        lista = []
        for i in range(cantidad_servi):
            servicios = input("Ingrese los servicios de la mascota: ")
            lista.append(servicios)
        biblioteca["petstore"]["pet"].append({"tipo" : tipo, "raza" : raza,"precio" : precio,"servicios" : lista})
    else: 
        servicio = input("Ingrese el servicio la mascota: ")
        biblioteca["petstore"]["pet"].append({"tipo" : tipo, "raza" : raza,"precio" : precio,"servicios" : servicio})
    with open("./PetShopping.json", "w") as archivo:
        json.dump(biblioteca, archivo)
    print('********* La mascota fue agregada con exito *********')    

#Mostrar por tipo


def mostrarTIPO_mascota (biblioteca):
    mostar_mascotas(biblioteca)
    with open("./PetShopping.json", "r") as archivo:
        tipo=json.load(archivo)
        agenda=tipo["petstore"]["pet"]

        p=input("Ingrese el tipo de mascota que desea buscar: ")
        for i in agenda:
            if i in agenda:
                if i["tipo"]==p:
                    print([i])

#Funcion para editar

def actualizar_mascota (biblioteca):
    mostar_mascotas(biblioteca)
    id = int(input("Ingrese el id de la mascota a actualizar: "))
    opc_edit = int(input('''Que datos quiere editar:
    1.Tipo de mascota
    2.Raza
    3.Precio
    4.Servicios\n'''))
    if opc_edit ==1: 
        tipo = input("Ingrese el tipo de mascota: ")
        biblioteca["petstore"]["pet"][id]["tipo"] = tipo
        print('********* Tipo de mascota se agregó correctamente *********')
    elif opc_edit ==2:
        raza = input("Ingrese la raza de la mascota: ")
        biblioteca["petstore"]["pet"][id]["raza"] = raza
        print('********* La raza de la mascota se agregó correctamente *********')
    elif opc_edit==3:
        precio = input("Ingrese el precio de la mascota: ")
        biblioteca["petstore"]["pet"][id]["precio"] = precio
        print('********* El precio de la mascota se agregó correctamente *********')
    elif opc_edit == 4:
        numero_servicios = input("¿Va a ingresar mas de un servicio? S/N \n")
        if numero_servicios == "s" or numero_servicios == "S":
            cantidad_servi = int(input("Cuantos servicios va a ingresar: \n"))
            lista_servicios = []
            for i in range(cantidad_servi):
                servicios = input("Ingrese los servicios a cambiar: ")
                lista_servicios.append(servicios)
            biblioteca["petstore"]["pet"][id]["servicios"] = lista_servicios
            print('********* Los servicios de la mascota se agregaron correctamente *********')
        else:
            servicio = input("Ingrese los servicios a cambiar: ")
            biblioteca["petstore"]["pet"][id]["servicios"] = servicio
            print('********* El servicio de la mascota se agregó correctamente *********')
    else:
        print('********* INGRESE UNA OPCION VALIDA *********')        
    with open("./PetShopping.json", "w") as archivo:
        json.dump(biblioteca, archivo)
    
#Funcion para eliminar
    
def eliminar_mascota (biblioteca):
    mostar_mascotas(biblioteca)
    id = int(input("Ingrese el id de la mascota a eliminar: "))
    biblioteca["petstore"]["pet"].pop(id)
    print("********* La mascota fue agregada con exito *********")
    with open("./PetShopping.json", "w") as archivo:
        json.dump(biblioteca, archivo)
    
opcion_men = True 

while opcion_men:

    menu_principal()
    opcion = int(input())
    if opcion == 1:
        mostar_mascotas(biblioteca)
    elif opcion == 2:
        crear_nueva_mascota(biblioteca)
    elif opcion == 3:
        mostrarTIPO_mascota(biblioteca)
    elif opcion == 4:
        actualizar_mascota(biblioteca)
    elif opcion == 5:
        eliminar_mascota(biblioteca)
    else:
        opcion_men =False
        print("***** Fin del programa *****")