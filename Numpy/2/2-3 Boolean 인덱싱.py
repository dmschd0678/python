import numpy as np

arr = np.array([1,2,3,4])
print(arr[[True,False,True,True]])

arr = np.array([[1,2,3,4],
                [5,6,7,8]])
print(arr[[True,False],True])
print(arr[arr > 3])
print(arr[arr >= 2])