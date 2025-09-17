import numpy as np

# Transformar em Array
arrayI = ['Ve', 1]
array = np.array(arrayI)

print(f'{("Tipo Lista").center(30, "=")}')
print(type(arrayI))

print(f'{("Tipo Array").center(30, "=")}')
print(type(array))

# Transformar em Matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz = np.array(matriz)
print(f'\n{("Matriz").center(30, "=")}\n{matriz}')

# Shape
print(f'\n{("Shape do Array").center(30, "=")}\n{array.shape}')
print(matriz.shape)

# Dimensões
print(f'\n{("Dimensão do Array").center(30, "=")}\n{array.ndim}')
print(matriz.ndim)

# ReShape
grades = [1, 2, 3, 4, 5, 6]
grades = np.array(grades)
grades = np.reshape(grades, (2, 3))
print(f'\n{("Notas Reformatadas").center(30, "=")}\n\n {grades}')

# Criar Array
createArray = np.arange(1,20,2) # 1 Até 10 de 2 em 2.
createArray = np.reshape(createArray,(2,5))
print(f'\n{createArray}')

# Matriz números únicos
zeros = np.zeros((2,2))
print(f'\n{zeros}')

full = np.full((5,2),6) # Matriz apenas com número 6.
random = np.random.rand(2,2) # Números aleatórios. (randint para inteiro)
print(random)