# 📊 Customer Churn Prediction using Machine Learning Pipeline

## 📌 Project Overview

This project implements an **end-to-end machine learning pipeline** to predict customer churn using structured telecom data. The pipeline is built using **Scikit-learn Pipeline API**, ensuring a clean, reusable, and production-ready workflow.

Customer churn prediction is a critical business problem where companies aim to identify customers likely to leave their service.

---

## 🎯 Objectives

* Build a complete ML pipeline for churn prediction
* Perform data preprocessing (scaling + encoding)
* Train multiple models (Logistic Regression & Random Forest)
* Perform hyperparameter tuning using GridSearchCV
* Evaluate models using appropriate metrics
* Export the trained pipeline for production use

---

## 📂 Dataset

* **Dataset Name:** Telco Customer Churn Dataset
* Contains customer information such as:

  * Demographics
  * Services subscribed
  * Billing information
* **Target Variable:** `Churn` (Yes/No)

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* Scikit-learn
* Joblib

---

## 🧠 Machine Learning Pipeline

The pipeline consists of:

### 🔹 1. Data Preprocessing

* Handling missing values
* Converting `TotalCharges` to numeric
* Feature scaling using StandardScaler
* One-hot encoding for categorical variables

### 🔹 2. Pipeline Construction

Used **Pipeline** and **ColumnTransformer** to combine:

* Numerical transformations
* Categorical transformations
* Model training

---

## 🤖 Models Used

### 1️⃣ Logistic Regression

* Used with `class_weight="balanced"`
* Handles class imbalance effectively

### 2️⃣ Random Forest Classifier

* Ensemble learning method
* Tuned using multiple hyperparameters

---

## 🔍 Hyperparameter Tuning

Performed using **GridSearchCV**:

* Cross-validation (CV = 5)
* Optimized based on **F1-score**

---

## 📊 Evaluation Metrics

Due to class imbalance in the dataset:

* **Accuracy is not reliable**
* Focus is on:

  * **F1 Score**
  * Precision
  * Recall

---

## 📈 Results

| Model               | Accuracy | F1 Score |
| ------------------- | -------- | -------- |
| Logistic Regression | ~0.73    | ~0.61    |
| Random Forest       | ~0.75    | ~0.60    |

### ✅ Key Insight:

F1-score was prioritized over accuracy because the dataset is imbalanced. After applying class balancing, the model provides more reliable churn predictions.

---

## 🏆 Final Model Selection

**Logistic Regression** was selected as the final model because:

* Comparable performance
* Simpler and faster
* Easier to interpret

---

## 💾 Model Export

The trained pipeline is saved using **joblib**:

```bash
churn_pipeline.pkl
```

This allows reuse without retraining.

---

## 🔄 How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Train Model

```bash
python train_pipeline.py
```

### 3️⃣ Make Predictions

```bash
python predict.py
```

---

## 📁 Project Structure

```
churn-pipeline/
│
├── train_pipeline.py
├── predict.py
├── churn_pipeline.pkl
├── Telco-Customer-Churn.csv
├── requirements.txt
└── README.md
```

---

## 🚀 Key Features

* End-to-end ML pipeline
* Handles categorical + numerical data
* Hyperparameter tuning
* Model export for production
* Reusable and scalable design

---

## 🧠 Skills Demonstrated

* Machine Learning Pipelines
* Data Preprocessing
* Feature Engineering
* Hyperparameter Tuning
* Model Evaluation
* Production-ready ML workflows

---

## 📌 Conclusion

This project demonstrates how to build a **production-ready machine learning pipeline** for a real-world business problem. It highlights the importance of proper evaluation metrics, especially when dealing with imbalanced datasets.

---

## 👨‍💻 Author

**Abdul Waqar**
BS Computer Science (AI Specialization)
