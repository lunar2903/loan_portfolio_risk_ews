#EDA = Exploratory Data Analysis.
import pandas as pd
import matplotlib.pyplot as plt

# Load clean dataset
df = pd.read_csv("data/loan_portfolio_clean.csv")

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# 1. Number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# 2. First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# 3. Column names
print("\nColumns:")
print(df.columns.tolist())

# 4. Data types
print("\nData Types:")
print(df.dtypes)

# 5. Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------
# 6. Numerical Variable Summary
# --------------------------------

numeric_columns = [
    "credit_score",
    "annual_income",
    "loan_amount",
    "outstanding_amount",
    "interest_rate",
    "missed_payments",
    "dpd",
    "previous_dpd",
    "collateral_value"
]

print("\nNumerical Variable Summary:")
print(df[numeric_columns].describe())

# --------------------------------
# 7. DPD Distribution
# --------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["dpd"], bins=10)

plt.title("Distribution of Days Past Due (DPD)")
plt.xlabel("DPD (Days)")
plt.ylabel("Number of Loans")

plt.show()

# --------------------------------
# 8. Credit Score Distribution
# --------------------------------

plt.figure(figsize=(8, 5))

plt.hist(df["credit_score"], bins=20)

plt.title("Distribution of Credit Scores")
plt.xlabel("Credit Score")
plt.ylabel("Number of Loans")

plt.show()
# --------------------------------
# 9. Default Rate by Credit Score
# --------------------------------

credit_bins = [300, 579, 669, 739, 799, 850]
credit_labels = ["Poor", "Fair", "Good", "Very Good", "Excellent"]

df["credit_band"] = pd.cut(
    df["credit_score"],
    bins=credit_bins,
    labels=credit_labels
)

default_rate = (
    df.groupby("credit_band", observed=False)["loan_status"]
    .apply(lambda x: (x == "Default").mean() * 100)
)

plt.figure(figsize=(8, 5))

default_rate.plot(kind="bar")

plt.title("Default Rate by Credit Score Band")
plt.xlabel("Credit Score Band")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=0)

plt.show()

# --------------------------------
# 10. Default Rate by Missed Payments
# --------------------------------

missed_payment_bins = [-1, 0, 2, 4, float("inf")]
missed_payment_labels = [
    "No Missed Payments",
    "Low (1-2)",
    "Moderate (3-4)",
    "High (5+)"
]

df["missed_payment_band"] = pd.cut(
    df["missed_payments"],
    bins=missed_payment_bins,
    labels=missed_payment_labels
)

default_rate_missed = (
    df.groupby("missed_payment_band", observed=False)["loan_status"]
    .apply(lambda x: (x == "Default").mean() * 100)
)

plt.figure(figsize=(8, 5))

default_rate_missed.plot(kind="bar")

plt.title("Default Rate by Missed Payment Band")
plt.xlabel("Missed Payment Band")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=0)

plt.show()

# --------------------------------
# 11. Loan Status Distribution
# --------------------------------

status_counts = df["loan_status"].value_counts()

plt.figure(figsize=(8, 5))

status_counts.plot(kind="bar")

plt.title("Loan Portfolio by Status")
plt.xlabel("Loan Status")
plt.ylabel("Number of Loans")
plt.xticks(rotation=0)

plt.show()

# --------------------------------
# 12. Default Rate by Loan Type
# --------------------------------

default_rate_loan_type = (
    df.groupby("loan_type")["loan_status"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

default_rate_loan_type.plot(kind="bar")

plt.title("Default Rate by Loan Type")
plt.xlabel("Loan Type")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=0)

plt.show()

# --------------------------------
# 13. Default Rate by Region
# --------------------------------

default_rate_region = (
    df.groupby("region")["loan_status"]
    .apply(lambda x: (x == "Default").mean() * 100)
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

default_rate_region.plot(kind="bar")

plt.title("Default Rate by Region")
plt.xlabel("Region")
plt.ylabel("Default Rate (%)")
plt.xticks(rotation=0)

plt.show()
# --------------------------------
# 14. Correlation Analysis
# --------------------------------

numeric_columns = [
    "age",
    "annual_income",
    "credit_score",
    "loan_amount",
    "outstanding_amount",
    "interest_rate",
    "loan_term",
    "monthly_installment",
    "missed_payments",
    "dpd",
    "previous_dpd",
    "collateral_value"
]

correlation_matrix = df[numeric_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix)

plt.figure(figsize=(12, 8))

plt.imshow(correlation_matrix, cmap="coolwarm")
plt.colorbar()

plt.xticks(
    range(len(numeric_columns)),
    numeric_columns,
    rotation=90
)

plt.yticks(
    range(len(numeric_columns)),
    numeric_columns
)

plt.title("Correlation Matrix")

plt.tight_layout()
plt.show()