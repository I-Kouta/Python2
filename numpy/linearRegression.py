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
a = 1
b = 1
h = a * X + b

m = X.shape[0] # データ数
j = (1/(2*m)) * ((h - Y) ** 2).sum() # 点ごとに予測値と正解値の差を二乗してデータ数mで平均をとる

plt.scatter(X, Y)
plt.plot(X, h, c="orange")
plt.xlabel('height')
plt.ylabel('weight')
plt.show()
