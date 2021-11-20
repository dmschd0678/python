import numpy as np

arr = np.array([1,2,3], dtype=np.float)
print(arr, arr.dtype)

arr = np.array([1.2,2.4,4.5], dtype=np.int)
print(arr, arr.dtype)

arr = np.array([0,1,1,0,1], dtype=np.bool)
print(arr,arr.dtype)

arr = arr.astype(np.float32)
print(arr, arr.dtype)

arr = np.array([1,2,3.4,1])
print(arr, arr.dtype)

arr = np.array([1,2,3,4,"63"])
print(arr, arr.dtype)

arr = np.array([1,2,3,4,"63"], dtype=np.int)
print(arr, arr.dtype)
