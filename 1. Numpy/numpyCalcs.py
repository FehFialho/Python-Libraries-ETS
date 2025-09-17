import numpy as np

nums = np.random.randint(1,10,5) # 1 até 10, 5 Valores
print(nums)

print(f'Maior Número: {nums.max()}')
print(f'Menor Número: {nums.min()}')
print(f'Indice Maior Número: {nums.argmax()}')
print(f'Mediana: {np.median(nums)}')
print(f'Média: {nums.mean()}')
print(f'Desvio Padrão: {nums.std()}')
print(f'Variância: {nums.var()}')

print(f'Pegar itens específicos: {nums[:3]}')