import numpy as np

# 1차원 배열
arr = np.arange(5,31,5)
print(arr[[0,2,4]])

# 2차원 배열
arr = np.array([[5, 10, 15, 20],
                [25, 30, 35, 40],
                [45, 50, 55, 60]])
print(arr[[0,2],2:])    # 0 2행의 2번째 열에서 끝까지
print(arr[1:,[2,3]])