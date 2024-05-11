import streamlit as st
from extraer_diccionario import extraer_diccionario
import google.generativeai as genai
import fitz
import os
import json 

PROMPT_CV = """
Eres un experto en extracción de información de imágenes. 
Tu tarea es analizar las imágenes del CV que te proporciono y extraer la siguiente información, organizándola en un diccionario de Python:

Información personal: Nombre completo, profesión, información de contacto (teléfono, email, dirección, LinkedIn, etc.).
Aptitudes y habilidades: Lista de aptitudes relevantes para el puesto, incluyendo habilidades técnicas y blandas.
Idiomas: Lista de idiomas que domina el candidato y su nivel de competencia.
Software: Lista de programas y herramientas de software que el candidato sabe utilizar.
Formación: Lista de títulos académicos, incluyendo nombre del título, institución, fecha de graduación y cualquier otra información relevante (como promedio académico).
Experiencia laboral: Lista de experiencias laborales previas, incluyendo nombre de la empresa, puesto desempeñado, fechas de inicio y fin, y una descripción de las responsabilidades y logros en cada puesto.

Asegúrate de:

Identificar correctamente la estructura del CV y extraer la información de las secciones correspondientes.
Manejar diferentes formatos de CVs y adaptarte a la variación en la presentación de la información. 
Extraer la información de forma precisa y evitar errores de interpretación. 
Organizar la información de manera clara y estructurada dentro del diccionario de Python.
Unicamente quiero el diccionario, sin intentar asignarlo a una variable o algo parecido.
"""

def mostrar_cv():
    st.title('Cargador y Analizador de CVs en PDF')
    st.markdown("""
    <style>
        .big-font {
            font-size:18px;
            color: #4f8bf9;
        }
        .info-text {
            font-size:16px;
        }
    </style>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Elige un archivo PDF", type="pdf", help="Sube el CV que deseas analizar.")

    if uploaded_file is not None:
        if 'cv_info' not in st.session_state or 'uploaded_file_name' not in st.session_state or st.session_state.uploaded_file_name != uploaded_file.name:
            process_cv(uploaded_file)

        editable_cv_info = edit_cv_info(st.session_state.cv_info)
        if st.button('Guardar cambios'):
            save_edited_cv(editable_cv_info, f"docs/{st.session_state.uploaded_file_name}_edited.json")
            st.success("Cambios guardados exitosamente!")

def process_cv(uploaded_file):
    pdf_path = f"docs/{uploaded_file.name}"
    image_folder = "images"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.markdown(f'<p class="big-font">Archivo subido: {uploaded_file.name}</p>', unsafe_allow_html=True)
    
    with st.spinner('Procesando tu CV...'):
        image_paths = pdf_to_images(pdf_path, image_folder)
        if image_paths:
            cv_info = analyze_image_with_ai(image_paths[0])
            st.session_state.cv_info = cv_info
            st.session_state.uploaded_file_name = uploaded_file.name
            st.success('Perfil añadido exitosamente!')

def edit_cv_info(cv_info):
    st.markdown('<p class="info-text">Edita la información extraída del CV:</p>', unsafe_allow_html=True)
    edited_info = {}
    for key, value in cv_info.items():
        st.subheader(f"{key}:")
        if isinstance(value, dict):
            edited_info[key] = edit_nested_dict(value)
        elif isinstance(value, list):
            edited_info[key] = edit_list(value, key)
        else:
            edited_info[key] = st.text_input(key, str(value) if value else '')
    return edited_info

def edit_nested_dict(nested_dict):
    edited_dict = {}
    for sub_key, sub_value in nested_dict.items():
        if isinstance(sub_value, list):
            edited_dict[sub_key] = edit_list(sub_value, sub_key)
        else:
            edited_dict[sub_key] = st.text_input(sub_key, str(sub_value) if sub_value else '')
    return edited_dict

def edit_list(value_list, key):
    st.write(f"Editando la lista de {key}:")
    edited_list = []
    for i, item in enumerate(value_list):
        if isinstance(item, dict):
            edited_list.append(edit_nested_dict(item))
        else:
            edited_item = st.text_input(f"{key} {i+1}", item)
            edited_list.append(edited_item)
    return edited_list

def save_edited_cv(data, file_path):
    new_file_path = f"{file_path}_edited.json"
    with open(new_file_path, 'w') as f:
        json.dump(data, f, indent=4)
    st.success(f"CV guardado como {new_file_path}")

def analyze_image_with_ai(image_path):
    sample_file = genai.upload_file(path=image_path, display_name="Sample CV")
    file = genai.get_file(name=sample_file.name)
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
    response = model.generate_content([PROMPT_CV, file])
    return extraer_diccionario(response.text)

def pdf_to_images(pdf_path, base_output_folder):
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_folder = os.path.join(base_output_folder, pdf_name)
    os.makedirs(output_folder, exist_ok=True)
    doc = fitz.open(pdf_path)
    image_paths = []
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        pix = page.get_pixmap()
        output_path = f"{output_folder}/page_{page_number + 1}.jpg"
        pix.save(output_path, "jpeg")
        image_paths.append(output_path)
    return image_paths