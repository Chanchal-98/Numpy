import numpy as np

# Daily sales data
sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

# Total weekly sales
print("Total weekly sales: ",np.sum(sales))

# Average daily sales
print("Average daily sales: ",np.mean(sales))

# Highest and lowest sales day
print("Highest sales: ",np.max(sales))

#Lowest sales day
print("Lowest sales: ",np.min(sales))

# Standard deviation of sales
print("Standard deviation of sales: ",np.std(sales))

# Identify days where sales were above average
average = np.mean (sales)
days = np.where(sales > average)[0] + 1
print("Average sales: ",average)
print("Days with above-average sales: ",days)
