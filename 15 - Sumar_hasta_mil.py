#1+2+3+4+...... ¿hasta que número tendremos que llegar
#para que la suma alcance o supere el valor 1000
total=1000
suma=0
contador=0
while suma<total:
    contador=contador+1
    suma=suma+contador
print (f"El número máximo para alcanzar o superar los 1.000 es {contador} siendo su suma total {suma}")
print (f"El número anterior es {contador-1} y la suma total es {suma-contador}")