import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_prices_data():
    df = pd.read_csv("outputs/dataset/housing_records.csv")
    return df


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_house_data():
    df = pd.read_csv(
        "inputs/datasets/house-prices/house-price/inherited_houses.csv")
    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)