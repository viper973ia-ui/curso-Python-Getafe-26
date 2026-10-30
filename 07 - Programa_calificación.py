#lee la nota de un alumno y dependiendo del número (0-10)
#le indica si es suspenso (menos de 5), aprobado (5 o 6),
#notable (7 o 8) o sobresaliente (9 o 10)
#El simbolo | es con la combinación de teclas de Alt Gr + 1
nota=int(input("Introduce la nota del alumno (de 0 a 10); "))
match nota:
    case 0|1|2|3|4:
        print("Suspenso")
    case 5|6:
        print ("Aprobado")
    case 7|8:
        print ("Notable")
    case 9|10:
        print ("Sobresaliente")
    case _:
        print ("Nota no váliuda")