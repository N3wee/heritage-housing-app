import joblib
import numpy as np
import pandas as pd

def test_model_load_and_predict():
    model = joblib.load("models/linreg_model.joblib")
    # minimal input matching the training features
    X = pd.DataFrame(
        {
            "OverallQual": [5],
            "GrLivArea": [1500],
            "GarageArea": [400],
            "YearBuilt": [1990],
            "TotalBsmtSF": [800],
            "LotArea": [8000],
        }
    )
    y_log = model.predict(X)[0]
    y = np.expm1(y_log)
    assert y > 0  # price must be positive
