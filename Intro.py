# REEMPLAZA SOLO LA SECCIÓN DE ESTILOS (st.markdown CSS) POR ESTA VERSIÓN

st.markdown("""
<style>

/* Fondo general */
.stApp {
    background: linear-gradient(to bottom, #f8fbff, #eaf4ff);
    color: black !important;
}

/* TODO el texto general en negro */
html, body, [class*="css"] {
    color: black !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #dceeff !important;
    color: black !important;
}

/* Texto dentro del sidebar */
section[data-testid="stSidebar"] * {
    color: black !important;
}

/* Títulos principales */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: black !important;
    margin-bottom: 10px;
}

/* Subtítulo */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: black !important;
    margin-bottom: 30px;
}

/* Subheaders Streamlit */
h1, h2, h3, h4, h5, h6 {
    color: black !important;
}

/* Párrafos */
p {
    color: black !important;
}

/* Labels */
label {
    color: black !important;
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
    color: black !important;
}

/* Texto dentro de tarjetas */
.card h3, .card p {
    color: black !important;
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

/* Info boxes */
.stInfo, .stAlert {
    color: black !important;
}

/* Caption */
.caption {
    color: black !important;
}

/* Separadores */
hr {
    border: 1px solid #b0c4de;
}

</style>
""", unsafe_allow_html=True)
