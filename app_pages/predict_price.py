import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_california_housing_data, load_pkl_file
from src.machine_learning.evaluate_regression import (
    regression_performance,
    regression_evaluation,
    regression_evaluation_plots
)

def page_predict_price_ml_body():

    # Load regression pipeline files
    vsn = 'v1'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_median_house_value/{vsn}/regression_pipeline.pkl"
    )
    sale_price_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_median_house_value/{vsn}/features_importance.png"
    )
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_median_house_value/{vsn}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_median_house_value/{vsn}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_median_house_value/{vsn}/y_train.csv").squeeze()
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_median_house_value/{vsn}/y_test.csv").squeeze()

    st.write("### ML Pipeline: Predict Median House Value")
    # Display pipeline training summary conclusions
    st.success(
        "A Regressor model was trained to predict the median house value in California. "
        "The initial data set contained 10 features. "
        "Feature engineering was carried out on the remaining data. "
        "The model was then tuned using a hyperparameter search and was "
        "found to "
        "**meet the project requirement** with an R2 Score of 0.8 or "
        "better on "
        "both train and test sets. The model identified the four most "
        "important features necessary to achieve the best predictive "
        "power. ")
    st.write("---")

    # Show pipeline steps
    st.write("### ML pipeline to predict median house value.")
    st.code(sale_price_pipe)
    st.write("---")

    # Show best features
    st.write("### The features the model was trained on and their importance.")
    st.write(X_train.columns.to_list())
    st.image(sale_price_feat_importance)

    st.write(
        "The model was ultimately trained on the following four features: \n"
        "* Median Income (median_income) \n"
        "* Total Rooms (total_rooms) \n"
        "* Total Bedrooms (total_bedrooms) \n"
        "* Housing Median Age (housing_median_age) \n"
    )
    st.write("---")

    # Evaluate performance on both sets
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test,
                           pipeline=sale_price_pipe)

    st.write("**Performance Plot**")
    regression_evaluation_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test,
                                y_test=y_test, pipeline=sale_price_pipe,
                                alpha_scatter=0.5)

# Load the California H