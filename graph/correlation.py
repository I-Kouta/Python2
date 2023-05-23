# 相関関係のグラフ作成(python correlation.py)
import numpy as np
import matplotlib.pyplot as plt

n = 100
x = np.random.uniform(1, 10, n) # 座表のデータ
y = np.random.uniform(0, 100, n) # y座標のデータ(xとの相関がある)
correlation = np.corrcoef(x, y)[0, 1]
# グラフ描写
plt.scatter(x, y, color="b", label="Data")
plt.title(f"Correlation: {correlation:.2f}")
plt.xlim(0, 12)
plt.ylim(0, 100)
plt.xlabel('hours of study per day')
plt.ylabel('result')
plt.legend()
plt.grid(True)
plt.show()
