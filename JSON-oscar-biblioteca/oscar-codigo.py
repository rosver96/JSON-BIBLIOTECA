import json
'''Elabore un programa Python para gestionar el CRUD del archivo de datos Biblioteca.json con las siguientes funcionalidades:

Mostrar en pantalla todos los libros
Crear Nuevo libro con la posibilidad de múltiples autores por Libro
Mostrar los datos de un libro consultado por título
Actualizar los datos de un libro consultado por título
Eliminar un Libro de la biblioteca'''


opcion_men = True


#Funcion para tener el .json en una variable o definicion
def obteber_infjson(archivo):
    with open(archivo,"r") as file:
        libros = json.load(file)
    return libros

#Funcion para guardar 
def guardar_libros(libros, archivo):
    with open(archivo, 'w') as f:
        json.dump(libros, f)

libreria = "./biblioteca_.json"
#Contiene la informacion de la funcion obtener_infjson()
g_biblioteca = obteber_infjson(libreria)


def menu():
    opcion = int(input('''
    Ingrese la opcion que quiere realizar:
    1.Mostrar todos los libros
    2.Agregar un nuevo libro
    3.Mostrar los datos de un libro
    4.Editar los datos de un libro
    5.Eliminar un libro
    0.Salir
    '''))
    return opcion

 

def mostrar_libros(libros):
    print('*********** LIBROS DISPONIBLES ***********')
    with open("./biblioteca_.json","r") as archivo:
        libros = json.load(archivo)
        for libro in libros["bookstore"]["book"]:
            print(libro["title"]["__text"])
    archivo.close()

def agregar_libro():
    can_lib = int(input('Cuantos libros quiere agregar: '))
    for i in range(can_lib):
        idioma = input('Ingrese el idioma del libro: ')
        titulo = input('Ingrese el titulo del libro: ')
        año_c = input('Ingrese el año de creacion del libro: ')
        precio = input('Ingrese el precio del numero: ')
        categoria = input('Ingrese la categoria del libro: ')
        print('¿El libro que va a ingresar tiena mas de un autor? S/N')
        opcion_auts = input()
        if opcion_auts == 's' or opcion_auts == 'S':
            can_auts = int(input('Cuantos autores tiene el libro: '))
            lista_autores = []
            for i in range(can_auts):
                autor = input('Ingrese el nombre del autor: ')
                lista_autores.append(autor)
            g_biblioteca["bookstore"]["book"].append({
            "title":{
                    "_lang": idioma,
                    "__text": titulo
                },
            "author": lista_autores,
            "year": año_c,
            "price": precio,
            "_category": categoria
                })   
            
        else:
            autor = input('Ingrese el nombre del autor: ')
            g_biblioteca["bookstore"]["book"].append({
                    "title":{
                        "_lang": idioma,
                        "__text": titulo
                    },
                    "author": autor,
                    "year": año_c,
                    "price": precio,
                    "_category": categoria
                })
        with open("biblioteca_.json", 'w') as archivo:
            json.dump(g_biblioteca, archivo)

def mostrar_por_titulo(libros):
    titulo = input('Ingrese el titulo del libro que quiere consultar: ')
    print('AUTOR(ES)\t\t\tPRECIO\t\t\tCATEGORIA')    
    for libro in libros["bookstore"]["book"]:
        if libro["title"]["__text"] == titulo:
            concatenador = ""
            if isinstance(libro["author"],list) == True:
                for i in libro["author"]:
                    concatenador += i + "\n"
                print(concatenador,"\t\t\t\t",libro["price"],"\t\t\t",libro["_category"],"\t\t")
            else:
                print(libro["author"],"\t\t\t",libro["price"],"\t\t\t",libro["_category"],"\t\t")   

def editar_libros(libros):
    mostrar_libros(libros)
    titulo_edit = input('Ingrese el titulo del libro que quiere editar: ')
    for libro in libros["bookstore"]["book"]:
        if libro["title"]["__text"] == titulo_edit:
            print('''Ingrese el dato que quiere seleccionar
                    1.Autor
                    2.Año de publicacion
                    3.Precio
                    4.Categoria''')
            opcion_edi = input()
            if opcion_edi == "1":
                opcion_auts =input('¿El libro que va a ingresar tiena mas de un autor? S/N')
                if opcion_auts == 's' or opcion_auts == 'S':
                    can_aut = int(input('Cuantos autores tiene el libro: '))
                    lista_autores = []
                    for i in range(can_aut):
                        autor = input('Ingrese el nombre del autor: ')
                        lista_autores.append(autor)
                    libro["author"] = lista_autores
                else:
                    autor = input('Ingrese el nombre del autor: ')
                    libro["author"] = autor
            elif opcion_edi =="2":
                año_publi = input('Ingrese el año de publicacion: ')
                libro["year"] = año_publi
            elif opcion_edi =="3":
                precio = input('Ingrese el precio del libro: ')
                libro["price"] = precio
            elif opcion_edi =="4":
                cate_lib = input('Ingrese la categoria del libro: ')
                libro["_category"] = cate_lib
            else:
                print('Seleccione una opcion valida')

def elminar_libro(libros):
    mostrar_libros(libros)
    titulo_elim = input('Ingrese el titulo del libro que quiere eliminar: ')
    for libro in libros["bookstore"]["book"]:
        if libro["title"]["__text"] == titulo_elim:
            libros["bookstore"]["book"].remove(libro)

    
while opcion_men:
    select = menu()
    if select == 1:
        mostrar_libros(g_biblioteca)
    elif select == 2:
        agregar_libro()
    elif select == 3:
        mostrar_por_titulo(g_biblioteca)
    elif select == 4:
        editar_libros(g_biblioteca)
    elif select ==5:
        elminar_libro(g_biblioteca)
    guardar_libros(g_biblioteca,libreria)
else:
    False

