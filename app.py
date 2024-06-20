import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Cargar los datos desde un archivo subido
uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding='latin1')
    
    # Eliminar duplicados y llenar valores faltantes
    df.drop_duplicates(inplace=True)
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Configuración de Streamlit
    st.title("Reportes de Playlist")

    # Sidebar para navegación
    st.sidebar.title("Menú de Reportes")
    opciones = [
        "Distribución de Popularidad (Violin Plot)",
        "Promedio de Popularidad por Artista",
        "Relación entre Duración y Popularidad",
        "Evolución de la Popularidad por Año",
        "Distribución de la Energía (Boxplot)",
        "Distribución de Danceability",
        "Top 10 Tracks por Popularidad",
        "Top 10 Artistas por Cantidad de Tracks",
        "Top 10 Tracks por Duración",
        "Relación entre Popularidad y Energía",
        "Mapa de Calor de Correlaciones"
    ]
    seleccion = st.sidebar.radio("Selecciona un reporte:", opciones)

    # Funciones de visualización (definir aquí las funciones como se mostró anteriormente)

    # Mostrar el reporte seleccionado (definir aquí el código para mostrar el reporte seleccionado)

else:
    st.write("Por favor, sube un archivo CSV para continuar.")
