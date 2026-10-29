
import numpy as np

# 1. Store student exam scores
scores = np.array([65, 70, 80, 85, 100])

# 2. Calculate statistics
mean_score = np.mean(scores)
median_score = np.median(scores)
highest_score = np.max(scores)
lowest_score = np.min(scores)

# 3. Display the results
print("Student Scores:", scores)
print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
