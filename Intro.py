import streamlit as st
from PIL import Image

# ---------------- CONFIGURACIÓN GENERAL ----------------
st.set_page_config(
    page_title="🚀 Portafolio de Aplicaciones IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- ESTILOS VISUALES ----------------
st.markdown("""
<style>
/* Fondo general */
.stApp {
    background: linear-gradient(to bottom, #f8fbff, #eaf4ff);
}

/* Sidebar elegante */
section[data-testid="stSidebar"] {
    background-color: #dceeff;
    color: #1b1b1b;
}

/* Títulos */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #102542;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #2c3e50;
    margin-bottom: 30px;
}

/* Tarjetas */
.card {
    background-color: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
    text-align: center;
    margin-bottom: 25px;
    min-height: 420px;
}

/* Título tarjeta */
.card h3 {
    color: #0b3d91;
    font-size: 22px;
}

/* Texto */
.card p {
    color: #333333;
    font-size: 15px;
}

/* Botones enlaces */
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

/* Separadores */
hr {
    border: 1px solid #b0c4de;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🤖 Portafolio de Aplicaciones con Inteligencia Artificial</div>', unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Explora proyectos desarrollados con IA, visión computacional, voz, análisis documental y sistemas multimodales 🚀
</div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("📌 Sobre este Portafolio")
    st.write("""
    Este espacio reúne aplicaciones de Inteligencia Artificial desarrolladas para:
    
    ✅ Visión por computadora  
    ✅ OCR y análisis de documentos  
    ✅ Control por voz  
    ✅ Reconocimiento de escritura  
    ✅ Traducción multimodal  
    ✅ Sistemas ciberfísicos  
    
    Cada tarjeta incluye:
    🏷️ Nombre del proyecto  
    🖼️ Imagen representativa  
    🔗 Botón directo  
    """)
    st.info("💡 Consejo: Haz clic en 'Abrir App' para probar cada proyecto.")

# ---------------- ENLACE GENERAL ----------------
st.subheader("🌐 Página Principal de Aplicaciones")
st.markdown("[🚀 Abrir sitio general](https://cmcorreaapps-myapps.streamlit.app/)")

st.markdown("---")

# ---------------- DATOS DE APLICACIONES ----------------
apps = [
    {
        "titulo": "🔍 Reconocimiento de Objetos (YOLO)",
        "imagen": "txt_to_audio.png",
        "descripcion": "Detecta objetos en imágenes usando visión computacional.",
        "link": "https://yolov5-o9vuxeujucdxmhfnqynr8h.streamlit.app/"
    },
    {
        "titulo": "📄 Chat PDF Inteligente",
        "imagen": "Chat_pdf.png",
        "descripcion": "Analiza documentos PDF y responde preguntas con IA.",
        "link": "https://chatpdf-rg6mhi6hhsopbaasqgeujc.streamlit.app/"
    },
    {
        "titulo": "🎤 Control por Voz MQTT",
        "imagen": "voice_ctrl.jpg",
        "descripcion": "Controla dispositivos mediante comandos de voz.",
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
        "descripcion": "Extrae texto de imágenes, audio y documentos para análisis.",
        "link": "https://ocr-audio-xqwj7rk5ypspm8gsykjixq.streamlit.app/"
    },
    {
        "titulo": "🌎 Traductor Multimodal",
        "imagen": "OIG8.jpg",
        "descripcion": "Convierte voz, texto y traducción inteligente.",
        "link": "https://traductor-twencn4crpnz2wkrpggjgm.streamlit.app/"
    },
    {
        "titulo": "🖼️ Vision App",
        "imagen": "OIG4.jpg",
        "descripcion": "Analiza imágenes con IA avanzada.",
        "link": "https://visionapp-kmxmr5glehhw888dc6fwne.streamlit.app/"
    },
    {
        "titulo": "☁️ WordCloud Inteligente",
        "imagen": "wordcloud.jpg",
        "descripcion": "Genera análisis visual de palabras clave.",
        "link": "https://wordcloud-vmcqegj6fxwz8p7lprwkov.streamlit.app/"
    },
    {
        "titulo": "📡 Sistema Ciberfísico",
        "imagen": "OIG6.jpg",
        "descripcion": "Interacción entre sensores, IA y mundo físico.",
        "link": "https://sendcmqtt-8jnbvrpiutqcbblad9p6lo.streamlit.app/"
    }
]

# ---------------- MOSTRAR EN GRID ----------------
cols = st.columns(3)

for i, app in enumerate(apps):
    with cols[i % 3]:
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(f"<h3>{app['titulo']}</h3>", unsafe_allow_html=True)

        try:
            image = Image.open(app["imagen"])
            st.image(image, use_container_width=True)
        except:
            st.warning("⚠️ Imagen no encontrada")

        st.markdown(f"<p>{app['descripcion']}</p>", unsafe_allow_html=True)

        st.markdown(
            f'<a class="link-button" href="{app["link"]}" target="_blank">🚀 Abrir App</a>',
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("✨ Portafolio desarrollado con Streamlit | Diseño mejorado con mayor contraste, organización visual y navegación clara.")
