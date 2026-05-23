# Healthcare Claims Analytics

A Python-based healthcare analytics project that analyzes patient claims, utilization trends, department costs, risk segmentation, and claim forecasting.

## Objectives
- Clean and validate healthcare claims data
- Analyze monthly claim amount trends
- Compare cost by department
- Study length of stay vs claim amount
- Segment patients by healthcare utilization and risk
- Forecast future claim amounts using Ridge Regression

## Tech Stack
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Pytest

## Key Outputs
### Visualizations
- Monthly Claim Amount Trend
- Claim Amount by Department
- Length of Stay vs Claim Amount

### Analytics Outputs
- Patient Risk Segmentation
- Forecasted Claim Amount Results
- Cleaned Healthcare Dataset

## Machine Learning
Used Ridge Regression to build a baseline healthcare claim forecasting model.


```bash


Healthcare-Claims-Analytics/
│
├── data/
│   └── raw/
│       └── healthcare_claims.csv
│
├── src/
│   ├── data_prep.py
│   ├── eda.py
│   ├── segmentation.py
│   ├── model.py
│   └── utils.py
│
├── reports/
│   ├── monthly_claim_amount.png
│   ├── claim_by_department.png
│   ├── los_vs_claim_amount.png
│   ├── patient_segments.csv
│   └── claim_forecast_results.csv
│
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
