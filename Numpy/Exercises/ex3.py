import numpy as np

a = np.random.randint(1,10,5)
b = np.arange(1,6)

print(f'Vetores: {a,b}')

print(f'\nSoma: {np.add(a,b)}')
print(f'Subtração: {np.subtract(a,b)}')
print(f'Produto: {np.multiply(a,b)}')