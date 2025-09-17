import numpy as np

matriz = np.random.randint(1,10,9).reshape(3,3)
print(matriz)

transposta = np.zeros((3,3))

transposta[0] = matriz[:,0]
transposta[1] = matriz[:,1]
transposta[2] = matriz[:,2]

print(f'\nMatriz Transposta:\n{transposta}')