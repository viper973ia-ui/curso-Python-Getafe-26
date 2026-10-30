lista=[4,1,8,2,11]
#muestra cada número de la lista
#print(lista[0])
#print(lista[1])

#muestra los números pares de la lista

print ("Imprime los datos de la lista que son PARES")
for num in lista:
    if num%2==0:
        print (num)

#sustituye cada elemento de la lista por su cuadrado
#y luego  imprimes la lista entera y la suma de todo
#su contenido

indice=0
suma=0
calculo=0

print ("Imprime la lista inicial")
print (lista)

for num in lista:
    
    lista[indice]=num*num  #también valdría esta forma lista[indice]=num**2
    indice=indice+1
print ("Imprime la lista de los cuadrados de la lista inicial")
print (lista)
indice=0
for num in lista:
    suma=suma+num
print (f"La suma de todos los elementos es {suma} ")

#Solución altenativa a lo anterior
for indice,num in enumerate(lista):  #enumerate: es UNA FUNCION para recorrer el indice y el valor (indice , num)
    lista[indice]=num**2
print(lista)
suma=0
for num in lista:
    suma=suma+num
print(f"La suma de todos la lista {lista} es {suma} ")