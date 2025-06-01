import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_data_visuals_body():
    st.title("📊 Data Insights")

    st.markdown("""
    ### 📌 Visual Correlation with Sale Price
    These plots help us understand how various house features influence the final sale price.
    """)

    # Load pre-cleaned data
    df = pd.read_csv("data/house_prices_cleaned.csv")

    # Plot 1: SalePrice vs GrLivArea
    st.subheader("🔹 Sale Price vs Above-Ground Living Area (GrLivArea)")
    fig1, ax1 = plt.subplots()
    sns.scatterplot(x='GrLivArea', y='SalePrice', data=df, ax=ax1)
    st.pyplot(fig1)

    # Plot 2: SalePrice vs OverallQual
    st.subheader("🔹 Sale Price vs Overall Quality")
    fig2, ax2 = plt.subplots()
    sns.boxplot(x='OverallQual', y='SalePrice', data=df, ax=ax2)
    st.pyplot(fig2)

    # Plot 3: Correlation Heatmap
    st.subheader("🔹 Correlation Heatmap (Top Numeric Features)")
    numeric_df = df.select_dtypes(include='number')
    corr = numeric_df.corr()
    top_corr = corr['SalePrice'].sort_values(ascending=False).head(10).index
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_df[top_corr].corr(), annot=True, cmap='coolwarm', ax=ax3)
    st.pyplot(fig3)

    st.markdown("""---""")
    st.markdown("""
    ✅ **Takeaway:** Features like **GrLivArea** (above-ground living area), **OverallQual** (quality), and **GarageArea** show strong correlation with house price.
    """)
