import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)  # xの範囲を設定
y = 2*x**2 + 4*x + 3  # 二次曲線の式

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Curve')
plt.grid(True)
plt.show()
