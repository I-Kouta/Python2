# 相関関係のグラフ作成(python correlation.py)
import numpy as np
import matplotlib.pyplot as plt

n = 100
targetCorrelation = 0.7 # 相関係数を指定
x = np.random.uniform(1, 10, n) # x座表のデータ

# yの値を生成
y_mean = targetCorrelation * (x - 1) * 10 / 9 # xとの線形関係をもつyの平均値
y_std = np.sqrt(1 - targetCorrelation ** 2) # yの標準偏差
y_scaled = np.random.normal(loc=y_mean, scale=y_std)
y = np.interp(y_scaled, (y_scaled.min(), y_scaled.max()), (0, 100))

# グラフ描写
plt.scatter(x, y, color="b", label="Data")
plt.title(f"Correlation: {targetCorrelation}")
plt.xlim(0, 12)
plt.ylim(0, 100)
plt.xlabel('hours of study per day')
plt.ylabel('result')
plt.legend()
plt.grid(True)
plt.show()
