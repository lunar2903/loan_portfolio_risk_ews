import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import ttest_ind
from scipy.stats import chi2_contingency, ttest_ind, pearsonr

# Load clean dataset
df = pd.read_csv("data/loan_portfolio_clean.csv")

print("=" * 50)
print("HYPOTHESIS TESTING")
print("=" * 50)

# Create missed payment groups
df["missed_payment_band"] = pd.cut(
    df["missed_payments"],
    bins=[-1, 0, 2, 4, float("inf")],
    labels=[
        "No Missed Payments",
        "Low (1-2)",
        "Moderate (3-4)",
        "High (5+)"
    ]
)

# Create default indicator
df["default"] = (df["loan_status"] == "Default").astype(int)

# Create contingency table
contingency_table = pd.crosstab(
    df["missed_payment_band"],
    df["default"]
)

print("\nContingency Table:")
print(contingency_table)

# Chi-Square Test
chi2, p_value, degrees_of_freedom, expected = chi2_contingency(
    contingency_table
)

print("\nChi-Square Statistic:", chi2)
print("P-value:", p_value)
print("Degrees of Freedom:", degrees_of_freedom)

# Decision
if p_value < 0.05:
    print("\nResult: Reject the null hypothesis.")
else:
    print("\nResult: Fail to reject the null hypothesis.")

# Credit score bands
df["credit_band"] = pd.cut(
    df["credit_score"],
    bins=[300, 579, 669, 739, 799, 850],
    labels=["Poor", "Fair", "Good", "Very Good", "Excellent"]
)

# Contingency table
credit_table = pd.crosstab(
    df["credit_band"],
    df["default"]
)

print("\nCredit Score Contingency Table:")
print(credit_table)

# Chi-Square Test
chi2_credit, p_credit, dof_credit, expected_credit = chi2_contingency(
    credit_table
)

print("\nCredit Score Chi-Square Statistic:", chi2_credit)
print("Credit Score P-value:", p_credit)
print("Degrees of Freedom:", dof_credit)

if p_credit < 0.05:
    print("\nResult: Reject the null hypothesis.")
else:
    print("\nResult: Fail to reject the null hypothesis.")

# --------------------------------
# T-Test: Loan Amount vs Default
# --------------------------------

defaulted_loans = df.loc[
    df["default"] == 1,
    "loan_amount"
]

non_defaulted_loans = df.loc[
    df["default"] == 0,
    "loan_amount"
]

# Perform independent samples t-test
t_statistic, p_value_ttest = ttest_ind(
    defaulted_loans,
    non_defaulted_loans,
    equal_var=False
)

print("\nT-Test: Loan Amount vs Default")

print("Average loan amount - Defaulted:",
      defaulted_loans.mean())

print("Average loan amount - Non-defaulted:",
      non_defaulted_loans.mean())

print("T-Statistic:", t_statistic)
print("P-value:", p_value_ttest)

if p_value_ttest < 0.05:
    print("\nResult: Reject the null hypothesis.")
else:
    print("\nResult: Fail to reject the null hypothesis.")

# --------------------------------
# T-Test: DPD vs Default
# --------------------------------

defaulted_dpd = df.loc[
    df["default"] == 1,
    "dpd"
]

non_defaulted_dpd = df.loc[
    df["default"] == 0,
    "dpd"
]

t_statistic_dpd, p_value_dpd = ttest_ind(
    defaulted_dpd,
    non_defaulted_dpd,
    equal_var=False
)

print("\nT-Test: DPD vs Default")

print("Average DPD - Defaulted:",
      defaulted_dpd.mean())

print("Average DPD - Non-defaulted:",
      non_defaulted_dpd.mean())

print("T-Statistic:", t_statistic_dpd)
print("P-value:", p_value_dpd)

if p_value_dpd < 0.05:
    print("\nResult: Reject the null hypothesis.")
else:
    print("\nResult: Fail to reject the null hypothesis.")

# --------------------------------
# Pearson Correlation Test
# --------------------------------

correlation, p_value_corr = pearsonr(
    df["credit_score"],
    df["loan_amount"]
)

print("\nPearson Correlation: Credit Score vs Loan Amount")

print("Correlation coefficient:", correlation)
print("P-value:", p_value_corr)

if p_value_corr < 0.05:
    print("\nResult: Reject the null hypothesis.")
else:
    print("\nResult: Fail to reject the null hypothesis.")