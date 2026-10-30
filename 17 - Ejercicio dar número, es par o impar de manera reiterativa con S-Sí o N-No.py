""""
Desarrolla un programa en Python que permita al usuario introducir números enteros y determine si cada número introducido es par o impar.

El programa deberá funcionar de la siguiente manera:

Solicitar al usuario que introduzca un número entero.
Comprobar si el número introducido es par o impar.
Mostrar por pantalla el resultado.
Preguntar al usuario si desea introducir otro número:
Si responde S, el programa volverá a solicitar un nuevo número.
Si responde N, el programa finalizará.
El proceso deberá repetirse hasta que el usuario indique que no desea continuar.
"""

#*******************************************************************

continuar = "S"

while continuar == "S":
    
    # Pedimos un número al usuario

    numero = int(input("Introduce un número: "))

    # Comprobamos si el número es par o impar

    if numero % 2 == 0:
        # es par
        print(f"el número {numero} es PAR")
    else:
        # es impar
        print(f"el número {numero} es IMPAR")
    
    # Preguntamos si quiere introducir otro número
    
    continuar = input("¿Quieres introducir otro número? (S/N): ").upper()
    
    while continuar not in ("S", "N"):
        print("\033[1;5;31mOpción no válida. Introduce S o N.\033[0m")
        continuar = input("¿Quieres introducir otro número? (S/N): ").upper()

#print("Programa finalizado.")

print("\033[1;5;32mPrograma finalizado.\033[0m")




