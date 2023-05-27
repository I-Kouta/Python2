# 相関関係のグラフ作成(python correlation.py)
import numpy as np
import matplotlib.pyplot as plt

n = 100
targetCorrelation = 0.8 # 相関係数を指定

x = np.random.uniform(1, 10, n) # x座表のデータ
# yの値を生成
y_mean = targetCorrelation * x # xとの線形関係をもつyの平均値
y_std = np.sqrt(1 - targetCorrelation ** 2) # yの標準偏差
y = np.random.normal(loc=y_mean, scale=y_std)
# targetCovariance = np.array([[1, targetCorrelation], [targetCorrelation, 1]]) # yを生成する相関係数行列
# 共分散行列の固有値分解を行い、変換行列を取得
# eigenvalues, eigenvectors = np.linalg.eig(targetCovariance)
# transformationMatrix = eigenvectors @ np.diag(np.sqrt(eigenvalues))
# 相関が反映されたyを生成
# y = np.random.randn(n, 2) @ transformationMatrix
# y = np.interp(y[:, 1], (y[:, 1].min(), y[:, 1].max()), (1, 10))
# correlation = np.corrcoef(x, y)[0, 1]
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
