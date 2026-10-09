import streamlit as st
import pandas as pd

st.title("Padaria Cotemig")
st.subheader("Bem vindo a padaria do Cotemig")

st.write("---")

df = pd.DataFrame({'itens': ["Pão Francês (kg)","Pão de Queijo (un)","Leite Integral (L)","Queijo Mussarela (g)","Presunto (g)","Café Espesso (un)","Bolo de Cenoura (fatia)"], 'precos': [14.90,2.50,5.80,12.50,9.80,6.00,8.50]})

df

st.write("---")

opcao = st.selectbox('Escolha o produto:', ["Pão Francês (kg)","Pão de Queijo (un)","Leite Integral (L)","Queijo Mussarela (g)","Presunto (g)","Café Espesso (un)","Bolo de Cenoura (fatia)"])

quantidade = st.number_input("Digite a quantidade: ", min_value=0)

if st.button("Calcular"):
    preco = df.loc[df["itens"] == opcao, "precos"].values[0] * quantidade
    st.write(f"Preço total: R${preco}")


    