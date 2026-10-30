#Teniendo en cuenta que alevín es 10 años y benjamín es 16.
#Hacer un programa que solicite la edad y nos muestre a que grupo
#pertence (el más cercano a su edad). La edad debe estar
#entre 9 y 18 años.
limite_inf,limite_sup,benjamin,alevin=9,18,10,16
edad=int(input("Introduce la edad; "))
if edad<limite_inf or edad>limite_sup:
    print ("La edad no es válida")
else:
    distancia_benjamin=edad-benjamin
    distancia_alevin=alevin-edad
    if distancia_benjamin>distancia_alevin:
        print ("Eres benjamín")
    else:
        print ("Eres alevín")