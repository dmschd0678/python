import numpy as np

# np.zeros()
arr = np.zeros([2,2])
print(arr)

print()

# np.ones()
arr = np.ones([3,5])
print(arr)

print()

# np.full()
arr = np.full((2,3),5)
print(arr)

print()

# np.eye()
arr = np.eye(5,4, k=0)   # k = 대각 원소 시작 지점
print(arr)

arr = np.array([[1,2,3],
                [4,5,6]])

print()
# arr.zeros_like()
arr_z = np.zeros_like(arr)
print(arr_z)

print()

# np.ones_like()
arr_o = np.ones_like(arr)
print(arr_o)

print()

# np.full_like()
arr_f = np.full_like(arr, 6)
print(arr_f)