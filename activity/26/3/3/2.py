# ===============================
# Activity 2: Outlier Treatment
# ===============================

import numpy as np
import pandas as pd

# House prices in $100,000s
prices = np.array([2.5, 3.0, 2.8, 3.2, 15.0, 2.9, 3.1, 2.7, 100.0])

df = pd.DataFrame(prices, columns=["Price"])

print("Original Data:")
print(df)

# -------------------------------
# 1. Identify Outliers (Z-score)
# -------------------------------

from scipy.stats import zscore

df["Z_score"] = zscore(df["Price"])

outliers = df[np.abs(df["Z_score"]) > 3]

print("\nDetected Outliers (|Z| > 3):")
print(outliers)

# -------------------------------
# 2. Treat the 100.0 typo
# Replace 100.0 with correct 10.0
# -------------------------------

df_corrected = df.copy()
df_corrected.loc[df_corrected["Price"] == 100.0, "Price"] = 10.0

print("\nAfter Correcting 100.0 to 10.0:")
print(df_corrected)

# -------------------------------
# 3. Decision about 15.0
# -------------------------------

# Option 1: Keep it (legitimate mansion)
print("\nKeeping 15.0 since it is legitimate.")

# Optional: Cap extreme values (example using 95th percentile)

upper_cap = np.percentile(df_corrected["Price"], 95)
df_corrected["Capped_Price"] = np.where(
    df_corrected["Price"] > upper_cap,
    upper_cap,
    df_corrected["Price"]
)

print("\nData after optional capping at 95th percentile:")
print(df_corrected)