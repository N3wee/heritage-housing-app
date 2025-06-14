import streamlit as st


def page_project_summary_body():
    st.title("🏠 Heritage Housing Price Estimator")

    st.markdown(
        """
    ### 📌 Project Overview
    This project predicts the sale price of inherited homes located in Ames,
    Iowa, using machine learning models trained on historical housing data.

    The application aims to support users (like Lydia Doe, our fictional client) in:
    - Understanding which features influence house prices most
    - Accurately estimating the price of properties using a trained ML model

    ### 🧰 What this app offers:
    - A data-driven analysis of the Ames housing market
    - Interactive visualizations
    - ML-powered house price prediction tool
    ---
    #### 👩🏻‍💻 Built with:
    - Python & scikit-learn
    - Streamlit
    - pandas & matplotlib
    """
    )
