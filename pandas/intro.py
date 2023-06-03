import pandas as pd

alunos = {
    'nome': ['Arya', 'Brandom', 'Rickon', 'Robb', 'Sansa'],
    'nota': [10, 9, 4, 9, 6],
    'aprovado': ['Sim', 'Sim', 'Não', 'Sim', 'Não']
}

# Cria um "dataframe" de uma coluna, com indicé (id). Apenas arrays unidimensionais
objeto = pd.Series([9, 8, 7, 6, 5, 4, 3, 2, 1])

# Transforma um dicionário em dataframe
dataframe = pd.DataFrame(alunos)

# Retorna a quantidade de linhas e colunas que um dataFrame possui
dataframe.shape

# Retorna informações úteis para as colunas de valores numéricos, como media, desvio padrão, mínimo, máximo etc:
#            nota
# count   5.00000
# mean    7.60000
# std     2.50998
# min     4.00000
# 25%     6.00000
# 50%     9.00000
# 75%     9.00000
# max    10.00000
dataframe.describe()
