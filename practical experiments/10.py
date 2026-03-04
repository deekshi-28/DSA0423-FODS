import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [25, 27, 30, 33, 35, 36, 34, 33, 32, 30, 28, 26]
rainfall = [10, 20, 15, 30, 45, 60, 120, 150, 100, 80, 40, 20]

# 🔹 Line Plot for Temperature
plt.figure()
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature Data")
plt.xlabel("Months")
plt.ylabel("Temperature (°C)")
plt.show()

# 🔹 Scatter Plot for Rainfall
plt.figure()
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall Data")
plt.xlabel("Months")
plt.ylabel("Rainfall (mm)")
plt.show()