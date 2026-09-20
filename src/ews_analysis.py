import pandas as pd

# Load EWS dataset
df = pd.read_csv("data/ews_alerts.csv")

print("=" * 50)
print("EWS ANALYSIS")
print("=" * 50)

# --------------------------------
# 1. Alert Distribution
# --------------------------------

print("\nAlert Distribution:")

alert_distribution = (
    df["ews_alert_level"]
    .value_counts()
)

print(alert_distribution)


# --------------------------------
# 2. Alert Distribution %
# --------------------------------

print("\nAlert Distribution (%):")

alert_percentage = (
    df["ews_alert_level"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print(alert_percentage)


# --------------------------------
# 3. Exposure by Alert Level
# --------------------------------

print("\nExposure by Alert Level:")

exposure_by_alert = (
    df.groupby("ews_alert_level")["outstanding_amount"]
    .sum()
    .sort_values(ascending=False)
)

print(exposure_by_alert)


# --------------------------------
# 4. Average DPD by Alert Level
# --------------------------------

print("\nAverage DPD by Alert Level:")

avg_dpd = (
    df.groupby("ews_alert_level")["dpd"]
    .mean()
    .round(2)
)

print(avg_dpd)# --------------------------------
# 5. Critical Loan Analysis
# --------------------------------

print("\n" + "=" * 50)
print("CRITICAL LOANS")
print("=" * 50)

critical_loans = (
    df[df["ews_alert_level"] == "Critical"]
    [
        [
            "loan_id",
            "customer_id",
            "loan_type",
            "loan_status",
            "outstanding_amount",
            "credit_score",
            "dpd",
            "missed_payments",
            "ltv",
            "ews_alert_level"
        ]
    ]
    .sort_values(
        "outstanding_amount",
        ascending=False
    )
)

print("\nTop 10 Critical Loans by Outstanding Exposure:")

print(
    critical_loans.head(10).to_string(index=False)
)

# --------------------------------
# 6. Customer Risk Concentration
# --------------------------------

print("\n" + "=" * 50)
print("CUSTOMER RISK CONCENTRATION")
print("=" * 50)

customer_risk = (
    df.groupby("customer_id")
    .agg(
        total_loans=("loan_id", "count"),
        critical_loans=("ews_alert_level", lambda x: (x == "Critical").sum()),
        total_exposure=("outstanding_amount", "sum"),
        max_dpd=("dpd", "max"),
        total_missed_payments=("missed_payments", "sum")
    )
    .reset_index()
)

customer_risk = customer_risk[
    customer_risk["critical_loans"] > 0
].sort_values(
    "total_exposure",
    ascending=False
)

print("\nTop 10 Customers with Critical Loans by Exposure:")

print(
    customer_risk.head(10).to_string(index=False)
)

# --------------------------------
# 7. Risk Exposure Concentration
# --------------------------------

print("\n" + "=" * 50)
print("RISK EXPOSURE CONCENTRATION")
print("=" * 50)

total_exposure = df["outstanding_amount"].sum()

exposure_concentration = (
    df.groupby("ews_alert_level")["outstanding_amount"]
    .sum()
    .reset_index()
)

exposure_concentration["exposure_percentage"] = (
    exposure_concentration["outstanding_amount"]
    / total_exposure
    * 100
).round(2)

exposure_concentration = exposure_concentration.sort_values(
    "outstanding_amount",
    ascending=False
)

print("\nExposure by EWS Alert Level:")

print(
    exposure_concentration.to_string(index=False)
)

# --------------------------------
# High-Risk Exposure
# --------------------------------

high_risk_exposure = df[
    df["ews_alert_level"].isin(["Critical", "Warning"])
]["outstanding_amount"].sum()

high_risk_percentage = (
    high_risk_exposure
    / total_exposure
    * 100
)

print("\nCritical + Warning Exposure:")
print(f"₹{high_risk_exposure:,.2f}")

print("\nCritical + Warning Exposure %:")
print(f"{high_risk_percentage:.2f}%")
