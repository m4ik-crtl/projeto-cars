import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df = pd.read_csv('vehicles_us.csv')

# Cabeçalho com texto explicativo
st.header("Análise de Anúncios de Carros Usados")
st.write("""
    Este aplicativo apresenta uma análise interativa de anúncios de veículos usados nos EUA.
    Explore a distribuição de quilometragem, o relacionamento entre preço e ano,
    e outros insights sobre os tipos de veículos e suas cores.
""")

# Exibindo o Data Viewer com a tabela de dados
st.subheader("Visualização dos Dados")
st.write(df)

# Exibindo o histograma de quilometragem com checkbox
if st.checkbox("Mostrar histograma da quilometragem"):
    st.write("Histograma da coluna 'odometer' (quilometragem dos veículos):")
    fig = px.histogram(df, x="odometer", title="Distribuição de Quilometragem")
    st.plotly_chart(fig, use_container_width=True)

# Exibindo o gráfico de dispersão (Preço x Ano)
st.subheader("Gráfico de Dispersão: Preço x Ano do Modelo")
fig = px.scatter(df, x="model_year", y="price", color="type", 
                 title="Preço x Ano do Modelo dos Veículos")
st.plotly_chart(fig, use_container_width=True)

# Exibindo histograma de contagem de tipos de veículos por cor
st.subheader("Distribuição de Tipos de Veículos por Cor")
fig = px.histogram(df, x="paint_color", color="type", barmode="group", 
                   title="Contagem de Tipos de Veículos por Cor")
st.plotly_chart(fig, use_container_width=True)
