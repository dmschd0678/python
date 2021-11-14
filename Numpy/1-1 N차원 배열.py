import numpy as np

# 1차원 배열
arr = np.array([1,2,3])
print(arr)
print()

# 2차원 배열
arr = np.array([[1,2,3],
                [4,5,6]])
print(arr)
print()

# 튜플
tpl = (4,5,6)
arr = np.array(tpl)
print(arr)
print()

# 리스트
lst = [1,2,3]
arr = np.array(lst)
print(arr)
print()

lst2 = [[1,2,3],[4,5,6]]
arr = np.array(lst2)
print(arr)
print()

# shape
arr1 = np.array([1,2,3])
arr2 = np.array([[1,2,3],[4,5,6]])

print(arr1.shape)
print(arr2.shape)
print()

# ndim  차원
print(arr1.ndim)
print(arr2.ndim)
print()

# size
print(arr1.size)
print(arr2.size)
print()