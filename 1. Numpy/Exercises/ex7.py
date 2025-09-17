import numpy as np

a = np.random.randint(1,6,9).reshape(3,3) # Gera valores de 1 até 5 (6 Não Inclusivo), 9 Valores.
b = np.random.randint(1,6,(3,3)) #  Gera valores de 1 até 5 (6 Não Inclusivo), 9 Valores já em 3 x 3.

c = a == b
print(f'Tabela 1:\n{a}\nTabela 2:\n{b}')
print(f'\n{c}') # Comparação (uau)