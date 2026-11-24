# Dia 10: st.selectbox
import streamlit as st
st.header("Seleção")

st.write("Barra de seleção única (dia 10)") # Apenas 1 escolha
option = st.selectbox(
    "Qual é a sua cor favorita?",
    ("Vermelho", "Amarelo", "Azul")
)
st.write("Você selecionou: ", option)

# Dia 11: st.multiselect
st.write("Barra de seleção múltipla (dia 11)")

options = st.multiselect(
    "Que cores você curte?",
    ["Vermelho", "Amarelo", "Azul"]
)
st.write("Você gosta de: ", options)

# Dia 12: st.checkbox
st.write("Caixa de seleção múltipla (dia 12)")

Vermelho = st.checkbox("Vermelho")
if Vermelho:
    st.write("Vermelho como ketchup")
Amarelo = st.checkbox("Amarelo")
if Amarelo:
    st.write("Amarelo como mostarda")
Azul = st.checkbox("Azul")
if Azul:
    st.write("Azul como embalagem de maionese")