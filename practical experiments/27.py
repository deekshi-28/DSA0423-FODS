import numpy as np
from scipy import stats

# Sample revenue data (example)
revenue = np.array([120, 150, 130, 170, 160, 140, 155, 165, 175, 145])

# Sample size
n = len(revenue)

# Mean and standard deviation
mean = np.mean(revenue)
std_dev = np.std(revenue, ddof=1)

# Confidence interval (95%)
confidence = 0.95
z_value = stats.norm.ppf((1 + confidence) / 2)

# Standard error
standard_error = std_dev / np.sqrt(n)

# Margin of error
margin = z_value * standard_error

lower_bound = mean - margin
upper_bound = mean + margin

print("Sample Mean:", mean)
print("95% Confidence Interval:", (lower_bound, upper_bound))