import numpy as np

arr = np.arange(12)
print(arr, arr.ndim)

arr = arr.reshape((3,4))
print(arr, arr.ndim)

arr = arr.reshape((2,3,2))
print(arr, arr.ndim)

arr = arr.reshape((2,2,1,3))
print(arr, arr.ndim)