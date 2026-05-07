import streamlit as st
from PIL import Image

# ---------------- CONFIGURACIÓN ----------------
st.set_page_config(
    page_title="🚀 Portafolio de Aplicaciones IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- ESTILOS ----------------
st.markdown("""
<style>

/* Fondo general */
.stApp {
    background: linear-gradient(to bottom, #f8fbff, #eaf4ff);
    color: black !important;
}

/* Todo el texto negro */
html, body, [class*="css"], p, div, span, label {
    color: black !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #dceeff !important;
}

section[data-testid="stSidebar"] * {
    color: black !important;
}

/* Títulos */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: black !important;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: black !important;
    margin-bottom: 30px;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
    color: black !important;
}

/* Tarjetas */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
    text-align: center;
    margin-bottom: 25px;
    min-height: 430px;
    border: 1px solid #d9e6f2;
}

/* Botón */
.link-button {
    display: inline-block;
    padding: 10px 18px;
    background-color: #0b3d91;
    color: white !important;
    text-decoration: none;
    border-radius: 10px;
    font-weight: bold;
    margin-top: 10px;
}

.link-button:hover {
    background-color: #072c66;
}

/* Separador */
hr {
    border: 1px solid #b0c4de;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🤖 Portafolio de Aplicaciones con Inteligencia Artificial</div>', unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Explora proyectos de visión computacional, voz, OCR, RAG y sistemas multimodales 🚀
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("📌 Sobre este Portafolio")
    st.write("""
    Aquí encontrarás aplicaciones desarrolladas en:
    
    ✅ Visión por computadora  
    ✅ OCR y documentos  
    ✅ Control por voz  
    ✅ Reconocimiento de escritura  
    ✅ Traducción IA  
    ✅ Sistemas ciberfísicos  
    """)
    st.info("💡 Haz clic en cada botón para abrir la aplicación.")

# ---------------- ENLACE GENERAL ----------------
st.subheader("🌐 Página Principal")
st.markdown("[🚀 Abrir sitio principal](https://cmcorreaapps-myapps.streamlit.app/)")

st.markdown("---")

# ---------------- APLICACIONES ----------------
apps = [
    {
        "titulo": "🔍 Reconocimiento de Objetos (YOLO)",
        "imagen": "txt_to_audio.png",
        "descripcion": "Detecta objetos en imágenes con visión computacional.",
        "link": "https://yolov5-o9vuxeujucdxmhfnqynr8h.streamlit.app/"
    },
    {
        "titulo": "📄 Chat PDF Inteligente",
        "imagen": "Chat_pdf.png",
        "descripcion": "Analiza documentos PDF y responde preguntas.",
        "link": "https://chatpdf-rg6mhi6hhsopbaasqgeujc.streamlit.app/"
    },
    {
        "titulo": "🎤 Control por Voz MQTT",
        "imagen": "voice_ctrl.jpg",
        "descripcion": "Control de dispositivos usando voz.",
        "link": "https://ctrlvoice-aosnsdxaemdnxox4g4dhn8.streamlit.app/"
    },
    {
        "titulo": "✍️ Reconocimiento de Escritura",
        "imagen": "OIG5.jpg",
        "descripcion": "Reconoce números escritos a mano.",
        "link": "https://drawrecog-zsogvkezvecvt3isbulwgf.streamlit.app/"
    },
    {
        "titulo": "🧠 OCR + Audio + RAG",
        "imagen": "OIG3.jpg",
        "descripcion": "Extrae y analiza información de audio, imágenes y texto.",
        "link": "https://ocr-audio-xqwj7rk5ypspm8gsykjixq.streamlit.app/"
    },
    {
        "titulo": "🌎 Traductor Multimodal",
        "imagen": "OIG8.jpg",
        "descripcion": "Traducción de voz y texto.",
        "link": "https://traductor-twencn4crpnz2wkrpggjgm.streamlit.app/"
    },
    {
        "titulo": "🖼️ Vision App",
        "imagen": "OIG4.jpg",
        "descripcion": "Analiza imágenes con IA.",
        "link": "https://visionapp-kmxmr5glehhw888dc6fwne.streamlit.app/"
    },
    {
        "titulo": "☁️ WordCloud Inteligente",
        "imagen": "wordcloud.jpg",
        "descripcion": "Visualización avanzada de palabras.",
        "link": "https://wordcloud-vmcqegj6fxwz8p7lprwkov.streamlit.app/"
    },
    {
        "titulo": "📡 Sistema Ciberfísico",
        "imagen": "OIG6.jpg",
        "descripcion": "Interacción entre IA y sensores físicos.",
        "link": "https://sendcmqtt-8jnbvrpiutqcbblad9p6lo.streamlit.app/"
    }
]

# REEMPLAZA SOLO ESTA PARTE:
# cols = st.columns(3)
# for i, app in enumerate(apps):

# ---------------- GRID DINÁMICO SIN ESPACIOS VACÍOS ----------------
for row_start in range(0, len(apps), 3):
    row_apps = apps[row_start:row_start + 3]
    cols = st.columns(len(row_apps))  # Solo crea columnas necesarias

    for col, app in zip(cols, row_apps):
        with col:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.markdown(f"### {app['titulo']}")

            try:
                image = Image.open(app["imagen"])
                st.image(image, use_container_width=True)
            except:
                st.warning("⚠️ Imagen no encontrada")

            st.write(app["descripcion"])

            st.markdown(
                f'<a class="link-button" href="{app["link"]}" target="_blank">🚀 Abrir App</a>',
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)
# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("✨ Portafolio IA | Diseño organizado, mayor contraste y navegación clara.")
