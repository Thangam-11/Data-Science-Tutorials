🎯 Project Title: Water Quality Prediction using Machine Learning

🔍 Objective:

To build a machine learning model that predicts whether a given water sample is safe or unsafe for consumption based on its chemical and biological contents.

📊 Dataset:
Collected or provided data on various water quality parameters.

Each row is a water sample.

Features include:
aluminium, arsenic, bacteria, lead, nitrates, uranium, etc.

Target column: is_safe

1 = Safe

0 = Unsafe

🧹 Steps Followed:
# 1. Data Preprocessing
Checked for missing values and removed/fixed them.

Handled outliers using IQR (Interquartile Range) capping.

Normalized or standardized the data if needed.

# 2. Class Imbalance Handling
The data was imbalanced (is_safe = 1 was rare).

Used SMOTE (Synthetic Minority Over-sampling Technique) to balance classes.

# 3. Train-Test Split
Used train_test_split to divide the dataset (80% train, 20% test) with stratify=y to maintain class ratio.

# 4. Model Building
Trained three different models:

Logistic Regression

Decision Tree

Random Forest

Selected the best performing model based on accuracy, precision, recall, or F1-score.

# 5. Model Saving
Saved the best model using joblib so it can be reused in a web app.

#🌐 Streamlit Web App

Used Streamlit to create a simple and interactive web application where users can:

Enter test results for a water sample (chemical values).

Click a button to predict if it's safe or unsafe.

See the result with a message and prediction confidence.