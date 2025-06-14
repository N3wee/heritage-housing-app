# 📄 app_pages/page_price_prediction.py

import streamlit as st
import pandas as pd
import joblib
import numpy as np


def page_price_prediction_body():
    st.title("🏠 Predict House Sale Price")

    st.info(
        "Use the form below to input features of a house and predict its sale price in Ames, Iowa."
    )

    # Load the trained model
    try:
        model = joblib.load("models/linreg_model.joblib")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return

    # Input form
    with st.form("prediction_form"):
        overall_qual = st.slider("Overall Quality", min_value=1, max_value=10, value=5)
        gr_liv_area = st.number_input("Above Ground Living Area (sq ft)", value=1500)
        garage_area = st.number_input("Garage Area (sq ft)", value=400)
        year_built = st.number_input(
            "Year Built", min_value=1800, max_value=2024, value=1990
        )
        total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", value=800)
        lot_area = st.number_input("Lot Area (sq ft)", value=8000)

        submit = st.form_submit_button("Predict Price")

    # Run prediction
    if submit:
        input_data = pd.DataFrame(
            {
                "OverallQual": [overall_qual],
                "GrLivArea": [gr_liv_area],
                "GarageArea": [garage_area],
                "YearBuilt": [year_built],
                "TotalBsmtSF": [total_bsmt_sf],
                "LotArea": [lot_area],
            }
        )

        log_price = model.predict(input_data)[0]
        sale_price = np.expm1(log_price)

        st.success(f"💰 Estimated Sale Price: ${sale_price:,.0f}")
