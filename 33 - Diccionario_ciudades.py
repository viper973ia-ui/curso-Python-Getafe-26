ciudades={}
ciudades["Madrid"]=3200000
ciudades["Getafe"]=100000
ciudades["Alcorcón"]=170000
ciudades["Avila"]=1300000
del(ciudades["Avila"])

# ************** Recorrer diccionarios **************

for k,v in ciudades.items():
    print(f"La ciudad {k} tiene {v} habitantes.")
