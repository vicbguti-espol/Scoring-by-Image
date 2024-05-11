import streamlit as st
from PIL import Image
import io
import google.generativeai as genai
from extraer_diccionario import extraer_diccionario

# Configurar la clave de la API de Google
GOOGLE_API_KEY = "AIzaSyCdbJ0a3XuKJ7UbB0_z5e244wwDFm99bIk"
genai.configure(api_key=GOOGLE_API_KEY)

PROMPT_OFERTA_LABORAL = """
    Analiza una imagen de una oferta laboral. Basado, en los siguientes categorias: 
    --Educación,
    --Experiencia (tiempo, cargo, tarea y empresa), Reconocimientos y logros, proyectos desarrollados, Certificaciones,
    --Voluntariado
    --Idiomas, 
    --Disponibilidad, 
    --Conocimientos,
    --Ubicación

    Necesito que me devuelvas un diccionario y únicamente un diccionario de phyton, ningún texto adicional, en donde se clasifique cada criterio interno de las categorias por importancia, esta sera numerica del 0 al 1. Por ejemplo: 
    Conocimientos (Categoria):
    -SQL (CRITERIO): 0.5
    -MONGODB (CRITERIO): 0.3
    -C# (CRITERIO): 0.6

    Este es un ejemplo del diccionario, en donde esta vacio es un ejemplo para que ubiques asi en caso de que suceda:
    {
        "Educación": {
        Criterios

        },
        "Experiencia": {
        Criterios

        },
        "Reconocimientos y logros": {},  # Vacío, sin menciones en la oferta
        "Proyectos desarrollados": {},  # Vacío, sin especificaciones en la oferta
        "Certificaciones": {},  # Vacío, sin menciones en la oferta
        "Voluntariado": {},  # Vacío, sin menciones en la oferta
        "Idiomas": {
        Criterios
        },
        "Disponibilidad": {
        Criterios
        },
        "Conocimientos": {
        Criterios
        },
        "Ubicación": {
        Criterios
        }
    }
"""

# Función para procesar la imagen
def procesar_imagen():
    st.header("Procesamiento de Imagen por Partes")

    uploaded_image = st.file_uploader("Sube una imagen", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        # Cargar la imagen utilizando PIL
        image = Image.open(io.BytesIO(uploaded_image.read()))
        st.image(image, caption="Imagen Original", use_column_width=True)

        # Guardar la imagen temporalmente
        image_path = "temp_image.jpg"
        image.save(image_path)

        # Subir la imagen a Gemini
        sample_file = genai.upload_file(path=image_path, display_name="Sample drawing")
        file = genai.get_file(name=sample_file.name)

        # Crear un objeto de modelo generativo para Gemini
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

        # Generar contenido utilizando el modelo generativo y la imagen
        response = model.generate_content([PROMPT_OFERTA_LABORAL, file]) 

        oferta_laboral = extraer_diccionario(response.text)

        # Mostrar el texto extraído
        st.write("Diccionario:", oferta_laboral)

        return oferta_laboral