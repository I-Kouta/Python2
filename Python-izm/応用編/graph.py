
# 正規分布のグラフ
# python graph.py

import numpy as np
from scipy.stats import norm # normは正規分布
import matplotlib.pyplot as plt

X = np.arange(0, 100, 0.1) # 0から100まで0.1刻み

# pdfは確率密度関数
# 平均60、標準偏差10(ばらつき具合、値が大きいほどばらつきが大きい)
Y = norm.pdf(X, 60, 10)

# グラフの表示
plt.bar(X, Y, width = 0.1)
plt.show()
