# 偽陽性と陽性者率のグラフ(python falsePositive1.py)
# 陽性者率は0.01~0.4程度で指定する
import numpy as np
import matplotlib.pyplot as plt

# 陽性者率と特異度の範囲指定
n = 100000 # サンプル数
positive_rates_x = np.linspace(0.01, 0.4) # 陽性者率(x軸)
specificities = 0.7 # 特異度

# 偽陽性率算出のための情報
truePositive = n * positive_rates_x * specificities # 真陽性の数
falsePositive = n * (1 - positive_rates_x) * (1 - specificities) # 偽陽性の数
falsePositiveRates = (falsePositive) / (falsePositive + truePositive) # 偽陽性の割合

# グラフ作成
plt.plot(positive_rates_x, falsePositiveRates)
plt.xlabel("positive rate") # 陽性者率
plt.ylabel("false positive rate") # 偽陽性率
plt.title(f"positive rate - false positive rate (specificities:{specificities * 100}%)") # 特異度を変数で表示させる
plt.grid(True)
plt.show()
