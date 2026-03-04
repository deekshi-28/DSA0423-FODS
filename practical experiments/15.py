import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Sample Data (Recovery Scores)
control_group = np.array([50, 52, 48, 47, 49, 51, 46, 50])
treatment_group = np.array([60, 62, 58, 65, 63, 59, 61, 64])

# Perform Independent t-test
t_statistic, p_value = stats.ttest_ind(control_group, treatment_group)

print("T-Statistic:", t_statistic)
print("P-Value:", p_value)

# Decision
alpha = 0.05
if p_value < alpha:
    print("Reject Null Hypothesis: Treatment is statistically significant.")
else:
    print("Fail to Reject Null Hypothesis: No significant difference.")

# Visualization
means = [np.mean(control_group), np.mean(treatment_group)]
labels = ['Control Group', 'Treatment Group']

plt.figure()
plt.bar(labels, means)
plt.title("Comparison of Control vs Treatment Group")
plt.ylabel("Average Recovery Score")
plt.show()