import numpy as np

arr = np.array([[1,2,3],
                [0,1,4],
                [1,5,2]])

# min()
print(np.min(arr))
print(arr.min())
print(arr.min(axis=1)) # axis : 0 세로 값 비교, 1 가로 값 비교

print()

# max()
print(np.max(arr))
print(arr.max())
print(arr.max(axis=1))

print()

# sum()
print(np.sum(arr))
print(arr.sum())
print(arr.sum(axis=1))

print()

# mean()    평균 값
print(np.mean(arr))
print(arr.mean())
print(arr.mean(axis=1))

print()

# std() 표준편차
print(np.std(arr))
print(arr.std())
print(arr.std(axis=1))

print()

# cumsum() 누적 합
print(np.cumsum(arr))
print(arr.cumsum())
print(arr.cumsum(axis=1))

print()

# median() 중앙 값
print(np.median(arr, axis=0))