import numpy as np


data = np.array([[10,20,30],[40,50,60],[70,80,90]])

# Row wise sum
result = np.sum(data, axis=1)
print("Row wise sum: ",np.sum(data, axis=1))

# Column wise sum
result = np.sum(data, axis=0)
print("Column wise sum: ",result)

# Minimum value
result = np.min(data)
print("Minimum value: ",result)

# Maximum value
result = np.max(data)
print("Maximum value: ",result)

# Overall mean
result = np.mean(data)
print("Overall mean: ",result)