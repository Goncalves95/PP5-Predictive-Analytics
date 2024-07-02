import streamlit as st
import matplotlib.pyplot as plt


def home_page_body():
    """
    Displays contents of the project home page
    """
    
    image_main = plt.imread(f"images/ames_city.jpeg")
    image_isu = plt.imread(f"images/ames_university_city.jpeg")
    
    st.image(image_main, caption='Ames City')

    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Purpose and Motivation**\n\n"
        f"The primary purpose of this project is to provide a tool that enables"
        f" users to predict the potential sale price of a property in"
        f" Ames, Iowa, by providing detailed and relevant information about the"
        f" real estate in question.\n\n"
        f"Specifically, a client has requested this application to"
        f" estimate the sale price for several inherited properties in"
        f" Ames, Iowa. The client has supplied a publicly available dataset"
        f" which is used to train the machine learning model and"
        f" predict local real estate sale prices.\n\n"
        f"**Project Terminology**\n"
        f"* A **client** is a person who uses this service or product.\n"
        f"* The **sale price** is the estimated value of a home as it"
        f" might be realized in a typical and unencumbered real estate"
        f" transaction.\n"
        f"* The home whose value is being estimated may be referred to as"
        f" **property, real estate, house, or home**.\n"
        f"* The **features** or **attributes** of a home are the characteristics"
        f" used to describe the property.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset can be accessed at"
        f" [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data),"
        f" where it is hosted by Code Institute.\n"
        f"* The dataset represents a record of approximately 1500 real estate"
        f" sales in Ames, Iowa. Each record contains 23 features detailing"
        f" the house profile, such as Floor Area, Basement, Garage,"
        f" Kitchen, Lot,"
        f" Porch, Wood Deck, and Year Built. It also includes the Sale Price."
        f" The features are extensive, so please visit the site for more"
        f" information.")

    # copied from README file - "Business Requirements" section
    st.success(
        f"**Business Requirements**\n\n"
        f"The project has three main business requirements:\n"
        f"1. The client wants to understand the relationship"
        f" between a property's attributes/features and its sale price."
        f" Therefore, the client expects data visualizations that illustrate"
        f" the correlation between these variables and the sale prices.\n"
        f"2. The client is interested in predicting the potential sale prices"
        f" for properties in Ames, Iowa, with a specific focus on estimating the"
        f" value of the properties she has inherited.\n"
        f"3. The client would like to have easy access to the results through"
        f" an online application.")

    # Link to README file, so the users can have access to full
    # project documentation
    st.write(
        f"* For additional information about this project, please consult the"
        f" [README](https://github.com/Goncalves95/PP5-Predictive-Analytics/blob/main/README.md)"
        f" file on the project's GitHub page.\n"
        f"* This project was developed by Fernando Gonçalves. For study purposes"
        f" about the developer, visit her"
        f" [MyPortfolio](https://www.iamfernando.com).")
    
    #Map from the principal park on the city Ames
    d = {'lat': [42.035724], 'lon': [93.600002]}
    df_ames = pd.DataFrame(data=d)
    st.map(data=df_ames, zoom=15)

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