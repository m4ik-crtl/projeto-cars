import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
st.header("Análise de Anúncios de Carros")

if st.checkbox("Mostrar histograma da quilometragem"):
    st.write("Histograma da coluna odometer")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("Mostrar gráfico de dispersão preço x ano"):
    st.write("Gráfico de dispersão entre preço e ano do modelo")
    fig = px.scatter(df, x="model_year", y="price", color="type")
    st.plotly_chart(fig, use_container_width=True)

