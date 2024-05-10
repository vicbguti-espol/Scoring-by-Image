import re
import json
import ast

def extraer_diccionario(texto):
    # Expresión regular para encontrar el texto entre tres comillas triples
    patron = r'```python\s*(.*?)\s*```'

    # Buscar todas las coincidencias en el texto
    coincidencias = re.findall(patron, texto, re.DOTALL)

    # Si se encuentra al menos una coincidencia
    if coincidencias:
        # Extraer la última coincidencia (por si hay múltiples bloques de código)
        diccionario_texto = coincidencias[-1]

        # # Convertir las cadenas Unicode a texto plano
        diccionario_texto = json.loads(diccionario_texto)

        # # Cargar el texto del diccionario como un diccionario de Python
        # diccionario = eval(diccionario_texto)

        return diccionario_texto
    else:
        return None
    