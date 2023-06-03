import pandas as pd

alunos = {
    'nome': ['Arya', 'Brandom', 'Rickon', 'Robb', 'Sansa'],
    'nota': [10, 9, 4, 9, 6],
    'aprovado': ['Sim', 'Sim', 'Não', 'Sim', 'Não']
}

dataframe = pd.DataFrame(alunos)

# Conseguimos manipular apenas uma coluna, semelhante a selecionar um item de um dicioário

# Selecionando uma coluna
dataframe['nome']

# selecionando linhas específicas
# A função loc irá receber um array com o indice de todas as linhas que você quer buscar
dataframe.loc[[0, 3]] # Retorna as linhas de indice 0 e 3
dataframe.loc[1:3] # Retorna as linhas do indice 1 até o 3

# Retorna apenas as linhas em que a coluna nome for igual a 'Arya'
dataframe.loc[dataframe['nome'] == 'Arya']