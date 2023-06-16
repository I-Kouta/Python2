# ロジスティック回帰・分類アルゴリズム(python classifying.py)
import numpy as np
import matplotlib.pyplot as plt
# x:入力データ
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# y:対応する正解ラベル(0:正常, 1:異常)
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# パラメータ設定
m = x.shape[0] # データ数
a = 0
b = 0
iterations = 100000
alpha = 0.01
cost = []
for iter in range(iterations):
    # 仮説を定義
    z = a * x + b # 線形回帰の仮説
    h = 1 / (1 + np.exp(-z)) # シグモイド関数
    a -= (alpha / m) * (((h - y) * x).sum())
    b -= (alpha / m) * ((h - y).sum())

    z = a * x + b
    h = 1 / (1 + np.exp(-z)) # シグモイド関数
    j = -((y * np.log(h) + (1 - y) * np.log(1 - h)).sum()) / m # 目的関数(交差エントロピー関数)
    cost.append(j)

print("学習後のa:%f,"% a)
print("学習後のb:%f,"% b)
print("学習後の目的関数の値:%f,"% j)

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(cost)
ax1.set_xlabel('iteration')
ax1.set_ylabel('cost')

ax2 = fig.add_subplot(1, 2, 2)
ax2.set_yticks([0, 1]) #y軸の目盛り
ax2.scatter(x, y)
x = np.arange(0, 20, 0.1)
z = a * x + b
h = 1 / (1 + np.exp(-z))
ax2.plot(x, h, c="orange")
ax2.legend((u"data", u"regression line")) # 凡例
plt.xlabel('number of defective pridcts')
plt.ylabel('Label')

plt.tight_layout()
plt.show()
