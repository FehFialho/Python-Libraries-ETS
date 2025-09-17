import numpy as np

vetor = np.arange(1,26).reshape((5,5)) # Gerando Matriz de 1 até 26
print(vetor)

segunda = vetor[:,1]
print(f'Segunda Coluna: {segunda}')