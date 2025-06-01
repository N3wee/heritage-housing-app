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

---

## 📅 Next Steps (Planned)

- Clean missing values and outliers

- Feature engineering (log-transform skewed variables, encode categoricals)

- Train basic regression models (e.g., Linear Regression, Random Forest)

- Deploy model into the Streamlit app

---

## 📚 Data Source

This project uses the [Ames Housing Dataset](https://www.kaggle.com/codeinstitute/housing-prices-data) provided by Code Institute on Kaggle.

---

## 📎 Acknowledgements

This project is developed as part of the Full Stack Diploma at Code Institute. Dataset courtesy of Kaggle (public domain). Guidance and feedback from project mentors and course materials are acknowledged.