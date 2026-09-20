import pandas as pd

# Load raw data
df = pd.read_csv("data/loan_portfolio.csv")

print("=" * 50)
print("DATA CLEANING & VALIDATION")
print("=" * 50)

# -----------------------------
# 1. Convert date columns
# -----------------------------

date_columns = [
    "application_date",
    "disbursement_date",
    "last_payment_date"
]

for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")


# -----------------------------
# 2. Check missing values
# -----------------------------

print("\nMissing values after date conversion:")
print(df.isnull().sum())


# -----------------------------
# 3. Check duplicate records
# -----------------------------

print("\nDuplicate rows:", df.duplicated().sum())
print("Duplicate loan IDs:", df["loan_id"].duplicated().sum())


# -----------------------------
# 4. Business rule validation
# -----------------------------

print("\nBUSINESS RULE CHECKS")

checks = {
    "Invalid age": (df["age"] < 18) | (df["age"] > 100),
    "Invalid credit score": (df["credit_score"] < 300) | (df["credit_score"] > 850),
    "Invalid loan amount": df["loan_amount"] <= 0,
    "Invalid outstanding amount": df["outstanding_amount"] < 0,
    "Outstanding greater than loan": (
        df["outstanding_amount"] > df["loan_amount"]
    ),
    "Invalid interest rate": df["interest_rate"] <= 0,
    "Invalid loan term": df["loan_term"] <= 0,
    "Invalid missed payments": df["missed_payments"] < 0,
    "Invalid DPD": df["dpd"] < 0,
    "Invalid previous DPD": df["previous_dpd"] < 0,
    "Invalid collateral value": df["collateral_value"] < 0,
}

for check_name, condition in checks.items():
    print(f"{check_name}: {condition.sum()}")


# -----------------------------
# 5. Date validation
# -----------------------------

invalid_dates = (
    (df["disbursement_date"] < df["application_date"]) |
    (df["last_payment_date"] < df["disbursement_date"])
)

print("\nInvalid date sequences:", invalid_dates.sum())


# -----------------------------
# 6. Loan status validation
# -----------------------------

status_mismatch = (
    ((df["dpd"] >= 90) & (df["loan_status"] != "Default")) |
    ((df["dpd"].between(30, 89)) & (df["loan_status"] != "Delinquent")) |
    ((df["dpd"] < 30) & (df["loan_status"] != "Active"))
)

print("Loan status mismatches:", status_mismatch.sum())


# -----------------------------
# 7. Save clean dataset
# -----------------------------

df.to_csv(
    "data/loan_portfolio_clean.csv",
    index=False
)

print("\nClean dataset saved:")
print("data/loan_portfolio_clean.csv")

print("\n" + "=" * 50)
print("CLEANING & VALIDATION COMPLETE")
print("=" * 50)