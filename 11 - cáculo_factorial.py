#Realizar un programa que solicite la introducción de un número y cálcule
#su factorial - Ejemplo 7! => 7*6*5*4*3*2*1
factorial=1
limite=int(input("Introduce un número entero:"))
for num in range(2,limite+1):
    factorial=factorial*num
    print (factorial)
print(f"El factorial del número {limite} es {factorial}")