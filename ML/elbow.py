
# エルボー法
# python elbow.py
# データと予測値との差異を評価する尺度(低いほどよい)

from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
import math

X, y = make_blobs(
    n_samples = 150,
    n_features = 2,
    centers = 3,
    cluster_std = 0.8,
    shuffle = True,
    random_state = 0)


class KMeans2D_2():
    def __init__(self, k = 3):
        self.n_clusters = k
        self.labels_ = np.random.randint(0, self.n_clusters, X.shape[0])

        self.old_labels = np.ones(X.shape[0]) * -1

        self.cluster_centers_ = np.zeros((self.n_clusters, X.shape[1]))
        self.dist = np.zeros((X.shape[0], self.n_clusters))
        self.dist_2 = np.zeros(X.shape[0])

    def predict(self, X):
        while (not(self.labels_ == self.old_labels).all()):

            self.inertia_ = 0 # SSE

            for i in range(self.n_clusters):
                X_clusterd = X[self.labels_ == i,:]

                if X_clusterd.size != 0:
                    self.cluster_centers_[i,:] = X_clusterd.mean(axis = 0)
                else :
                    for n, x in enumerate(X):
                        self.dist_2[n] = self.distance_2(x, self.cluster_centers_[i,:])

                    self.cluster_centers_[i,:] = X[self.dist_2.argmax(axis = 0)]

                for x in X_clusterd: # 抜き出したXについてSSE計算
                    self.inertia_  += self.distance_2(x, self.cluster_centers_[i,:])

            for i, x in enumerate(X):
                for j, center in enumerate(self.cluster_centers_):
                    self.dist[i][j] = math.sqrt(self.distance_2(x, center))

            self.old_labels = self.labels_

            self.labels_ = self.dist.argmin(axis = 1)
        return self.labels_

    def distance_2(self, p, q):
        return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

# グラフの描画
max_k = 10
distortions = []

for k in range(1, max_k):
    km2 = KMeans2D_2(k)
    labels = km2.predict(X)
    print(f"k = {k}, km2.inertia_ = {km2.inertia_}")
    distortions.append( km2.inertia_ )

plt.plot(range(1, max_k), distortions, marker="o")
plt.xlabel("k")
plt.ylabel("SSE")
plt.show()
