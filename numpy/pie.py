# モンテカルロ法をやってみる(python pie.py)
import matplotlib.pyplot as plt
import numpy as np

NUM = 5000 # 実行回数
x = 0 # 点のx値
y = 0 # 点のy値
pai=0.0 # 求めた円周率を格納
a = 0 # 1/4の円に入ってる点の数をカウント
i = 0 # ループカウンタ
while i < NUM:
    x = np.random.rand() # ランダムな点の位置x
    y = np.random.rand() # ランダムな点の位置y
    if x * x + y * y <= 1: # 原点との距離が1未満なら
        a += 1 # 1/4の円の中なのでカウント
        plt.scatter(x, y, color = 'red') # 赤い点で書く
    else: # 円の外であれば
        plt.scatter(x, y, color = 'blue') # 青い点で書く
    i += 1 # ループカウンタ増
pai = 4 * a / NUM # 円周率を求める式
plt.title(f"pie = {pai}")
plt.show()
