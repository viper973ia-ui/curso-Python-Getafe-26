temperaturas="12.4,23.6,17.8,3.5,29.0,11.6"
#¿Cúal es la temperatura más baja?

controltemperatura=10000000

for n in temperaturas.split(","):
    n=float(n)
    if n<controltemperatura:
        controltemperatura=n
print(f"La temperatura más baja es de {controltemperatura} grados")

#En Python, la expresión temperaturas.split(",") se utiliza para dividir 
# una cadena de texto (string) en una lista de partes más pequeñas, usando la coma (,) 
# como el punto de separación.

## *************************************************************************************

##   ***** LA FORMA + CORTA DE HACERLO ES: *****

print("La temperatura más baja es de ", min(float(n) for n in temperaturas.split(",")), "grados (En una sola línea)")

## *************************************************************************************