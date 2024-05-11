import streamlit as st

# Datos falsos de ejemplo
perfiles = [
    {"nombre": "Juan Pérez", "Educación": 0.9, "Experiencia": 0.8, "Certificaciones": 0.7, "Conocimientos": 0.85, "Ubicación": 0.95},
    {"nombre": "Ana Gómez", "Educación": 0.78, "Experiencia": 0.88, "Certificaciones": 0.65, "Conocimientos": 0.80, "Ubicación": 0.50},
    {"nombre": "Carlos Díaz", "Educación": 0.85, "Experiencia": 0.9, "Certificaciones": 0.75, "Conocimientos": 0.70, "Ubicación": 0.90},
    {"nombre": "Luisa Romero", "Educación": 0.95, "Experiencia": 0.70, "Certificaciones": 0.65, "Conocimientos": 0.95, "Ubicación": 0.85}
]

def mostrar_resultados():
    st.title("Top 5 Perfiles para la Oferta Laboral")
    
    # Datos ficticios para el leaderboard
    perfiles = [
        {"nombre": "María López", "puntaje": 92, "descripción": "Experta en Data Science con 5 años de experiencia en el sector financiero."},
        {"nombre": "Carlos Fernández", "puntaje": 88, "descripción": "Desarrollador Senior Full-stack, especializado en React y Node.js."},
        {"nombre": "Juana Martínez", "puntaje": 85, "descripción": "Gerente de Proyectos con certificación PMP, ha liderado más de 10 proyectos internacionales."},
        {"nombre": "Roberto Sánchez", "puntaje": 82, "descripción": "Especialista en Marketing Digital con enfoque en SEO y campañas PPC."},
        {"nombre": "Ana Torres", "puntaje": 80, "descripción": "Ingeniera de software con experiencia en sistemas embebidos y IoT."}
    ]

    for perfil in perfiles:
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image("https://via.placeholder.com/150", width=150)  # Placeholder para imagen del perfil
            with col2:
                st.markdown(f"#### {perfil['nombre']}")
                st.markdown(f"**Puntaje:** {perfil['puntaje']}")
                st.markdown(perfil['descripción'])
