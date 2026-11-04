
##   ****** FUNCIONES ESPECIALES: ********
##   *************************************

import functools as ft


numeros=[1,8,3,-4,9,-2,-11,16]
positivos=list(filter(lambda n:n>0,numeros))  #devuelve una lista con los elementos 
                                              #que cumplen la condición
print(f"Los números positivos por filter (lambda) son: {positivos}")

#por comprensión de listas
positivos=[n for n in numeros if n>0]
print(f"Los números positivos por lista de comprensión son: {positivos}")

# Calcula la suma de los cuadrados de todos los positivos de la lista

print(ft.reduce(lambda a, b: a + b, map(lambda n: n**2, positivos)))  #devuelve
                                                                      #un objeto map

