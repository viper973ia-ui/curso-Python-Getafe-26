lista_libros = {}

while True:
    print(
        "\n====================================="
        "\n            MENÚ DE LIBROS           "
        "\n====================================="
        "\n1.- Añadir libro"
        "\n2.- Mostrar todos los libros"
        "\n3.- Buscar por título"
        "\n4.- Libros por precio máximo"
        "\n5.- Salir"
        "\n====================================="
    )

    try:
        opcion = int(input("Elige opción (1 - 5): "))
    except ValueError:
        continue

    if opcion == 1:
        titulo = input("Introduce el título del libro: ")
        if titulo in lista_libros:
            print("❌ El libro ya existe.")
        else:
            autor = input("Introduce el autor del libro: ")
            precio = float(input("Introduce el precio del libro: "))
            lista_libros[titulo] = {"autor": autor, "precio": precio}

    elif opcion == 2:
        for t in lista_libros:
            print(f"- {t}")

    elif opcion == 3:
        titulo = input("Introduce el título a buscar: ")
        if titulo in lista_libros:
            print(f"Datos: {lista_libros[titulo]}")
        else:
            print("❌ Libro no encontrado.")

    elif opcion == 4:
        max_p = float(input("Introduce el precio máximo: "))
        for t, datos in lista_libros.items():
            if datos["precio"] <= max_p:
                print(f"- {t} ({datos['precio']}€)")

    elif opcion == 5:
        print("Saliendo del programa...")
        break
