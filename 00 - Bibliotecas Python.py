import sys
import importlib
import inspect
import pandas as pd

# Listado de librerías clave a analizar (puedes añadir las que tengas instaladas)
librerias_objetivo = [
    'os', 'sys', 'math', 'datetime', 'json', 're', 'collections', 'itertools',
    'numpy', 'pandas', 'requests'
]

datos_funciones = []

for lib_name in librerias_objetivo:
    try:
        # Importar dinámicamente la librería
        lib = importlib.import_module(lib_name)
        
        # Inspeccionar todos los miembros de la librería
        for miembro_nombre, miembro_objeto in inspect.getmembers(lib):
            # Filtrar solo funciones y funciones integradas (built-in)
            if inspect.isfunction(miembro_objeto) or inspect.isbuiltin(miembro_objeto):
                # Intentar obtener la firma de la función (argumentos)
                try:
                    firma = str(inspect.signature(miembro_objeto))
                except Exception:
                    firma = "(Argumentos no disponibles/Built-in)"
                
                # Obtener la descripción (docstring)
                doc = inspect.getdoc(miembro_objeto)
                doc_corta = doc.split('\n')[0] if doc else "Sin descripción disponible."
                
                datos_funciones.append({
                    "Librería": lib_name,
                    "Módulo/Clase": lib_name,
                    "Nombre de la Función": miembro_nombre,
                    "Sintaxis / Argumentos": f"{miembro_nombre}{firma}",
                    "Descripción / Detalle": doc_corta
                })
                
    except ImportError:
        # Si la librería no está instalada, saltar a la siguiente
        continue

# Crear el DataFrame y exportar a un único archivo Excel
df = pd.DataFrame(datos_funciones)
archivo_salida = "librerias_python.xlsx"
df.to_excel(archivo_salida, index=False)

print(f"¡Archivo '{archivo_salida}' generado con éxito con {len(df)} funciones detalladas!")