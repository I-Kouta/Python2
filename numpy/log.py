# 対数関数(python log.py)
import numpy as np
from sympy import Symbol, log
from sympy.plotting import plot
import matplotlib.pyplot as plt
# 関数の定義
def log10(x):
    return np.log10(x)
x_values = np.linspace(0.1, 1, 100)
f1 = -log10(x_values)
f2 = -log10(1 - x_values)
# グラフ表示
plt.plot(x_values, f1, label='f1 = -log(X)')
plt.plot(x_values, f2, label='f2 = -log(1 - X)')
plt.legend()
plt.grid()
plt.show()
