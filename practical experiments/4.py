import pandas as pd

# Load CSV file
property_data = pd.read_csv("property_data.csv")

# 1️⃣ Average listing price in each location
avg_price_location = property_data.groupby('location')['listing_price'].mean()

# 2️⃣ Number of properties with more than 4 bedrooms
more_than_4_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]

# 3️⃣ Property with the largest area
largest_property = property_data.loc[property_data['area_sqft'].idxmax()]

# Display Results
print("Average Listing Price by Location:")
print(avg_price_location)

print("\nNumber of properties with more than 4 bedrooms:", more_than_4_bedrooms)

print("\nProperty with the Largest Area:")
print(largest_property)
