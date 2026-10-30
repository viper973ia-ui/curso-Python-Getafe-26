#solicitar la introducción de numeros, uno a uno
#y los guardamos en una lista. Después de pedir un número,
#pregunta si quiere introducir otro, si dice si(S), pide uno nuevo
# y así sucesivamente hasta que diga que no(n).
#al final, muestra la lista completa
resp="s"
lista=[]
while resp=="s" or resp=="S":
    try:
        num=int(input("Escribe un número "))
        lista.append(num)
        resp=input("¿Desea introducir otro número(s/n)? ")
    except ValueError:
        print("No es un valor numérico, vuelve a intentar")
    except EOFError:
        print("Error de lectura")
        break    
print(f"La lista es: {lista}")   