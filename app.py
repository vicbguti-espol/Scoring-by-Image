import streamlit as st
from procesamiento_imagen import procesar_imagen
from calificaciones import mostrar_calificaciones

def main():
    st.title("Aplicación de Streamlit")

    # Initialize or get the value of 'oferta_laboral' from session state
    if 'oferta_laboral' not in st.session_state:
        st.session_state.oferta_laboral = None

    # Crear un menú de selección para elegir entre las dos aplicaciones
    app_choice = st.sidebar.selectbox("Selecciona una aplicación", ["Procesamiento de Imagen", "Calificaciones", "Resultados"])

    if app_choice == "Procesamiento de Imagen":
        # Update 'oferta_laboral' in session state
        st.session_state.oferta_laboral = procesar_imagen()

    elif app_choice == "Calificaciones":
        # Use 'oferta_laboral' from session state
        mostrar_calificaciones(st.session_state.oferta_laboral)

if __name__ == "__main__":
    main()
