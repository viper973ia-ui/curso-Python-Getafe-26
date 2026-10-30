#Al iniciar el programa se debe mostrar el siguiente menu:
#1.- Añadir notas
#2.- Mostrar notas extremas
#3.- Total de aprobados
#4.- Nota media
#5.- Mostrar todas
#6.- Salir


#El usuario elije una opción (1 al 6) y el programa le muestra o le pide
#los datos necesarios para llevar a cabo la acción. Después,
#vuelve a salir el menú y así hasta que elija la opción de salir.

lista=[]
contador=0
indice=0
salir=False
opcion=1
notas=0


while opcion != 6:
    try:
        print("=====================================")
        print("          MENÚ DE NOTAS              ")
        print("=====================================")
        print("1.- Añadir notas")
        print("2.- Mostrar notas extremas")
        print("3.- Total de aprobados")
        print("4.- Nota media")
        print("5.- Mostrar todas")
        print("6.- Salir")
        opcion=int(input("Elije opción (1 - 6); "))
        match opcion:
            case 1:
                num=int(input("Escribe una nota a la lista; "))
                lista.append(num)
            case 2:
                print(f"La nota Más Alta es {max(lista)}")
                print(f"La nota Más Baja es {min(lista)}")  
            case 3:
                aprobados=0
                for n in lista:
                    if n>=5:
                        aprobados+=1
                print (f"El total de aprobados es de {aprobados}")
            case 4:
                for n in lista:
                    notas=notas+n
                if (len(lista)==0):
                    print("No hay notas para calcular la media")
                else:
                    print (f"La nota media es de {notas/len(lista)}")
            case 5:
                print(lista)
            case 6:
                print("fin del programa")
                salir=True
                exit
            case _:
                print("Opción no válido")
    except ValueError:
        print("No es un valor numérico, vuelve a intentar")   
