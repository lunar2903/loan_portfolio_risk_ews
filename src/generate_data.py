import pandas as pd
import numpy as np

np.random.seed(42)

N = 10000

data = {
    "loan_id": [f"LN{i:06d}" for i in range(1, N + 1)],
    "customer_id": [f"CUST{i:06d}" for i in np.random.randint(1, 8000, N)],
    "loan_type": np.random.choice(
        ["Personal", "Home", "Auto", "Business", "Education"],
        N
    ),
    "age": np.random.randint(21, 65, N),
    "gender": np.random.choice(["Male", "Female"], N),
    "employment_type": np.random.choice(
        ["Salaried", "Self-Employed", "Business Owner"],
        N
    ),
    "annual_income": np.random.randint(200000, 3000000, N),
    "credit_score": np.random.randint(500, 850, N),
    "loan_amount": np.random.randint(50000, 2500000, N),
    "interest_rate": np.round(np.random.uniform(7, 18, N), 2),
    "loan_term": np.random.choice([12, 24, 36, 48, 60, 72, 84], N),
    "region": np.random.choice(
        ["North", "South", "East", "West", "Central"],
        N
    ),
    "application_date": pd.date_range(
        start="2022-01-01",
        periods=N,
        freq="6h"
    ).date,
    "missed_payments": np.random.poisson(1, N),
    "dpd": np.random.choice(
        [0, 5, 10, 15, 30, 60, 90, 120],
        N,
        p=[0.55, 0.08, 0.07, 0.06, 0.10, 0.06, 0.05, 0.03]
    ),
    "previous_dpd": np.random.choice(
        [0, 10, 30, 60, 90],
        N,
        p=[0.65, 0.10, 0.10, 0.08, 0.07]
    ),
    "collateral_value": np.random.randint(0, 3000000, N)
}

df = pd.DataFrame(data)

# Calculate outstanding amount
df["outstanding_amount"] = (
    df["loan_amount"] *
    np.random.uniform(0.1, 0.95, N)
).round(2)

# Calculate monthly installment
df["monthly_installment"] = (
    df["loan_amount"] / df["loan_term"]
).round(2)

# Total payments
df["total_payments"] = (
    df["loan_term"] - df["missed_payments"]
).clip(lower=0)

# Payment dates
df["disbursement_date"] = pd.to_datetime(
    df["application_date"]
) + pd.to_timedelta(np.random.randint(1, 30, N), unit="D")

df["last_payment_date"] = (
    df["disbursement_date"] +
    pd.to_timedelta(np.random.randint(30, 700, N), unit="D")
)

# Loan status
df["loan_status"] = np.where(
    df["dpd"] >= 90,
    "Default",
    np.where(
        df["dpd"] >= 30,
        "Delinquent",
        "Active"
    )
)

# Arrange columns
df = df[
    [
        "loan_id",
        "customer_id",
        "loan_type",
        "age",
        "gender",
        "employment_type",
        "annual_income",
        "credit_score",
        "loan_amount",
        "outstanding_amount",
        "interest_rate",
        "loan_term",
        "region",
        "application_date",
        "disbursement_date",
        "last_payment_date",
        "monthly_installment",
        "total_payments",
        "missed_payments",
        "dpd",
        "previous_dpd",
        "collateral_value",
        "loan_status"
    ]
]

# Save dataset
output_path = "data/loan_portfolio.csv"
df.to_csv(output_path, index=False)

print(f"Dataset created successfully: {output_path}")
print(f"Total records: {len(df)}")
print("\nLoan status distribution:")
print(df["loan_status"].value_counts())