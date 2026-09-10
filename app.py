import streamlit as st

st.set_page_config(page_title="Portal Ejecutivo", layout="centered")

st.title("Portal de Acceso - Reportes")
st.write("Seleccione el panel al que desea ingresar:")

# Reemplazá con las URLs reales de tus apps agregando el ?token=...
url_gdu = "https://tu-app-gdu.streamlit.app/?token=ClaveSecretaDirectivos123"
url_farmashop = "https://tu-app-farmashop.streamlit.app/?token=ClaveSecretaDirectivos123"

# Botones que abren las webs en una nueva pestaña
col1, col2 = st.columns(2)
with col1:
    st.link_button("📊 Ingresar a GDU", url_gdu, use_container_width=True)
with col2:
    st.link_button("📊 Ingresar a FARMASHOP", url_farmashop, use_container_width=True)