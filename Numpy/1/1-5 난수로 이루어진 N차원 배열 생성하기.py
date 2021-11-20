import numpy as np
import matplotlib.pyplot as plt

# np.rnadom.normal()
arr = np.random.normal(0,1,(2,3)) # 평균값, 표준편차, 개수(행렬)
print(arr)

arr = np.random.normal(0,1,1000)
plt.hist(arr, bins=100)
plt.show()

# np.random.rand()
arr = np.random.rand(1000)
plt.hist(arr, bins=100)
plt.show()

# np.random.randn()
arr = np.random.randn(1000)
plt.hist(arr, bins=100)
plt.show()

# np.random.randint()
arr = np.random.randint(low=1, high=5,size=(3,4))
print(arr)

arr = np.random.randint(100,200,1000)
plt.hist(arr, bins=100)
plt.show()