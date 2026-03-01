# Task 2: Predict Future Stock Prices (Short-Term)

## Objective
The objective of this task is to use historical stock market data to predict the
next day’s closing price using machine learning techniques.

---

## Dataset Used
- **Source:** Yahoo Finance  
- **Library:** yfinance  
- **Stock Selected:** Apple Inc. (AAPL)  
- **Data Type:** Historical daily stock prices  
- **Features Used:**
  - Open
  - High
  - Low
  - Volume
- **Target Variable:** Next day closing price

---

## Tools and Libraries
- Python  
- pandas  
- numpy  
- matplotlib  
- yfinance  
- scikit-learn  
- Jupyter Notebook  

---

## Methodology
1. Historical stock data was downloaded using the yfinance library.
2. Data inspection and cleaning were performed.
3. A new target variable was created by shifting the closing price to represent
   the next day’s close.
4. The dataset was split into training and testing sets while preserving
   time order.
5. A Linear Regression model was trained using Open, High, Low, and Volume features.
6. The model was evaluated using standard regression metrics.
7. Actual vs predicted closing prices were visualized.

---

## Model Used
- **Linear Regression**

Linear Regression was selected due to its simplicity and suitability for
short-term trend prediction.

---

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

These metrics were used to measure prediction accuracy and model performance.

---

## Key Results and Findings
- The model successfully captured short-term trends in stock prices.
- Predictions closely followed actual closing prices.
- Some deviation occurred due to market volatility.
- The approach is suitable for short-term prediction but limited for long-term
  forecasting.

---

## Conclusion
This task demonstrated how machine learning can be applied to real-world
financial data. Using historical stock prices and a Linear Regression model,
the next day’s closing price was predicted with reasonable accuracy.
