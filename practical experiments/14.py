import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("C:/Users/deek/Downloads/fods/practical experiments/data.csv")

# Combine all feedback into one string
text = " ".join(data['feedback'])

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Define simple stop words list
stop_words = ["the", "is", "and", "for", "i", "a", "an", "to"]

# Remove stop words
words = [word for word in text.split() if word not in stop_words]

# Calculate frequency
word_freq = Counter(words)

# Take user input
N = int(input("Enter number of top frequent words to display: "))

# Get top N words
top_words = word_freq.most_common(N)

print("\nTop", N, "Most Frequent Words:")
for word, count in top_words:
    print(word, ":", count)

# Plot bar chart
words_plot = [item[0] for item in top_words]
counts_plot = [item[1] for item in top_words]

plt.figure()
plt.bar(words_plot, counts_plot)
plt.title("Top Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()