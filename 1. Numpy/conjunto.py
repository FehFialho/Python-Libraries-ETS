import numpy as np

a = [1,2,3,4]
b = [4,5,6,6]

np.unique(a) # Verifica Unicos.
np.union1d(a,b) # União dos valores sem epetir os iguais.
print(np.intersect1d(a,b)) # Intersecção (Valores em Comum).