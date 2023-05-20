# 相関関係のグラフ作成
import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.random.rand(n) # 座表のデータ
y = x + np.random.rand(n) * 0.5 # y座標のデータ(xとの相関がある)
correlation = np.corrcoef(x, y)[0, 1]
# グラフ描写
plt.scatter(x, y, color="b", label="Data")
plt.title(f"Correlation: {correlation:.2f}")
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
