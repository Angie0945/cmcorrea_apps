# =========================================================
# 🌟 PORTAFOLIO FINAL - APLICACIONES DE INTELIGENCIA ARTIFICIAL
# Estilo tipo profesor + links propios + diseño más bonito
# =========================================================

import streamlit as st
from PIL import Image

# =========================================================
# CONFIGURACIÓN
# =========================================================
st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide"
)

# =========================================================
# ESTILOS VISUALES
# =========================================================
st.markdown("""
<style>

/* Fondo */
.stApp {
    background: linear-gradient(135deg, #efe4ff, #f8f5ff);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #34145c;
}
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Título principal */
.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 900;
    color: #2d1457;
    margin-bottom: 0;
}

/* Subtítulo */
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #5c3b8a;
    margin-bottom: 25px;
}

/* Tarjetas */
.card {
    background-color: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
    margin-bottom: 25px;
    border: 2px solid #d8c1ff;
}

/* Links */
a {
    color: #6a0dad !important;
    font-weight: bold;
    text-decoration: none;
}

a:hover {
    color: #4b0082 !important;
}

/* Subheaders */
h3 {
    color: #34145c;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown('<div class="main-title">🤖 Aplicaciones de Inteligencia Artificial</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">✨ Portafolio de Angie Vargas | Interfaces Multimodales ✨</div>', unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.subheader("📚 Aplicaciones con Inteligencia Artificial")
    st.write("""
    La inteligencia artificial permite:
    
    ✅ Mejorar la toma de decisiones  
    ✅ Automatizar tareas rutinarias  
    ✅ Analizar datos en tiempo real  
    ✅ Crear interfaces multimodales  
    ✅ Integrar visión, voz y sistemas físicos  
    """)
    st.success("🚀 Proyecto académico final")

# =========================================================
# ENLACE GENERAL
# =========================================================
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.subheader("🌍 Recursos, páginas y ejercicios prácticos")
st.write(f"🔗 [Ir al sitio principal]({url_ia})")

# =========================================================
# COLUMNAS
# =========================================================
col1, col2, col3 = st.columns(3)

# =========================================================
# COLUMNA 1
# =========================================================
with col1:

    st.subheader("🔍 Reconocimiento de Objetos")
    try:
        st.image(Image.open("txt_to_audio.png"), width=210)
    except:
        st.info("Agregar imagen: txt_to_audio.png")
    st.write("Detección inteligente de objetos usando visión artificial.")
    st.write("🔗 [Abrir App](https://yolov5-o9vuxeujucdxmhfnqynr8h.streamlit.app/)")

    st.subheader("📄 Chat PDF Inteligente")
    try:
        st.image(Image.open("Chat_pdf.png"), width=210)
    except:
        st.info("Agregar imagen: Chat_pdf.png")
    st.write("Consulta documentos PDF, imágenes y audios con análisis tipo RAG.")
    st.write("🔗 [Abrir App](https://chatpdf-rg6mhi6hhsopbaasqgeujc.streamlit.app/)")

    st.subheader("📝 OCR + Audio")
    try:
        st.image(Image.open("OIG3.jpg"), width=210)
    except:
        st.info("Agregar imagen: OIG3.jpg")
    st.write("Extrae texto desde imágenes y audio para análisis.")
    st.write("🔗 [Abrir App](https://ocr-audio-xqwj7rk5ypspm8gsykjixq.streamlit.app/)")

# =========================================================
# COLUMNA 2
# =========================================================
with col2:

    st.subheader("🎤 Control por Voz MQTT")
    try:
        st.image(Image.open("voice_ctrl.jpg"), width=210)
    except:
        st.info("Agregar imagen: voice_ctrl.jpg")
    st.write("Control de dispositivos físicos mediante comandos de voz.")
    st.write("🔗 [Abrir App](https://ctrlvoice-aosnsdxaemdnxox4g4dhn8.streamlit.app/)")

    st.subheader("✍️ Reconocimiento de Dígitos")
    try:
        st.image(Image.open("OIG8.jpg"), width=210)
    except:
        st.info("Agregar imagen: OIG8.jpg")
    st.write("Reconocimiento de números escritos a mano.")
    st.write("🔗 [Abrir App](https://drawrecog-zsogvkezvecvt3isbulwgf.streamlit.app/)")

    st.subheader("🌐 MQTT Sender")
    try:
        st.image(Image.open("OIG6.jpg"), width=210)
    except:
        st.info("Agregar imagen: OIG6.jpg")
    st.write("Envío de comandos y control de sistemas ciberfísicos.")
    st.write("🔗 [Abrir App](https://sendcmqtt-8jnbvrpiutqcbblad9p6lo.streamlit.app/)")

# =========================================================
# COLUMNA 3
# =========================================================
with col3:

    st.subheader("🖼️ Vision App")
    try:
        st.image(Image.open("OIG4.jpg"), width=210)
    except:
        st.info("Agregar imagen: OIG4.jpg")
    st.write("Análisis visual avanzado con IA.")
    st.write("🔗 [Abrir App](https://visionapp-kmxmr5glehhw888dc6fwne.streamlit.app/)")

    st.subheader("🌎 Traductor Multimodal")
    try:
        st.image(Image.open("txt_to_audio2.png"), width=210)
    except:
        st.info("Agregar imagen: txt_to_audio2.png")
    st.write("Convierte voz, texto e idioma en experiencias multimodales.")
    st.write("🔗 [Abrir App](https://traductor-twencn4crpnz2wkrpggjgm.streamlit.app/)")

    st.subheader("☁️ WordCloud IA")
    try:
        st.image(Image.open("data_analisis.png"), width=210)
    except:
        st.info("Agregar imagen: data_analisis.png")
    st.write("Visualización creativa de datos y palabras clave.")
    st.write("🔗 [Abrir App](https://wordcloud-vmcqegj6fxwz8p7lprwkov.streamlit.app/)")

# =========================================================
# PROYECTO EXTRA
# =========================================================
st.markdown("---")
st.subheader("⭐ Proyecto Especial")
st.write("🧠 Aplicación adicional de experimentación en IA:")
st.write("🔗 [Abrir Proyecto](https://dxhjstjwszpkfh6g79wucg.streamlit.app/)")

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")
st.caption("💜 Diseñado por Angie Vargas | Streamlit + IA + Interfaces Multimodales")
