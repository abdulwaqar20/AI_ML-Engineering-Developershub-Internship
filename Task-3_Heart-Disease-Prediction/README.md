# Task 3: Heart Disease Prediction

## Objective
The objective of this task is to build a machine learning model that predicts
whether a person is at risk of heart disease based on medical and health-related
attributes.

---

## Dataset Used
- **Name:** Heart Disease UCI Dataset  
- **Source:** Kaggle  
- **Type:** Medical dataset  
- **Target Variable:**  
  - `target`  
    - 0 → No heart disease  
    - 1 → Presence of heart disease  

---

## Tools and Libraries
- Python  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- Jupyter Notebook  

---

## Methodology
1. Loaded the Heart Disease dataset and inspected its structure.
2. Checked and handled missing values.
3. Performed Exploratory Data Analysis (EDA) to understand trends and relationships.
4. Split the dataset into training and testing sets.
5. Applied feature scaling using StandardScaler.
6. Trained a Logistic Regression classification model.
7. Evaluated the model using accuracy, confusion matrix, and ROC-AUC.
8. Analyzed feature importance using Logistic Regression coefficients.

---

## Model Used
- **Logistic Regression**

Logistic Regression was chosen due to its suitability for binary classification
and its interpretability in medical applications.

---

## Evaluation Metrics
- Accuracy  
- Confusion Matrix  
- ROC Curve  
- ROC-AUC Score  

---

## Key Results and Findings
- The model achieved strong classification performance with an ROC-AUC score
  of approximately **0.88**.
- The confusion matrix showed a high number of correct predictions and
  relatively few false negatives.
- Chest pain type, maximum heart rate, and ST depression were important
  predictors of heart disease.
- Feature importance analysis provided medically interpretable insights.

---

## Conclusion
This task demonstrated the application of binary classification techniques
to medical data. Logistic Regression proved effective for predicting heart
disease risk while maintaining interpretability.

The model can assist in early risk assessment but should not replace
professional medical diagnosis.

---

## Author
Abdul Waqar
