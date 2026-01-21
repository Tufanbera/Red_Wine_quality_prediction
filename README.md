**Red Wine Quality Prediction Using Machine Learning**

# 📌 Project Overview
Wine quality assessment is traditionally performed by human experts through sensory evaluation, which is subjective, time-consuming, and expensive.
This project aims to automate wine quality classification using machine learning based on physicochemical properties of red wine.


The model predicts whether a wine is:
Good Quality
Not Good Quality

This solution supports wineries in making early, data-driven quality decisions.

## 🎯 Business Objective

Reduce dependency on manual wine tasting
Identify good-quality wines early
Understand chemical factors influencing quality
Build a deployable ML classification pipeline

### 🧠 Machine Learning Problem
Type: Supervised Learning
Task: Binary Classification
Challenge: Class Imbalance

#### 📊 Dataset Description
Source: Portuguese Red Wine Dataset
Records: ~1,600
Target Variable: quality

Target Transformation
Original Quality	New Label
≥ 7	Good (1)
< 7	Not Good (0)

####  Input Features

Fixed acidity
Volatile acidity
Citric acid
Residual sugar
Chlorides
Free sulfur dioxide
Total sulfur dioxide
Density
pH
Sulphates
Alcohol

##### 🔍 Project Workflow

Data understanding & cleaning
Exploratory Data Analysis (EDA)
Feature scaling & selection
Model training (baseline → advanced)
Hyperparameter tuning
Model evaluation using ROC-AUC
Final model selection & saving

###### 📈 Models Used

Logistic Regression (Baseline)
Decision Tree
Random Forest 
Xgboost

📏 Evaluation Metrics

ROC-AUC
Precision
Recall
F1-Score
Confusion Matrix

ROC-AUC was prioritized over accuracy due to class imbalance.