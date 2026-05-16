# 📊 DHC Data Science & Analytics Internship

## Overview

This repository contains all five Data Science & Analytics internship tasks for **DevelopersHub Corporation**. Each task is implemented as a complete Jupyter Notebook featuring data loading, EDA, model training, evaluation, and conclusions.

**Libraries used:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

---

## Tasks

## Task 1: Term Deposit Subscription Prediction

**Objective:** Predict whether a bank customer will subscribe to a term deposit.
**Dataset:** Bank Marketing Dataset (UCI Machine Learning Repository)
**Approach:**
- Loaded and explored the dataset (45,211 rows, 17 columns)
- Label-encoded all categorical features; used `class_weight='balanced'` for imbalance
- Trained **Logistic Regression** and **Random Forest** classifiers
- Evaluated using Confusion Matrix, F1-Score, and ROC-AUC curves
- Used **SHAP TreeExplainer** to explain 5 individual predictions with force plots

**Key Results:**
- Random Forest achieves higher AUC than Logistic Regression on this imbalanced dataset
- Top features: `duration`, `poutcome`, `balance`, `age`
- SHAP confirms longer call duration is the strongest predictor of subscription

---

## Task 2: Customer Segmentation Using Unsupervised Learning

**Objective:** Cluster mall customers by spending habits and propose targeted marketing strategies.
**Dataset:** Mall Customers Dataset
**Approach:**
- Conducted full EDA on Age, Annual Income, Spending Score, and Gender
- Applied **K-Means Clustering** with Elbow Method + Silhouette Score to find optimal k=5
- Visualised clusters using **PCA** (2D projection) and **t-SNE**
- Built a radar chart of cluster profiles
- Proposed distinct marketing strategies for each of 5 segments

**Key Results:**
- 5 well-separated segments identified: Budget Conscious, High Earners Low Spenders, Target Stars, Impulsive Young Spenders, Mature Moderate Spenders
- Target Stars (high income, high spending) are the most valuable segment
- High Earners Low Spenders represent the biggest untapped opportunity

---

## Task 3: Energy Consumption Time Series Forecasting

**Objective:** Forecast short-term household energy usage using ARIMA, Prophet, and XGBoost.
**Dataset:** Household Power Consumption Dataset (UCI)
**Approach:**
- Parsed and resampled time series data to daily averages
- Engineered time-based features: hour, day-of-week, month, lag features (1d, 7d, 14d), rolling statistics
- Compared **ARIMA(2,0,2)**, **Facebook Prophet**, and **XGBoost Regressor**
- Evaluated all models using MAE and RMSE on a 30-day hold-out test set
- Plotted actual vs. forecasted consumption for all three models

**Key Results:**
| Model   | MAE    | RMSE   |
|---------|--------|--------|
| ARIMA   | higher | higher |
| Prophet | mid    | mid    |
| XGBoost | lowest | lowest |

- XGBoost wins by leveraging lag features and rolling statistics
- Clear seasonal patterns: higher consumption in winter and evening hours

---

## Task 4: Loan Default Risk with Business Cost Optimization

**Objective:** Predict loan defaults and find the optimal decision threshold based on cost-benefit analysis.
**Dataset:** Home Credit Default Risk Dataset
**Approach:**
- Cleaned and preprocessed data with median imputation and standard scaling
- Trained **Logistic Regression** and **XGBoost** binary classifiers with class balancing
- Defined business cost matrix: FN = $5,000 (bad loan approved), FP = $1,200 (good loan rejected)
- Swept thresholds from 0.01 to 0.99 to find the threshold that minimises total business cost
- Visualised cost curve, FP/FN trade-off, and confusion matrices at default vs. optimal threshold

**Key Results:**
- XGBoost significantly outperforms Logistic Regression (higher AUC)
- Default threshold (0.5) is suboptimal — the business-optimal threshold is lower (more conservative)
- Shifting to the optimal threshold produces significant financial savings
- Top features: EXT_SOURCE_2, AMT_INCOME_TOTAL, AMT_ANNUITY, DAYS_BIRTH

---

## Task 5: Interactive Business Dashboard in Streamlit

**Objective:** Build an interactive dashboard for analysing sales, profit, and segment-wise performance.
**Dataset:** Global Superstore Dataset
**Approach:**
- Generated and cleaned a realistic Global Superstore dataset (5,000 orders)
- Built a full **Streamlit** dashboard (`dashboard.py`) with:
  - Sidebar filters: Year, Region, Category, Sub-Category, Segment
  - KPI cards: Total Sales, Total Profit, Total Orders, Avg Margin %, Units Sold
  - Charts: Monthly Sales Trend, Category Pie, Regional Profit, Top Sub-Categories, Top 5 Customers, Segment Comparison, Discount Impact, Ship Mode Analysis
  - Filterable data table

**How to Run:**
```bash
pip install streamlit
streamlit run dashboard.py
# Opens at http://localhost:8501
```

**Key Insights:**
- Technology is the top-selling category; Office Supplies has the highest margin
- Discounts above 30% consistently generate losses — should be capped at 20%
- West region leads in both sales and profit
- Consumer segment accounts for the largest revenue share

---

## Results Summary

| Task   | Model Used                          | Metric           | Score  |
|--------|-------------------------------------|------------------|--------|
| Task 1 | Logistic Regression / Random Forest | AUC              | ~0.79+ |
| Task 2 | K-Means Clustering (k=5)            | Silhouette Score | ~0.45+ |
| Task 3 | ARIMA / Prophet / XGBoost           | RMSE             | ~0.12+ |
| Task 4 | Logistic Regression / XGBoost       | AUC              | ~0.72+ |
| Task 5 | Streamlit Dashboard (BI)            | —                | —      |

---