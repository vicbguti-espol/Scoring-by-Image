import streamlit as st
from categorias import obtener_criterios_por_categoria

# Estructura de datos global para almacenar todas las calificaciones
datos_globales = {}

class Calificaciones:
    @staticmethod
    def mostrar_categoria_seleccionada(categoria_seleccionada):
        st.header("Categoría: {}".format(categoria_seleccionada))

    @staticmethod
    def recopilar_calificaciones(categoria_seleccionada, oferta_laboral):
        datos = {}
        for criterio, valor_por_defecto in oferta_laboral[categoria_seleccionada].items():
            st.write(criterio)
            if isinstance(valor_por_defecto, dict):
                primer_elemento = list(valor_por_defecto.values())[0]
                try:
                    valor_por_defecto_numerico = float(primer_elemento)
                except (ValueError, TypeError):
                    valor_por_defecto_numerico = 0.5
            else:
                try:
                    valor_por_defecto_numerico = float(valor_por_defecto)
                except (ValueError, TypeError):
                    valor_por_defecto_numerico = 0.5
            clave_slider = "{} - {}".format(categoria_seleccionada, criterio)  # Generar clave única para el slider
            calificacion = st.slider("Calificación (0 - 1) para {}".format(criterio), 0.0, 1.0, valor_por_defecto_numerico, 0.1, key=clave_slider)
            if categoria_seleccionada not in datos:
                datos[categoria_seleccionada] = {}
            datos[categoria_seleccionada][criterio] = calificacion
        return datos

def mostrar_calificaciones(oferta_laboral):
    st.header("Criterios de Calificación Identificados")

    categorias = obtener_criterios_por_categoria(oferta_laboral)

    # Crear una lista de nombres de pestañas
    nombres_pestanas = list(categorias.keys())

    # Usar los nombres de pestañas en st.tabs()
    tabs = st.tabs(nombres_pestanas)
    for i, categoria in enumerate(categorias.keys()):
        with tabs[i]:  # Usar el índice para acceder a la pestaña correcta
            Calificaciones.mostrar_categoria_seleccionada(categoria)
            datos_globales[categoria] = Calificaciones.recopilar_calificaciones(categoria, oferta_laboral)

    if st.button("Ver datos recolectados hasta el momento"):
        st.header("Datos recolectados:")
        st.write(datos_globales)
