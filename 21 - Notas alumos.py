notas_alumnos=[6.4,2.9,5.5,8.0,3.1,7.2]
#indica cuantos alumnos han aprobado

aprobados=0

for n in notas_alumnos:
    if n>=5:
        aprobados=aprobados+1
print ("El total de aprobados es ", aprobados)

#Dime la nota más alta

NotaMAX=0
NotaMAYOR=notas_alumnos[0]   #inicializamos la variable con cualquiera de 
#las notas de la lista (en este caso es el índice 0)

for n in notas_alumnos:
    if n>NotaMAX:
        NotaMAX=n
print(f"La Nota Máxima es ",NotaMAX)

print(f"La nota Más Alta es {max(notas_alumnos)}")
print(f"La nota Más Baja es {min(notas_alumnos)}")

print(f"La notas en orden son : {sorted(notas_alumnos)}")
print(f"La notas en orden son : {sorted(notas_alumnos,reverse=True)}")

    