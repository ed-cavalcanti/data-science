import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/edney/OneDrive/Documentos/Study/python/athlete_events.csv')

# Criando histograma (gráfico com colunas)
dados.hist(column='Age', bins=100)
# Mostrando histograma
plt.show()