# Elabore un programa Python para gestionar el CRUD del archivo de datos Biblioteca.json con las siguientes funcionalidades:

# Mostrar en pantalla todos los libros
# Crear Nuevo libro con la posibilidad de múltiples autores por Libro
# Mostrar los datos de un libro consultado por título
# Actualizar los datos de un libro consultado por título
# Eliminar un Libro de la biblioteca

print("\n\n")
import json

def menu ():
    print(" ******** MENU BIBLIOTECA *******\n")
    print(" 1).Mostrar todos los libros \n 2).Crear Nuevo libro con la posibilidad de múltiples autores por Libro \n 3).Mostrar los datos de un libro consultado por título \n 4).Actualizar los datos de un libro consultado por título \n 5).Eliminar un Libro de la biblioteca \n 0).salir")

# LISTAR LIBROS (1)
def mostrarLibros():
    print("********* LISTADO DE LIBROS *********\n")
    # print("title\t\t\tauthor\t\t\tyear\t\t\tprice\t\t\tcategory")
    with open("./Biblioteca.json" ,"r") as archivo :
        libros = json.load(archivo)
    for libro in libros["bookstore"]["book"]:
        print(" \nlang: ",libro["title"]["_lang"],"\n","text: ",libro["title"]["__text"],"\n","author: ",libro["author"],"\n","year: ",libro["year"],"\n","price: ",libro["price"],"\n","category: ",libro["_category"])
    archivo.close()    
# CREAR LIBROS (2)
def crearLibros():
   with open("./Biblioteca.json" ,"r") as archivo :
        libros = json.load(archivo)
        idioma = input("ingrese el idioma del libro: ")
        titulo = input("ingrese el titulo del libro: ")
        autor = input("ingrese el autror: ")
        año = int(input("ingrese el año del libro: "))
        precio = int(input("ingrese el precio del libro: "))
        categoria = input("ingrese la categoria del libro: ")
        libros["bookstore"]["book"].append({"title":{"_lang":idioma,"__text":titulo}, "author": autor, "year" : año, "price":precio, "_category":categoria})
        with open ("./Biblioteca.json" ,"w") as archivo:
           json.dump(libros,archivo)
# CONSULTAR TITULO(3)
def consultaTitulo():
    with open ("./Biblioteca.json","r") as archivo:
        libros = json.load(archivo)
    titulo = input("ingrese el titulo del libro: ")
    print("LENGUAJE\t\t\ttitulo\t\t\tAUTOR\t\t\tAÑO\t\t\tPRECIO\t\t\tcategoria")
    for libro in libros["bookstore"]["book"]:
         if libro ["title"]["__text"] == titulo:
            print(" \nlang: ",libro["title"]["_lang"],"\n","text: ",libro["title"]["__text"],"\n","author: ",libro["author"],"\n","year: ",libro["year"],"\n","price: ",libro["price"],"\n","category: ",libro["_category"])
    archivo.close()
        
# ACTUALIZAR LIBRO(4)    
def actualizarLibro(libro):
    with open("./Biblioteca.json"'r') as archivo:
        biblioteca = json.load(archivo)
    for libro in biblioteca['bookstore']['book']:
        if libro['title']['__text'] == titulo:mostrarLibros()
        print("¿QUE DATO DESEAS ACTUALIZAR?\n")
        print("1. AUTOR")
        print("2. AÑO")
        print("3. PRECIO")
        print("4. CATEGORIA")
        opcion = input()
        if opcion == "1":
            autor = input("INGRESA EL NUEVO NOMBRE DE AUTOR\n")
            libro['author'] = autor
        elif opcion == "2":
            year = input("INGRESE EL NUEVO AÑO\n")
            libro['year'] = year
        elif opcion == "3":
            price = input("INGRESE EL NUEVO PRECIO\n")
            libro['price'] = price
        elif opcion == "4":
            categoria = input("INGRESE LA NUEVA CATEGORIA\n")
            libro['_category'] = categoria
        else:
            print("Opción inválida\n")
            return
        
            print(f"Los datos del libro {titulo} se han actualizado correctamente\n")
            break
    else:
        print(f"No se encontró un libro con el título {titulo}")
        
    with open("./Biblioteca.json" 'w') as archivo:
        json.dump(biblioteca, archivo,)
# ELIMINAR LIBRO(5)
def eliminarLibro():
    with open('./Biblioteca.json', 'r') as archivo:
         biblioteca = json.load(archivo)
    titulo = input("Ingrese el titulo del libro que quiere eliminar: ")
    for libro in biblioteca['bookstore']['book']:mostrarLibros()
    if libro["title"]["__text"] == titulo:
        biblioteca["bookstore"]["book"].remove(libro)
        print("el libro",titulo, "ha sido eleiminado correctamente")       
    else:
        print("no se encontro un libro con el titulo",titulo)
    with open ("Biblioteca.json","w") as archivo:
        json.dump(biblioteca,archivo)

menu()


opc = int(input())

while opc != 0:
    if opc == 1:
        mostrarLibros()
    elif opc == 2:
        crearLibros()
    elif opc == 3:
        consultaTitulo()
    elif opc == 4:
       actualizarLibro()  
    elif opc == 5:
        eliminarLibro()
    else:
        print("ingrese una opcion valida: ")
    menu()
    opc = int(input())