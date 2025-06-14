import streamlit as st
st.set_page_config(
    page_title="Heritage Housing Estimator",
    page_icon="🏠",
    layout="centered"
)
from app_pages.multipage import MultiPage  
from app_pages.page_data_visuals import page_data_visuals_body
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_price_prediction import page_price_prediction_body
from app_pages.page_home import page_home_body
from app_pages.page_hypothesis import page_hypothesis_body

app = MultiPage(app_name="Heritage Housing Price Estimator")


app.add_page("🏠 Home", page_home_body)

app.add_page("📊 Data Insights", page_data_visuals_body)

app.add_page("📊 Hypotheses & Validation", page_hypothesis_body)

app.add_page("🏷️ Predict House Price", page_price_prediction_body)

app.add_page("🏠 Project Summary", page_project_summary_body)

app.run()
