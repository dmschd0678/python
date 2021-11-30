import numpy as np

arr1 = np.array([[1,2,3],
                 [4,5,6]])
arr2 = np.array([[1,0,3],
                 [4,-2,9]])
# 비교 연산
print(arr1 == arr2)
print(arr1 >= arr2)

print(np.array_equal(arr1, arr2))

# 삼각 함수
arr = np.array([[1,2,3],
                [4,5,6]])
# sin()
print(np.sin(arr))

# cos()
print(np.cos(arr))

# tan()
print(np.tan(arr))

# pi
print(np.pi)