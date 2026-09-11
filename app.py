import streamlit as st

st.set_page_config(page_title="Portal Ejecutivo", layout="centered")

st.title("Portal de Acceso - Reportes")
st.write("Seleccione el panel al que desea ingresar:")

# URLs configuradas con el token de acceso directo gerencial
url_gdu = "https://control-stock-gdu-clbhtifv7ciwrrsdqsyib4.streamlit.app/?token=LG-DirectivosVIP"
url_farmashop = "https://stock-farmashop-pjud6onrpoukxpnvl4tptj.streamlit.app/?token=LG-DirectivosVIP"
url_distribuidores = "https://distribuidores-interior-cmwcyghkovuyfluwcdmzt6.streamlit.app/?token=LG-DirectivosVIP"

# Botones de acceso directo ordenados verticalmente
st.link_button("🛒 Ingresar a GDU", url_gdu, use_container_width=True)
st.link_button("💊 Ingresar a FARMASHOP", url_farmashop, use_container_width=True)
st.link_button("🚚 Ingresar al Panel de DISTRIBUIDORES", url_distribuidores, use_container_width=True)
