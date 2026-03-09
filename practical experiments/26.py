import numpy as np
import matplotlib.pyplot as plt

# Temperature data (°C)
temperature = np.array([25, 27, 30, 32, 35, 33, 31, 29])

# Rainfall data (mm)
rainfall = np.array([10, 12, 15, 18, 25, 20, 17, 14])

# Calculate correlation coefficient
correlation_matrix = np.corrcoef(temperature, rainfall)
correlation = correlation_matrix[0,1]

print("Correlation Coefficient:", correlation)

# Scatter plot
plt.scatter(temperature, rainfall)
plt.title("Temperature vs Rainfall")
plt.xlabel("Temperature (°C)")
plt.ylabel("Rainfall (mm)")
plt.show()