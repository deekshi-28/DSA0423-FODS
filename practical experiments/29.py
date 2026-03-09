import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("C:/Users/deek/Downloads/fods/practical experiments/customer_reviews.csv")

# Calculate mean rating
mean_rating = data['rating'].mean()

# Standard deviation
std_dev = data['rating'].std()

# Sample size
n = len(data)

# Standard error
standard_error = std_dev / np.sqrt(n)

# Z value for 95% confidence
z = 1.96

# Confidence interval
lower = mean_rating - z * standard_error
upper = mean_rating + z * standard_error

print("Average Rating:", mean_rating)
print("95% Confidence Interval:", (lower, upper))