# -*- coding: utf-8 -*-
"""KMeans_DBSCAN-dataset-CC_GENERAL.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AGTkyNnaik50lAH3U7Ij3S-BUZdiGYgJ

#Trabalho 1 de IA.
#Alunos: Alisson e Maurício

#Sobre o dataset

O CC_GENERAL é um conjunto de dados com informações sobre transações de cartões de crédito, frequentemente usado para tarefas de aprendizado de máquina, como classificação ou previsão de fraude. Contém as seguintes colunas, que fornecem informações detalhadas sobre o comportamento financeiro dos clientes em relação ao uso de cartões de crédito, o que é útil para a análise de risco de crédito ou para detecção de fraudes.:

CUST_ID: Um identificador único para cada cliente no conjunto de dados.

BALANCE: O saldo do cliente no momento da transação.

BALANCE_FREQUENCY: A frequência de uso do saldo pelo cliente.

PURCHASES: O total de compras realizadas pelo cliente.

ONEOFF_PURCHASES: O total de compras realizadas de uma só vez (não parceladas).

INSTALLMENTS_PURCHASES: O total de compras realizadas em parcelas.

CASH_ADVANCE: O valor de adiantamentos em dinheiro feitos pelo cliente.

PURCHASES_FREQUENCY: A frequência com que o cliente realiza compras.

ONEOFF_PURCHASES_FREQUENCY: A frequência de compras únicas (não parceladas).

PURCHASES_INSTALLMENTS_FREQUENCY: A frequência com que o cliente faz compras em parcelas.

CASH_ADVANCE_FREQUENCY: A frequência com que o cliente faz adiantamentos em dinheiro.

CASH_ADVANCE_TRX_FREQUENCY: A frequência de transações de adiantamentos em dinheiro.

PURCHASES_TRX_FREQUENCY: A frequência de transações de compras.

CREDIT_USAGE: A utilização do crédito disponível (relação entre o crédito utilizado e o limite disponível).

BALANCE_PAYMENT: O pagamento feito pelo cliente em relação ao saldo.

MINIMUM_PAYMENTS: O pagamento mínimo exigido pelo banco para aquele mês.

PRC_FULL_PAYMENT: A porcentagem do pagamento total realizado em relação ao valor total.

TENURE: O tempo (em meses) que o cliente tem de relacionamento com a instituição financeira.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import plotly.graph_objects as go
import plotly.express as ex
import seaborn as sns
import matplotlib.pyplot as plt

dados=pd.read_csv('/content/CC GENERAL.csv')

dados.head(10)

"""#Tratamento dos dados"""

dados.describe()

# Verificar os tipos de dados em cada coluna
dados.dtypes

# Drop na coluna CUST_ID (não numérica) e em colunas com baixa correlação
dadosLimpos = dados.drop(columns=['CUST_ID']) #identificador único para cada cliente.
dadosLimpos = dadosLimpos.drop(columns=['TENURE']) #O tempo (em meses) que o cliente tem de relacionamento com a instituição financeira
dadosLimpos = dadosLimpos.drop(columns=['PRC_FULL_PAYMENT']) #A porcentagem do pagamento total realizado em relação ao valor total.
dadosLimpos = dadosLimpos.drop(columns=['MINIMUM_PAYMENTS']) #O pagamento mínimo exigido pelo banco para aquele mês
dadosLimpos = dadosLimpos.drop(columns=['BALANCE_FREQUENCY']) #O pagamento feito pelo cliente em relação ao saldo.

# Substituindo valores ausentes pela media
dadosLimpos.fillna(dadosLimpos.mean(), inplace=True)

dadosLimpos.describe()

"""#Correlação dos dados"""

# Calcular a matriz de correlação
correlacao = dadosLimpos.corr()

# Configurar o gráfico
plt.figure(figsize=(10, 8))

# Criar o mapa de correlação (heatmap)
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, vmin=-1, vmax=1)

# Exibir o gráfico
plt.title('Mapa de Correlação')
plt.show()

#calculando a correlação média de cada coluna, em módulo
correlacao.abs().mean()

"""#Normalização / Padronização"""

# Normalização/Padronização dos dados
scaler = StandardScaler()
dadosLimpos_scaler = scaler.fit_transform(dadosLimpos)

dadosLimpos_scaler

"""#Análise de número de clusters"""

# Determinar o número ideal de clusters usando o método elbow
inertia = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)  # Explicitly set n_init
    kmeans.fit(dadosLimpos_scaler)
    inertia.append(kmeans.inertia_)

# Plotar a curva elbow
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o')
plt.xlabel('Numero de Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

"""#KMEANS sem PCA"""

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Fit K-Means with the chosen number of clusters (e.g., k=3)
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)  # Explicitly set n_init
clusters = kmeans.fit_predict(dadosLimpos_scaler)

# Visualisar os clusters usando PCA
pca = PCA(n_components=2)
pca_data = pca.fit_transform(dadosLimpos_scaler)

plt.figure(figsize=(8, 5))
plt.scatter(pca_data[:, 0], pca_data[:, 1], c=clusters, cmap='viridis', alpha=0.7)
plt.colorbar(label='Cluster')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('K-Means Clusters (visualização com PCA)')
plt.show()

"""#PCA"""

#Redução de dimensionalidade
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
dadosLimpos_scaler_PCA=pca.fit_transform(dadosLimpos_scaler)

"""# Análise de número de clusters após aplicação do  PCA


"""

# Determinar o número ideal de clusters usando o método elbow
inertia = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)  # Explicitly set n_init
    kmeans.fit(dadosLimpos_scaler_PCA)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o')
plt.xlabel('Numero de Clusters (k)')
plt.ylabel('Inertia')
plt.title('Elbow Method for Optimal k')
plt.show()

"""#KMEANS com PCA"""

k_means = KMeans(n_clusters = 2, random_state=42, n_init=10)
k_means.fit(dadosLimpos_scaler_PCA)

centroides_km = k_means.cluster_centers_
labels_km = k_means.labels_

# Calcular o índice de silhueta
score = silhouette_score(dadosLimpos_scaler_PCA, labels_km)
print(f"Silhouette Score: {score}")

import plotly.express as ex
figura1 = ex.scatter(x = dadosLimpos_scaler_PCA[:,0], y = dadosLimpos_scaler_PCA[:,1], color = labels_km)
figura2 = ex.scatter(x = centroides_km[:,0], y = centroides_km[:,1], size = [5,5])
figura3 = go.Figure(data = figura1.data + figura2.data)
figura3.show()

sum(labels_km==-1), sum(labels_km==0), sum(labels_km==1)

"""#DBSCAN com PCA"""

from sklearn.cluster import DBSCAN
import plotly.express as ex
import plotly.graph_objects as go
#dbscan = DBSCAN(eps = 0.9, min_samples=100)
dbscan = DBSCAN(eps = 0.9)
dbscan.fit(dadosLimpos_scaler_PCA)
labels_ds = dbscan.labels_
# Calcular o índice de silhueta
score = silhouette_score(dadosLimpos_scaler_PCA, labels_ds)
print(f"Silhouette Score: {score}")
print(sum(labels_ds==-1), sum(labels_ds==0), sum(labels_ds==1)) # Contagem de cada cluster
ex.scatter(x = dadosLimpos_scaler_PCA[:, 0], y = dadosLimpos_scaler_PCA[:, 1], color = labels_ds)

"""#Clusters com as colunas ONEOFF_PURCHASES e PURCHASES, correlação=0,92"""

purchases = dadosLimpos.iloc[:, [1, 2]]  # Seleciona as colunas 2 e 3 (índices 1 e 2)

# Normalização/Padronização dos dados
scaler_3 = StandardScaler()
purchases = scaler_3.fit_transform(purchases)

# KMeans
k_means_3 = KMeans(n_clusters=2, random_state=42, n_init=10)
k_means_3.fit(purchases)
centroides_3 = k_means_3.cluster_centers_
labels_3 = k_means_3.labels_

# Calcular o índice de silhueta
score_3 = silhouette_score(purchases, labels_3)
print(f"Silhouette Score: {score_3}")

# Contagem dos clusters
print(sum(labels_3 == -1),sum(labels_3 == 0), sum(labels_3 == 1))

# Visualizar com Plotly
figura1 = go.Scatter(x=purchases[:, 0], y=purchases[:, 1], mode='markers', marker=dict(color=labels_3))
figura2 = go.Scatter(x=centroides_3[:, 0], y=centroides_3[:, 1], mode='markers', marker=dict(size=10, color='red', symbol='x'))
figura3 = go.Figure(data=[figura1, figura2])
figura3.show()

purchases = dadosLimpos.iloc[:, [1, 2]]  # Selecionando as colunas 2 e 3 (índices 1 e 2)

# Normalização/Padronização dos dados
scaler_4 = StandardScaler()
purchases = scaler_4.fit_transform(purchases)

# Aplicando DBSCAN
dbscan_4 = DBSCAN(eps=0.9)
dbscan_4.fit(purchases)
labels_4 = dbscan_4.labels_

# Calcular o índice de silhueta
score_4 = silhouette_score(purchases, labels_4)
print(f"Silhouette Score: {score_4}")

# Contagem dos clusters
print(sum(labels_4 == -1), sum(labels_4 == 0), sum(labels_4 == 1))  # Contagem de cada cluster

ex.scatter(x = purchases[:, 0], y = purchases[:, 1], color = labels_4)
