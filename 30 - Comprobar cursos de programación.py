cursos=["Java","Python","Typescript","C","Dart"]
#Preguntar al usuario que lenguaje quiere aprender, y el programa
#le indicará si existe un curso para ese lenguaje o no.

#print(cursos)
continuar="S"

# Es el más corto **** Nota.- TAMBIÉN VALE PARA "TUPLAS" ***

lenguaje = input("¿Qué lenguaje quieres aprender? ")

if lenguaje in cursos:
    print(f"Sí existe un curso para {lenguaje}")
else:
    print(f"No existe un curso para {lenguaje}")

# Este es el recurrente, que se repite hasta que el usuario decida salir

while continuar=="S" or continuar=="s":
    lenguaje = input("¿Qué lenguaje quieres aprender? ")

    if lenguaje in cursos:
        print(f"Sí existe un curso para {lenguaje}")
    else:
        print(f"No existe un curso para {lenguaje}")

    continuar = input("¿Quieres buscar otro lenguaje? (S/N): ")
    if continuar != "S" and continuar != "s":
        print("Fin del programa")
    else:
        continuar="S"

## Según el profesor;

lenguaje = input("¿Qué lenguaje quieres aprender? ")
lenguaje.lower() # Para minúsculas
lenguaje.upper() # Para mayúsculas
encontrado=False
for n in cursos:
    if n==lenguaje:
        encontrado=True
        break
if not encontrado:
    print(f"No existe un curso para {lenguaje}")
    

# Otra forma 

cursos=["Java","Python","Typescript","C","Dart"]
#Pregunta al usuario que lenguaje quiere aprender, y el programa
#le indicará si existe un curso para ese lenguaje o no
lenguaje=input("¿Qué lenguaje quieres aprender?")

"""
encontrado=False
for c in cursos:
    if c.lower()==lenguaje.lower():
        print("Tengo ese curso!")
        encontrado=True
        break
if not encontrado:
    print("Lo siento, no tengo ese curso")
"""
if lenguaje.lower() in [c.lower() for c in cursos]:
   print("Tengo ese curso!")
else:
   print("Lo siento, no tengo ese curso") 