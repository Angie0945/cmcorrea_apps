import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="IA Portfolio", layout="wide")

# --- ESTILO CSS PERSONALIZADO (MODERNO Y LIMPIO) ---
st.markdown("""
    <style>
    /* Fondo general */
    .main {
        background-color: #ffffff;
    }
    
    /* Estilo de las Tarjetas (Cards) */
    .project-card {
        background-color: #fcfaff; /* Lila casi blanco */
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 25px;
        border-left: 10px solid #6f42c1; /* Borde morado */
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
        min-height: 420px;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        border-left: 10px solid #e83e8c; /* Cambia a rosado al pasar el mouse */
    }

    /* Títulos y texto dentro de las cards */
    .card-title {
        color: #000000 !important;
        font-weight: bold;
        font-size: 1.4rem;
        margin-bottom: 10px;
    }
    
    .card-text {
        color: #333333 !important;
        font-size: 0.95rem;
        margin-bottom: 15px;
    }

    /* Botones modernos */
    .card-button {
        background-color: #6f42c1;
        color: white !important;
        padding: 10px 20px;
        border-radius: 20px;
        text-decoration: none;
        font-weight: bold;
        display: inline-block;
        margin-top: auto;
    }
    
    .card-button:hover {
        background-color: #e83e8c;
    }

    /* Ocultar barra lateral y menús innecesarios */
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<h1 style='text-align: center; color: #000000;'>✨ Mis Aplicaciones de IA ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6f42c1; font-size: 1.2rem;'>Explora mis proyectos de Inteligencia Artificial de forma rápida y visual.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- FUNCIÓN PARA GENERAR TARJETAS ---
def create_card(title, description, link, icon_url):
    st.markdown(f"""
        <div class="project-card">
            <img src="{icon_url}" width="100" style="margin-bottom: 15px;">
            <div class="card-title">{title}</div>
            <p class="card-text">{description}</p>
            <a class="card-button" href="{link}" target="_blank">🚀 Abrir Aplicación</a>
        </div>
    """, unsafe_allow_html=True)

# --- GRID DE PROYECTOS (3 COLUMNAS) ---
col1, col2, col3 = st.columns(3)

with col1:
    create_card(
        "Detección YOLO 🔍", 
        "Identifica múltiples objetos en tiempo real con alta precisión.",
        "https://yolov5-o9vuxeujucdxmhfnqynr8h.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2589/2589175.png"
    )
    create_card(
        "Chat con PDF 📄", 
        "Sube tus archivos y haz preguntas directamente a tus documentos (RAG).",
        "https://https://chatpdf-cyzzvlqfzyjrt85er7txmd.streamlit.app//",
        "https://cdn-icons-png.flaticon.com/512/337/337946.png"
    )
    create_card(
        "Nube de Palabras ☁️", 
        "Visualiza los conceptos más importantes de cualquier texto.",
        "https://wordcloud-vmcqegj6fxwz8p7lprwkov.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/3203/3203071.png"
    )

with col2:
    create_card(
        "Control por Voz 🗣️", 
        "Interacción inteligente mediante comandos de voz procesados por IA.",
        "https://ctrlvoice-aosnsdxaemdnxox4g4dhn8.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/1082/1082842.png"
    )
    create_card(
        "Reconocimiento 🎨", 
        "IA capaz de entender dibujos y dígitos escritos a mano.",
        "https://drawrecog-zsogvkezvecvt3isbulwgf.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/588/588395.png"
    )
    create_card(
        "Traductor IA 🌍", 
        "Traducción multilingüe avanzada con contexto semántico.",
        "https://traductor-twencn4crpnz2wkrpggjgm.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/3898/3898082.png"
    )

with col3:
    create_card(
        "OCR & Audio 🎙️", 
        "Extrae texto de imágenes y conviértelo en audio instantáneamente.",
        "https://ocr-audio-xqwj7rk5ypspm8gsykjixq.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/802/802340.png"
    )
    create_card(
        "Vision App 👁️", 
        "Análisis visual profundo usando modelos GPT-4 Vision.",
        "https://visionapp-kmxmr5glehhw888dc6fwne.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2103/2103833.png"
    )
    create_card(
        "IoT MQTT 🌐", 
        "Conexión con el mundo físico mediante protocolos de sensores.",
        "https://sendcmqtt-8jnbvrpiutqcbblad9p6lo.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2344/2344654.png"
    )

# --- PIE DE PÁGINA ---
st.markdown("<br><br><p style='text-align: center; color: #888;'>Hecho con ❤️ y Streamlit</p>", unsafe_allow_html=True)
