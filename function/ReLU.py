# ランプ関数:勾配消失が起こりにくい(python ReLU.py)
import numpy as np
import matplotlib.pyplot as plt

# DeLU関数の定義
def relu(x):
  return np.maximum(0, x) # 入力が0以下の場合は0を出力する

# Leaky ReLU関数の定義
def leakyrelu(x):
  return np.where(x > 0, x, 0.01 * x) # xが0未満の場合には0.01倍を返す

x = np.linspace(-5, 5, 1000)
y = leakyrelu(x)
y_r = relu(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, label = "leakyrelu")
ax.plot(x, y_r, label = "relu")
plt.legend()
plt.grid()
plt.show()
