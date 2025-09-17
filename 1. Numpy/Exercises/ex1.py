import numpy as np

vetor = np.arange(0,10)
print(vetor)

multiplos = (vetor % 2 == 0)
vetor[multiplos] = -1
print(f'\n{vetor}')