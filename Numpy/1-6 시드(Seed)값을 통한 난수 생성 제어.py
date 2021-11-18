import numpy as np

arr = np.random.rand(10)
print("난수 발생1\n",arr)

arr = np.random.rand(10)
print("난수 발생2\n",arr)

np.random.seed(100)
arr = np.random.rand(10)
print("난수 발생1\n",arr)

np.random.seed(100)
arr = np.random.rand(10)
print("난수 발생2\n",arr)