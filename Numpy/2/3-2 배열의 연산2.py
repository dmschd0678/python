import numpy as np

# 1차원 행렬
arr1 = np.array([2,3,4])
arr2 = np.array([1,2,3])

print(np.dot(arr1,arr2))

# 2차원 행렬
"""
[[a,b]  [[e,f]      [[ae + bg, af + bh]
[c,d]]  [g,h]]   => [ce + dg, cf + dh]]
"""

arr1 = np.array([[1,2],
                 [4,5]])
arr2 = np.array([[1,2],
                 [0,3]])

print(np.dot(arr1, arr2))

# 절댓값
arr1 = np.array([[1,-2],
                 [-4,5]])
print(np.abs(arr1))

# 올림
arr1 = np.array([[1.932, -2.339],
                 [-4.145, 5.206]])
print(np.ceil(arr1))

# 내림
print(np.floor(arr1))

# 반올림
print(np.round(arr1))

# 버림
print(np.trunc(arr1))