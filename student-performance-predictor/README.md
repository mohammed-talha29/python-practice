# Student Performance Predictor

A machine learning project that predicts a student's final score based on study hours, attendance, previous score, and assignment score.

## Project Overview

The Student Performance Predictor uses Linear Regression to estimate a student's final performance.

The project includes:

- Synthetic student dataset generation
- Exploratory Data Analysis (EDA)
- Linear Regression model training
- Model evaluation using R² and MAE
- 5-fold cross-validation
- Prediction error analysis
- Interactive student score prediction

## Features

The model uses four input features:

| Feature | Description |
|---|---|
| Study Hours | Average study hours per day |
| Attendance | Attendance percentage |
| Previous Score | Student's previous academic score |
| Assignment Score | Assignment performance score |

The target variable is:

**Final Score**

## Machine Learning Model

The project uses:

**Linear Regression**

Linear Regression was selected after comparing model performance.

Final model performance:

- **Average R² Score:** 0.936
- **Average MAE:** 2.247
- **R² Standard Deviation:** 0.019
- **MAE Standard Deviation:** 0.281

The model explains approximately 93.6% of the variation in final scores during 5-fold cross-validation.

The average prediction error is approximately 2.25 points.

## Project Structure

```text
student-performance-predictor/
│
├── data/
│   └── students.csv
│
├── generate_data.py
├── eda.py
├── train_model.py
├── cross_validation.py
├── error_analysis.py
├── predict.py
├── predictor.py
└── student_model.pkl