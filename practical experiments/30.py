import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("C:/Users/deek/Downloads/fods/practical experiments/shoe_sales.csv")

print("Frequency Distribution of Shoe Sizes:")
print(data)

# Bar chart
plt.bar(data['shoe_size'], data['quantity'])
plt.title("Frequency Distribution of Shoe Sizes Sold")
plt.xlabel("Shoe Size")
plt.ylabel("Quantity Sold")
plt.show()