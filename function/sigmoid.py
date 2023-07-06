# シグモイド関数(python sigmoid.py)
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x, a): # シグモイド間数の定義
    return 1 / (1 + np.exp(-a * x))

x = np.linspace(-8, 8, 1000)
a = np.linspace(0.1, 1.0, 10)

fig = plt.figure(figsize = (12, 12))
for i in range(len(a)):
    text = "a = " + str(a[i])
    ax = fig.add_subplot(5, 5, i + 1, title = text)
    ax.plot(x, sigmoid(x, a[i]))

fig.subplots_adjust(wspace=0.5, hspace=0.5)
plt.show()
