import numpy as np

matriz = np.random.randint(0,11,16).reshape(4,4)
print(matriz)

print(f'\nMédia: {matriz.mean()}')
print(f'Desvio Padrão: {matriz.std()}')