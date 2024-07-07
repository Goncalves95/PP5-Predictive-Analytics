import streamlit as st

def page_project_hypothesis_body():
    st.write("### Ames Housing Price Predictor Hypotheses and Validation")

    # Hypothesis 1
    st.success(
        f"**H1 - The primary purpose of this project is to provide a tool that enables users to predict the potential sale price of a property in Ames, Iowa.**\n"
        f"* **Correct.** From the project's purpose and motivation, we found that the client wants to estimate the sale price for several inherited properties in Ames, Iowa, USA.\n\n"
    )

    # Hypothesis 2
    st.success(
        f"**H2 - The project's dataset represents a record of approximately 1500 real estate sales in Ames, Iowa.**\n"
        f"* **Correct.** We validated this hypothesis by accessing the dataset at Kaggle, where it is hosted by Code Institute.\n\n"
    )

    # Hypothesis 3
    st.success(
        f"**H3 - The client wants to understand the relationship between a property's attributes/features and its sale price.**\n"
        f"* **Correct.** We found that the client expects data visualizations that illustrate the correlation between these variables and the sale prices.\n"
    )