# ランプ関数:勾配消失が起こりにくい(python ReLU.py)
import numpy as np
import matplotlib.pyplot as plt

# DeLU関数の定義
def relu(x):
  return np.maximum(0, x) # 入力が0以下の場合は0を出力する

x = np.linspace(-8, 8, 1000)
y = relu(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.grid()
plt.show()
