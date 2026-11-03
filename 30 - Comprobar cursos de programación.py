cursos=["Java","Python","Typescript","C","Dart"]
#Preguntar al usuario que lenguaje quiere aprender, y el programa
#le indicará si existe un curso para ese lenguaje o no.

#print(cursos)
continuar="S"

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
encontrado=False
for n in cursos:
    if n==lenguaje:
        encontrado=True
        break
if not econtrado:
    print(f"No existe un curso para {lenguaje}")
    