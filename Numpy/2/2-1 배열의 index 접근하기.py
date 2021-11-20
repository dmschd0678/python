import numpy as np

# 1차원 배열
arr = np.arange(10)
print(arr)

print(arr[3])
print(arr[1])
try:
    print(arr[10])
except IndexError:
    print("index 범위를 넘음")
print(arr[-1])
print(arr[-0])

print()

# 2차원 배열
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])
print(arr, arr.shape, arr.ndim)
print(arr[0,3])

print()

# 1차원 배열 범위 값 탐색
arr = np.arange(10)
print(arr)
print(arr[3:8])
print(arr[3:])
print(arr[:7])
print(arr[:-1])

# 2차원 배열 범위 값 탐색
arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])
print(arr[0, :])
print(arr[:,1])

print(arr[:3, :])
print(arr[:2, 2:])