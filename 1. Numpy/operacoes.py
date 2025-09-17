import numpy as np

a = np.random.randint(0,50,5) 
b = np.random.randint(0,50,5)

print(a,b)

print(a + 10)# Soma 10 em todos os elementos.
print(np.sum(a))# Retorna a soma total de todos os elementos.
print(np.add(a,b))# Soma de acordo com o indice (subtract - e multiply * ).