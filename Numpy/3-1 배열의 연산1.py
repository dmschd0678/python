import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
arr2 = np.array([[2,2,2],
                 [2,2,2],
                 [2,2,2]])

print(arr)
print(arr2)

# 덧셈
print(arr + arr2)
print(np.add(arr,arr2))

# 뺄셈
print(arr - arr2)
print(np.subtract(arr,arr2))

# 곱셈
print(arr * arr2)
print(np.multiply(arr,arr2))

# 나눗셈
print(arr / arr2)
print(np.divide(arr,arr2))

# 제곱
print(arr ** 5)
print(np.square(arr))

# 제곱근
print(np.sqrt(arr))

# 몫
print(arr // 2)

# 나머지
print(arr % 2)