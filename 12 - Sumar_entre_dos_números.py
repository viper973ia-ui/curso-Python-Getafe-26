#Solicita la introducción de dos números y calcula suma de todos los números
#comprendidos entre le menor y el mayor (inlucyendo ambos)
suma=0
num_1=int(input("Introduce el primer número: "))
num_2=int(input("Introduce el segundo número: "))
if num_1<num_2:
    limite_inferior,limite_superior=num_1,num_2  # es una forma de declarar variables en una sola línea
else:
    limite_inferior=num_2
    limite_superior=num_1
for c in range(limite_inferior,limite_superior+1):
    suma=suma+c
print(f"La suma de los números comprendidos entre {limite_inferior} y {limite_superior} es {suma}")

#***************************************************************************
#solución 2
"""
if num_1<num_2:
    for c in range(num_1,num_2+1)
        suma=suma+c
    print(f"La suma de los números comprendidos entre {limite_inferior} y {limite_superior} es {suma}")
else:
    for c in range(num_2,num_1+1)
            suma=suma+c
        print(f"La suma de los números comprendidos entre {limite_inferior} y {limite_superior} es {suma}")
"""
#*****************************************************************************
#solucion 3
"""
if num_1>num_2:
    num_1,num2=num_2,num_1
    for c in range(num_1,num2+1)
        suma=suma+c
    print(f"La suma de los números comprendidos entre {limite_inferior} y {limite_superior} es {suma}")
"""


    
