import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("customer_data.csv")

# Select features
X = data[['total_spent','visit_frequency']]

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3)
data['Cluster'] = kmeans.fit_predict(X)

print("Customer Clusters:")
print(data)

# Visualization
plt.scatter(data['total_spent'], data['visit_frequency'], c=data['Cluster'])
plt.title("Customer Segmentation using K-Means")
plt.xlabel("Total Amount Spent")
plt.ylabel("Visit Frequency")
plt.show()