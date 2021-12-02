import numpy as np

arr = np.random.randint(10,size=10)
print(arr)


print(np.sort(arr))
print(np.sort(arr)[::-1])

print(arr)  # 배열의 값 변경 x

# arr = np.sort(arr)
arr.sort()
print(arr)