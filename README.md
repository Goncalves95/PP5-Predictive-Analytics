# :earth_americas: **Heritage Housing Ames, USA** :house_with_garden:
 
![Heritage Housing Ames](assets/images/ames-iowa-skyline-com-construções-da-cor-e-o-céu-azul-100932701.jpg)

Come and see the [Live App](https://heritage-housing-fernando-74a4ebdc845a.herokuapp.com/#heritage-housing-ames-usa)

## Table of Contents

- [:earth\_americas: **Heritage Housing Ames, USA** :house\_with\_garden:](#earth_americas-heritage-housing-ames-usa-house_with_garden)
  - [Table of Contents](#table-of-contents)
  - [:round\_pushpin: Objectives and Goals](#round_pushpin-objectives-and-goals)
  - [:book: History](#book-history)
  - [:floppy\_disk: Dataset Content](#floppy_disk-dataset-content)
  - [:bookmark: Business Requirements](#bookmark-business-requirements)
  - [:white\_check\_mark: Hypothesis and how to validate?](#white_check_mark-hypothesis-and-how-to-validate)
  - [:open\_file\_folder: ML Business Case](#open_file_folder-ml-business-case)
  - [:outbox\_tray: User Storys](#outbox_tray-user-storys)
  - [:clipboard: Dashboard Design](#clipboard-dashboard-design)
    - [Home Page](#home-page)
    - [Predict Price Page](#predict-price-page)
    - [Property Sale Price Analysis Page](#property-sale-price-analysis-page)
    - [Price Predictor Interface Page](#price-predictor-interface-page)
  - [:bug: Unfixed Bugs](#bug-unfixed-bugs)
  - [:triangular\_ruler: PEP8 Compliance Testing](#triangular_ruler-pep8-compliance-testing)
  - [:mortar\_board: Future Work](#mortar_board-future-work)
  - [:crystal\_ball: Deployment](#crystal_ball-deployment)
    - [Heroku](#heroku)
  - [:computer: Technologies](#computer-technologies)
    - [Development and Deployment](#development-and-deployment)
    - [Data Analysis and Machine Learning](#data-analysis-and-machine-learning)
  - [:mega: Credits](#mega-credits)
    - [Sources of code](#sources-of-code)
    - [Media](#media)
  - [:mega: Acknowledgements](#mega-acknowledgements)

## :round_pushpin: Objectives and Goals

The Heritage Housing Ames project aims to provide a valuable tool for individuals looking to sell their houses in Ames, Iowa. The main objectives and goals of this project are:

Develop a machine learning model to predict the sale price of properties in Ames, Iowa, based on various features such as overall quality, basement area, garage area, and more.
Create a user-friendly interface for users to input their property features and receive a predicted sale price, helping them to set a competitive price for their property.
Analyze the relationship between property features and sale prices, providing insights and recommendations for users to make informed decisions about buying or selling properties.
Assist homeowners in understanding the value of their property and making data-driven decisions to maximize their sale price.

## :book: History

The Heritage Housing Ames project was inspired by a client who inherited several properties in Ames, Iowa, and was looking for a way to estimate their sale prices. With a lack of knowledge about the local real estate market, the client was struggling to determine the value of their properties. This project aims to provide a solution to this problem by developing a machine learning model that can predict sale prices based on various property features.

## :floppy_disk: Dataset Content

The primary purpose of this project is to provide a tool that enables users to predict the potential sale price of a property in Ames, Iowa, by providing detailed and relevant information about the" real estate in question.
Specifically, a client has requested this application to estimate the sale price for several inherited properties in Ames, Iowa. The client has supplied a publicly available dataset which is used to train the machine learning model and predict local real estate sale prices.

**Project Terminology**
* A **client** is a person who uses this service or product.
* The **sale price** is the estimated value of a home as it might be realized in a typical and unencumbered real estate transaction.
* The home whose value is being estimated may be referred to as **property, real estate, house, or home**.
* The **features** or **attributes** of a home are the characteristics used to describe the property.

**Project Dataset**
* The dataset can be accessed at [Kaggle](https://www.kaggle.com/datasets/codeinstitute/housing-prices-data), where it is hosted by Code Institute.\n
* The dataset represents a record of approximately 1500 real estate sales in Ames, Iowa. Each record contains 23 features detailing the house profile, such as Floor Area, Basement, Garage, Kitchen, Lot, Wood Deck, and Year Built. It also includes the Sale Price. The features are extensive.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## :bookmark: Business Requirements

The project has three main business requirements:

1. The client wants to understand the relationship between a property's attributes/features and its sale price.
Therefore, the client expects data visualizations that illustrate the correlation between these variables and the sale prices.

2. The client is interested in predicting the potential sale prices for properties in Ames, Iowa, with a specific focus on estimating the value of the properties she has inherited.

3. The client would like to have easy access to the results through an online application.

## :white_check_mark: Hypothesis and how to validate?

1. Hypothesis 1: The overall quality (OverallQual) of a property significantly impacts its sale price in Ames, Iowa.

    - Feature Importance: Utilize feature importance analysis from machine learning models (e.g., Random Forest Regression) to quantify the impact of OverallQual on predicting sale prices.
    - Correlation Analysis: Conduct correlation studies (Pearson, Spearman) to validate the strength and direction of the relationship between OverallQual and Sale Price.
    - Visualization: Create scatterplots and regression plots to visually inspect how changes in OverallQual correspond to changes in Sale Price.

2. Hypothesis 2: Properties with larger ground-level living areas (GrLivArea) tend to command higher sale prices in Ames, Iowa.

    - Correlation Analysis: Use statistical measures (Pearson, Spearman) to assess the correlation between GrLivArea and Sale Price.
    - Visual Examination: Plot histograms and scatterplots to visualize the distribution and relationship between GrLivArea and Sale Price.
    - Model Insights: Extract insights from regression model coefficients and feature importance scores to understand GrLivArea's impact on predicting Sale Price.

3. Hypothesis 3: The age of a property (YearBuilt) influences its sale price, with newer constructions generally commanding higher prices in Ames, Iowa.

    - Trend Analysis: Analyze trends over time by plotting Sale Price against YearBuilt.
    - Descriptive Statistics: Calculate summary statistics and trends to identify any patterns or anomalies related to property age and sale prices.
    - Machine Learning Model Analysis: Use regression models to quantify the predictive power of YearBuilt on Sale Price, considering potential nonlinear relationships.

## :open_file_folder: ML Business Case

- The project addresses the need to predict property sale prices for inherited properties in Ames, Iowa, leveraging machine learning to support informed decision-making and financial planning.

    Objectives:

    Prediction Task: Develop a regression model to estimate sale prices based on property features like overall quality, basement area, second floor area, and garage area.
    Client Needs: Enable the client to understand and evaluate the financial implications of inherited properties for potential sale.
    Methodology:

    1. Data Preparation: Cleaned and preprocessed a dataset of Ames real estate transactions, handling missing values and engineering relevant features.

    2. Model Selection: Implemented regression models including Linear Regression and Random Forest Regression, optimizing for accuracy and interpretability.

    3. Model Evaluation: Evaluated models using metrics such as R-squared, Mean Squared Error (MSE), and Root Mean Squared Error (RMSE), ensuring robust performance.

    4. Deployment: Developed a user-friendly interface using Streamlit for the client to input property features and obtain predicted sale prices in real-time.

    Business Value:

    Informed Decisions: Provides accurate predictions to support strategic decisions on managing and selling inherited properties.
    Financial Planning: Facilitates financial planning by estimating property values and potential sale proceeds.
    Operational Efficiency: Enhances efficiency by leveraging data-driven insights to streamline decision-making processes.

## :outbox_tray: User Storys

- SOME USER STORYS:

**User Story 1** As a client, I want to be able to input the features of a property (e.g. Overall Quality, Total Basement Area, 2nd Floor Area, Garage Area) so that I can get an estimated sale price for the property.

**User Story 2** As a client, I want to visualize the correlation between different property features and sale prices so that I can better understand which features have the most impact on sale prices.

**User Story 3** As a client, I want to be able to predict the total value of my inherited properties in Ames, Iowa so that I can make informed decisions about selling or holding onto them.

**User Story 4** As a client, I want to have access to an online application that allows me to easily input property features and get estimated sale prices so that I can quickly and easily evaluate different properties.

**User Story 5** As a client, I want to be able to view a summary of the machine learning pipeline used to predict sale prices so that I can understand the methodology behind the predictions and have confidence in the results.

## :clipboard: Dashboard Design

### Home Page

Content:

Image Display

Purpose: Visual representation of Ames City and Iowa State University.
Details: Display images (ames_city.jpeg and ames_university_city.jpeg) using st.image.
Project Summary

Purpose: Provide an overview of the project's goals and dataset information.
Details:
Uses st.write and st.info to present project purpose, motivation, terminology, and dataset details.
Describes the dataset sourced from Kaggle, containing features related to real estate in Ames, Iowa.
Provides links to the Kaggle dataset and GitHub README file for more information.
Business Requirements

Purpose: Outline the primary business requirements of the project.
Details:
Presented with st.success to highlight three main requirements:
Understanding the relationship between property features and sale price.
Predicting sale prices for properties in Ames, Iowa, especially inherited ones.
Providing easy access to results via an online application.
Additional Information

Purpose: Offer access to further project documentation and developer information.
Details:
Provides links to the GitHub README file for comprehensive project details.
Includes a link to the developer's portfolio for more about the developer, Fernando Gonçalves.
Widgets and Interaction:

This page primarily consists of static content displayed using Streamlit's st.image, st.write, and st.info functions.
Links provided enable users to access external resources for deeper understanding and engagement.
Future Updates:

Consider integrating interactive elements such as buttons or dropdowns for enhanced user interaction.
Update visual content based on user feedback or additional project developments.

### Project Hypothesis Page

This page provides insights and validation for the hypotheses related to the Heritage Housing Ames project. It includes:

- Hypothesis 1: The overall quality (OverallQual) of a property significantly impacts its sale price in Ames, Iowa.
  - Validation: Confirmed. The feature importance analysis and correlation studies show a strong positive correlation between OverallQual and Sale Price.

- Hypothesis 2: Properties with larger ground-level living areas (GrLivArea) tend to command higher sale prices in Ames, Iowa.
  - Validation: Confirmed. Analysis reveals a strong positive correlation between GrLivArea and Sale Price, indicating larger living areas are associated with higher sale prices.

- Hypothesis 3: The age of a property (YearBuilt) influences its sale price, with newer constructions generally commanding higher prices in Ames, Iowa.
  - Validation: Confirmed. Trend analysis and regression models demonstrate that YearBuilt has a significant positive impact on Sale Price, with newer properties tending to have higher sale prices.

### Predict Price Page

Content:

ML Pipeline Summary

Purpose: Overview of the machine learning pipeline used to predict property sale prices.
Details:
Utilizes st.success to summarize the training process:
Model trained on 23 initial features with 'SalePrice' as the target.
Two features dropped due to significant missing data; remaining data underwent feature engineering.
Hyperparameter tuning resulted in achieving an R2 Score of 0.8 or higher on both train and test sets.
Highlights four crucial features for predictive power.
ML Pipeline Details

Purpose: Display details of the trained machine learning pipeline.
Details:
Uses st.code to showcase the Python code of the regression pipeline (sale_price_pipe).
Provides transparency into the pipeline's configuration and steps.
Feature Importance

Purpose: Showcases the importance of features used in the model.
Details:
Displays the list of features (X_train.columns.to_list()) and their importance through an image (sale_price_feat_importance).
Specifies the top four features the model was ultimately trained on, emphasizing their significance.
Pipeline Performance

Purpose: Evaluates and visualizes the performance of the trained pipeline.
Details:
Utilizes regression_performance to display performance metrics on both training and test sets.
Includes a performance plot (regression_evaluation_plots) to visualize predicted versus actual sale prices.
Widgets and Interaction:

This page primarily presents static content with summary information, pipeline code, feature importance visuals, and performance metrics.
Visual plots provide interactive elements to view performance trends and model predictions.
Future Updates:

Consider integrating more interactive elements such as sliders or dropdowns for users to explore different aspects of model performance.
Enhance visualization techniques based on user feedback or further developments in data analysis techniques.

### Property Sale Price Analysis Page
Content:

Project Background and Client Expectations

Purpose: Provides an overview of the project goals and client expectations related to understanding property attributes' correlation with sale prices.
Details:
Uses st.success to summarize the client's interest in visualizing the correlation between property features and sale prices.
Highlights Business Requirement 1: Visualization of correlated variables against sale prices.
Data Inspection

Purpose: Allows users to inspect the dataset.
Details:
Uses st.checkbox to optionally display the dataset's basic information (number of rows, columns, and first 10 rows).
Provides information on categorical features related to basement exposure, finish type, garage finish, kitchen quality, overall condition, and overall quality.
Correlation Study

Purpose: Conducts a correlation study to analyze relationships between variables and sale prices.
Details:
Uses heatmaps to display Pearson and Spearman correlation results.
Highlights the most correlated features (OverallQual, GrLivArea, GarageArea, TotalBsmtSF, YearBuilt, 1stFlrSF) with Sale Price through bar plots.
Provides scatterplots to visually depict the correlation of these variables with Sale Price.
Predictive Power Score (PPS)

Purpose: Utilizes PPS to identify predictive relationships between variables.
Details:
Displays a heatmap of PPS scores, indicating linear or non-linear relationships between variables and Sale Price.
Shows a bar plot of top predictive scores for Sale Price.
Widgets and Interaction:

Checkbox: Allows users to toggle visibility of dataset information and correlation plots.
Histograms and Scatterplots: Visualize correlations between variables (OverallQual, GrLivArea, etc.) and Sale Price, with histograms showing data distribution and scatterplots highlighting trends.
Future Updates:

Consider enhancing user interaction with more dynamic features like sliders for threshold adjustments in correlation heatmaps.
Incorporate tooltips or hover-over descriptions in plots to provide detailed insights.
Explore interactive features to filter data based on specific criteria or variable selections dynamically.

### Price Predictor Interface Page

The Price Predictor Interface page in your Streamlit dashboard is designed to predict the potential sale prices of properties in Ames, Iowa, focusing specifically on properties inherited by the client. Here’s a breakdown of the page content and functionality:

Content and Features:

Project Background and Client Expectations

Purpose: Provides an overview of the client's interest in predicting sale prices for inherited properties.
Details:
Uses st.success to highlight Business Requirement 2: Predicting sale prices for inherited properties.
Provides information on the key features used in prediction and their importance as determined by the machine learning model.
Mentions the alignment of these features with the initially identified correlated variables from the data analysis.
Input Features for Prediction

Purpose: Allows users (the client) to input specific property features for prediction.
Details:
Uses draw_inputs_widgets function to generate input widgets for four key features: Overall Quality, Total Basement Area, 2nd Floor Area, and Garage Area.
Each widget is designed as a number input field with defined minimum and maximum values, step sizes, and default values based on the dataset statistics.
Prediction Execution

Purpose: Executes the prediction based on user-input features.
Details:
Provides a button (Run Predictive Analysis) to trigger the prediction process using the machine learning pipeline (sale_price_pipe).
Upon button press, calls the predict_sale_price function to predict the sale price using the provided features.
Displays the predicted sale prices or relevant insights based on the prediction results.
Inherited Properties Prediction

Purpose: Predicts the total value of inherited properties.
Details:
Displays the features of inherited properties fetched using load_inherited_house_data() and filtered to match the features used in prediction (sale_price_features).
Provides a button (Run Prediction) to initiate the prediction process for inherited properties.
Computes the total estimated value based on the predicted sale prices of inherited properties and formats the output as a monetary value.
Widgets and Interaction:

Number Input Fields: Allow users to input values for Overall Quality, Total Basement Area, 2nd Floor Area, and Garage Area.
Buttons: Trigger actions such as running predictive analysis and displaying prediction results.
Data Loading: Utilizes functions from src.data to load datasets necessary for prediction and analysis.
Future Enhancements:

Consider incorporating error handling for invalid inputs or edge cases.
Implement interactive visualizations or charts to complement prediction results.
Provide additional insights or recommendations based on predicted sale prices.

## :bug: Unfixed Bugs

The app does not currently contain any unfixed bugs.

## :triangular_ruler: PEP8 Compliance Testing

All python files where passed through the [CI Python Linter](https://pep8ci.herokuapp.com/). 
Those files incuded the `app_pages` files. The small errors like trailing white spaces was fixes, and appear few small errors to such as long lines and too many leading '#' for block comment (because my sign name).

## :mortar_board: Future Work

While the Heritage Housing Ames project has achieved its primary objectives, there are several areas for further research and improvement:

Integrate additional data sources: Incorporating data from other sources, such as local economic indicators, weather patterns, or crime rates, could improve the accuracy of the sale price predictions.
Expand to other regions: The model could be adapted to predict sale prices in other regions or cities, providing a more comprehensive solution for homeowners and real estate agents.
Improve model interpretability: Developing techniques to explain the predictions made by the model could provide users with a better understanding of how the property features contribute to the predicted sale price.
Enhance user interface: Further development of the user interface could include features such as interactive visualizations, personalized recommendations, or integration with popular real estate platforms.
Investigate alternative machine learning approaches: Exploring other machine learning algorithms or techniques, such as deep learning or ensemble methods, could lead to improved prediction accuracy or more robust models.

## :crystal_ball: Deployment

### Heroku

- The App live link is: <https://heritage-housing-uriem-381968c86628.herokuapp.com>
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## :computer: Technologies

### Development and Deployment

- [GitHub](https://github.com/) was used to create the project repository, story project files and record commits.
- [Code Anywhere](https://codeanywhere.com/) was used as the development environment.
- [Streamlit](https://streamlit.io/) was used to develop the online app interface.
- [Jupyter Notebooks](https://jupyter.org/) were used to analyse and engineer the data, and develop and evaluate the model pipeline.
- [Heroku](https://www.heroku.com/) was used to deploy the project.
- [Kaggle](https://www.kaggle.com/) was used to access the dataset


### Data Analysis and Machine Learning

- [NumPy](https://numpy.org/) was used for mathematical operations for examples determining means, modes, and standard deviations.
- [Feature Engine](https://feature-engine.trainindata.com/en/latest/index.html) was used for various data cleaning and preparation tasks.
- [SciKit Learn](https://scikit-learn.org/stable/) was used for many machine learning tasks.
- [Pandas](https://pandas.pydata.org/) was used for reading and writing data files, inspecting, creating and manipulating series and dataframes.
- [ydata_profiling](https://ydata-profiling.ydata.ai/docs/master/index.html) was used to create an extensive Profile Report of the dataset.
- [PPScore](https://pypi.org/project/ppscore/) was used to determine the predictive power score of the data features.
- [MatPlotLib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) were used for constructing plots to visualize the data analysis.

## :mega: Credits

### Sources of code

- The CI Churnometer Walkthrough Project and the CI course content was used to source various functions and classes in the development process.
- The CI Churnometer Walkthrough Project was also the source of the Steamlit pages which were then modified and adapted to the app deployed in this project.

### Media

- The images of Iowa State University was taken from [Niche.com](https://www.niche.com/colleges/iowa-state-university/)
- The Ames images was taken from [dreamstime.com](https://pt.dreamstime.com/ames-iowa-skyline-com-as-constru%C3%A7%C3%B5es-da-cor-isoladas-em-backgro-branco-image101534629)

## :mega: Acknowledgements

Thanks and appreciation go to the following sources and people:

- Several past projects provided valuable additional information on how to complete a successful project:
- Setup of widgest learned with t-hullis[Link](https://github.com/t-hullis/milestone-project-heritage-housing-issues/tree/main)
- Learning more with Data Professor for building web aplications data sets [Link](https://www.youtube.com/@DataProfessor)
- Lear building app with NeuralNine [Link](https://www.youtube.com/@NeuralNine)
- Check some House Price Prediction Machine Learning End-To-End Project with IndianAI Produtions [Link](https://www.youtube.com/@IndianAIProduction)
- Preject steps and customise themes with 1littlecoder [Link](https://www.youtube.com/watch?v=iUgNIFrVejc)
- Predictive Power Score learned with Paul van der Laken [Link](https://github.com/paulvanderlaken/ppsr)
- Heritage Housing Issues project by T. Hullis [Link](https://github.com/t-hullis/milestone-project-heritage-housing-issues)
- Heritage Housing Issues project by Amare Teklay Hailu [Link](https://github.com/Amareteklay/heritage-housing-issues/blob/main/README.md)
- Heritage Housing Issues project by Farid Benachenhou [Link](https://github.com/faridjos/milestone-project-heritage-housing-issues)
- StackOverflow helped resolve several issues through out the project.
- As always, I want to express my gratitude to my husband, Railson Gonçalves.

Come and see the [Live App](https://heritage-housing-fernando-74a4ebdc845a.herokuapp.com/#heritage-housing-ames-usa)

**Developed by: Fernando Gonçalves**
[My Portfolio](www.iamfernando.io)