import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="IA Portfolio", layout="wide")

# --- ESTILO CSS (COMPACTO Y ESTÉTICO) ---
st.markdown("""
    <style>
    /* Fondo general */
    .main {
        background-color: #ffffff;
    }
    
    /* Encabezado con degradado para resaltar el título blanco */
    .header-container {
        background: linear-gradient(90deg, #6f42c1 0%, #e83e8c 100%);
        padding: 40px;
        border-radius: 15px;
        margin-bottom: 30px;
        text-align: center;
    }
    
    /* Estilo de las Tarjetas (Cards más pequeñas) */
    .project-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 20px;
        border: 1px solid #eee;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 320px; /* Altura fija más pequeña */
    }
    
    .project-card:hover {
        transform: scale(1.02);
        box-shadow: 0px 8px 15px rgba(111, 66, 193, 0.2);
        border-color: #6f42c1;
    }

    .card-title {
        color: #000000 !important;
        font-weight: bold;
        font-size: 1.1rem;
        margin: 10px 0;
    }
    
    .card-text {
        color: #555555 !important;
        font-size: 0.85rem;
        line-height: 1.2;
    }

    .card-button {
        background-color: #000000;
        color: white !important;
        padding: 8px 15px;
        border-radius: 8px;
        text-decoration: none;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 10px;
    }
    
    .card-button:hover {
        background-color: #6f42c1;
    }

    /* Ocultar barra lateral */
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("""
    <div class="header-container">
        <h1 style='color: white; margin: 0; font-size: 2.5rem;'>Mis Aplicaciones de IA</h1>
        <p style='color: rgba(255,255,255,0.8); margin-top: 10px;'>Explora mi portafolio de proyectos inteligentes 🚀</p>
    </div>
    """, unsafe_allow_html=True)

# --- FUNCIÓN PARA GENERAR TARJETAS ---
def create_card(title, description, link, icon_url):
    st.markdown(f"""
        <div class="project-card">
            <div>
                <img src="{icon_url}" width="60" style="margin: 0 auto;">
                <div class="card-title">{title}</div>
                <p class="card-text">{description}</p>
            </div>
            <a class="card-button" href="{link}" target="_blank">Ver Proyecto</a>
        </div>
    """, unsafe_allow_html=True)

# --- GRID DE PROYECTOS (4 COLUMNAS PARA CARDS MÁS PEQUEÑAS) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    create_card(
        "Chat PDF 📄", 
        "Conversa con tus documentos usando RAG.",
        "https://chatpdf-cyzzvlqfzyjrt85er7txmd.streamlit.app/", # Link actualizado
        "https://cdn-icons-png.flaticon.com/512/337/337946.png"
    )
    create_card(
        "YOLO Vision 🔍", 
        "Detección de objetos en tiempo real.",
        "https://yolov5-o9vuxeujucdxmhfnqynr8h.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2589/2589175.png"
    )

with col2:
    create_card(
        "Control Voz 🗣️", 
        "Comandos de voz para interfaces.",
        "https://ctrlvoice-aosnsdxaemdnxox4g4dhn8.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/1082/1082842.png"
    )
    create_card(
        "Dígitos 🎨", 
        "Reconocimiento de trazos manuales.",
        "https://drawrecog-zsogvkezvecvt3isbulwgf.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/588/588395.png"
    )

with col3:
    create_card(
        "Traductor 🌍", 
        "Traducción con contexto IA.",
        "https://traductor-twencn4crpnz2wkrpggjgm.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/3898/3898082.png"
    )
    create_card(
        "OCR Audio 🎙️", 
        "De imagen a texto y luego a voz.",
        "https://ocr-audio-xqwj7rk5ypspm8gsykjixq.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/802/802340.png"
    )

with col4:
    create_card(
        "Vision App 👁️", 
        "Análisis visual con GPT-4o.",
        "https://visionapp-kmxmr5glehhw888dc6fwne.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2103/2103833.png"
    )
    create_card(
        "IoT MQTT 🌐", 
        "Conectividad física y sensores.",
        "https://sendcmqtt-8jnbvrpiutqcbblad9p6lo.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2344/2344654.png"
    )

st.markdown("<br><p style='text-align: center; color: #aaa; font-size: 0.8rem;'>© 2026 Portafolio Digital de IA</p>", unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown("<br><br><p style='text-align: center; color: #888;'>Hecho con ❤️ y Streamlit</p>", unsafe_allow_html=True)
