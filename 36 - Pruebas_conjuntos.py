
"""
dias={"lunes","martes","miércoles"}
dias.add("jueves")
dias.add("lunes")  
print(dias)  
"""
dia=input("dime un día de la semana: ")
dias={"lunes","martes","miércoles"}

if dia in dias:
    print("ese día ya existe")
else:
    dias.add(dia)
print(dias)

lista_dias=list(dias)

print(lista_dias)

lista_numeros=[4,7,11,3,2,11,9,4,7]

conjunto_numeros=set(lista_numeros)  # Localiza los elementos únicos del conjunto

print(conjunto_numeros)  # Muestra los elementos únicos del conjunto

lista_numeros_unicos=list(conjunto_numeros)  # Convierte el conjunto en una lista

print(lista_numeros_unicos)  # Muestra la lista de elementos únicos
