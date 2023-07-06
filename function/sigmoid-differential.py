# シグモイド関数を微分(python sigmoid-differential.py)
import numpy as np
import matplotlib.pyplot as plt
# f'(x) = f(x) * (1 - f(x))
def grad_sigmoid(x): # 微分後のsigmoid関数を定義
    sigmoid = 1 / (1 + np.exp(-x))
    return sigmoid * (1 - sigmoid)
    # return np.exp(-x) / (1 + np.exp(-x)) ** 2

x = np.linspace(-5, 5, 100)
y = grad_sigmoid(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.grid()
plt.show()
