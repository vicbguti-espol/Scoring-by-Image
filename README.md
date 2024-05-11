# CV Match

CV Match es una aplicación desarrollada para analizar y clasificar perfiles profesionales basados en ofertas laborales específicas. Utiliza tecnología de IA para extraer información relevante de los currículos y ofertas laborales, permitiendo a los reclutadores encontrar los candidatos más adecuados de manera eficiente.

## Características Principales

- **Análisis de CV**: Extrae información clave de los currículos en formato PDF.
- **Evaluación de Ofertas Laborales**: Analiza imágenes de ofertas laborales para determinar los requisitos necesarios.
- **Calificación de Perfiles**: Clasifica los perfiles basados en su adecuación a los requisitos de la oferta.
- **Leaderboard de Candidatos**: Muestra un ranking de los candidatos que mejor se adaptan a los requerimientos del cliente.

## Tecnologías Utilizadas

- Streamlit
- PyMuPDF (fitz)
- PIL (Python Imaging Library)
- Google Generative AI

## Instalación

Para instalar y ejecutar CV Match en tu entorno local, sigue los siguientes pasos:

### Requisitos Previos

Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Clonar el Repositorio

Primero, clona este repositorio en tu máquina local usando:

```bash
git clone https://github.com/tu_usuario/cv_match.git
cd cv_match
```

### Instalar Dependencias
Instala todas las dependencias necesarias ejecutando:


```bash
pip install -r requirements.txt
```

### Ejecutar la Aplicación
Una vez instaladas las dependencias, puedes iniciar la aplicación con:


```bash
streamlit run app.py
```