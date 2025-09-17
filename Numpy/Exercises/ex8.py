import numpy as np

x = int(input("Digite a dimensão da matriz! ")) 

def gerarMatriz(x):
    matriz = np.full((x,x),0)

    for i in range(x):
        for j in range(x):
            if i == j: # Indice para coluna e linha é igual.
                matriz[i][j] = 1
            if (i + j) == x - 1: # A soma dos indices da diagonal secundária resulta no valor de x - 1.
                matriz[i][j] = 2
                if i == j: # Comparação Adicional para o 3.
                    matriz[i][j] = 3 

    print(f'\n{matriz}')

gerarMatriz(x)