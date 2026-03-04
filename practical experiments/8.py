import numpy as np

# Product prices sold in the past month
product_prices = np.array([1200, 1500, 800, 2000, 1750, 950, 1100, 1600])

# Calculate average price
average_price = np.mean(product_prices)

print("Product Prices:", product_prices)
print("Average Price of Products Sold:", average_price)