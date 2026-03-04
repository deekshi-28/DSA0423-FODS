# ===============================
# Activity 1: EDA with Shape & Outliers
# ===============================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis, zscore

# -------------------------------
# 1. Generate Synthetic Data
# -------------------------------

np.random.seed(42)

# Normal distribution
normal_data = np.random.normal(loc=50, scale=5, size=1000)

# Exponential distribution (right skewed)
skewed_data = np.random.exponential(scale=1, size=1000)

# -------------------------------
# 2. Visualization
# -------------------------------

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
sns.histplot(normal_data, kde=True)
plt.title("Normal Distribution")

plt.subplot(1,2,2)
sns.histplot(skewed_data, kde=True)
plt.title("Exponential Distribution (Right Skewed)")

plt.tight_layout()
plt.show()

# -------------------------------
# 3. Calculate Skewness & Kurtosis
# -------------------------------

print("Normal Data Skewness:", skew(normal_data))
print("Skewed Data Skewness:", skew(skewed_data))

print("\nNormal Data Kurtosis (Fisher):", kurtosis(normal_data))
print("Skewed Data Kurtosis (Fisher):", kurtosis(skewed_data))

# Note:
# Fisher's definition → 0 means normal distribution

# -------------------------------
# 4. Outlier Detection (Z-score)
# -------------------------------

def detect_outliers(data):
    z_scores = zscore(data)
    outliers = np.abs(z_scores) > 3
    return np.sum(outliers)

outlier_count = detect_outliers(skewed_data)

print("\nNumber of outliers in skewed_data (|Z| > 3):", outlier_count)