# ロジスティック回帰・分類アルゴリズム(python classifying.py)
import numpy as np
import matplotlib.pyplot as plt
# x:入力データ
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# y:対応する正解ラベル(0:正常, 1:異常)
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# パラメータ設定
a = 0
b = 0
# 仮説を定義
z = a * x + b # 線形回帰の仮説
h = 1 / (1 + np.exp(-z)) # シグモイド関数

plt.yticks([0, 1]) #y軸の目盛り
plt.scatter(x, y)
plt.plot(x, h, c="orange")
plt.legend((u"data", u"regression line")) # 凡例
plt.xlabel('Number of defective pridcts')
plt.ylabel('Label')
plt.show()
