import streamlit as st
from utils import calcular_nota

st.title("Calculadora Nota Ebau")

with st.form("Calcula tu nota de ebau: "):
    media_bachiller = st.number_input("Media de Bachiller: ", min_value=0.00, max_value=10.00)
    st.markdown("""---""")
    st.subheader("Fase Obligatoria")
    lengua = st.number_input("Nota de Lengua: ", min_value=0.00, max_value=10.00)
    ingles = st.number_input("Nota de Inglés: ", min_value=0.00, max_value=10.00)
    historia = st.number_input("Nota de Historia: ", min_value=0.00, max_value=10.00)
    opcional_1 = st.number_input("Nota de La Primera Opcional: ", min_value=0.00, max_value=10.00)
    st.markdown("""---""")
    st.subheader("Fase Optativa")
    opcional_2 = st.number_input("Nota de La Segunda Opcional: ", min_value=0.00, max_value=10.00)
    opcional_3 = st.number_input("Nota de La Tercera Opcional: ", min_value=0.00, max_value=10.00)
    submit = st.form_submit_button("Calcular")

    if submit:
        nota = calcular_nota(media_bachiller, lengua, ingles, historia, opcional_1, opcional_2, opcional_3)
        if nota > 5:
            st.success(f"Tu nota es: {round(nota, 5)}")
        else:
            st.warning(f"Tu nota es: {round(nota, 5)}")

