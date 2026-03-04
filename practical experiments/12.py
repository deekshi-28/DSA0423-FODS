import pandas as pd

# Load CSV file
sales_data = pd.read_csv("sales_data12.csv")

# Calculate total quantity sold per product
total_sales = sales_data.groupby('product_name')['quantity_sold'].sum()

# Sort in descending order and get top 5
top_5_products = total_sales.sort_values(ascending=False).head(5)

print("Top 5 Most Sold Products:")
print(top_5_products)