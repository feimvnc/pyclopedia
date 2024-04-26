# import numpy as np
# from scipy.spatial.distance import cdist
# from sklearn.datasets import load_iris
# from sklearn.cluster import KMeans
# import matplotlib.pyplot as plt

# iris = load_iris()
# x = iris.data
# print(type(x), x[:10])

# res = list()
# n_cluster = range(2,20)
# for n in n_cluster:
#     kmeans = KMeans(n_clusters=n)
#     kmeans.fit(x)
#     res.append(np.average(np.min(cdist(x, kmeans.cluster_centers_, 'euclidean'), axis=1)))

# plt.plot(n_cluster, res)
# plt.title('elbow curve')
# plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

data = pd.read_csv('country_clusters.csv')

x = data.iloc[:,1:3]
kmeans = KMeans(3)
kmeans.fit(x)

identified_clusters = kmeans.fit_predict(x)
identified_clusters
data_with_clusters = data.copy()
data_with_clusters['Cluster'] = identified_clusters
data_with_clusters

wcss = []
# 'cl_num' is a that keeps track the highest number of clusters we want to use the WCSS method for.
# Note that 'range' doesn't include the upper boundery
cl_num=7
for i in range (1,cl_num):
    kmeans= KMeans(i)
    kmeans.fit(x)
    wcss_iter = kmeans.inertia_
    wcss.append(wcss_iter)



number_clusters = range(1,cl_num)
plt.plot(number_clusters, wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('Within-cluster Sum of Squares')
plt.show()



