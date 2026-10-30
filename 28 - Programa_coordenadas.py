#Solicitar al usuario la introducción de unas coordenadas (x,y),
#cada pareja de coordenadas se guarda en una lista,
#Cada vez que solicitamos coordenadas
#preguntamos  si quiere introducir nuevas coordenadas
#En caso afirmativo, se solicita de nuevo
#si responde que no finaliza el programa mostrando la lista
#de coordenadas

import math

coordenadas=[]
resp="S"
controldistancia=10000000


while resp=="S" or resp=="s":
    x=int(input("(x: ); "))
    y=int(input("( :y); "))
    
    coordenadas.append((x,y))
    resp=input("¿Quieres introducir nuevas coordenadas (S/N)? ")
print (coordenadas)

## **** OJO estamos registrando tuplas dentro de una lista
# *************************************************************

#Se pide al usuario su posición, después el programa
#le mostrará las coordenadas del punto
#más cercano a su posición

x2=int(input("Posición X de tu ubicación (x: ); "))
y2=int(input("Posición Y de tu ubicación ( :y)"))

for n in coordenadas:
    distancia=math.hypot(n[0]-x2,n[1]-y2)
    if distancia<controldistancia:
        controldistancia=distancia
        puntocercano=n

print (f"El punto más cercano a tu ubicación es {puntocercano} y la distancia es de {controldistancia}")

## *********************************************************************************
## **** OJO otra forma de llamar a la biblioteca math pero solo la función hypot es: *****
##    from math import hypot
## ** de esta forma no es necesario poner math.hypot, sino solo hypot
## **********************************************************************************

# Utilizando la definición de una función,

#def distancia(punto1,punto2):
#    return math.hypot(punto1[0]-punto2[0],punto1[1]-punto2[1])
