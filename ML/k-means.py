
# k平均法
# python k-means.py

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# データ数、特微量の数, データ点分布の中心の数, ガウス分布のパラメータ
X, y = make_blobs(n_samples = 150, n_features = 2, centers = 3, cluster_std = 0.8, shuffle = True, random_state = 0)

plt.scatter(X[:,0], X[:,1])
plt.grid()
plt.show()
