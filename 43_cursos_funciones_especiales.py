cursos=[
    {"denominacion":"Python y datos","horario":"mañana","fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","horario":"mañana","fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","horario":"tarde","fecha_fin":"04/12/2025"},
    {"denominacion":"Programador certificado","horario":"festivos","fecha_fin":"30/09/2025"}  
]

# Se pide al usuario que introduzca horario de los cursos y le 
# mostraremos los nombres de los cursos con ese horario.

horario_usuario=(input("Introduce el horario de los cursos (mañana, tarde o festivos): ")).lower()

# print (horario_usuario)

cursos_disponibles=(list(map(lambda lb:lb["denominacion"],
                             filter(lambda hr:hr["horario"]==horario_usuario, cursos))))


print (cursos_disponibles)



 