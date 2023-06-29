# ニュートラルネットワーク(python neutral.py)
# パーセプトロン：複数の信号を受け取った時に0, 1どちらかを出力する
import numpy as np
import matplotlib.pyplot as plt

def simple_perceptron(x1, x2):
    w1 = 0.2 # x1の重み
    w2 = 0.8 # x2の重み
    b = -0.7 # 発火しやすさを調整するパラメータ
    y = x1 * w1 + x2 * w2 + b
    if y <= 0:
      return 0
    elif y > 0:
      return 1

# いくつか値をいれて、実際にためしてみましょう↓
print(simple_perceptron(0, 0))
print(simple_perceptron(0, 1))

def sigmoid(x): # シグモイド間数の定義
    return 1 / (1 + np.exp(-x))

# シグモイド関数を描画
x = np.linspace(-6, 6, 1000)
y = sigmoid(x) # 0~1の値を返す

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.show()
