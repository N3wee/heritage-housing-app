# import streamlit as st
# import pandas as pd
# import joblib
# import numpy as np

# def page_price_prediction_body():
#     st.title("🏷️ Predict House Sale Price")

#     st.markdown("### Enter property details to estimate the sale price")

#     # Define form
#     with st.form("prediction_form"):
#         overall_qual = st.selectbox("Overall Quality (1–10)", list(range(1, 11)), index=5)
#         gr_liv_area = st.number_input("Above-Ground Living Area (sq ft)", min_value=500, max_value=5000, value=1500)
#         garage_area = st.number_input("Garage Area (sq ft)", min_value=0, max_value=1500, value=400)
#         year_built = st.number_input("Year Built", min_value=1870, max_value=2023, value=1995)
#         full_bath = st.selectbox("Number of Full Bathrooms", [0, 1, 2, 3], index=1)

#         submit = st.form_submit_button("Estimate Price")

#     if submit:
#         # Create DataFrame with matching feature names from training
#         input_data = pd.DataFrame({
#             'OverallQual': [overall_qual],
#             'GrLivArea': [gr_liv_area],
#             'GarageArea': [garage_area],
#             'YearBuilt': [year_built],
#             'FullBath': [full_bath]
#         })

#         try:
#             model = joblib.load("models/linreg_model.joblib")
#             prediction_log = model.predict(input_data)[0]
#             prediction = np.expm1(prediction_log)

#             st.success(f"🏠 Estimated Sale Price: **${prediction:,.0f}**")
#         except Exception as e:
#             st.error(f"❌ Error loading model or making prediction: {e}")
