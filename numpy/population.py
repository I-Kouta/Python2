# 多項式回帰(python population.py)
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(1, 31, 1) # 年齢の入力データ
# 年齢に対応する正解データ
Y = np.array([85745, 86140, 86557, 86845, 87023, 87034, 87260, 87161, 87042, 86920,
              86758, 86380, 86139, 85706, 85404, 85077, 84422, 83731, 83015, 82300,
              81493, 81735, 81342, 80175, 79010, 77850, 77282, 76562, 75962, 75451])
Y = Y.reshape(30, 1) # 行列計算ができるように二次元配列の形式にする

def stand(x):
    M = x.mean()
    S = x.std()
    X = (x - M) / S
    return X

X = stand(X)
Y = stand(Y)

m = X.shape[0]
X_ = np.c_[X ** 2, X, np.ones([m, 1])] # 配列を結合
theta = np.ones([3, 1]) # パラメータを設定

iterations = 1000
alpha = 0.01
cost = []

for iter in range(iterations):
    h = np.dot(X_, theta) # 現在のパラメータで仮説を計算
    theta[0] = theta[0] - (alpha / m) * (h - Y).T.dot(X ** 2)
    theta[1] = theta[1] - (alpha / m) * (h - Y).T.dot(X)
    theta[2] = theta[2] - (alpha / m) * (h - Y).sum()
    h = np.dot(X_, theta) # 更新後のパラメータで仮設と目的関数を計算
    J = (1 / (2 * m)) * ((h - Y) ** 2).sum()
    cost.append(J)

print("学習後のa1: %f,"% theta[0])
print("学習後のa2: %f,"% theta[1])
print("学習後のb: %f,"% theta[2])
print("学習後の目的関数の値: %f,"% J)
print(cost)

fig = plt.figure() # 目的関数の値の推移と仮説のグラフを並べて表示
# 1つめ
ax1 = fig.add_subplot(1, 2, 1)
ax1.plot(cost) # 目的関数の値を保存したリストをプロット
ax1.set_xlabel('iteration')
ax1.set_ylabel('cost')
# 2つめのグラフ
ax2 = fig.add_subplot(1, 2, 2)
ax2.scatter(X, Y)
h = np.dot(X_, theta)
ax2.plot(X, h, c="red")
ax2.legend((u"data", u"regression line"))
ax2.set_xlabel('year')
ax2.set_ylabel('population(15-64)')
plt.tight_layout()
plt.show()
