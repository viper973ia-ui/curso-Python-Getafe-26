numeros=[4,3,7,8,7,9,2]
#dada esa lista de notas, crea otra lista
#que contenga solo los aprobados. Además, le 
#añadirás un punto extra a cada uno
#finalmente se imprime la lista
#[8,9,8,10]
"""
aprobados=[]
for nota in numeros:
    if nota>=5:
        aprobados.append(nota+1)
"""
#compresión de listas
#función que haga la tarea indicada arriba, pero 
#devolviendo el resultado como una tupla
def obtener_aprobados():
    return tuple([nota+1 for nota in numeros if nota>=5])


print(obtener_aprobados())