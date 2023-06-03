# Pacote que facilita operações matemáticas
import numpy as np

# Construção de array
# As listas podem guardar vários tipos de dados diferentes, enquanto o array se limita a apenas 1 tipo
nums = np.array([1, 2, 3, 4, 5, 6, 7])

nums.max() # Retorna o maior elemento
nums.min() # Retorna o menor elemento
nums.sum() # Retorna a soma todos os elementos
nums.mean() # Retorna a media dos elementos
nums.std() # Retorna o desvio padrão

# Posso criar array com mais de uma dimensão, ou seja, uma matriz
matrix = np.array([(1,2,3), (4,5,6), (7,8,9)])
print(matrix[0][0])
