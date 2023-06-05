# 偽陽性と特異度のグラフ(python falsePositive2.py)
# 特異度は0.5~0.9程度で指定する
import numpy as np
import matplotlib.pyplot as plt

n = 100000 # サンプル数
positive_rates = 0.01 # 陽性者率
specificities_x = np.linspace(0.55, 0.9) # 特異度(x軸)

truePositive = n * positive_rates * specificities_x # 真陽性の数
falsePositive = n * (1 - positive_rates) * (1 - specificities_x) # 偽陽性の数
falsePositiveRates = (falsePositive) / (falsePositive + truePositive) # 偽陽性の割合

plt.plot(specificities_x, falsePositiveRates)
plt.xlabel("specificities") # 特異度
plt.ylabel("false positive rate") # 偽陽性率
plt.title(f"positive rate - specificities (positive rates:{positive_rates * 100}%)") # 陽性者率を変数で表示させる
plt.grid(True)
plt.show()
