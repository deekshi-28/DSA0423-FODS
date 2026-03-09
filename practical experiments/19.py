import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("transaction_data.csv")

# Select features
X = data[['total_spent','items_purchased']]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3)
data['Cluster'] = kmeans.fit_predict(X)

print("Customer Segmentation:")
print(data)

# Scatter plot visualization
plt.scatter(data['total_spent'], data['items_purchased'], c=data['Cluster'])
plt.title("Customer Segmentation using K-Means")
plt.xlabel("Total Amount Spent")
plt.ylabel("Items Purchased")
plt.show()