import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from src.data import (load_house_prices_data, load_pkl_file, load_inherited_house_data)
from src.ml.evaluate_regression import regression_performance
from src.ml.predictive import predict_price

# Constants
MIN_PERCENTAGE = 0.2
MAX_PERCENTAGE = 2.5
MIN_OVERALL_QUALITY = 1
MAX_OVERALL_QUALITY = 10
MEDIAN_STEP = 20


def page_price_predictor_body():
    """
    Main function to generate the price predictor interface
    """
    sale_price_pipe, sale_price_features = load_predict_sale_price_files()
    display_interface()
    x_live = generate_live_data(sale_price_features)
    predict_sale_price(x_live, sale_price_features, sale_price_pipe)
    display_inherited_properties(sale_price_features, sale_price_pipe, x_live)


def load_predict_sale_price_files():
    """
    Load the sale price pipeline and features from files
    """
    vsn = 'v2'
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
    """
    Display the sale price predictor interface
    """
    st.write("### Sale Price Predictor Interface")
    st.success(
        f"* The client is interested in predicting the potential sale prices"
        f" for properties in Ames, Iowa, and specifically, she wants to"
        f" determine a potential value for the properties she inherited."
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


def generate_live_data(sale_price_features):
    """
    Generate live data for the price predictor
    """
    X_live = draw_inputs_widgets(sale_price_features)
    return X_live


def predict_sale_price(x_live, sale_price_features, sale_price_pipe):
    print("X_live shape:", x_live.shape)
    print("sale_price_features:", sale_price_features)
    
    # Re-order the columns to match the order in sale_price_features
    x_live = x_live[sale_price_features]
    
    # Verify the shape
    print(x_live.shape)
    
    if st.button("Run Predictive Analysis"):
        prediction = predict_price(x_live, sale_price_features, sale_price_pipe)
        # Check the type and value of prediction
        print("Prediction:", prediction)
        
        # Ensure prediction is numeric and format it as a float with two decimal places
        if isinstance(prediction, (int, float)):
            st.write(f"* The predicted sale price is: **${prediction:.2f}**")
        else:
            st.write(f"* The predicted sale price could not be determined.")


def display_inherited_properties(sale_price_features, sale_price_pipe, x_live):
    """
    Display the price prediction for the client's inherited properties
    """
    st.write("### Price prediction for the client's inherited properties:")
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


def draw_inputs_widgets(sale_price_features):
    """
    Draw the input widgets for the price predictor
    """
    # Load the house prices dataset
    df = load_house_prices_data()

    # Set the minimum and maximum percentage values for the input widgets
    percentageMin, percentageMax = 0.2, 2.5

    # Create four columns to organize the input widgets
    col01, col02 = st.beta_columns(2)
    col03, col04 = st.beta_columns(2)

    # Create an empty DataFrame to store the live input data
    X_live = pd.DataFrame([], index=[0], columns=sale_price_features)

    # Create input widgets for four features
    with col01:
        feature = "OverallQual"
        st_widget = st.number_input(
            label='Overall Quality',
            min_value=1,
            max_value=10,
            value=int(df[feature].median()),
            step=1
        )
        X_live[feature] = st_widget

    with col02:
        feature = "TotalBsmtSF"
        st_widget = st.number_input(
            label='Total Basement Square',
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=20
        )
        X_live[feature] = st_widget

    with col03:
        feature = "2ndFlrSF"
        st_widget = st.number_input(
            label='2nd Floor Square',
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=20
        )
        X_live[feature] = st_widget

    with col04:
        feature = "GarageArea"
        st_widget = st.number_input(
            label="Garage Area Square",
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=20
        )
        X_live[feature] = st_widget

    # Fill missing columns with default values (median or 0)
    for col in sale_price_features:
        if col not in X_live.columns:
            if col in df.columns:
                X_live[col] = df[col].median()
            else:
                X_live[col] = 0

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