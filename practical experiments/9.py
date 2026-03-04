import matplotlib.pyplot as plt

# Monthly Sales Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [50000, 60000, 55000, 70000, 65000, 80000]

# 🔹 Line Plot
plt.figure()
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales - Line Plot")
plt.xlabel("Months")
plt.ylabel("Sales (₹)")
plt.show()

# 🔹 Bar Plot
plt.figure()
plt.bar(months, sales)
plt.title("Monthly Sales - Bar Plot")
plt.xlabel("Months")
plt.ylabel("Sales (₹)")
plt.show()