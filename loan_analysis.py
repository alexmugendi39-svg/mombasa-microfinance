"""
Mombasa Microfinance - Loan Repayment Analysis
150 fictional loan records
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. CREATE DATASET (150 fictional loans)
np.random.seed(42)
n = 150

amounts = np.concatenate([
    np.random.lognormal(mean=np.log(35000), sigma=0.55, size=135),
    np.random.uniform(150000, 350000, size=10),
    np.random.uniform(3000, 8000, size=5)
])
np.random.shuffle(amounts)
amounts = np.round(amounts, 0).astype(int)

days = np.round(14 + 0.00008 * amounts + np.random.normal(0, 6, size=n)).astype(int)
days = np.clip(days, 3, 60)

counties = np.random.choice(
    ["Mombasa", "Kwale", "Kilifi", "Tana River", "Lamu", "Taita-Taveta"],
    size=n, p=[0.55, 0.15, 0.15, 0.05, 0.05, 0.05]
)

sales = pd.DataFrame({
    "loan_id": [f"MSA-{i+1:03d}" for i in range(n)],
    "amount_kes": amounts,
    "days_to_first_repayment": days,
    "county": counties
})

# 2. FULL STATISTICAL SUMMARY
print("=== FULL SUMMARY ===")
print(sales.describe(include="all"))
print("\n=== LOAN AMOUNT SUMMARY ===")
print(sales["amount_kes"].describe())

# 3. OUTLIERS - IQR METHOD
Q1 = sales["amount_kes"].quantile(0.25)
Q3 = sales["amount_kes"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = sales[(sales["amount_kes"] < lower) | (sales["amount_kes"] > upper)]
print(f"\nQ1={Q1}, Q3={Q3}, IQR={IQR}")
print(f"Lower fence={lower:.2f}, Upper fence={upper:.2f}")
print(f"Outliers found: {len(outliers)}")
print(outliers[["loan_id", "amount_kes", "days_to_first_repayment", "county"]])

# 4. CORRELATION
corr = sales["amount_kes"].corr(sales["days_to_first_repayment"])
print(f"\nCorrelation (amount vs days to first repayment): {corr:.3f}")
print("Plain sentence: Larger loans tend to take longer before the first repayment.")

# 5. HISTOGRAM
plt.figure(figsize=(10, 6))
plt.hist(sales["amount_kes"], bins=20, edgecolor="black")
plt.axvline(sales["amount_kes"].mean(), color="red", linestyle="--", label=f"Mean: {sales['amount_kes'].mean():,.0f}")
plt.axvline(sales["amount_kes"].median(), color="green", linestyle="--", label=f"Median: {sales['amount_kes'].median():,.0f}")
plt.title("Distribution of Loan Amounts - Mombasa Microfinance (n=150)")
plt.xlabel("Loan Amount (KES)")
plt.ylabel("Number of Loans")
plt.legend()
plt.tight_layout()
plt.savefig("loan_amounts_histogram.png", dpi=150)
plt.show()
