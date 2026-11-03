#lista de reproducción
lista_reproduccion=[
    {"titulo":"canción inventada","duracion":3.20,"valoracion":4},
    {"titulo":"Bohemian Rapsody","duracion":5.40,"valoracion":10},
    {"titulo":"Green summer","duracion":4.10,"valoracion":7}
]
#Se solicita la introducción de los datos de una nueva canción.
#Si la canción no existe, se agrega a la lista. Si ya existe no se hace nada
#y se agrega a la lista
#Después, el programa muestra todos los titulos almacenados
#y la valoración media de toda la lista de reproducción 


# ****** Definimos una función para buscar si la canción ya existe en la lista de reproducción ******
def buscar_cancion(titulo):
    for cancion in lista_reproduccion:
        if cancion["titulo"].lower() == titulo.lower():
            return True
    return False     # si llega aquí es porque no ha encontrado la canción.
# ***************************************************************************************************

# Otra función CON SIMPLICACIÓN de LISTAS ***********************

def comprobar_cancion(titulo):
    return titulo in [can["titulo"] for can in lista_reproduccion]

# **********************************************************************
#              Tener en cuenta la simplicidad en una línea (OJO con la lectura del código)
# **********************************************************************

contador=0
suma=0

cancion_nueva=input("Introduce titulo de la canción: ")
duracion_cancion_nueva=float(input("Introduce duración de la canción: "))
valoración_cancion_nueva=int(input("Introduce valoración de la canción: "))

control_cancion_nueva=buscar_cancion(cancion_nueva)

#print(control_cancion_nueva)         **** Es un Control para ver que valor tiene la variable control
                                      #  control_cancion_nueva, que es True si la canción ya existe 
                                   

if not control_cancion_nueva:
    nuevo_diccionario={"titulo":cancion_nueva,"duracion":duracion_cancion_nueva,"valoracion":valoración_cancion_nueva}
    lista_reproduccion.append(nuevo_diccionario)
    
    print(f"La canción {cancion_nueva} ha sido añadida a la lista de reproducción.")
else:
    print(f"La canción {cancion_nueva} ya existe en la lista de reproducción.")


"""
for k in lista_reproduccion:    # Recorremos la lista de reproducción, 
                                # que contiene diccionarios, y mostramos el título de cada canción. 
                                # Además, vamos sumando las valoraciones para calcular la media al 
                                # final. 
  
    print(f"Título: {k['titulo']}")
    suma += k['valoracion']
    contador += 1

if contador > 0:
    media = suma / contador
    print(f"Valoración media: {media:.2f}")
"""    

    
#  **** SIMPLIFICANDO dentro del FOR ****


for k in lista_reproduccion:
    suma+=k['valoracion']
    print(k["titulo"])
print(f"Valoración media: {suma/len(lista_reproduccion)}")

