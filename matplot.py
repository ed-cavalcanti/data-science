import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Relaciona a variável x com a y e cria um gráfico
# plt.scatter(x, y)

# Cria um array de 0 até 1000 "pulando" de um em um
x1 = np.arange(0, 1000, 1)

# Pega variável x1 e plota o gráfico dela elevado a 2
# plt.plot(x1, x1 ** 2)
# plt.show()

# Crie um gráfico relacionando o peso e a altura dos atletas masculinos
dados = pd.read_csv('C:/Users/edney/OneDrive/Documentos/Study/python/athlete_events.csv')

masc_athlets = dados.loc[dados['Sex'] == 'M']
heigths = dados['Height']
weigths = dados['Weight']

plt.scatter(heigths, weigths)
plt.show()
