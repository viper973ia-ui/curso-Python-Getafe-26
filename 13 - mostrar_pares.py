#Realizar un programa que solicite la introducción de un número 
#después, muestra todos los pares entre 1 y ese número
número=int(input("Introduce un número: "))
for c in range(1,número+1):
    if c%2==0:
        print (c)
