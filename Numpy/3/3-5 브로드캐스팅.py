import numpy as np

arr1 = np.array([[0,0,0],
                [1,1,1],
                [2,2,2]])

arr2 = np.array([[5,6,7]])

print(arr1 + arr2)

arr1 = np.array([[1,1,1]])
arr2 = np.array([[0],
                 [1],
                 [2]])
print(arr1 + arr2)