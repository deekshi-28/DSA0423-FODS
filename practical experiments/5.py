import numpy as np

# Create 4x4 matrix (Students × Subjects)
# Order: Math, Science, English, History

student_scores = np.array([
    [85, 78, 90, 88],
    [92, 80, 85, 87],
    [76, 85, 88, 90],
    [89, 92, 84, 86]
])

# Calculate average score for each subject (column-wise)
subject_averages = np.mean(student_scores, axis=0)

# Subject names
subjects = ["Math", "Science", "English", "History"]

# Find subject with highest average
highest_avg_index = np.argmax(subject_averages)
highest_subject = subjects[highest_avg_index]

# Display Results
print("Average Score for Each Subject:")
for i in range(len(subjects)):
    print(subjects[i], ":", subject_averages[i])

print("\nSubject with Highest Average Score:", highest_subject)
