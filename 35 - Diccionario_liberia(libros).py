"""
Realiza un progrma para la organizacion de una libreria
un libro tiene tres propiedades: titulo, autor y precio.

Cuando se inicie el programa, se va a mostrar un menu:
1-Nuevo libro
2-Mostrar todos
3-Buscar por titulo
4-Libros por precio maximo
5-Salir

1-Se piden los datos del nuevo libro y se guardan (OJO: no se pueden repetir titulos)
2-Se muestran los titulos de todos los libros
3-Se le pide el titulo y se muestran todos sus datos
4-Se le pide el precio maximo y se muestran los titulos de los libros cuyo precio sea igual o 
inferior al introducido.
Despues de ejecutar cualquiera de las anteriores opciones, se muestra de nuevo el menu.
Asi hasta que elija la opcion 5 que sale del programa
""" 

# ***** Declaración de función para COMPROBAR si el libro ya existe en la lista de libros *****
def comprobar_libro(titulo):
    return titulo in [libro["titulo"] for libro in lista_libros]
# **********************************************************************
# **********************************************************************

opcion=1
lista_libros=[]

while opcion != 5:
    try:
        print("=====================================")
        print("          MENÚ DE LIBROS             ")
        print("=====================================")
        print("1.- Añadir libro")
        print("2.- Mostrar todos los libros")
        print("3.- Buscar por titulo")
        print("4.- Libros por precio maximo")
        print("5.- Salir")
        print("=====================================")
        opcion=int(input("Elije opción (1 - 5); "))
        match opcion:
            case 1:
                titulo=input("Introduce el titulo del libro: ")
                autor=input("Introduce el autor del libro: ")
                precio=float(input("Introduce el precio del libro: "))
                libro={"titulo": titulo, "autor": autor, "precio": precio}
                if not comprobar_libro(titulo):
                    lista_libros.append(libro)
                else:
                    print("El libro ya existe en la librería.") 
            case 2:
                for libro in lista_libros:
                    print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Precio: {libro['precio']}")
            case 3:
                titulo_buscar=input("Introduce el titulo del libro a buscar: ")
                for libro in lista_libros:
                    if libro["titulo"] == titulo_buscar:
                        print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Precio: {libro['precio']}")
                        break
                else:
                    print("El libro no se encuentra en la librería.")
            case 4:
                precio_maximo=float(input("Introduce el precio máximo: "))
                for libro in lista_libros:
                    if libro["precio"] <= precio_maximo:
                        print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Precio: {libro['precio']}")
            case 5:
                print("FIN del PROGRAMA")
                salir=True
                exit               
            case _:
                print("Opción no válido")
    except ValueError:
        print("No es un valor numérico, vuelve a intentar")  