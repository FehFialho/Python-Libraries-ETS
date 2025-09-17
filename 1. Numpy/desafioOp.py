import numpy as np

num = np.random.randint(1,20,6).reshape((2,3))

print(num)

num = np.reshape(num, (3,2))

num[0] += 5
num[1] *= 3
num[:, 1] = num[:, 1] / 2

print(f'\n{num}')