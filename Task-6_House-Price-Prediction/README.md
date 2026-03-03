# 🏠 Task 6: House Price Prediction using Linear Regression

**DevelopersHub AI/ML Engineering Internship**

------------------------------------------------------------------------

## 📌 Project Overview

This project demonstrates a complete Machine Learning regression
pipeline for predicting house prices using Linear Regression.

Instead of focusing only on model training, this task emphasizes:

-   Proper data preprocessing\
-   Exploratory Data Analysis (EDA)\
-   Feature relationship understanding\
-   Reliable model evaluation

The objective was to build a prediction model on a well-prepared dataset
and evaluate performance using standard regression metrics.

------------------------------------------------------------------------

## 📂 Project Structure

    task-6-house-price-prediction/
    │
    ├── house_price_prediction.ipynb   # Full ML workflow notebook
    ├── dataset.csv                    # Dataset for training & testing
    ├── requirements.txt               # Project dependencies
    └── README.md

------------------------------------------------------------------------

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

``` bash
git clone https://github.com/abdulwaqar20/AI_ML-Engineering-Developershub-Internship/Task-6_House-Price-Prediction.git
cd Task-6_House-Price-Prediction
```

### 2️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

### 3️⃣ Launch the Notebook

``` bash
jupyter notebook House-Price-Prediction.ipynb
```

------------------------------------------------------------------------

## 📦 Dependencies

-   pandas\
-   numpy\
-   matplotlib\
-   seaborn\
-   scikit-learn\
-   jupyter

Install all dependencies using:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🔄 Machine Learning Workflow

### ✅ 1. Data Cleaning & Preprocessing

-   Handled missing values\
-   Removed unnecessary columns\
-   Ensured numerical compatibility for modeling\
-   Prepared clean and structured input data

Good preprocessing improves model reliability and prediction stability.

------------------------------------------------------------------------

### 📊 2. Exploratory Data Analysis (EDA)

Visual analysis was performed to understand:

-   Feature distributions\
-   Data patterns\
-   Relationships between variables

EDA helped guide feature selection before training the model.

------------------------------------------------------------------------

### 🔗 3. Correlation Analysis

A correlation heatmap was generated to:

-   Identify features strongly related to house prices\
-   Detect multicollinearity\
-   Understand feature importance visually

------------------------------------------------------------------------

### 🧪 4. Train--Test Split

The dataset was divided into:

-   Training data --- used for learning patterns\
-   Testing data --- used for unbiased evaluation

This ensures realistic performance measurement.

------------------------------------------------------------------------

### 🤖 5. Model Training

A Linear Regression model was trained using the Scikit-learn library on
the processed dataset.

------------------------------------------------------------------------

### 📈 6. Model Evaluation

Model performance was evaluated using:

  Metric                           Description<br>
  -------------------------------- ------------------------------------
  - MAE (Mean Absolute Error):-        Average prediction error magnitude<br>
  - RMSE (Root Mean Squared Error):-   Penalizes larger prediction errors<br>

Using both metrics provides a clearer understanding of prediction
accuracy.

------------------------------------------------------------------------

## 🧠 Model Details

  Property             Value
  ---------------------------------------
  - Algorithm:-            Linear Regression<br>
  - Framework:-            Scikit-learn<br>
  - Problem Type:-         Regression<br>
  - Evaluation Metrics:-   MAE, RMSE<br>

------------------------------------------------------------------------

## 🛠️ Tools & Technologies

  Tool           Purpose<br>
  -------------- ---------------------------<br>
  - Python:-         Core programming language<br>
  - Pandas:-         Data manipulation<br>
  - NumPy:-          Numerical computations<br>
  - Matplotlib:-     Data visualization<br>
  - Seaborn:-        Statistical visualization<br>
  - Scikit-learn:-   Machine learning modeling<br>

------------------------------------------------------------------------

## 🎓 Key Learnings

This task highlighted how data preparation directly impacts model
performance.

### Important Takeaways:

-   Clean data significantly improves regression results\
-   Linear Regression is simple, fast, and interpretable\
-   Correlation analysis helps identify meaningful features\
-   Combining MAE and RMSE gives balanced performance insight
