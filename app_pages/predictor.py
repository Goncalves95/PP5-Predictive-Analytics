import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from src.data_management import (
    load_house_prices_data,
    load_pkl_file,
    load_inherited_house_data)
from src.machine_learning.evaluate_regression import regression_performance
from src.machine_learning.predictive_analysis_ui import predict_price


def page_price_predictor_body():

    # load predict sale price files
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

    # Generate Live Data
    X_live = draw_inputs_widgets()

    # predict on live data
    if st.button("Run Predictive Analysis"):
        predict_sale_price(X_live, sale_price_features, sale_price_pipe)

    st.write("---")

    st.write("### Price prediction for the clients inherited properties:")
    in_df = load_inherited_house_data()
    in_df = in_df.filter(sale_price_features)

    st.write("* Features of Inherited Homes")
    st.write(in_df)

    if st.button("Run Prediction"):
        inherited_price_prediction = predict_sale_price(
            in_df, sale_price_features, sale_price_pipe)
        total_value = inherited_price_prediction.sum()
        total_value = float(total_value.round(1))
        total_value = '${:,.2f}'.format(total_value)

        st.write(f"* The total value is estimated"
                 f" to be:")
        st.write(f"**{total_value}**")


def draw_inputs_widgets():

    # load dataset
    df = load_house_prices_data()
    percentageMin, percentageMax = 0.2, 2.5

    # we create input widgets for the 4 best features
    col01, col02 = st.beta_columns(2)
    col03, col04 = st.beta_columns(2)

    # We are using these features to feed the ML pipeline -
    # create an empty DataFrame, which will be the live data
    X_live = pd.DataFrame([], index=[0])

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
            label='Total Basement SQFT',
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=20
        )
    X_live[feature] = st_widget

    with col03:
        feature = "2ndFlrSF"
        st_widget = st.number_input(
            label='2nd Floor SQFT',
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=20
        )
    X_live[feature] = st_widget

    with col04:
        feature = "GarageArea"
        st_widget = st.number_input(
            label="Garage Area SQFT",
            min_value=int(df[feature].min()*percentageMin),
            max_value=int(df[feature].max()*percentageMax),
            value=int(df[feature].median()),
            step=20
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