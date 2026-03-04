# Input data
prices = [100, 200, 50]
quantities = [2, 1, 4]
discount_rate = 10   # in percentage
tax_rate = 5         # in percentage

# Step 1: Calculate Subtotal
subtotal = 0
for i in range(len(prices)):
    subtotal += prices[i] * quantities[i]

# Step 2: Apply Discount
discount_amount = subtotal * (discount_rate / 100)
after_discount = subtotal - discount_amount

# Step 3: Apply Tax
tax_amount = after_discount * (tax_rate / 100)
final_total = after_discount + tax_amount

# Output
print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("After Discount:", after_discount)
print("Tax Amount:", tax_amount)
print("Final Total Cost:", final_total)