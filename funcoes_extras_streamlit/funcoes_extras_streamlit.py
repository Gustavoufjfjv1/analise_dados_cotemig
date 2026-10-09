import streamlit as st
import pandas as pd

st.set_page_config(page_title="Loja de carros", page_icon="---", layout="wide")


CATALOGO_CARROS = {
    "Fiat Uno 2010": {"categoria": "Hatch", "preco": 26900.00},
    "VW Gol G5": {"categoria": "Hatch", "preco": 27500.00},
    "Renault Kwid": {"categoria": "Compacto", "preco": 48000.00},
    "Chevrolet Onix": {"categoria": "Hatch", "preco": 68900.00},
    "Fiat Mobi": {"categoria": "Compacto", "preco": 62000.00},
    "Toyota Corolla": {"categoria": "Sedan", "preco": 89000.00},
    "VW Saveiro": {"categoria": "Picape", "preco": 72000.00},
    "Honda Civic": {"categoria": "Sedan", "preco": 125000.00},
}

if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# -----------------------------------------------------------------------------

st.title(" Dashboard de Carros - Ponto de Venda")
st.markdown("---")

col1, col2 = st.columns([1, 1], gap="large")


with col1:
    st.subheader("Seleção de Veículos")
   
    # Form de adição de item
    with st.form("form_item", clear_on_submit=False):
        carro_nome = st.selectbox("Escolha o Produto", list(CATALOGO_CARROS.keys()))
        preco_unit = CATALOGO_CARROS[carro_nome]["preco"]
        st.caption(f"Preço Unitário: **R$ {preco_unit:.2f}**")
       
        quantidade = st.number_input("Quantidade", min_value=1, value=1, step=1)
       
        btn_adicionar = st.form_submit_button("Adicionar ao Carrinho", use_container_width=True)
       
        if btn_adicionar:
            subtotal = preco_unit * quantidade
            st.session_state.carrinho.append({
                "Produto": carro_nome,
                "Preço Unit. (R$)": preco_unit,
                "Qtd": quantidade,
                "Subtotal (R$)": subtotal
            })
            st.success(f"**{carro_nome}** adicionado com sucesso!")

    # Exibe o carrinho atual
    st.subheader("Carrinho de Compras")
    if st.session_state.carrinho:
        df_carrinho = pd.DataFrame(st.session_state.carrinho)
       
        st.dataframe(
            df_carrinho,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Preço Unit. (R$)": st.column_config.NumberColumn(
                    "Preço Unit.",
                    format="R$ %.2f"
                ),
                "Subtotal (R$)": st.column_config.NumberColumn(
                    "Subtotal",
                    format="R$ %.2f"
                )
            }
        )
       
        if st.button("Limpar Carrinho", use_container_width=True):
            st.session_state.carrinho = []
            st.rerun()
    else:
        st.info("O carrinho está vazio. Adicione itens acima.")


with col2:
    st.subheader(" Pagamento e Fechamento")
   
    # Cálculo do total acumulado
    total_compra = sum(item["Subtotal (R$)"] for item in st.session_state.carrinho)
   
    # Cartão com o Total da Compra
    st.metric(label="TOTAL DA COMPRA", value=f"R$ {total_compra:.2f}")
   
    st.markdown("---")
   
    # Entrada de dinheiro
    valor_recebido = st.number_input(
        "Dinheiro Entregue pelo Cliente (R$)",
        min_value=0.0,
        value=0.0,
        step=5.0,
        format="%.2f"
    )
   
    # Validação e Cálculo de Troco
    if total_compra == 0:
        st.warning("Adicione produtos ao carrinho antes de prosseguir com o pagamento.")
    else:
        troco = valor_recebido - total_compra
       
        if valor_recebido == 0:
            st.info("Aguardando o recebimento do dinheiro...")
        elif valor_recebido < total_compra:
            falta = total_compra - valor_recebido
            st.error(f"**Dinheiro Insuficiente!** Faltam **R$ {falta:.2f}** para concluir a venda.")
        else:
            st.success(f" **Pagamento Concluído!**")
            st.metric(label="TROCO A DEVOLVER", value=f"R$ {troco:.2f}")
           
            # Resumo da Venda
            with st.expander("Ver Comprovante da Venda"):
                st.write(f"**Itens Comprados:** {len(st.session_state.carrinho)}")
                st.write(f"**Total:** R$ {total_compra:.2f}")
                st.write(f"**Pago em Dinheiro:** R$ {valor_recebido:.2f}")
                st.write(f"**Troco:** R$ {troco:.2f}")
           
            if st.button("Finalizar Atendimento e Novo Cliente", type="primary", use_container_width=True):
                st.session_state.carrinho = []
                st.rerun()