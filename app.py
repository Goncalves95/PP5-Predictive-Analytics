import streamlit as st
from app_pages.multipage import MultiPage

# Load pages scripts
from app_pages.home_page import home_page_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.predict_price import page_predict_price_ml_body
from app_pages.analysis import page_analysis_body
from app_pages.predictor import page_price_predictor_body

app = MultiPage(app_name="Heritage Housing Ames, USA")  # Create an instance of the app

# Add your app pages here using.add_page()
app.add_page("🏠 Project Summary", home_page_body)
app.add_page("🧠 Preject Hypothesis", page_project_hypothesis_body)
app.add_page("📈 Predictor Price", page_price_predictor_body)
app.add_page("💰 Predict Price", page_predict_price_ml_body)
app.add_page("📊 Analysis Prices", page_analysis_body)


app.run()  # Run the app


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