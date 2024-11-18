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

if st.checkbox('Mostrar tabela') == True:
  st.write(dadosfiltrados)

st.map(dadosfiltrados, latitude="Lat_d", longitude="Long_d")
st.bar_chart(df['NM_UF'].value_counts()) #gráfico de barras por estado
st.bar_chart(df['NM_MUNIC'].value_counts()[:10]) 

st.metric('# Municípios', len(df['NM_MUNIC'].unique()))
#st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

st.metric('# Comunidades', len(df['NM_AGLOM'].unique()))
#st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())

st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])

numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))
