import streamlit as st

def page_project_hypothesis_body():
    st.write("### Heritage Housing Ames, USA Hypotheses and Validation")

    # Hypothesis 1
    st.success(
        f"**H1 - The overall quality (OverallQual) of a property significantly impacts its sale price in Ames, Iowa.**\n"
        f"* **Correct.** From the feature importance analysis and correlation studies, we found that OverallQual has a strong positive correlation with Sale Price.\n\n"
    )

    # Hypothesis 2
    st.success(
        f"**H2 - Properties with larger ground-level living areas (GrLivArea) tend to command higher sale prices in Ames, Iowa.**\n"
        f"* **Correct.** Our analysis revealed a strong positive correlation between GrLivArea and Sale Price, indicating that larger living areas are associated with higher sale prices.\n\n"
    )

    # Hypothesis 3
    st.success(
        f"**H3 - The age of a property (YearBuilt) influences its sale price, with newer constructions generally commanding higher prices in Ames, Iowa.**\n"
        f"* **Correct.** Our trend analysis and regression models showed that YearBuilt has a significant positive impact on Sale Price, with newer properties tend to have higher sale prices.\n"
    )
