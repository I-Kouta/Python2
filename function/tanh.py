# ハイポバリックタンジェント関数: -1 ~ 1(python tanh.py)
import numpy as np
import matplotlib.pyplot as plt
# tanh関数の定義
def tanh(x):
    y = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return y

x = np.linspace(-8, 8, 1000)
y = tanh(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.legend()
plt.grid()
plt.show()
