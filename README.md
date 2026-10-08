# Medical-Appointment-NoShow-Prediction
Machine Learning project for predicting medical appointment no-shows and forecasting appointment demand using Python, Scikit-Learn, and Streamlit.
# Medical Appointment No-Show Prediction & Demand Forecasting

## Project Overview

This project focuses on predicting patient appointment no-shows and forecasting future appointment demand for healthcare resource planning. The objective is to help healthcare organizations reduce missed appointments, optimize staffing, and improve service quality using Machine Learning techniques.

---

## Business Problem

Healthcare centers often face challenges such as:

- High patient no-show rates
- Revenue loss due to missed appointments
- Wasted specialist capacity
- Difficulty in staff scheduling
- Unpredictable appointment demand
- Inefficient resource allocation

This project addresses these challenges through predictive analytics and forecasting.

---

## Dataset Information

- Total Records: 109,593
- Features: 26
- Target Variable: `no_show`

### Important Features

- specialty
- appointment_time
- gender
- disability
- place
- appointment_shift
- age
- patient_needs_companion
- average_temp_day
- average_rain_day
- Hipertension
- Diabetes
- Alcoholism
- Scholarship
- SMS_received

---

## Project Workflow

### 1. Data Preprocessing

- Missing value treatment
- Categorical encoding
- Feature engineering
- Data cleaning

### 2. Exploratory Data Analysis (EDA)

- Attendance pattern analysis
- Patient demographics analysis
- Specialty-wise trends
- Correlation analysis

### 3. No-Show Prediction Model

Algorithms Considered:

- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

### 4. Demand Forecasting Model

Algorithms Used:

- Random Forest Regressor

Evaluation Metrics:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## Model Results

### Classification Model

- Accuracy: 71.5%
- F1 Score: 0.47

### Forecasting Model

- Appointment demand forecasting implemented using machine learning techniques.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Streamlit
- Joblib
- XGBoost

---

## Project Structure

```text
Medical-Appointment-NoShow-Prediction
│
├── Medical_Appointment_NoShow.ipynb
├── app.py
├── requirements.txt
├── README.md
├── no_show_model.pkl
├── demand_forecast_model.pkl
```

---

## How To Run The Project

Install required libraries:

```bash
pip install -r requirements.txt
```

Run Streamlit application:

```bash
streamlit run app.py
```

---

## Future Improvements

- Hyperparameter tuning
- LightGBM implementation
- LSTM based forecasting
- Real-time deployment
- Automated SMS reminder integration

---

## Important Note

**⚠️ Unable to upload `no_show_mode**pkl`**
