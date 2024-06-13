import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_data_exploration():
    st.title('Exploração de Dados')
    
    # Carregar dados (exemplo)
    df = pd.read_csv('data/dataset.csv')
    
    # Exibir pandas profiling ou outras análises
    st.subheader('Visão Geral dos Dados')
    st.write(df.head())
    
    # Exemplo de gráfico de correlação
    st.subheader('Matriz de Correlação')
    corr_matrix = df.corr()
    sns.heatmap(corr_matrix, annot=True)
    st.pyplot()
    
if __name__ == '__main__':
    run_data_exploration()