import streamlit as st

def page_home_body():
    st.title("🏠 Heritage Housing Price Estimator")
    
    st.markdown("""
    Welcome to the **Heritage Housing Price Estimator**!

    This app allows you to:
    - 🔍 Explore and understand factors that affect house prices in Ames, Iowa
    - 📈 Validate hypotheses using data visualizations
    - 🤖 Predict the price of a house based on key features using a trained ML model

    ---
    **Navigation Tips**
    - Use the sidebar to move between sections of the app
    - Start with 'Data Insights' to explore trends
    - Try out 'Predict House Price' to test the estimator!

    ---
    **About the Project**

    This tool is part of a Full Stack Software Development diploma and showcases skills in:
    - Data analysis & preprocessing
    - Machine learning modeling
    - Streamlit web app development
    - Model deployment and project presentation
    """)
