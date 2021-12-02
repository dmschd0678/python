import numpy as np

arr = np.random.randint(15, size = (3,4))
print(arr)
# print(np.sort(arr))
# print(np.sort(arr, axis=0))
print(np.sort(arr, axis=None))  # 1차원으로 정렬

# argsort() # 정렬된 값의 인덱스 반환
print(np.sort(arr,axis=0))
print(np.argsort(arr,axis=0))