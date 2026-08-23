import numpy as np

# 1D Array
arr1 = np.arange(1,11)
print("Array: ",arr1)
print("Data Type: ",arr1.dtype)
print("Shape: ",arr1.shape)

# 2D Array
arr2 = np.arange(1,10).reshape(3, 3)
print("Array: ",arr2)
print("Data Type: ",arr2.dtype)
print("Shape: ",arr2.shape)

list = np.array([10,20,30,40,50])
print("Array: ",list)
print("Data type: ",list.dtype)
print("Shape: ",list.shape)