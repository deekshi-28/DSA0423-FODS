import pandas as pd

# Load CSV file
sales_data = pd.read_csv("sales_data.csv")

# Calculate Total Sales
sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

# Display updated DataFrame
print("Updated Sales Data:")
print(sales_data)