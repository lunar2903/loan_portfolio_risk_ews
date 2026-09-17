import pandas as pd

# Load raw dataset
df = pd.read_csv("data/loan_portfolio.csv")

print("=" * 50)
print("LOAN PORTFOLIO DATA PROFILE")
print("=" * 50)

# 1. Dataset dimensions
print("\n1. DATASET SIZE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Column names
print("\n2. COLUMNS")
print(df.columns.tolist())

# 3. Data types
print("\n3. DATA TYPES")
print(df.dtypes)

# 4. Missing values
print("\n4. MISSING VALUES")
print(df.isnull().sum())

# 5. Duplicate rows
print("\n5. DUPLICATES")
print("Duplicate rows:", df.duplicated().sum())

# 6. Duplicate loan IDs
print("\n6. DUPLICATE LOAN IDs")
print("Duplicate loan IDs:", df["loan_id"].duplicated().sum())

# 7. Numerical summary
print("\n7. NUMERICAL SUMMARY")
print(df.describe())

# 8. Categorical summary
print("\n8. CATEGORICAL SUMMARY")

for column in df.select_dtypes(include="object").columns:
    print(f"\n{column}:")
    print(df[column].value_counts())

print("\n" + "=" * 50)
print("PROFILING COMPLETE")
print("=" * 50)