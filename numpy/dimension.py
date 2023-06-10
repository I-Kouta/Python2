# 次元削減アルゴリズム,主成分分析(PCA)(python dimension.py)
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine

wine = load_wine() # データセットをロード
graph_datasets = [0, 1, 2]
x = wine.data[:, graph_datasets] # 3次元のデータを読み込む
y = wine.target # 分類ラベル
feature_indices = graph_datasets
feature_name = [wine.feature_names[i] for i in feature_indices] # 特微量の名前
target_name = wine.target_names # 目的量の名前

s = np.cov(x, rowvar = 0, bias = 1) # 共分散行列を求める
eigen = np.linalg.eig(s) # 固有方程式を解く
w = (eigen[1])[:, :2] # 固有ベクトルを2つ並べて変換行列を作成
x_pca = x.dot(w) # 変換行列を作用させて線形変換を行う

fig = plt.figure(figsize=(12, 5))
fig.subplots_adjust(wspace=0.5)
ax1 = fig.add_subplot(1, 2, 1, projection="3d") # 3Dで投影
colors = ["red", "blue", "green"]
for yy in np.unique(y):
    ax1.scatter(
        x[:,0][y==yy],
        x[:,1][y==yy],
        x[:,2][y==yy],
        label=feature_name[yy],
        color=colors[yy],
        edgecolors='black')
ax1.set_xlabel(feature_name[0])
ax1.set_ylabel(feature_name[1])
ax1.set_zlabel(feature_name[2])
ax1.set_title("original 3D plot")
plt.legend()

ax2 = fig.add_subplot(1, 2, 2)
for yy in np.unique(y):
    ax2.scatter(
        x[:,0][y==yy],
        x[:,1][y==yy],
        label=feature_name[yy],
        color=colors[yy],
        edgecolors='black')
ax2.set_xlabel(feature_name[0])
ax2.set_ylabel(feature_name[1])
ax2.set_title("2D plot after PCA")
plt.legend()
plt.show()
