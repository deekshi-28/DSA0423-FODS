import numpy as np

# Columns: Bedrooms, Square Footage, Sale Price
house_data = np.array([
    [3, 1500, 5000000],
    [5, 2500, 12000000],
    [4, 1800, 7000000],
    [6, 3000, 15000000],
    [2, 1200, 4000000],
    [5, 2700, 11000000]
])

# Filter houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Extract sale prices (column index 2)
sale_prices = filtered_houses[:, 2]

# Calculate average sale price
average_price = np.mean(sale_prices)

print("Houses with more than 4 bedrooms:")
print(filtered_houses)

print("\nAverage Sale Price:", average_price)