import streamlit as st
import pandas as pd

st.write("Notas 3ª etapa")

st.write("----------------------------------------------------------------------------------------")

st.write("3A1")

st.write("Ola mundo")

nome = st.text_input("Qual seu nome: ")

st.write(f"Ola, {nome}, bem-vindo ao Colégio Cotemig")

st.write("----------------------------------------------------------------------------------------")

df = pd.DataFrame({'disciplina': ["Python", "Matemática", "Português"], 'nota': [10, 5, 0]})

df

st.write("A Eliza está brava, estude mais português")

st.write("----------------------------------------------------------------------------------------")

selecao = st.selectbox("Selecione uma opção:", ["Python", "Matemática", "Português"])

st.write(f"Você escolheu {selecao}")