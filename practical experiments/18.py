import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("temperature_data.csv")

# Mean temperature
mean_temp = data.groupby('city')['temperature'].mean()

# Standard deviation
std_temp = data.groupby('city')['temperature'].std()

# Temperature range
temp_range = data.groupby('city')['temperature'].apply(lambda x: x.max() - x.min())

# City with highest range
highest_range_city = temp_range.idxmax()

# City with most consistent temperature
most_consistent_city = std_temp.idxmin()

print("Mean Temperature for Each City:")
print(mean_temp)

print("\nStandard Deviation for Each City:")
print(std_temp)

print("\nTemperature Range for Each City:")
print(temp_range)

print("\nCity with Highest Temperature Range:", highest_range_city)
print("City with Most Consistent Temperature:", most_consistent_city)