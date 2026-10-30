#Pide dos números y muestra el resultado de dividir el mayor entre el menor
num1=int (input("Introduce un número "))
num2=int (input("Introduce otro número número "))

if num1>num2:
    print (f"{num1} entre {num2} es {num1/num2}")
else:
    print(f"{num2} entre {num1} es {num2/num1}")
    
