# -*- coding: utf-8 -*-
"""Cópia de Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mOA48cov4Xcf49fjra2MulrXwLpwUuD7
"""

markdown

"""### instalando bibliotecas

"""

import pandas as pd 
import matplotlib.pyplot as plt

"""### importando arquivo CSV"""

california_h_df = pd.read_csv('./sample_data/california_housing_train.csv')

"""### Tipos de visualização

- Display
- 
Print
"""

#print(california_h_df)

"""### Dados simples do *Data Frame*
- head (mostra por *default* as 5 primeiras linhas)
- shape (mostra a quantidade de linhas e colunas)
- describe (exibe um resumo de uma série de informações do data frame)
"""

# display(california_h_df.head(5))

# display(california_h_df.shape)

display(california_h_df.describe())

"""### Pegar somente uma coluna"""

total_rooms = california_h_df['total_bedrooms']

display(total_rooms)

"""### Pegar mais de uma coluna"""

filtros = california_h_df[['total_rooms','total_bedrooms','population']]
display(filtros)

"""### Método .loc
- Pegar uma única linha
- Pegra linhas com 1 condicional
- Pegar linhas e colunas espefíficas
- Pegar um valor específico

"""

# Pegar uma unica linha
# display(california_h_df.loc[1])

# Pegar um range de linhas
# display(california_h_df.loc[1:20])

# Pegar linhas com uma condicional
# display(california_h_df.loc[california_h_df['total_rooms'] >= 12000])

# Pegar várias linhas e colunas usando uma condição
# display(california_h_df.loc[california_h_df['total_rooms'] >= 12000, ['population']])

# Pegar a coluna de uma linha específica
display(california_h_df.loc[3:5,'total_rooms'])

"""### Criar uma coluna e adicionar no *DataFrame*"""

# Criando a partir de uma coluna já existente 
# california_h_df['Metade_total_rooms'] = california_h_df['total_rooms']/4
# display(california_h_df)

# Criando uma coluna com um valor fixo
# california_h_df['outra_nova_coluna'] = 5
# display(california_h_df)

"""### Apagar colunas"""

# Excluir coluna (série)
california_h_df = california_h_df.drop('Metade_total_rooms',axis=1)
display(california_h_df)

"""### Apagar linhas"""

california_h_df = california_h_df.drop(2,axis=0)
display(california_h_df)

"""### Deletar valores vazios
- Deletar linhas/colunas vazias
- Deletar linhas que possuem valores vazios

"""

# Deletar linhas que tem todos os valores nulos
california_h_df = california_h_df.dropna(how='all', axios=0)

# Deletar colunas que tem todos os valores nulos
california_h_df = california_h_df.dropna(how='all', axios=1)

# Deletar linhas que possuem pelo menos um valor vazio
california_h_df = california_h_df.dropna()

# Preencher os valores vazios com a média da coluna
california_h_df['total_rooms'] = california_h_df['total_rooms'].fillna(california_h_df['total_rooms'].mean())

# Preencher com o valor da ultima linha acima que contem valor
california_h_df = california_h_df.ffill()

"""### Calculando indicadores
- Groupy (agrupa os dados por uma condição)
- Value Counts (conta o número de vezes que um valor aparece)
"""

from pandas._libs.hashtable import value_count
# Conta número de vezes que o valor aparece
#total_rooms = california_h_df['total_rooms'].value_counts()
#display(total_rooms)

# Group By - Agrupa os dados por uma condição

total_rooms_media = california_h_df.groupby('total_rooms').sum()
display(total_rooms_media)

"""###  Gerando um gráfico """

plt.plot(total_rooms_media['median_income'])