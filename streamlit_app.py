import streamlit as st
from app_pages.multipage import MultiPage  
from app_pages.page_data_visuals import page_data_visuals_body
from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_price_prediction import page_price_prediction_body

app = MultiPage(app_name="Heritage Housing Price Estimator")

app.add_page("🏠 Project Summary", page_project_summary_body)

app.add_page("📊 Data Insights", page_data_visuals_body)

app.add_page("🏷️ Predict House Price", page_price_prediction_body)


app.run()
