import streamlit as st
import pandas as pd
import numpy as np
import joblib


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_house_prices_data():
    df = pd.read_csv("outputs/dataset/housing_records.csv")
    return data


@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_house_data():
    df = pd.read_csv(
        "inputs/dataset/house-price/house-price/inherited_houses.csv")
    return data


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)