# 多項式回帰(python population.py)
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(1, 31, 1) # 年齢の入力データ
# 年齢に対応する正解データ
Y = np.array([85745, 86140, 86557, 86845, 87023, 87034, 87260, 87161, 87042, 86920,
              86758, 86380, 86139, 85706, 85404, 85077, 84422, 83731, 83015, 82300,
              81493, 81735, 81342, 80175, 79010, 77850, 77282, 76562, 75962, 75451])

def stand(x):
    M = x.mean()
    S = x.std()
    x = (x - M) / S
    return x

X = stand(X)
Y = stand(Y)

m = X.shape[0]
X_ = np.c_[X ** 2, X, np.ones([m, 1])] # 配列を結合
theta = np.ones([3, 1]) # パラメータを設定
h = np.dot(X_, theta) # 仮説

J = (1 / (2 * m)) * ((h - Y) ** 2).sum()
print("初期値での目的関数の値:%f"%J)

plt.scatter(X, Y) #散布図
plt.plot(X, h, c='red')
plt.legend((u'Data',u'Regression line'))
plt.xlabel('Year')
plt.ylabel('Population(15-64)')
plt.show()
