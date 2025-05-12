import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Budapest Beer Countdown", layout="centered")

# Refresca la app cada segundo
st_autorefresh(interval=1000, key="refresh_countdown")

# 📸 Imagen de Budapest (puedes subirla a GitHub y usar el enlace RAW o subirla directamente en la app)
# Imagen desde tu repo con ancho fluido moderno
st.image("https://raw.githubusercontent.com/txema-taboas/budapest/main/Budapest.jpg", use_container_width=True



# 🍺 Encabezado divertido
st.title("🍻 Cuenta atrás para beber cervezas!!!")

# Fechas fijas
fecha_inicio_str = "2025-05-22 06:45:00"
fecha_fin_str = "2025-05-26 22:00:00"
fecha_inicio = datetime.strptime(fecha_inicio_str, "%Y-%m-%d %H:%M:%S")

st.markdown(f"**Fechas de la visita:** {fecha_inicio_str} a {fecha_fin_str}")

# Calcular cuenta atrás
ahora = datetime.now()
if ahora >= fecha_inicio:
    st.success("¡Ya estás en Budapest! 🥳")
else:
    diferencia = fecha_inicio - ahora
    dias = diferencia.days
    horas, resto = divmod(diferencia.seconds, 3600)
    minutos, segundos = divmod(resto, 60)

    st.markdown(f"### ⏱️ Faltan {dias} días, {horas:02} horas, {minutos:02} minutos y {segundos:02} segundos.")

