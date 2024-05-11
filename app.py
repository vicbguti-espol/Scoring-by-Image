import streamlit as st
from procesamiento_imagen import procesar_imagen
from calificaciones import mostrar_calificaciones
from cargar_cv import mostrar_cv

def main():
    # st.set_page_config(page_title="Consultora de Recursos Humanos", layout="wide")

    st.title("Consultora de Recursos Humanos")

    # Descripción con un tamaño de texto más grande
    st.markdown("""
    Bienvenido a la aplicación de gestión de recursos humanos. Utiliza las herramientas disponibles para gestionar y buscar perfiles profesionales.
    """, unsafe_allow_html=False)

    # Menú lateral para selección de herramientas con estilos personalizados
    st.sidebar.title("Navegación")
    app_choice = st.sidebar.radio(
        "Selecciona una opción:",
        ["Guardar Perfiles", "Buscar Perfiles Adaptados", "Resultados"]
    )

    if app_choice == "Guardar Perfiles":
        st.subheader("Guardar Perfiles del Personal")
        st.markdown("""
        Carga y analiza CVs para guardar en la base de datos de la consultora.
        """, unsafe_allow_html=False)
        mostrar_cv()

    elif app_choice == "Buscar Perfiles Adaptados":
        st.subheader("Buscar Perfiles Adaptados")
        st.markdown("""
        Utiliza criterios específicos para buscar en la base de datos los perfiles que mejor se adapten a los requisitos de los clientes.
        """, unsafe_allow_html=False)
        if 'oferta_laboral' not in st.session_state:
            st.session_state.oferta_laboral = None
        st.session_state.oferta_laboral = procesar_imagen()

    elif app_choice == "Resultados":
        st.subheader("Resultados de Búsqueda")
        st.markdown("""
        Muestra los resultados de las búsquedas de perfiles adaptados a los clientes.
        """, unsafe_allow_html=False)
        if st.session_state.oferta_laboral is not None:
            mostrar_calificaciones(st.session_state.oferta_laboral)
        else:
            st.write("No hay resultados para mostrar. Por favor realiza una búsqueda primero.")

if __name__ == "__main__":
    main()
