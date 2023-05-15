import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)  # xの範囲を設定
y1 = x**2 - 6*x - 5  # 二次曲線の式1:(x - 3)**2 - 14
y2 = -x**2 + 3*x - 2  # 二次曲線の式2:-(x - 3/2)**2 + 1/4

plt.plot(x, y1, label='Quadratic Curve 1')
plt.plot(x, y2, label='Quadratic Curve 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Curve')
plt.legend()
plt.grid(True)
plt.show()
