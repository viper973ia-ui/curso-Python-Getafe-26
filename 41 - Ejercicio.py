#Solicitamos al usuario que introduzca un lenguaje y le mostramos
#todos los cursos relacionados con ese lenguaje.

# Lista de cursos proporcionada
cursos_str = "Java basico,Python principiantes,C,Java avanzado,Java enterprise,python web,cobol"

# Convertimos la cadena en una lista real separando por las comas
lista_cursos = [curso.strip() for curso in cursos_str.split(",")]

# Solicitamos al usuario el lenguaje que desea buscar
busqueda = input("Introduce el lenguaje de programación que buscas: ").strip()

# Filtramos los cursos que contienen la palabra buscada (ignorando mayúsculas/minúsculas)
cursos_encontrados = [curso for curso in lista_cursos if busqueda.lower() in curso.lower()]

# Mostramos los resultados al usuario
print(f"\nResultados para '{busqueda}':")
if cursos_encontrados:
    for curso in cursos_encontrados:
        print(f"- {curso}")
else:
    print("No se encontraron cursos relacionados con ese lenguaje.")
