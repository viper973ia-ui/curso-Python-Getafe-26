lista=[5,2,11,6,44,20,1]

lista_ordenada=sorted(lista)                   # la ordena de menor a mayor

print (lista)

print (lista_ordenada)                        

lista_ordenada2=sorted(lista,reverse=True)      # la ordena de mayor a menor

print (lista_ordenada2)     
 
nombres=["bicicleta","oro","casa","martillo"]
print(sorted(nombres))

#ordenación por números de carácteres

print(sorted(nombres,key=lambda e:len(e)))    # imprime de menor a Mayor


print(sorted(nombres,reverse=True,key=lambda e:len(e)))    # imprime de Mayor a menor
