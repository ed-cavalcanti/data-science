import pandas as pd

alunos = {
    'nome': ['Arya', 'Brandom', 'Rickon', 'Robb', 'Sansa'],
    'nota': [10, 9, 4, 9, 6],
    'aprovado': ['Sim', 'Sim', 'Não', 'Sim', 'Não']
}

dataframe = pd.DataFrame(alunos)

# Criando dataframe apenas com alunos aprovados
alunos_aprovados = dataframe.loc[dataframe['aprovado'] == 'Sim']

# Criando dataframe apenas com alunos reprovados
alunos_reprovados = dataframe.loc[dataframe['nota'] <= 7]



dados = pd.read_csv('C:/Users/edney/OneDrive/Documentos/Study/python/athlete_events.csv')

# Renomear colunas do dataframe
dados.rename(columns={'Name':'Nome', 'Sex':'Sexo', 'Age':'Idade'}, inplace=True)

# Contabiliza todos os valores da coluna
dados['Medal'].value_counts()
# saída
# Gold      13372
# Bronze    13295
# Silver    13116

# Excluir coluna
dados.drop('ID', axis = 1, inplace=True) # axis = 1 (coluna) / axis = 0 linha
print(dados.head())