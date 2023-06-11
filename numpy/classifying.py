# ロジスティック回帰・分類アルゴリズム(python classifying.py)
import numpy as np
import matplotlib.pyplot as plt
# x:入力データ
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
# y:対応する正解ラベル(0:正常, 1:異常)
y = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

plt.yticks([0,0.5,1]) #y軸の目盛り
plt.scatter(x[:10] ,y[:10], c='b')
plt.scatter(x[10:] ,y[10:], c='r')
plt.xlabel('Number of defective pridcts')
plt.ylabel('Label')
plt.show()
