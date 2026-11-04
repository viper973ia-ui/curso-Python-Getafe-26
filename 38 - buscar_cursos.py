cursos=[
    {"denominacion":"Python y datos","calificaciones":[5.6,7.8,3.3,7.2],"fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","calificaciones":[8.2,7.8,6.3,4.2,9.0],"fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","calificaciones":[5.8,4.3,7.5],"fecha_fin":"04/12/2025"},
    {"denominacion":"Programador certificado","calificaciones":[7.8,6.6,4.8,5.3,7.7],"fecha_fin":"30/09/2025"}  
] 

# Nombre del curso con la nota media más alta
# Nombre del curso que finalizó antes

contar_notas=0
suma_notas=0
nota_media_max=0
fecha_fin_min="31/12/9999"


for curso in cursos:
    suma_notas=sum(curso["calificaciones"])
    contar_notas=len(curso["calificaciones"])
    nota_media=suma_notas/contar_notas
    
    if nota_media>nota_media_max:
        nota_media_max=nota_media
        curso_nota_media_max=curso["denominacion"]
        
    
    fecha_fin=curso["fecha_fin"]
    if "fecha_fin_min" not in locals() or fecha_fin<fecha_fin_min:   # (No coge la última línea que es la correcta)
        fecha_fin_min=fecha_fin
        curso_fecha_fin_min=curso["denominacion"]

print("Curso con la nota media más alta:\n", curso_nota_media_max,"con nota media de:", nota_media_max)
print("Curso que finalizó antes: \n", curso_fecha_fin_min,"con fecha de finalización:", fecha_fin_min)

## ********************************************************
#                 utilizando funciones
## ********************************************************
def calcular_nota_media(curso):
    suma_notas=sum(curso["calificaciones"])
    contar_notas=len(curso["calificaciones"])
    nota_media=suma_notas/contar_notas
    return nota_media