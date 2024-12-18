# -*- coding: utf-8 -*-
"""TesteKMeans-dataset-wine-quality.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1atxWfWGcBP5cC6PqJjzy5HYWxbBVYc6v
"""

import pandas as pd

dados = pd.read_csv('/content/wine.csv')

dados.head(3)

xx = dados.iloc[:,1]

xx1 = dados.iloc[:, 3]

X = dados.iloc[:, [1, 3]].values

X

X.append(xx)

X = dados.iloc[:, 1:3].values

y = dados.iloc[:, -1]

import plotly.express as ex

ex.scatter(x = X[:, 0], y = X[:, 1])

from sklearn.cluster import KMeans

k_means = KMeans(n_clusters = 2)

k_means.fit(X)

centroides = k_means.cluster_centers_
labels = k_means.labels_

labels

import plotly.graph_objects as go

figura1 = ex.scatter(x = X[:, 0], y = X[:, 1], color = labels)
figura2 = ex.scatter(x = centroides[:,0], y = centroides[:, 1], size = [5, 5])
figura3 = go.Figure(data = figura1.data + figura2.data)
figura3.show()