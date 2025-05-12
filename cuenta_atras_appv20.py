import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
from st_screen_stats import WindowQueryHelper

st.set_page_config(page_title="Budapest Beer Countdown", layout="centered")

# 🔁 Refrescar automáticamente cada segundo
st_autorefresh(interval=1000, key="responsive_countdown")

# 🧠 Inicializar el helper para detectar el tamaño de la ventana
helper = WindowQueryHelper()

# Detectar si es una pantalla móvil (ancho máximo de 480px)
is_mobile = helper.maximum_window_size(max_width=480, key="max_width_480")["status"]

if is_mobile:
    # 📱 Diseño para móviles: imagen arriba, texto abajo
    st.image("https://raw.githubusercontent.com/txema-taboas/budapest/main/Budapest.jpg", use_container_width=True)
    st.markdown(
        "<h1 style='color:#ff9900; font-family:Courier New; text-align:center;'>🍻 ¡Cuenta atrás para beber cervezas!</h1>",
        unsafe_allow_html=True
    )
else:
    # 🖥️ Diseño para escritorio: imagen a la izquierda, texto a la derecha
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("https://raw.githubusercontent.com/txema-taboas/budapest/main/Budapest.jpg", use_container_width=True)
    with col2:
        st.markdown(
            "<h1 style='color:#ff9900; font-family:Courier New;'>🍻 ¡Cuenta atrás para beber cervezas!</h1>",
            unsafe_allow_html=True
        )

# 🗓️ Fechas del viaje
fecha_inicio_str = "2025-05-22 06:45:00"
fecha_fin_str = "2025-05-26 22:00:00"
fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d %H:%M:%S")

st.markdown(
    f"<h4 style='color:#bbbbbb;'>Fechas de la visita:<br>{fecha_inicio_str} → {fecha_fin_str}</h4>",
    unsafe_allow_html=True
)

# ⏱️ Cuenta atrás
ahora = datetime.now()
if ahora >= fecha_inicio:
    st.success("¡Ya estás en Budapest! 🥳🍺")
else:
    diferencia = fecha_inicio - ahora
    dias = diferencia.days
    horas, resto = divmod(diferencia.seconds, 3600)
    minutos, segundos = divmod(resto, 60)

    st.markdown(
        f"<h2 style='color:#00ff99; font-family:Courier New;'>⏱️ {dias} días, {horas:02}h {minutos:02}m {segundos:02}s</h2>",
        unsafe_allow_html=True
    )





