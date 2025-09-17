import numpy as np

impares = np.random.randint(1,10,9)
print(impares)

for i in range(9):
    if impares[i] % 2 != 0:
        impares[i] = 0

impares = np.reshape(impares, (3, 3))

print(f'\n{impares}')

impares2 = np.random.randint(1,10,9).reshape((3,3))
mascara = (impares2 % 2 != 0)
impares2[mascara] = 0