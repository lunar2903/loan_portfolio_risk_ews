import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/loan_portfolio_clean.csv")

print("=" * 50)
print("LOAN PORTFOLIO RISK METRICS")
print("=" * 50)

# --------------------------------
# 1. Portfolio Default Rate
# --------------------------------

total_loans = len(df)

defaulted_loans = (
    df["loan_status"] == "Default"
).sum()

default_rate = (
    defaulted_loans / total_loans
) * 100

print("\nPORTFOLIO DEFAULT RATE")

print("Total Loans:", total_loans)
print("Defaulted Loans:", defaulted_loans)
print("Default Rate:", round(default_rate, 2), "%")

# --------------------------------
# 2. Portfolio Exposure
# --------------------------------

total_exposure = df["outstanding_amount"].sum()

default_exposure = df.loc[
    df["loan_status"] == "Default",
    "outstanding_amount"
].sum()

default_exposure_rate = (
    default_exposure / total_exposure
) * 100

print("\nPORTFOLIO EXPOSURE")

print(
    "Total Outstanding Exposure:",
    round(total_exposure, 2)
)

print(
    "Defaulted Exposure:",
    round(default_exposure, 2)
)

print(
    "Default Exposure Rate:",
    round(default_exposure_rate, 2),
    "%"
)

# --------------------------------
# 3. DPD Risk Metrics
# --------------------------------

average_dpd = df["dpd"].mean()

maximum_dpd = df["dpd"].max()

dpd_over_30 = (
    df["dpd"] > 30
).sum()

dpd_over_90 = (
    df["dpd"] >= 90
).sum()

print("\nDPD RISK METRICS")

print(
    "Average DPD:",
    round(average_dpd, 2)
)

print(
    "Maximum DPD:",
    maximum_dpd
)

print(
    "Loans with DPD > 30:",
    dpd_over_30
)

print(
    "Loans with DPD >= 90:",
    dpd_over_90
)

# --------------------------------
# 4. DPD Buckets for Roll Rate
# --------------------------------

bins = [-1, 0, 30, 60, 89, float("inf")]

labels = [
    "Current",
    "1-30",
    "31-60",
    "61-89",
    "90+"
]

df["previous_dpd_bucket"] = pd.cut(
    df["previous_dpd"],
    bins=bins,
    labels=labels
)

df["current_dpd_bucket"] = pd.cut(
    df["dpd"],
    bins=bins,
    labels=labels
)

print("\nROLL RATE TRANSITIONS")

roll_rate_table = pd.crosstab(
    df["previous_dpd_bucket"],
    df["current_dpd_bucket"]
)

print(roll_rate_table)

# --------------------------------
# 5. Roll Rate Percentages
# --------------------------------

roll_rate_percentage = (
    roll_rate_table
    .div(roll_rate_table.sum(axis=1), axis=0)
    * 100
)

print("\nROLL RATE PERCENTAGES")

print(
    roll_rate_percentage.round(2)
)

# --------------------------------
# 6. Portfolio Probability of Default
# --------------------------------

total_loans = len(df)

defaulted_loans = (
    df["loan_status"] == "Default"
).sum()

portfolio_pd = (
    defaulted_loans / total_loans
) * 100

print("\nPORTFOLIO PROBABILITY OF DEFAULT")

print(
    "Total Loans:",
    total_loans
)

print(
    "Defaulted Loans:",
    defaulted_loans
)

print(
    "Portfolio PD:",
    round(portfolio_pd, 2),
    "%"
)

# --------------------------------
# 7. Loss Given Default (LGD)
# --------------------------------

defaulted = df[
    df["loan_status"] == "Default"
].copy()

defaulted["recovery"] = defaulted[
    ["outstanding_amount", "collateral_value"]
].min(axis=1)

defaulted["loss_amount"] = (
    defaulted["outstanding_amount"]
    - defaulted["recovery"]
)

defaulted["lgd"] = (
    defaulted["loss_amount"]
    / defaulted["outstanding_amount"]
)

average_lgd = defaulted["lgd"].mean() * 100

total_default_exposure = (
    defaulted["outstanding_amount"].sum()
)

total_loss = (
    defaulted["loss_amount"].sum()
)

portfolio_lgd = (
    total_loss
    / total_default_exposure
) * 100

print("\nLOSS GIVEN DEFAULT (LGD)")

print(
    "Defaulted Loans:",
    len(defaulted)
)

print(
    "Default Exposure:",
    round(total_default_exposure, 2)
)

print(
    "Estimated Loss:",
    round(total_loss, 2)
)

print(
    "Average LGD:",
    round(average_lgd, 2),
    "%"
)

print(
    "Portfolio LGD:",
    round(portfolio_lgd, 2),
    "%"
)

# --------------------------------
# 8. Expected Loss (EL)
# --------------------------------

pd_rate = portfolio_pd / 100

lgd_rate = portfolio_lgd / 100

ead = total_exposure

expected_loss = (
    pd_rate
    * lgd_rate
    * ead
)

print("\nEXPECTED LOSS")

print(
    "PD:",
    round(pd_rate * 100, 2),
    "%"
)

print(
    "LGD:",
    round(lgd_rate * 100, 2),
    "%"
)

print(
    "EAD:",
    round(ead, 2)
)

print(
    "Expected Loss:",
    round(expected_loss, 2)
)

# --------------------------------
# 9. Risk Segmentation
# --------------------------------

df["risk_score"] = 0

# Credit Score
df.loc[df["credit_score"] < 580, "risk_score"] += 2
df.loc[
    df["credit_score"].between(580, 669),
    "risk_score"
] += 1

# DPD
df.loc[df["dpd"] >= 90, "risk_score"] += 3
df.loc[df["dpd"].between(30, 89), "risk_score"] += 2
df.loc[df["dpd"].between(1, 29), "risk_score"] += 1

# Missed Payments
df.loc[df["missed_payments"] >= 5, "risk_score"] += 2
df.loc[
    df["missed_payments"].between(3, 4),
    "risk_score"
] += 1

# LTV
df["ltv"] = (
    df["loan_amount"]
    / df["collateral_value"]
)

df.loc[df["ltv"] > 1.25, "risk_score"] += 2
df.loc[
    df["ltv"].between(1.00, 1.25),
    "risk_score"
] += 1

# Risk Category
df["risk_category"] = pd.cut(
    df["risk_score"],
    bins=[-1, 2, 5, float("inf")],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

print("\nRISK SEGMENTATION")

print(
    df["risk_category"].value_counts()
)

print("\nAverage Risk Score:")

print(
    round(df["risk_score"].mean(), 2)
)

# --------------------------------
# 10. Risk Category Default Rate
# --------------------------------

risk_default_rate = (
    df.groupby("risk_category", observed=False)["loan_status"]
    .apply(lambda x: (x == "Default").mean() * 100)
)

print("\nDEFAULT RATE BY RISK CATEGORY")

print(
    risk_default_rate.round(2)
)

