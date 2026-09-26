import streamlit as st
import streamlit.components.v1 as components

# Configuramos la página de Streamlit para que ocupe todo el ancho
st.set_page_config(layout="wide", page_title="Feliz Aniversario")

# Ocultamos el menú por defecto de Streamlit para que se vea como una web normal
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Leemos el archivo HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Mostramos la web HTML dentro de Streamlit
components.html(html_data, height=850, scrolling=True)
