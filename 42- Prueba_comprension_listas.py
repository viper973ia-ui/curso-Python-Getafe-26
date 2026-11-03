numeros=[3,-1,-9,4,2,11,-8,7-5]

# Crea una lista a partir de la anterior que contenga
# solo los positivos

positivos=[]

for n in numeros:
    if n>0:
        positivos.append(n)
        
print(positivos)
# **************************************************************
# **************************************************************
print()
print()
print("********** Otra forma de hacerlo - COMPRENSIÓN DE LISTAS **********")

positivos_comprension=[n for n in numeros if n>0]

print(f"Positivos (compositivos_comprension): {positivos_comprension}")

print()
print("*********** fin de la comprensión de listas ***********")

# **************************************************************
# **************************************************************

# **************************************************************
# indica si hay algún número par en la lista
# **************************************************************

if [n for n in numeros if n%2==0]:
    print("Hay algún número par en la lista")
else:
    print("No hay ningún número par en la lista")