import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("C:/Users/deek/Downloads/fods/practical experiments/car_data.csv")

# Multivariate Scatter Plot
plt.scatter(data['Horsepower'], data['Mileage'])
plt.title("Horsepower vs Mileage")
plt.xlabel("Horsepower")
plt.ylabel("Mileage")
plt.show()

# Scatter Plot Matrix
sns.pairplot(data)
plt.show()