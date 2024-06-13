import streamlit as st
from home import run_home
from data_exploration import run_data_exploration
from model_training import run_model_training
from predictions import run_predictions

def main():
    # Título da página
    st.title('Sistema de Predição')
    
    # Opções de navegação
    menu = ['Home', 'Exploração de Dados', 'Treinamento do Modelo', 'Previsões']
    choice = st.sidebar.selectbox('Menu', menu)
    
    # Mostrar página selecionada
    if choice == 'Home':
        run_home()
    elif choice == 'Exploração de Dados':
        run_data_exploration()
    elif choice == 'Treinamento do Modelo':
        run_model_training()
    elif choice == 'Previsões':
        run_predictions()

if __name__ == '__main__':
    main()