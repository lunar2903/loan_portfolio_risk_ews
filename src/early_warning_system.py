import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/loan_portfolio_clean.csv")

print("=" * 50)
print("EARLY WARNING SYSTEM")
print("=" * 50)

# --------------------------------
# 1. DPD Deterioration Signal
# --------------------------------

df["dpd_change"] = (
    df["dpd"] - df["previous_dpd"]
)

df["dpd_deterioration"] = (
    df["dpd_change"] > 0
)

print("\nEWS - DPD DETERIORATION")

print(
    "Loans with worsening DPD:",
    df["dpd_deterioration"].sum()
)

print(
    "Loans with improving/stable DPD:",
    (~df["dpd_deterioration"]).sum()
)

# --------------------------------
# 2. Missed Payment Signal
# --------------------------------

df["missed_payment_signal"] = pd.cut(
    df["missed_payments"],
    bins=[-1, 0, 2, 4, float("inf")],
    labels=[
        "No Signal",
        "Watch",
        "Warning",
        "Critical"
    ]
)

print("\nEWS - MISSED PAYMENT SIGNAL")

print(
    df["missed_payment_signal"].value_counts()
)

# --------------------------------
# 3. LTV Risk Signal
# --------------------------------

df["ltv"] = (
    df["loan_amount"]
    / df["collateral_value"]
)

df["ltv_signal"] = pd.cut(
    df["ltv"],
    bins=[-float("inf"), 0.75, 1.00, 1.25, float("inf")],
    labels=[
        "No Signal",
        "Watch",
        "Warning",
        "Critical"
    ]
)

print("\nEWS - LTV SIGNAL")

print(
    df["ltv_signal"].value_counts()
)

# --------------------------------
# 4. Credit Score Risk Signal
# --------------------------------

df["credit_score_signal"] = pd.cut(
    df["credit_score"],
    bins=[-float("inf"), 579, 669, 739, float("inf")],
    labels=[
        "Critical",
        "Warning",
        "Watch",
        "No Signal"
    ]
)

print("\nEWS - CREDIT SCORE SIGNAL")

print(
    df["credit_score_signal"].value_counts()
)

# --------------------------------
# 5. Final EWS Alert Level
# --------------------------------

def get_ews_alert(row):

    critical_signals = 0
    warning_signals = 0
    watch_signals = 0

    # DPD
    if row["dpd"] >= 90:
        critical_signals += 1
    elif row["dpd"] >= 30:
        warning_signals += 1
    elif row["dpd"] > 0:
        watch_signals += 1

    # Missed Payments
    if row["missed_payments"] >= 5:
        critical_signals += 1
    elif row["missed_payments"] >= 3:
        warning_signals += 1
    elif row["missed_payments"] >= 1:
        watch_signals += 1

    # LTV
    if row["ltv"] > 1.25:
        critical_signals += 1
    elif row["ltv"] > 1.00:
        warning_signals += 1
    elif row["ltv"] > 0.75:
        watch_signals += 1

    # Credit Score
    if row["credit_score"] < 580:
        critical_signals += 1
    elif row["credit_score"] < 670:
        warning_signals += 1
    elif row["credit_score"] < 740:
        watch_signals += 1

    # DPD deterioration
    if row["dpd_deterioration"]:
        warning_signals += 1

    # Final Alert
    if critical_signals >= 1:
        return "Critical"
    elif warning_signals >= 1:
        return "Warning"
    elif watch_signals >= 1:
        return "Watch"
    else:
        return "No Alert"


df["ews_alert_level"] = df.apply(
    get_ews_alert,
    axis=1
)

print("\nFINAL EWS ALERT LEVEL")

print(
    df["ews_alert_level"].value_counts()
)

# --------------------------------
# Risk Score & Risk Category
# --------------------------------

df["risk_score"] = 0

# Credit score
df.loc[df["credit_score"] < 580, "risk_score"] += 2
df.loc[
    df["credit_score"].between(580, 669),
    "risk_score"
] += 1

# DPD
df.loc[df["dpd"] >= 90, "risk_score"] += 3
df.loc[
    df["dpd"].between(30, 89),
    "risk_score"
] += 2
df.loc[
    df["dpd"].between(1, 29),
    "risk_score"
] += 1

# Missed payments
df.loc[df["missed_payments"] >= 5, "risk_score"] += 2
df.loc[
    df["missed_payments"].between(3, 4),
    "risk_score"
] += 1

# LTV
df.loc[df["ltv"] > 1.25, "risk_score"] += 2
df.loc[
    df["ltv"].between(1.00, 1.25),
    "risk_score"
] += 1

df["risk_category"] = pd.cut(
    df["risk_score"],
    bins=[-1, 2, 5, float("inf")],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

# --------------------------------
# 6. Create Final EWS Dataset
# --------------------------------

ews_columns = [
    "loan_id",
    "customer_id",
    "loan_type",
    "employment_type",
    "region",
    "loan_status",
    "credit_score",
    "loan_amount",
    "outstanding_amount",
    "collateral_value",
    "ltv",
    "missed_payments",
    "dpd",
    "previous_dpd",
    "dpd_change",
    "risk_score",
    "risk_category",
    "ews_alert_level"
]

ews_alerts = df[ews_columns].copy()

ews_alerts.to_csv(
    "data/ews_alerts.csv",
    index=False
)

print("\nFinal EWS dataset created successfully.")
print("Saved to: data/ews_alerts.csv")
print("Rows:", len(ews_alerts))
print("Columns:", len(ews_alerts.columns))

