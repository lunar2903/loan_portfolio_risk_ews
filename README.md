# Loan Portfolio Risk & Early Warning System

## Overview

This project looks at a loan portfolio from a risk and data analytics perspective. The goal was to take loan-level data, clean it, analyze it, identify risk patterns, and build an Early Warning System (EWS) that can help an analyst decide which loans or customers need closer attention.

The project uses Python for data preparation and analysis, SQL for portfolio-level queries, and Power BI for the final dashboard.

> **Note:** The dataset used in this project is synthetic. The results are meant to demonstrate the analysis process and should not be treated as real banking or credit-risk estimates.

---

## What the project covers

- Data profiling and cleaning
- SQL-based loan portfolio analysis
- Exploratory Data Analysis (EDA)
- Statistical hypothesis testing
- Credit risk metrics
- Risk segmentation
- Early Warning System
- Customer-level risk concentration
- Portfolio exposure analysis
- Power BI dashboard

---

## Project Workflow

```text
Loan Portfolio Data
        ↓
Data Profiling
        ↓
Data Cleaning & Validation
        ↓
SQL Analysis
        ↓
EDA
        ↓
Statistical Testing
        ↓
Risk Metrics
        ↓
Risk Segmentation
        ↓
Early Warning System
        ↓
EWS Analysis
        ↓
Power BI Dashboard
```

---

## Tools Used

### Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- Statsmodels

### Database
- PostgreSQL / Supabase
- SQL

### Visualization
- Microsoft Power BI

### Development
- VS Code
- Python virtual environment
- Git / GitHub

---

## Project Structure

```text
Loan_Risk_EWS/
│
├── data/
│   ├── loan_portfolio.csv
│   ├── loan_portfolio_clean.csv
│   └── ews_alerts.csv
│
├── src/
│   ├── generate_data.py
│   ├── data_profiling.py
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── hypothesis_testing.py
│   ├── risk_metrics.py
│   ├── early_warning_system.py
│   ├── ews_analysis.py
│   └── ews_summary.py
│
├── sql/
│
├── dashboard/
│   ├── Loan_Portfolio_Risk_EWS.pbix
│   └── dashboard_preview.png
│
├── reports/
├── notebooks/
├── requirements.txt
└── README.md
```

---

# Getting Started

## 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Loan_Risk_EWS
```

If the project is already on your computer, just open the project folder in VS Code.

---

## 2. Create a virtual environment

On Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 3. Install the required packages

```bash
pip install -r requirements.txt
```

---

# Running the Project

The Python files are designed to be run in the following order.

## Step 1 — Generate the dataset

```bash
python src/generate_data.py
```

This creates the synthetic loan dataset:

```text
data/loan_portfolio.csv
```

If you already have the dataset and don't want to regenerate it, you can skip this step.

---

## Step 2 — Profile the data

```bash
python src/data_profiling.py
```

This is the first check on the dataset. It looks at:

- Number of records and columns
- Data types
- Missing values
- Duplicate records
- Duplicate loan IDs
- Basic statistics

---

## Step 3 — Clean and validate the data

```bash
python src/data_cleaning.py
```

The cleaning script handles:

- Date conversion
- Missing-value checks
- Duplicate checks
- Loan ID validation
- Age validation
- Credit score validation
- Loan amount validation
- Outstanding amount checks
- Interest rate checks
- Date sequence checks
- Other business-rule checks

The cleaned file is saved as:

```text
data/loan_portfolio_clean.csv
```

---

## Step 4 — Exploratory Data Analysis

```bash
python src/eda.py
```

The EDA looks at things such as:

- Loan status
- DPD distribution
- Credit score
- Missed payments
- Loan type
- Region
- Credit bands
- Correlations

The purpose here is to understand the portfolio before applying more advanced analysis.

---

## Step 5 — Hypothesis Testing

```bash
python src/hypothesis_testing.py
```

The project uses:

- Chi-square tests
- Welch's t-tests
- Pearson correlation

Some of the questions tested include:

- Is there an association between missed-payment bands and default?
- Is there an association between credit-score bands and default?
- Is average loan amount different between defaulted and non-defaulted loans?
- Is DPD different between defaulted and non-defaulted loans?
- Is credit score correlated with loan amount?

A p-value is used to determine whether the observed relationship provides enough evidence to reject the null hypothesis.

---

## Step 6 — Calculate risk metrics

```bash
python src/risk_metrics.py
```

This script calculates:

- Default rate
- Outstanding exposure
- Defaulted exposure
- DPD statistics
- Roll rates
- Observed PD
- LGD
- EAD
- Expected Loss
- Risk scores
- Risk categories

The simplified Expected Loss calculation is:

```text
Expected Loss ≈ PD × LGD × EAD
```

These calculations are included to demonstrate the basic credit-risk concepts used in portfolio analysis.

---

## Step 7 — Generate EWS alerts

```bash
python src/early_warning_system.py
```

The Early Warning System uses several indicators:

- DPD deterioration
- Missed payments
- Loan-to-value (LTV)
- Credit score

Each loan receives one of four alert levels:

```text
No Alert
Watch
Warning
Critical
```

The resulting file is:

```text
data/ews_alerts.csv
```

The EWS is intended to highlight loans for analyst review. It is not an automated loan approval or rejection model.

---

## Step 8 — Analyze the EWS results

```bash
python src/ews_analysis.py
```

This looks at:

- Number of loans in each alert category
- Percentage of loans by alert
- Exposure by alert level
- Average DPD by alert
- Customers with multiple Critical loans
- Exposure concentration

---

## Step 9 — Generate the final EWS summary

```bash
python src/ews_summary.py
```

This produces a final terminal summary containing the main portfolio and EWS findings.

---

# SQL Analysis

The loan data was also loaded into PostgreSQL/Supabase for SQL analysis.

The SQL work includes:

- Default rate by loan type
- Default rate by region
- Credit-score bands
- DPD buckets
- Missed-payment bands
- Exposure by loan status
- Exposure percentages
- Employment-type analysis
- Loan amount bands
- LTV analysis
- DPD deterioration
- Multiple-loan customers
- Customer-level exposure
- Customer-level risk

SQL queries are kept in:

```text
sql/
```

---

# Power BI Dashboard

The project includes an interactive Power BI dashboard:

```text
dashboard/Loan_Portfolio_Risk_EWS.pbix
```

### Dashboard KPIs

- Total Loans
- Total Exposure
- Default Rate
- Expected Loss

### Charts

- EWS Alert Distribution
- Risk Category Distribution
- Default Rate by Loan Type
- Default Rate by Region
- Exposure by EWS Alert Level
- Loan Distribution by DPD
- Missed Payments Distribution

### Filters

- Loan Type
- Region
- EWS Alert Level

The dashboard can be opened using **Power BI Desktop**.

If the PBIX file uses a local file path or database connection, the data source may need to be updated when opening it on another computer.

---

# Results

The completed analysis produced the following results.

### Portfolio

| Metric | Result |
|---|---:|
| Total Loans | 10,000 |
| Outstanding Exposure | ₹6.63B |
| Observed Default Rate | 8.05% |
| Defaulted Exposure | ₹529.44M |

### EWS

| Metric | Result |
|---|---:|
| Critical Loans | 5,303 |
| Warning Loans | 3,035 |
| Critical + Warning Loans | 83.38% |
| Critical + Warning Exposure | ₹5.79B |
| Critical + Warning Exposure % | 87.26% |

### Average DPD by EWS Level

| EWS Level | Average DPD |
|---|---:|
| No Alert | 0.00 |
| Watch | 1.32 |
| Warning | 13.88 |
| Critical | 22.90 |

The increase in average DPD across the alert levels is a useful internal check that the EWS rules are producing progressively different risk groups.

---

# Key Findings

### 1. Portfolio exposure

The portfolio contains ₹6.63B in outstanding exposure, with an observed default rate of 8.05%.

### 2. EWS exposure

₹5.79B, or 87.26% of outstanding exposure, falls into the Critical or Warning categories under the rules used in this project.

This should be interpreted as **exposure requiring closer review under the EWS rules**, not as a prediction that this exposure will default.

### 3. Customer concentration

Some customers have several loans and multiple Critical alerts. Looking at customers in addition to individual loans helps identify concentration that may otherwise be missed.

### 4. Statistical testing

The credit-score band vs default test produced:

```text
p = 0.3111
```

At the 5% significance level, the result does not provide enough evidence to reject the null hypothesis.

The loan amount comparison produced:

```text
p = 0.846
```

There was also not enough evidence of a difference in average loan amount between defaulted and non-defaulted loans.

---

# Limitations

## Synthetic data

The dataset is generated for this project and does not represent a real bank portfolio.

## DPD and loan status

The synthetic data-generation logic uses DPD thresholds when assigning loan status. Because of this, the relationship between DPD and default is partly built into the data.

For that reason, the DPD-default relationship should not be presented as an independently validated predictive result.

## Simplified risk calculations

PD, LGD, EAD and Expected Loss are simplified for demonstration.

A production credit-risk framework would require more detailed assumptions, data and methodology.

## Roll-rate analysis

The `previous_dpd` and `dpd` fields are synthetic observations rather than genuine monthly account snapshots. The roll-rate analysis therefore demonstrates the method rather than representing actual historical migration.

## EWS

The EWS is rule-based. It is designed to flag accounts for analyst review and is not a production Probability of Default model.

---

# Reproducing the Analysis

After installing the dependencies, run:

```bash
python src/generate_data.py
python src/data_profiling.py
python src/data_cleaning.py
python src/eda.py
python src/hypothesis_testing.py
python src/risk_metrics.py
python src/early_warning_system.py
python src/ews_analysis.py
python src/ews_summary.py
```

Then open:

```text
dashboard/Loan_Portfolio_Risk_EWS.pbix
```

---

# Future Improvements

Possible next versions of the project could include:

- Real historical loan-performance data
- Monthly loan snapshots
- Predictive Probability of Default modelling
- Logistic regression
- Machine-learning models
- Vintage analysis
- Cohort analysis
- Time-series delinquency analysis
- More detailed LGD modelling
- IFRS 9 / CECL-aligned modelling
- Automated EWS notifications
- Automated Power BI refresh

---

# Author

**Rahul Kolhe**

BE Information Technology
