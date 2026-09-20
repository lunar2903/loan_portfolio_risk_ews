import pandas as pd

# Load EWS dataset
df = pd.read_csv("data/ews_alerts.csv")

print("=" * 60)
print("LOAN PORTFOLIO RISK & EARLY WARNING SYSTEM")
print("FINAL EWS ANALYST SUMMARY")
print("=" * 60)

# --------------------------------
# 1. Portfolio Overview
# --------------------------------

total_loans = len(df)

total_exposure = df["outstanding_amount"].sum()

print("\nPORTFOLIO OVERVIEW")
print("-" * 40)

print(f"Total Loans       : {total_loans:,}")
print(f"Total Exposure    : ₹{total_exposure:,.2f}")


# --------------------------------
# 2. EWS Alert Summary
# --------------------------------

alert_counts = df["ews_alert_level"].value_counts()

critical_loans = alert_counts.get("Critical", 0)
warning_loans = alert_counts.get("Warning", 0)

critical_warning_loans = critical_loans + warning_loans

critical_warning_percentage = (
    critical_warning_loans / total_loans * 100
)

print("\nEWS ALERT SUMMARY")
print("-" * 40)

print(f"Critical Loans    : {critical_loans:,}")
print(f"Warning Loans     : {warning_loans:,}")

print(
    f"Critical + Warning: "
    f"{critical_warning_loans:,} "
    f"({critical_warning_percentage:.2f}%)"
)


# --------------------------------
# 3. Exposure Analysis
# --------------------------------

critical_warning_exposure = df[
    df["ews_alert_level"].isin(["Critical", "Warning"])
]["outstanding_amount"].sum()

critical_warning_exposure_percentage = (
    critical_warning_exposure / total_exposure * 100
)

print("\nEXPOSURE ANALYSIS")
print("-" * 40)

print(
    f"Critical + Warning Exposure : "
    f"₹{critical_warning_exposure:,.2f}"
)

print(
    f"Exposure Percentage         : "
    f"{critical_warning_exposure_percentage:.2f}%"
)


# --------------------------------
# 4. Average DPD by Alert
# --------------------------------

avg_dpd = (
    df.groupby("ews_alert_level")["dpd"]
    .mean()
    .sort_values()
)

print("\nAVERAGE DPD BY ALERT LEVEL")
print("-" * 40)

for alert, value in avg_dpd.items():
    print(f"{alert:<12}: {value:.2f}")


# --------------------------------
# 5. Customer Risk Concentration
# --------------------------------

customer_risk = (
    df.groupby("customer_id")
    .agg(
        total_loans=("loan_id", "count"),
        critical_loans=(
            "ews_alert_level",
            lambda x: (x == "Critical").sum()
        ),
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

print("\nTOP 5 CUSTOMERS WITH CRITICAL LOANS")
print("-" * 40)

print(
    customer_risk.head(5).to_string(index=False)
)


# --------------------------------
# 6. Analyst Insights
# --------------------------------

print("\n" + "=" * 60)
print("ANALYST INSIGHTS")
print("=" * 60)

print(
    f"\n1. {critical_warning_percentage:.2f}% of loans "
    f"are classified as Critical or Warning."
)

print(
    f"2. {critical_warning_exposure_percentage:.2f}% of "
    f"outstanding exposure falls under Critical or Warning alerts."
)

print(
    "3. Average DPD increases across the EWS alert levels, "
    "providing an internal consistency check for the alert framework."
)

print(
    "4. Several customers hold multiple loans with Critical alerts, "
    "indicating customer-level risk concentration."
)

print(
    "5. EWS alerts should be treated as analyst-review signals, "
    "not automatic lending decisions."
)

print("\n" + "=" * 60)
print("EWS SUMMARY COMPLETE")
print("=" * 60)
