#Hacer un programa que muestre la suma de los 10 primeros
#números naturales (del 1 al 10)
suma=0
for num in range(1,11):
    suma=suma+num
print (f"La suma de los 10 primeros números naturales son: {suma}")

#Hacer un programa de todos los números entre 1 y un número leido por teclado
suma2=0
num_max=int(input("Introduce un número: "))
for num1 in range(1,num_max+1):
    suma2=suma2+num1
print (f"La suma de los números es: {suma2}")
