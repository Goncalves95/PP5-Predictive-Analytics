import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def home_page_body():
    """
    Displays contents of the project home page
    """

    image_main = plt.imread(f"images/ames_city.jpeg")
    image_isu = plt.imread(f"images/ames_university_city.jpeg")
    
    st.image(image_main, caption='Ames City')

    st.write("Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Welcome to Ames Housing Price Predictor!**\n\n"
        f"This project aims to provide a tool that enables users to predict the potential sale price of a property in Ames, Iowa.\n\n"
        f"Our client has requested this application to estimate the sale price for several inherited properties in Ames, Iowa.\n\n"
        f"**Key Terms**\n"
        f"* **Client**: A person who uses this service or product.\n"
        f"* **Sale Price**: The estimated value of a home as it might be realized in a typical and unencumbered real estate transaction.\n"
        f"* **Property**: The home whose value is being estimated.\n"
        f"* **Features**: The characteristics used to describe the property.\n\n"
        f"**Dataset**\n"
        f"* The dataset can be accessed at [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data).\n"
        f"* The dataset represents a record of approximately 1500 real estate sales in Ames, Iowa."
    )

    # copied from README file - "Business Requirements" section
    st.success(
        f"**Project Objectives**\n\n"
        f"Our project has three main objectives:\n"
        f"1. To understand the relationship between a property's attributes and its sale price.\n"
        f"2. To predict the potential sale prices for properties in Ames, Iowa.\n"
        f"3. To provide easy access to the results through an online application.",
    )

    # Link to README file, so the users can have access to full
    # project documentation
    st.write(
        f"* For additional information about this project, please consult the"
        f" [README](https://github.com/Goncalves95/PP5-Predictive-Analytics/blob/main/README.md)"
        f" file on the project's GitHub page.\n"
        f"* This project was developed by Fernando Gonçalves. For study purposes"
        f" about the developer, visit her"
        f" [MyPortfolio](https://www.iamfernando.com).")
    

    st.image(image_isu, caption='Ames, Iowa, USA.')


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