import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)  # xの範囲を設定
y1 = x**2 - 1
y2 = -x**2 + 1

plt.plot(x, y1, label='Quadratic Curve 1')
plt.plot(x, y2, label='Quadratic Curve 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Curve')
plt.legend()
plt.grid(True)
plt.show()
