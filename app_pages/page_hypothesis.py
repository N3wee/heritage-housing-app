import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def page_hypothesis_body():
    st.title("📈 Project Hypotheses and Validation")

    st.markdown(
        """
    This section presents the key hypotheses that guided our
    analysis and how the data supports (or refutes) them.

    ---
    ### Hypothesis 1: Overall Quality has a strong positive correlation with Sale Price
    """
    )

    df = pd.read_csv("data/house_prices_cleaned.csv")

    fig1, ax1 = plt.subplots()
    sns.boxplot(x="OverallQual", y="SalePrice", data=df, ax=ax1)
    ax1.set_title("Sale Price vs. Overall Quality")
    st.pyplot(fig1)

    st.markdown(
        """
    ✅ **Conclusion:** As the quality rating increases, the median
    sale price also increases significantly — confirming the hypothesis.

    ---
    ### Hypothesis 2: Houses with more Above-Ground Living Area are priced higher
    """
    )

    fig2, ax2 = plt.subplots()
    sns.scatterplot(x="GrLivArea", y="SalePrice", data=df, ax=ax2)
    ax2.set_title("Sale Price vs. Above-Ground Living Area")
    st.pyplot(fig2)

    st.markdown(
        """
    ✅ **Conclusion:** There is a strong positive linear trend,
    indicating larger homes tend to sell for more — supporting the hypothesis.
    """
    )
