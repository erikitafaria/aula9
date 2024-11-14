import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

df.drop(columns=['Unnamed: 0'], inplace=True)

list = ['Lat_d', 'Long_d']
df[list] = df[list].apply(pd.to_numeric, errors='coerce')

estados = df['NM_UF'].unique()
estadoselecionado = st.selectbox('Qual estado selecionar?',estados)

dadosfiltrados = df[df['NM_UF'] == estadoselecionado]

if st.checkbox('Mostrar tabela'):
  st.write(dadosfiltrados)

st.map(dadosfiltrados, latitude="Lat_d", longitude="Long_d")
