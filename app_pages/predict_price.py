import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data import load_house_prices_data, load_pkl_file
from src.ml.evaluate_regression import (
    regression_performance,
    regression_evaluation,
    regression_evaluation_plots)


def page_predict_price_ml_body():

    # load regression pipeline files
    vsn = 'v2'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_price/{vsn}/regression_pipeline.pkl"
    )
    sale_price_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_price/{vsn}/features_importance.png"
    )
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{vsn}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{vsn}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{vsn}/y_train.csv").squeeze()
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_price/{vsn}/y_test.csv").squeeze()

    st.write("### ML Pipeline: Predict Property Sale Price")
    # display pipeline training summary conclusions
    st.success(
        f"A Regressor model was trained to predict property sale prices in Ames, Iowa. "
        f"The dataset initially had 23 features with 'SalePrice' as the target. "
        f"After dropping two features with significant missing data, "
        f"feature engineering was applied to the remaining data. "
        f"The model was tuned via hyperparameter search, achieving an R2 Score of 0.8 or better "
        f"on both train and test sets. "
        f"Four crucial features were identified for optimal predictive power."
)
    st.write("---")

    # show pipeline steps
    st.write("### ML pipeline to predict property sale prices.")
    st.code(sale_price_pipe)
    st.write("---")

    # show best features
    st.write("### The features the model was trained on and their importance.")
    st.write(X_train.columns.to_list())
    st.image(sale_price_feat_importance)

    st.write(
        f"The model was ultimately trained on  the following four features: \n"
        f"* Overall Quality (OverallQual) \n"
        f"* Total Basement Area in squarefeet (TotalBsmtSF) \n"
        f"* 2nd Floor Area in squarefeet (2ndFlrSF) \n"
        f"* Garage Area in squarefeet (GarageArea) \n"
    )
    st.write("---")

    # evaluate performance on both sets
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test,
                           pipeline=sale_price_pipe)

    st.write("**Performance Plot**")
    regression_evaluation_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test,
                                y_test=y_test, pipeline=sale_price_pipe,
                                alpha_scatter=0.5)



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