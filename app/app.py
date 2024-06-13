import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('models/model.pkl')

# Prediction function
def predict(input_data):
    return model.predict(input_data)

# Streamlit UI
st.title("Predictive Analytics Application")

menu = ["Home", "Data Exploration", "Model Training", "Prediction"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Home")
    st.write("Welcome to the Predictive Analytics Application!")
    
elif choice == "Data Exploration":
    st.subheader("Data Exploration")
    df = pd.read_csv('data/dataset.csv')
    st.dataframe(df)
    st.write("### Summary Statistics")
    st.write(df.describe())

elif choice == "Model Training":
    st.subheader("Model Training")
    st.write("The model has been trained using a RandomForestClassifier.")
    st.write("Accuracy: ", model.score(X_test, y_test))

elif choice == "Prediction":
    st.subheader("Prediction")
    st.write("### Input Data")
    input_data = st.text_area("Enter input data in CSV format:")
    if st.button("Predict"):
        input_df = pd.read_csv(StringIO(input_data))
        prediction = predict(input_df)
        st.write("### Prediction Results")
        st.write(prediction)