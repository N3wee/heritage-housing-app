# 🏠 Heritage Housing Price Estimator

This Streamlit-based web app is being developed as part of a Diploma in Full Stack Software Development final project. It is a predictive analytics tool designed to estimate house prices in Ames, Iowa, using a dataset sourced from a public Kaggle repository.

---

## 📌 Project Purpose

The aim of this project is to assist users — such as homeowners, property investors, or analysts — in understanding which features most strongly influence house prices in Ames, Iowa, and to provide a predicted sale price based on specific property attributes.

The app will:
- Deliver data-driven insights using machine learning
- Allow users to input house features and receive price predictions
- Present intuitive dashboards for exploratory data analysis (EDA)

---

## 🧠 Learning Objectives Addressed So Far

| LO | Description |
|----|-------------|
| LO1 | Demonstrated understanding of dataset and business context |
| LO2 | Began mapping business requirements to data analysis tasks |
| LO4 | Performed data analysis to extract early insights |
| LO7 | Successfully loaded and processed data from a local source |

---

## 🗂️ Project Structure (to date)

heritage-housing-app/\
├── app_pages/ # Streamlit UI pages\
├── data/ # Raw input datasets\
│ ├── house_prices_records.csv\
│ ├── inherited_houses.csv\
│ └── house-metadata.txt\
├── notebooks/ # Development notebooks\
│ └── 01_data_exploration.ipynb\
├── src/ # Python modules (preprocessing, prediction logic)\
├── streamlit_app.py # Main entry point for the web app\
├── requirements.txt # Dependencies\
├── setup.sh # Heroku deployment script\
├── Procfile # Heroku process file\
└── README.md # This file

---

## 📊 Completed Tasks (So Far)

### ✅ Data Upload

The following datasets have been collected and stored in the `data/` folder:

- `house_prices_records.csv`: Core dataset from Ames, Iowa

- `inherited_houses.csv`: A smaller test set for prediction purposes

- `house-metadata.txt`: Supporting documentation for variables

### ✅ Data Exploration

In `01_data_exploration.ipynb`, the following have been completed:

- Dataset shape and summary statistics

- Identification of missing values

- Count of duplicate records

- Initial visualizations of key outliers (`SalePrice`, `GrLivArea`, `LotArea`)

### ✅ Data Cleaning

In `02_data_cleaning.ipynb`, the following cleaning steps were completed:

- **Duplicates removed** to prevent bias in modeling
- **Columns with >30% missing data** were dropped to simplify handling
- **Numerical columns** had missing values filled with the **median**
- **Categorical columns** had missing values filled with the **mode**
- The `SalePrice` column was **log-transformed** to reduce skewness in the target variable
- The cleaned dataset was saved as `house_prices_cleaned.csv` in the `data/` folder

### ✅ Feature Engineering

In `03_feature_engineering.ipynb`, the following preprocessing tasks were completed:

- Loaded the cleaned dataset
- Applied **One-Hot Encoding** to all categorical features using `pd.get_dummies()`
- Dropped the original `SalePrice` column (we will use the log-transformed version for modeling)
- Saved the fully preprocessed dataset as `house_prices_preprocessed.csv` in the `data/` folder


---

## 📅 Next Steps (Planned)

- Train basic regression models (e.g., Linear Regression, Random Forest)

- Deploy model into the Streamlit app

---

## 📚 Data Source

This project uses the [Ames Housing Dataset](https://www.kaggle.com/codeinstitute/housing-prices-data) provided by Code Institute on Kaggle.

---

## 📎 Acknowledgements

This project is developed as part of the Full Stack Diploma at Code Institute. Dataset courtesy of Kaggle (public domain). Guidance and feedback from project mentors and course materials are acknowledged.