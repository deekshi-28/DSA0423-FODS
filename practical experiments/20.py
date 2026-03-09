import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("soccer_players.csv")

# Top 5 players with highest goals
top_goals = data.sort_values(by='goals', ascending=False).head(5)

# Top 5 players with highest salary
top_salary = data.sort_values(by='salary', ascending=False).head(5)

# Average age
average_age = data['age'].mean()

# Players above average age
above_avg_age = data[data['age'] > average_age]

print("Top 5 Players with Highest Goals:")
print(top_goals[['name','goals']])

print("\nTop 5 Players with Highest Salary:")
print(top_salary[['name','salary']])

print("\nAverage Age of Players:", average_age)

print("\nPlayers Above Average Age:")
print(above_avg_age[['name','age']])

# Distribution of players by position
position_count = data['position'].value_counts()

position_count.plot(kind='bar')
plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()