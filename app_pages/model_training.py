import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def run_model_training():
    st.title('Treinamento do Modelo')
    
    # Carregar dados (exemplo)
    df = pd.read_csv('data/X.train.csv')
    df = pd.read_csv('data/Y.train.csv')
    
    # Preparar dados (exemplo)
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Treinar modelo (exemplo com RandomForestClassifier)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    # Avaliar modelo
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    st.subheader('Acurácia do Modelo:')
    st.write(f'Acurácia: {accuracy:.2f}')
    
if __name__ == '__main__':
    run_model_training()