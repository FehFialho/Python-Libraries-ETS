import numpy as np

x = int(input("Insira tamanho da matriz! "))

a = np.random.randint(1,10,(x,x))
print(f'\nPrimeira Matriz:\n{a}')

b = np.full((x,x),0)

for i in range(x):
    for j in range(x):
        b[i][j] = a[i][-j-1] # | (0 > -1) | (1 > -2) | (2 > -3) | (3 > -4) | 

print(f'\nMatriz Espelhada:\n{b}')

