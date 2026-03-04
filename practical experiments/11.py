import numpy as np

# Fuel efficiency values (MPG)
fuel_efficiency = np.array([18, 22, 25, 30, 28, 24])

# 1️⃣ Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# 2️⃣ Calculate percentage improvement
old_model = fuel_efficiency[0]   # 18 MPG
new_model = fuel_efficiency[3]   # 30 MPG

percentage_improvement = ((new_model - old_model) / old_model) * 100

# Display Results
print("Fuel Efficiency Data (MPG):", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency, "MPG")
print("Percentage Improvement from Model 1 to Model 4:",
      percentage_improvement, "%")