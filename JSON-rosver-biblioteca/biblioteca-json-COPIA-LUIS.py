import json # importamos json

direccion = "Biblioteca.json" 

def get_json_data(archivos):
    with open(archivos,"r") as file:
        diccionario = json.load(file)
    return diccionario

def save_json_data(diccionario, archivos):
    with open(archivos, "w") as f:
        json.dump(diccionario, f)

dicBiblioteca = get_json_data(direccion)

def mostrarMenu():
    print("\n**************MENU******************")
    print("************************************")
    print("1.MOSTRAR LIBROS DE LA BIBLIOTECA")
    print("2.CREAR LIBRO EN LA BIBLIOTECA")
    print("3.MOSTRAR DATOS DE UN LIBRO POR TITULO")
    print("4.ACTUALIZAR DATOS DE UN LIBRO POR TITULO")
    print("5.ELIMINAR UN LIBRO DE LA BIBLIOTECA INGRESANDO EL TITULO")
    print("0.SALIR DEL MENU\n")
    
def mostrarBiblioteca(diccionario):
    print("TITULO\t\t\t\tAUTOR(ES)\n")
    for elemento in diccionario["bookstore"]["book"]:
        if isinstance(elemento["author"], list) == True:
            concatenador = ""
            for i in elemento["author"]:
                concatenador += i + " , "
            print(elemento["title"]["__text"],"\t\t",concatenador)
        else:
            print(elemento["title"]["__text"],"\t\t\t",elemento["author"])

            
def crearLibro():
    cantidad = int(input("Ingrese cuantos libros quiere agregar"))
    for i in range(cantidad):
        lenguaje = input("Ingrese el lenguaje del libro: ")
        titulo = input("Ingrese el titulo del libro: ")
        anho = input("Ingrese el año de publicacion: ")
        precio = input("Ingrese el precio del libro: ")
        categoria = input("Ingrese la categoria: ")
        print("¿El libro a ingresar tiene mas de un autor? S/N")
        opcion = input()
        if opcion == "S" or opcion == "s":
            cuantos = int(input("Cuantos autores quiere ingresar: "))
            lista_autores = []
            for i in range(cuantos):
                autor = input("Ingrese el autor: ")
                lista_autores.append(autor)
            dicBiblioteca["bookstore"]["book"].append({"title":{"_lang": lenguaje,"__text": titulo},"author": lista_autores,"year": anho,"price": precio, "_category": categoria})
        else:
            autor = input("Ingrese el autor")
            dicBiblioteca["bookstore"]["book"].append({"title":{ "_lang": lenguaje,"__text": titulo},"author": autor,"year": anho,"price": precio, "_category": categoria})

def mostrarDatosPorTitulo(diccionario):
    titulo = input("Ingrese el titulo del libro: ")
    print("AUTOR(ES)\t\t\t\tPRECIO\t\tCATEGORIA")
    for elemento in diccionario["bookstore"]["book"]:
        if elemento["title"]["__text"] == titulo:
            concatenador = ""
            if isinstance(elemento["author"],list) == True:
                for i in elemento["author"]:
                    concatenador += i + " , "
                print(concatenador,"\t\t\t\t",elemento["price"],"\t\t",elemento["_category"],"\t\t")
            else:
                print(elemento["author"],"\t\t\t",elemento["price"],"\t\t",elemento["_category"],"\t\t")

def editarLibros(diccionario):
    mostrarBiblioteca(diccionario)
    titulo = input("Ingrese el titulo del libro a editar: ")
    for elemento in diccionario["bookstore"]["book"]:
        if elemento["title"]["__text"] == titulo:
            print('''Seleccione el dato a editar
                 [1] AUTOR
                 [2] AÑO DE PUBLICACION
                 [3] PRECIO
                 [4] CATEGORIA''')
            opcion = input()
            if opcion == "1":
                print("¿El libro a editar tiene mas de un autor? S/N")
                opciond = input()
                if opciond == "S" or opciond == "s":
                    cuantos = int(input("Cuantos autores quiere ingresar: "))
                    lista_autores = []
                    for i in range(cuantos):
                        autor = input("Ingrese el autor: ")
                        lista_autores.append(autor)
                    elemento["author"] = lista_autores
                else:
                    autor = input("Ingrese el autor: ")
                    elemento["author"] = autor
            elif opcion == "2":
                año_publi = input("Ingrese el año de publicacion: ")
                elemento["year"] = año_publi
            elif opcion == "3":
                precio = input("Ingrese el nuevo precio: ")
                elemento["precio"] = precio
            elif opcion == "4":
                categoria = input("Ingrese la nueva categoria: ")
                elemento["_category"] = categoria
            else:
                print("Seleccione una opcion valida") 
            
def eliminarLibros(diccionario):
    mostrarBiblioteca(diccionario)
    titulo = input("Ingrese el titulo del libro a editar")
    for elemento in diccionario["bookstore"]["book"]:
        if elemento["title"]["__text"] == titulo:
            diccionario["bookstore"]["book"].remove(elemento)

mostrarMenu()
opcion = input()

while opcion != "0":
    if opcion == "1":
        mostrarBiblioteca(dicBiblioteca)
    elif opcion == "2":
        crearLibro()
    elif opcion == "3":
        mostrarDatosPorTitulo(dicBiblioteca)
    elif opcion == "4":
        editarLibros(dicBiblioteca)
    elif opcion == "5":
        eliminarLibros(dicBiblioteca)
    save_json_data(dicBiblioteca,direccion)
    mostrarMenu()
    opcion = input()