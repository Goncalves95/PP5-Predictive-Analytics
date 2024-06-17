import streamlit as st

def run_home():
    st.title('Bem-vindo ao Sistema de Predição')
    st.write('Este é um sistema para realizar predições utilizando Machine Learning.')
    
    # Exemplo de botões para navegação
    if st.button('Exploração de Dados'):
        st.experimental_rerun()
    if st.button('Treinamento do Modelo'):
        st.experimental_rerun()
    if st.button('Previsões'):
        st.experimental_rerun()

if __name__ == '__main__':
    run_home()