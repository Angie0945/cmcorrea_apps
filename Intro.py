import streamlit as st
from PIL import Image

# ---------------- TÍTULO ----------------
st.title("Aplicaciones de Inteligencia Artificial.")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# ---------------- ENLACE GENERAL ----------------
url_ia = "https://cmcorreaapps-myapps.streamlit.app/"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# ---------------- COLUMNAS ----------------
col1, col2, col3 = st.columns(3)

# ---------------- COLUMNA 1 ----------------
with col1:

    st.subheader("Reconocimiento de Objetos")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.")
    url = "https://yolov5-o9vuxeujucdxmhfnqynr8h.streamlit.app/"
    st.write(f"YOLO: [Enlace]({url})")

    st.subheader("Reconocimiento de Escritura")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos cómo reconocer números escritos a mano.")
    url = "https://drawrecog-zsogvkezvecvt3isbulwgf.streamlit.app/"
    st.write(f"Escritura: [Enlace]({url})")

    st.subheader("Sistema Ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos interacción con el mundo físico.")
    url = "https://sendcmqtt-8jnbvrpiutqcbblad9p6lo.streamlit.app/"
    st.write(f"Ciberfísico: [Enlace]({url})")

# ---------------- COLUMNA 2 ----------------
with col2:

    st.subheader("Conversión de voz a texto")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.")
    url = "https://traductor-twencn4crpnz2wkrpggjgm.streamlit.app/"
    st.write(f"Voz a texto: [Enlace]({url})")

    st.subheader("Control por Voz")
    image = Image.open('voice_ctrl.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos control de dispositivos usando voz.")
    url = "https://ctrlvoice-aosnsdxaemdnxox4g4dhn8.streamlit.app/"
    st.write(f"Control por Voz: [Enlace]({url})")

    st.subheader("OCR Audio e Imagen")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos análisis de audio, imagen y texto.")
    url = "https://ocr-audio-xqwj7rk5ypspm8gsykjixq.streamlit.app/"
    st.write(f"OCR + Audio: [Enlace]({url})")

# ---------------- COLUMNA 3 ----------------
with col3:

    st.subheader("Generación en Contexto")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("En la siguiente veremos una aplicación que usa RAG a partir de documentos.")
    url = "https://chatpdf-rg6mhi6hhsopbaasqgeujc.streamlit.app/"
    st.write(f"RAG: [Enlace]({url})")

    st.subheader("Análisis de Imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos análisis inteligente de imágenes.")
    url = "https://visionapp-kmxmr5glehhw888dc6fwne.streamlit.app/"
    st.write(f"Vision: [Enlace]({url})")

    st.subheader("WordCloud Inteligente")
    image = Image.open('wordcloud.jpg')
    st.image(image, width=200)
    st.write("En la siguiente enlace veremos análisis visual de palabras.")
    url = "https://wordcloud-vmcqegj6fxwz8p7lprwkov.streamlit.app/"
    st.write(f"WordCloud: [Enlace]({url})")
