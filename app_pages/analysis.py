import plotly.express as px
import numpy as np
import streamlit as st
from src.data_management import load_house_prices_data
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
sns.set_style("whitegrid")


def page_analysis_body():

    # load data
    df = load_house_prices_data()
    # The variable most strongly correlated with Sale Price/target
    vars_to_study = ['OverallQual', 'GrLivArea',
                     'GarageArea', 'TotalBsmtSF', 'YearBuilt', '1stFlrSF']

    st.write("### Property Sale Price Analysis")
    st.success(
        f"* The client is interested in understanding the correlation "
        f" between a property's attributes/features and the sale price."
        f" Therefore, the client expects data visualization of the correlated"
        f" variables against the sale prices for illustration "
        f" (Business Requirement 1), \n"
    )

    # inspect data
    if st.checkbox("Inspect Sale Price Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")
        st.write(df.head(10))
        st.write(
            f"**Information on Categorical Features**\n\n"
            f"* Basement Exposure: Gd - Good Exposure, Av - Average Exposure, "
            f" Mn - Minimum Exposure, "
            f" No - No Exposure, None - No Basement.\n\n"
            f"* Basement Finish Type: GLQ - Good Living Quarters, ALQ - "
            f" Average"
            f" Living Quarters, BLQ - Below Average Living Quarters, REC - "
            f" Average Rec Room, LwQ - Low  Quality, Unf - Unfinished, None - "
            f" No Basement.\n\n"
            f"* Garage Finish: Fin - Finished, RFn - Rough Finish, "
            f" Unf - Unfinished, None - No Garage.\n\n"
            f"* Kitchen Quality: Ex - Excellent, Gd - Good, TA - "
            f" Typical/Average, Fa - Fair, Po - Poor.\n\n"
            f"* Overall Condition: 1 - Very Poor to 10 - Very Excellent.\n\n"
            f"* Overall Quality: 1 - Very Poor to 10 - Very Excellent.\n\n"
        )

    st.write("---")

    st.write("### Correlation Study")
    # Correlation Study Summary
    st.write(
        f"A correlation study was conducted to understand the variables' relationship "
        f"with Sale Price. Below, heatmaps display results from Pearson and Spearman correlations. "
        f"The most correlated features with Sale Price are highlighted in a bar plot: **{vars_to_study}**. "
        f"Additionally, scatterplots illustrate these variables' correlation with Sale Price.")

    st.info(
        f"*** Heatmap and Barplot: Pearson Correlation ***\n\n"
        f"The Pearson Correlation evaluates linear relationships between continuous variables, "
        f"indicating how closely their relationship can be represented by a straight line.\n"
        f"The heatmap identifies variables with a linear correlation to Sale Price exceeding 0.6, "
        f"with these variables depicted in a separate bar plot.")

    if st.checkbox("Pearson Correlation"):
        calc_display_pearson_corr_heat(df)
        calc_display_pearson_corr_bar(df)

    st.info(
        f"*** Heatmap and Barplot: Spearman Correlation ***\n\n"
        f"Spearman correlation evaluates monotonic relationships, where variables "
        f"move together but not necessarily linearly.\n"
        f"Similar to the Pearson heatmap, variables on the x-axis with a correlation "
        f"of 0.6 or higher with Sale Price are displayed in a corresponding bar plot.")

    if st.checkbox("Spearman Correlation"):
        calc_display_spearman_corr_heat(df)
        calc_display_spearman_corr_bar(df)

    st.info(
        f"*** Correlation Histograms and Scatterplots ***\n\n"
        f"The correlation analysis highlights the variables most strongly correlated with Sale Price:\n"
        f"- Overall Quality (OverallQual): Sale Price tends to increase with higher overall quality.\n"
        f"- Ground Level Living Area (GrLivArea): Sale Price tends to increase with larger living area.\n"
        f"- Garage Area (GarageArea): Sale Price tends to increase with larger garage area.\n"
        f"- Total Basement Area (TotalBsmtSF): Sale Price tends to increase with larger basement area.\n"
        f"- Year Built (YearBuilt): Sale Price tends to increase with newer construction.\n"
        f"- 1st Floor Square Footage (1stFlrSF): Sale Price tends to increase with larger first floor area.\n\n"
        f"The scatterplots below illustrate these correlations. A two-dimensional histogram shows data trends "
        f"and concentration, with darker areas indicating higher data density. Scatterplots color-coded by "
        f"Overall Quality further illustrate how higher quality corresponds to higher Sale Price across all plots.")

    # Correlation plots adapted from the Data Cleaning Notebook
    if st.checkbox("Correlation Plots of Variables vs Sale Price"):
        correlation_to_sale_price_hist_scat(df, vars_to_study)

    st.info(
        f"*** Heatmap and Barplot: Predictive Power Score (PPS) ***\n\n"
        f"The Predictive Power Score (PPS) identifies linear or non-linear relationships "
        f"between variables. Scores range from 0 (no predictive power) to 1 (perfect predictive power).\n"
        f"To interpret the plot, locate 'SalePrice' on the y-axis and follow across the row to "
        f"identify variables on the x-axis with a PPS greater than 0.15. 'Overall Quality (OverallQual)' "
        f"exhibits the highest predictive power for Sale Price.")

    if st.checkbox("Predictive Power Score"):
        calc_display_pps_matrix(df)


def correlation_to_sale_price_hist_scat(df, vars_to_study):
    """ Display correlation plot between variables and sale price """
    target_var = 'SalePrice'
    for col in vars_to_study:
        fig, axes = plt.subplots(figsize=(8, 5))
        axes = sns.histplot(data=df, x=col, y=target_var)
        plt.title(f"{col}", fontsize=20, y=1.05)
        st.pyplot(fig)
        st.write("\n\n")

        fig, axes = plt.subplots(figsize=(8, 5))
        axes = sns.scatterplot(data=df, x=col, y=target_var, hue='OverallQual')
        # plt.xticks(rotation=90)
        plt.title(f"{col}", fontsize=20, y=1.05)
        st.pyplot(fig)
        st.write("\n\n")


def calc_display_pearson_corr_heat(df):
    """ Calcuate and display Pearson Correlation """
    df_corr_pearson = df.corr(method="pearson")
    heatmap_corr(df=df_corr_pearson, threshold=0.6,
                 figsize=(12, 10), font_annot=10)


def calc_display_spearman_corr_heat(df):
    """ Calcuate and display Spearman Correlation """
    df_corr_spearman = df.corr(method="spearman")
    heatmap_corr(df=df_corr_spearman, threshold=0.6,
                 figsize=(12, 10), font_annot=10)


def calc_display_pearson_corr_bar(df):
    """ Calcuate and display Pearson Correlation """
    corr_pearson = df.corr(method='pearson')['SalePrice'].sort_values(
        key=abs, ascending=False)[1:]
    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=corr_pearson[:5].index, height=corr_pearson[:5])
    plt.title("Pearson Correlation with Sale Price", fontsize=15, y=1.05)
    st.pyplot(fig)


def calc_display_spearman_corr_bar(df):
    """ Calcuate and display Spearman Correlation """
    corr_spearman = df.corr(method='spearman')['SalePrice'].sort_values(
        key=abs, ascending=False)[1:]
    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=corr_spearman[:5].index, height=corr_spearman[:5])
    plt.title("Spearman Correlation with Sale Price", fontsize=15, y=1.05)
    st.pyplot(fig)


def calc_display_pps_matrix(df):
    """ Calcuate and display Predictive Power Score """
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(
        columns='x', index='y', values='ppscore')
    heatmap_pps(df=pps_matrix, threshold=0.15, figsize=(12, 10), font_annot=10)

    pps_topscores = pps_matrix.iloc[19].sort_values(
        key=abs, ascending=False)[1:6]

    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=pps_topscores.index, height=pps_topscores)
    plt.xticks(rotation=90)
    plt.title("Predictive Power Score for Sale Price", fontsize=15, y=1.05)
    st.pyplot(fig)


def heatmap_corr(df, threshold, figsize=(20, 12), font_annot=8):
    """ Heatmap for correlations from CI template"""
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[np.triu_indices_from(mask)] = True
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        axes = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                           mask=mask, cmap='viridis',
                           annot_kws={"size": font_annot},
                           ax=axes, linewidth=0.5
                           )
        axes.set_yticklabels(df.columns, rotation=0)
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    """ Heatmap for predictive power score from CI template"""
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        axes = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                           mask=mask, cmap='rocket_r',
                           annot_kws={"size": font_annot},
                           linewidth=0.05, linecolor='grey')
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)

# some learned from (https://github.com/8080labs/ppscore)


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