import numpy as np

arr = np.arange(9)
print(arr)

arr = np.arange(3, 13, 3)
print(arr)

#np.linspace()
arr = np.linspace(0,100,11)
print(arr)

#np.logspace

arr = np.linspace(1,10,10)
print(arr, end = '\n\n')

arr = np.logspace(1,10, 10, base=2)
print(arr)

arr = np.logspace(1,10,10)
print(arr)