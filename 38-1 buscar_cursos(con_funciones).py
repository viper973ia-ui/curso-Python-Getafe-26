from datetime import datetime

cursos = [
    {"denominacion": "Python y datos", "calificaciones": [5.6, 7.8, 3.3, 7.2], "fecha_fin": "10/03/2026"},
    {"denominacion": "Inglés científico", "calificaciones": [8.2, 7.8, 6.3, 4.2, 9.0], "fecha_fin": "22/07/2026"},
    {"denominacion": "Spring e hibernate", "calificaciones": [5.8, 4.3, 7.5], "fecha_fin": "04/12/2025"},
    {"denominacion": "Programador certificado", "calificaciones": [7.8, 6.6, 4.8, 5.3, 7.7], "fecha_fin": "30/09/2025"}
]

def calcular_media(curso):
    """Calcula la nota media de las calificaciones de un curso."""
    notas = curso["calificaciones"]
    return sum(notas) / len(notas)

def convertir_fecha(curso):
    """Convierte la cadena de texto de la fecha en un objeto datetime para poder comparar."""
    return datetime.strptime(curso["fecha_fin"], "%d/%m/%Y")

def resolver_ejercicio(lista_cursos):
    # 1. Encontrar el curso con la nota media más alta
    curso_mejor_nota = max(lista_cursos, key=calcular_media)
    
    # 2. Encontrar el curso que finalizó antes (fecha más antigua)
    curso_mas_antiguo = min(lista_cursos, key=convertir_fecha)
    
    # Mostrar resultados
    print(f"Curso con la nota media más alta: {curso_mejor_nota['denominacion']} (Media: {calcular_media(curso_mejor_nota):.2f})")
    print(f"Curso que finalizó antes: {curso_mas_antiguo['denominacion']} (Finalizó el: {curso_mas_antiguo['fecha_fin']})")

# Ejecutar la función principal
resolver_ejercicio(cursos)
