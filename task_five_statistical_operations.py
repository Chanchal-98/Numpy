import numpy as np

marks = np.array([78,85,90,66,72,88,95,60])

# Mean
print("Mean: ",np.mean(marks))

# Median
print("Median: ",np.median(marks))

# Variance
print("Variance: ",np.var(marks))

# Standard deviation
print("Standard deviation: ",np.std(marks))

# Minimum and Maximum
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))

# Range(min - max)
result = np.max(marks) - np.min(marks)
print("Range:", result)