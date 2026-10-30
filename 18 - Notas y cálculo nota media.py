#Solicita una nota, despues otra, y así sucesivamente hasta introducir un cero
#en ese momento, no pedirá más notas y mostrará la nota media de las introduccidas
#hasta el momento

notas=1
notaacumulada=0
contador=0

while notas != 0:
    notas=int(input("Introduce una nota (entre 1 y 10) - Teclea 0 para salir; "))
    if notas != 0:
        notaacumulada=notaacumulada+notas
        contador=contador+1
    elif notas==0 and contador==0:
            print(f"No hay notas")
        
    else:
        notamedia=notaacumulada/contador
        print(f"La nota media de los {contador} examenes es {notamedia}")