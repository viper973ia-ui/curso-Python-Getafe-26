
"""
dias={"lunes","martes","miércoles"}
dias.add("jueves")
dias.add("lunes")  
print(dias)  
"""
dia=input("dime un día de la semana: ")
dias={"lunes","martes","miércoles"}
if dia in dias:
    print("ese díaya existe")
else:
    dias.add(dia)
print(dias)
