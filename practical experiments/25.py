import numpy as np

# Population dataset
population = np.array([10, 12, 15, 18, 20, 22, 25, 28, 30, 35])

# Random sampling (select 5 values)
sample = np.random.choice(population, size=5)

# Mean estimation
mean_estimate = np.mean(sample)

# Variance estimation
variance_estimate = np.var(sample)

print("Population Data:", population)
print("Sample Data:", sample)

print("\nEstimated Mean:", mean_estimate)
print("Estimated Variance:", variance_estimate)