import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Cuenta Atrás", layout="centered")
st.title("⏳ Cuenta Atrás en Tiempo Real")

# Refrescar la app automáticamente cada 1000 ms (1 segundo)
st_autorefresh(interval=1000, key="cuenta_atras_refresco")

# Entrada editable de fecha
fecha_objetivo_str = st.text_input(
    "Introduce la fecha y hora objetivo (AAAA-MM-DD HH:MM:SS):",
    "2025-05-22 06:45:00"
)

try:
    objetivo = datetime.strptime(fecha_objetivo_str, "%Y-%m-%d %H:%M:%S")
    ahora = datetime.now()

    if objetivo < ahora:
        st.error("🎉 ¡La fecha ha llegado!")
    else:
        diferencia = objetivo - ahora
        dias = diferencia.days
        horas, resto = divmod(diferencia.seconds, 3600)
        minutos, segundos = divmod(resto, 60)

        st.markdown(f"### Faltan {dias} días, {horas:02} horas, {minutos:02} minutos y {segundos:02} segundos.")
except ValueError:
    st.error("❌ Formato inválido. Usa el formato AAAA-MM-DD HH:MM:SS.")
