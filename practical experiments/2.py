import pandas as pd

# Load CSV file
order_data = pd.read_csv("orders.csv")

# 1️⃣ Total number of orders made by each customer
orders_per_customer = order_data.groupby('customer_id').size()

# 2️⃣ Average order quantity for each product
avg_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

# 3️⃣ Earliest and Latest order dates
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()

# Display Results
print("Total Orders Per Customer:")
print(orders_per_customer)

print("\nAverage Order Quantity Per Product:")
print(avg_quantity_per_product)

print("\nEarliest Order Date:", earliest_date)
print("Latest Order Date:", latest_date)