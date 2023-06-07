# 線形回帰(python linearRegression.py)
import numpy as np
import matplotlib.pyplot as plt
# 身長のデータ
X = np.array([178, 190, 178, 187, 193, 196, 186, 181, 183, 178, 171, 174, 184, 176, 178,
              170, 176, 187, 178, 188, 179, 176, 180, 171, 186, 172, 171, 173, 190, 180])
# 対応する体重のデータ
Y = np.array([80, 85, 83, 80, 102, 100, 86, 88, 81, 85, 78, 74, 92, 82, 73,
              87, 83, 90, 93, 97, 75, 103, 76, 68, 100, 73, 86, 80, 95, 70])
# 標準化する間数定義
def stand(x):
    M = x.mean()
    S = x.std()
    x = (x - M) / S
    return x

X = stand(X) # 標準化
Y = stand(Y)
# 初期値1としてパラメータを設定
m = X.shape[0] # データ数
a = 1
b = 1
iterations = 1000 # 繰り返し回数(イテレーション)
alpha = 0.01 # 学習率
cost = [] # 目的関数の値を保存するためのリスト

for iter in range(iterations):
    h = a * X + b # 現在のパラメータで仮説を計算
    # パラメータ更新
    a = a - (alpha / m) * ((h - Y) * X).sum()
    b = b - (alpha / m) * ((h - Y) * X).sum()

    h = a * X + b # 更新後のパラメータで仮設と目的関数を計算
    J = (1 / ( 2 *m)) * ((h - Y) ** 2).sum()
    cost.append(J)

plt.scatter(X, Y)
plt.plot(X, h, c="orange")
plt.xlabel('height')
plt.ylabel('weight')
plt.show()
