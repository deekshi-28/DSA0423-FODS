from collections import Counter

# List of products sold
products = [
    "Laptop", "Mobile", "Tablet", "Mobile",
    "Laptop", "Mobile", "Headphones",
    "Tablet", "Mobile", "Laptop"
]

# Calculate frequency distribution
frequency = Counter(products)

print("Product Frequency Distribution:")
for product, count in frequency.items():
    print(product, ":", count)

# Find most popular product
most_popular = frequency.most_common(1)

print("\nMost Popular Product:", most_popular[0][0])
print("Times Sold:", most_popular[0][1])