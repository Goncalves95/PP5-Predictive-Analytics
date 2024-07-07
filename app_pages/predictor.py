import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from src.data import (
    load_house_prices_data,
    load_pkl_file,
    load_inherited_house_data)
from src.ml.evaluate_regression import regression_performance
from src.ml.predictive import predict_price

# Constants
MIN_PERCENTAGE = 0.2
MAX_PERCENTAGE = 2.5
MIN_OVERALL_QUALITY = 1
MAX_OVERALL_QUALITY = 10
MEDIAN_STEP = 20


def page_price_predictor_body():
    sale_price_pipe, sale_price_features = load_predict_sale_price_files()
    display_interface()
    x_live = generate_live_data()
    predict_sale_price(x_live, sale_price_features, sale_price_pipe)
    display_inherited_properties(sale_price_features, sale_price_pipe, x_live)

def load_predict_sale_price_files():
    vsn = 'v1'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_price/{vsn}/regression_pipeline.pkl"
    )
    sale_price_features = (
        pd.read_csv(
            f"outputs/ml_pipeline/predict_price/{vsn}/X_train.csv")
        .columns
        .to_list()
    )
    return sale_price_pipe, sale_price_features

def display_interface():
    st.write("### Sale Price Predictor Interface")
    st.success(
        f"* The client is interested in predicting the potential sale "
        f" prices"
        f" for properties in Ames, Iowa, and specifically, she wants to"
        f" determine a potential value for the properties she inherited "
        f" (Business Requirement 2). \n"
    )
    st.info(
        f"The price prediction will be based on four key features of the property, "
        f"which the client can input using the selections below. These features were "
        f"identified by our machine learning model as the most influential for predicting "
        f"Sale Price. They align closely with, but may vary slightly from, the variables "
        f"initially identified as most correlated in our initial data analysis. "
        f"The model conducts advanced analysis to pinpoint the optimal variables for "
        f"predicting Sale Price.\n\n"
        f"For more details on the machine learning model and feature importance, visit "
        f"**ML: Price Prediction** page.\n\n"
        f"**Information on categorical features used in prediction**:\n"
        f"- Overall Quality: Rated from 1 (Very Poor) to 10 (Very Excellent).\n\n"
        f"All three numerical features are measured in square feet."
    )
    st.write("---")

def generate_live_data():
    X_live = draw_inputs_widgets()
    return X_live

def predict_sale_price(x_live, sale_price_features, sale_price_pipe):
    if st.button("Run Predictive Analysis"):
        prediction = predict_price(x_live, sale_price_features, sale_price_pipe)
        st.write(f"* The predicted sale price is: **${prediction:.2f}**")

def display_inherited_properties(sale_price_features, sale_price_pipe, x_live):
    st.write("### Price prediction for the clients inherited properties:")
    in_df = load_inherited_house_data()
    in_df = in_df.filter(sale_price_features)

    st.write("* Features of Inherited Homes")
    st.write(in_df)

    if st.button("Run Prediction"):
        inherited_price_prediction = predict_price(in_df, sale_price_features, sale_price_pipe)
        total_value = inherited_price_prediction.sum()
        total_value = float(total_value.round(1))
        total_value = '${:,.2f}'.format(total_value)

        st.write(f"* The total value is estimated"
                 f" to be:")
        st.write(f"**{total_value}**")


def draw_inputs_widgets():
    data = load_house_prices_data()
    features = ["OverallQual", "TotalBsmtSF", "2ndFlrSF", "GarageArea"]

    X_live = pd.DataFrame([], index=[0])

    for feature in features:
        col = st.beta_columns(2)[features.index(feature) % 2]
        with col:
            if feature == "OverallQual":
                st_widget = st.number_input(
                    label=f"{feature}",
                    min_value=MIN_OVERALL_QUALITY,
                    max_value=MAX_OVERALL_QUALITY,
                    value=int(data[feature].median()),
                    step=1
                )
            else:
                st_widget = st.number_input(
                    label=f"{feature} SQFT",
                    min_value=int(data[feature].min() * MIN_PERCENTAGE),
                    max_value=int(data[feature].max() * MAX_PERCENTAGE),
                    value=int(data[feature].median()),
                    step=MEDIAN_STEP
                )
            X_live[feature] = st_widget

    return X_live


#############      #############      #############
#############      #############      #############
###                ###                ###       ###
###                ###                ###       ###
########           ########           #############
########           ########           #############
###                ###                ###       ###           #########
###                ###                ###        ###          ###   ###
###                #############      ###         ###         ###   ###
###                #############      ###         ###         #########