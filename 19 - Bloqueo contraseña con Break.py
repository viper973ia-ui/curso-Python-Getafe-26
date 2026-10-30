password="admin"
intentos=3
acierto=False
while intentos>0:
# intentos>0 and not acertado:   #-- Es lo mismo que la línea anterior
    registro=input("Introduce la contraseña para acceder:")
    if registro==password:
        print("Usuario válido!")
        acierto=True
        break
        #acertado=True
    else:
        intentos=intentos-1
        print(f"Vuelve a intentar! tienes {intentos} intentos antes del bloqueo")
    
    if not acierto:
        print("Ususario no válido!")
 
