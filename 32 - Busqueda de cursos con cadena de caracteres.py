cursos="Java basico,Python principiantes,C,Java avanzado,Java enterprise,python web,cobol"

#Solicitamos al usuario que introduzca un lenguaje y le mostramos
#todos los cursos relacionados con ese lenguaje.

lista_cursos=cursos.split(",")                   # Aquí se hace una lista de cursos (frases) a partir 
                                                 # de la cadena de texto, separando por comas.
lenguaje = input("¿Qué lenguaje quieres aprender? ")

for c in lista_cursos:
    if lenguaje.lower() in c.lower().split(" "):  # c.lower().split(" ") devuelve una lista 
                                                  # de palabras en el curso, y luego se verifica 
                                                  # si el lenguaje está en esa lista 
        print(c)


# ************** Cuando la lista son números **************        
lst=range(1,10)
print(lst)
