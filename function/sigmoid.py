# シグモイド関数(python sigmoid.py)
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x): # シグモイド間数の定義
    return 1 / (1 + np.exp(-x))

x = np.linspace(-8, 8, 1000)
y = sigmoid(x)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
plt.grid()
plt.show()
