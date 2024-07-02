# **Heritage Housing Ames, USA**
 
![Heritage Housing Ames](https://lh3.googleusercontent.com/p/AF1QipNKRtVDRmvx3OtNnix6GgYkVe6a-eD_0qM1x9dI=s1360-w1360-h1020)

## Table of content


## Dataset Content

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

## Business Requirements

The project has three main business requirements:

1. The client wants to understand the relationship between a property's attributes/features and its sale price.
Therefore, the client expects data visualizations that illustrate the correlation between these variables and the sale prices.

2. The client is interested in predicting the potential sale prices for properties in Ames, Iowa, with a specific focus on estimating the value of the properties she has inherited.

3. The client would like to have easy access to the results through an online application.

## Hypothesis and how to validate?

* List here your project hypothesis(es) and how you envision validating it (them).

## The rationale to map the business requirements to the Data Visualisations and ML tasks

* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

## ML Business Case

* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.

## Dashboard Design

* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)

## Unfixed Bugs

The app does not currently contain any unfixed bugs.

## PEP8 Compliance Testing

All python files where passed through the [CI Python Linter](https://pep8ci.herokuapp.com/). 
Those files incuded the `app_pages` files. A few small errors were fixed, such as long lines or trailing white spaces.

## Deployment

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

## Technologies

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

## Credits

### Sources of code

- The CI Churnometer Walkthrough Project and the CI course content was used to source various functions and classes in the development process.
- The CI Churnometer Walkthrough Project was also the source of the Steamlit pages which were then modified and adapted to the app deployed in this project.

### Media

- The image of main street Ames is from [Wikipedia](https://commons.wikimedia.org/wiki/File:Ames_Iowa_Main_Street_%28bannerportada_esvoy%29.jpg)

- The images of Iowa State University was taken from [Niche.com](https://www.niche.com/colleges/iowa-state-university/)

## Acknowledgements

Thanks and appreciation go to the following sources and people:

- Several past projects provided valuable additional information on how to complete a successful project:
- Setup of widgest learned with t-hullis[Link](https://github.com/t-hullis/milestone-project-heritage-housing-issues/tree/main)
- Predictive Power Score learned with Paul van der Laken [Link](https://github.com/paulvanderlaken/ppsr)
  - Heritage Housing Issues project by T. Hullis [Link](https://github.com/t-hullis/milestone-project-heritage-housing-issues)
  - Heritage Housing Issues project by Amare Teklay Hailu [Link](https://github.com/Amareteklay/heritage-housing-issues/blob/main/README.md)
  - Heritage Housing Issues project by Farid Benachenhou [Link](https://github.com/faridjos/milestone-project-heritage-housing-issues)
- StackOverflow helped resolve several issues through out the project.
- As always a big thank you to my husband, Railson Gonçalves.

**Developed by: Fernando Gonçalves**