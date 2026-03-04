import pandas as pd
import string
from collections import Counter

# Load CSV file
data = pd.read_csv("C:/Users/deek/Downloads/fods/practical experiments/reviews.csv")

# Combine all reviews into one string
text = " ".join(data['review'])

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Split into words
words = text.split()

# Calculate frequency distribution
word_frequency = Counter(words)

# Display frequency distribution
print("Word Frequency Distribution:")
for word, count in word_frequency.items():
    print(word, ":", count)