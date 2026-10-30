#Solcita la introducción de una contraseña, si es correcta
#le dice que es un susario válido. Si no es correcta, se le vuelve a pedir.
#Así, hasta tres intentos. Si después del tercer intento la contraseña es incorrecta y
#le dice que no es un usuario válido

contrasena="MiContrasena"
intentos=1

while intentos<=3:
    registro=input("Introduce la contraseña para acceder:")
    if registro!=contrasena:
        intentos=intentos+1
        if intentos==4:
            print (f"Usuario no válido")  
    else:
        intentos=4
        print (f"Ususario válido")

#otra forma de resolverlo
#***********************************************************************

#password="admin"
#intentos=3
#acertado=False
#intento=1
#while intentos>0 and acertado==False:
#while intentos>0 and not acertado:   #-- Es lo mismo que la línea anterior
    #registro=input("Introduce la contraseña para acceder:")
    #if registro==password:
        #acertado=True
    #else:
        #print(f"Vuelve a intentar!")
        #intentos=intentos-1
    #if acertado==True:
    #if acertado    #---significa lo mismo que la línea anterior (OJO y tenerlo en cuenta)
        #print("Usuario válido!")
    #else:
        #print("Ususario no válido!")
 
