# 偽陽性の割合のグラフ(python falsePositive.py)
import numpy as np
import matplotlib.pyplot as plt

def calculate_false_positive_rate(positive_rate, specificity):
    return 1 - specificity

# 陽性率と特異度の範囲指定
positive_rates = np.linspace(0.01, 0.5, 100) # 陽性率
specificities = np.linspace(0.5, 0.99, 100) # 特異度
# 偽陽性の割合計算
false_positive_rates = calculate_false_positive_rate(positive_rates, 1 - specificities)
# グラフ作成
plt.plot(positive_rates, false_positive_rates)
plt.xlabel("positive rate")
plt.ylabel("false positive rate")
plt.title("False Positive Rate vs Positive Rate")
plt.grid(True)
plt.show()
