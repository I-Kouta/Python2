# 試行回数と確率のグラフ(probability.py)
import numpy as np
import matplotlib.pyplot as plt

# 試行条件
num_trials = 100 # 試行回数
# 確率計算

# グラフ作成
plt.plot(range(num_trials), probabilities)
plt.xlabel('number of trials') # 試行回数
plt.ylabel('result') # 結果
plt.ylim(0, 1)
plt.show()
