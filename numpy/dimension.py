# 次元削減アルゴリズム,主成分分析(PCA)(python dimension.py)
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine

wine = load_wine() # データセットをロード
x = wine.data[:, :3] # 3次元のデータを読み込む
y = wine.target # 分類ラベル
feature_name = wine.feature_names[:3] # 特微量の名前
target_name = wine.target_names # 目的量の名前

s = np.cov(x, rowvar = 0, bias = 1) # 共分散行列を求める
print(f"共分散行列のサイズ:{s.shape}")
print(f"行列の値:{s}")

fig = plt.figure()
ax = fig.add_subplot(projection="3d") # 3Dで投影
colors = ["red", "blue", "green"]
for yy in np.unique(y):
    ax.scatter(
        x[:,0][y==yy],
        x[:,1][y==yy],
        x[:,2][y==yy],
        label=target_name[yy],
        color=colors[yy],
        edgecolors='black')
ax.set_xlabel(feature_name[0]) # alcohol:アルコール
ax.set_ylabel(feature_name[1]) # malic_acid:リンゴ酸
ax.set_zlabel(feature_name[2]) # ash:灰分
plt.legend()
plt.show()
