import numpy as np
import time

arr = np.arange(99999999)

# for
sum = 0
before = time.time()

# for i in arr:
#     sum += i

after = time.time()

print(sum, after - before)

# 벡터 연산
before = time.time()

sum = np.sum(arr)

after = time.time()

print(sum, after - before)

arr1 = np.arange(99999999)
arr2 = np.arange(99999999)

sum = 0
before = time.time()
# for i,j in zip(arr1,arr2):
#     sum += i  * j
after = time.time()

print(sum, after - before)

# 벡터 연산
before = time.time()
sum = np.dot(arr1,arr2)
after = time.time()
print(sum, after - before)
