import streamlit as st
import pandas as pd
import joblib

def run_predictions():
    st.title('Previsões')
    
    # Carregar modelo (exemplo)
    model = joblib.load('models/best_model.pkl')
    
    # Entrada de dados
    feature1 = st.number_input('Feature 1:')
    feature2 = st.number_input('Feature 2:')
    
    # Botão para fazer a predição
    if st.button('Predict'):
        prediction = model.predict([[feature1, feature2]])
        st.write('Resultado da predição:', prediction[0])
    
if __name__ == '__main__':
    run_predictions()