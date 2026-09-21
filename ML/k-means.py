
# k平均法
# python k-means.py

from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
import math

# yは正解ラベルだが、教師なし学習なので使わない
X, y = make_blobs(
    n_samples = 150, # データ数
    n_features = 2, # 特微量の数
    centers = 3, # データ点分布の中心の数
    cluster_std = 0.8, # ガウス分布のパラメータ
    shuffle = True,
    random_state = 0
    )

# 重心の計算処理、ラベルの更新処理
class KMeans2D():
    def __init__(self, k = 3):
        self.n_clusters = k
        # 0からクラスタ数-1までの整数からランダムにラベルを振る
        self.labels_ = np.random.randint(0, self.n_clusters, X.shape[0])

        # ラベルの変動確認用の配列
        self.old_labels = np.ones(X.shape[0]) * -1

        self.cluster_centers_ = np.zeros((self.n_clusters, X.shape[1])) # クラスタの重心を格納する配列
        self.dist = np.zeros((X.shape[0], self.n_clusters)) # 距離を格納する配列
        self.dist_2 = np.zeros(X.shape[0]) # 空のクラスタができたときの対策

    def predict(self, X):
        # ラベルの変動がなくなるまで繰り返す
        while (not(self.labels_ == self.old_labels).all()):
            for i in range(self.n_clusters):
                X_clusterd = X[self.labels_ == i, :] # ラベルに応じたXを抜き出す

                # 個数方向の平均として抜き出したXの重心を計算
                if X_clusterd.size != 0: # 空のクラスタじゃないときはそのまま重心計算
                    self.cluster_centers_[i,:] = X_clusterd.mean(axis = 0)
                else :
                    #空のクラスタが存在する場合はそのときの重心から最も遠い点を新たな重心に設定
                    for n, x in enumerate(X):
                        self.dist_2[n] = self.distance_2(x, self.cluster_centers_[i,:])

                    self.cluster_centers_[i, :] = X[self.dist_2.argmax(axis = 0)]

            # 全ての点について重心からの距離を計算
            for i, x in enumerate(X):
                for j, center in enumerate(self.cluster_centers_):
                    self.dist[i][j] = math.sqrt(self.distance_2(x, center))

            # 更新前のラベルを保存
            self.old_labels = self.labels_

            # 最も重心との距離が近かったクラスにラベルを更新
            self.labels_ = self.dist.argmin(axis = 1)
        return self.labels_

    # ユークリッド距離の計算
    def distance_2(self, p, q):
        return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

km = KMeans2D(k = 3)
labels = km.predict(X)

# 分類結果の描画
plt.scatter(X[labels == 0, 0], X[labels == 0, 1], s = 30, c="yellow", marker="o", label="cluster 1")
plt.scatter(X[labels == 1, 0], X[labels == 1, 1], s = 30, c="lightblue", marker="o", label="cluster 2")
plt.scatter(X[labels == 2, 0], X[labels == 2, 1], s = 30, c="lightgreen", marker="o", label="cluster 3")

plt.legend()
plt.grid()
plt.show()

# データの形状を確認
#print(X.shape)
#print(y.shape)
