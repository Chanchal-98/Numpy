import numpy as np

marks = np.array([78,85,90,66,72,88,95,60])

# Sort the array
print("Sort: ",np.sort(marks))

# 25th percentile
print("25th percentile: ", np.percentile(marks,25))

# 50th percentile
print("50th percentile: ", np.percentile(marks,50))

# 75th percentile
print("75th percentile: ", np.percentile(marks,75))


# Above the average marks
average = np.mean(marks)
count = np.sum(marks > average)
print("Average marks: ",average)
print("Students above average: ",count)

