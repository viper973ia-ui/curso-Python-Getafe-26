num=int(input("Introduce un número "))
if num<0:
    print("Mucho frio")
elif num >=0 and num<=10:
    print("Día fresco")
elif num>10 and num<40:
    print("Calor")
else:
    print("Indeterminado")