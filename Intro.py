import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Portafolio IA", layout="wide")

# --- ESTILO CSS (ESTÉTICA MINIMALISTA) ---
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    
    /* Encabezado con degradado y título blanco */
    .header-container {
        background: linear-gradient(90deg, #6f42c1 0%, #e83e8c 100%);
        padding: 45px;
        border-radius: 20px;
        margin-bottom: 40px;
        text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    
    /* Tarjetas de Proyecto Compactas */
    .project-card {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 25px;
        border: 1px solid #f0f0f0;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.03);
        transition: all 0.3s ease-in-out;
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 340px; /* Altura optimizada */
    }
    
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 12px 20px rgba(111, 66, 193, 0.15);
        border-color: #e83e8c;
    }

    .card-title {
        color: #000000 !important;
        font-weight: 700;
        font-size: 1.05rem;
        margin: 12px 0 8px 0;
        line-height: 1.2;
    }
    
    .card-text {
        color: #666666 !important;
        font-size: 0.85rem;
        line-height: 1.3;
        margin-bottom: 15px;
    }

    .card-button {
        background-color: #000000;
        color: white !important;
        padding: 10px 15px;
        border-radius: 10px;
        text-decoration: none;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        transition: background 0.3s;
    }
    
    .card-button:hover {
        background-color: #6f42c1;
        color: white !important;
    }

    /* Ocultar elementos innecesarios */
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("""
    <div class="header-container">
        <h1 style='color: white; margin: 0; font-size: 2.8rem; font-weight: 800;'>Mis Aplicaciones de IA</h1>
        <p style='color: rgba(255,255,255,0.9); margin-top: 15px; font-size: 1.1rem;'>
            Un recorrido por mis desarrollos en Inteligencia Artificial y Visión Computacional 🚀
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- FUNCIÓN PARA GENERAR TARJETAS ---
def create_card(title, description, link, icon_url):
    st.markdown(f"""
        <div class="project-card">
            <div>
                <img src="{icon_url}" width="55" style="margin: 0 auto; filter: drop-shadow(0px 2px 4px rgba(0,0,0,0.1));">
                <div class="card-title">{title}</div>
                <p class="card-text">{description}</p>
            </div>
            <a class="card-button" href="{link}" target="_blank">Explorar App</a>
        </div>
    """, unsafe_allow_html=True)

# --- GRID DE PROYECTOS (4 COLUMNAS) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    create_card(
        "Chat PDF 📄", 
        "Conversa con documentos mediante arquitectura RAG.",
        "https://chatpdf-cyzzvlqfzyjrt85er7txmd.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/337/337946.png"
    )
    create_card(
        "Texto a Audio 🔊", 
        "Síntesis de voz a partir de texto escrito.",
        "https://m69tbigtehsksnuuurppnf.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/727/727245.png"
    )
    create_card(
        "OCR + Trad + Voz 🎙️", 
        "Multimodal: lee, traduce y narra imágenes.",
        "https://ocr-audio-xqwj7rk5ypspm8gsykjixq.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/802/802340.png"
    )
    create_card(
        "WordCloud Voz ☁️", 
        "Generación de nubes de palabras por voz.",
        "https://wordcloud-vmcqegj6fxwz8p7lprwkov.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/3203/3203071.png"
    )

with col2:
    create_card(
        "Control Voz 🗣️", 
        "Interfaces controladas por comandos hablados.",
        "https://ctrlvoice-aosnsdxaemdnxox4g4dhn8.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/1082/1082842.png"
    )
    create_card(
        "Mi Primera App ✨", 
        "Introducción al desarrollo con Streamlit.",
        "https://intro-1-nqkl8hsuhjnzb2txp36oxn.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/1006/1006363.png"
    )
    create_card(
        "IA Vision (Básico) 🖼️", 
        "Reconocimiento general de imágenes.",
        "https://5svtxxql776wx9dgfjuuta.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2103/2103833.png"
    )

with col3:
    create_card(
        "Tablero Inteligente 🖋️", 
        "IA que interpreta bocetos y dibujos.",
        "https://drawrecog-zsogvkezvecvt3isbulwgf.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/588/588395.png"
    )
    create_card(
        "Reconocimiento OCR 📖", 
        "Extracción de texto desde archivos físicos.",
        "https://dxhjstjwszpkfh6g79wucg.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2784/2784461.png"
    )
    create_card(
        "Traductor Voz 🌍", 
        "Traducción instantánea de audio.",
        "https://traductor-twencn4crpnz2wkrpggjgm.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/3898/3898082.png"
    )

with col4:
    create_card(
        "Dígitos RNA 🔢", 
        "Red Neuronal que reconoce números a mano.",
        "https://vyvneanguuppgth4zyfgmr.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/1055/1055627.png"
    )
    create_card(
        "MQTT Control 🌐", 
        "Comunicación IoT y sistemas físicos.",
        "https://sendcmqtt-8jnbvrpiutqcbblad9p6lo.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2344/2344654.png"
    )
    create_card(
        "Análisis Vision App 👁️", 
        "Visión avanzada con modelos GPT-4o.",
        "https://visionapp-kmxmr5glehhw888dc6fwne.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/1531/1531391.png"
    )
    create_card(
        "YOLO Objetos 🔍", 
        "Detección inteligente de objetos múltiples.",
        "https://yolov5-o9vuxeujucdxmhfnqynr8h.streamlit.app/",
        "https://cdn-icons-png.flaticon.com/512/2589/2589175.png"
    )

# --- PIE DE PÁGINA ---
st.markdown("<br><br><p style='text-align: center; color: #bbb; font-size: 0.85rem;'>Diseñado para la excelencia en Inteligencia Artificial | 2026</p>", unsafe_allow_html=True)
