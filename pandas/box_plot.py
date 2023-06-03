import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/edney/OneDrive/Documentos/Study/python/athlete_events.csv')

# Criando diagrama de caixa
# é possível criar várias box de uma vez, passadno como parâmetro um array ex.: ['Age', 'Height', 'Weight']
dados.boxplot(column='Age')
# Mostrando diagrama
plt.show()