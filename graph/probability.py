# 試行回数と確率のグラフ(probability.py)
import numpy as np
import matplotlib.pyplot as plt

# 試行条件
num_trials = 500 # 試行回数
hitPer = 1 # パーセント表記
# 確率計算
x = np.arange(1, num_trials + 1)
y = 1 - (1 - hitPer/100) ** x

# グラフ作成
plt.plot(x, y)
plt.xlabel('number of trials') # 試行回数
plt.ylabel('result') # 結果
plt.ylim(0, 1)
plt.text(100, 0.4, r'$y = 1 - \left(1 - \frac{%d}{100}\right)^x$' % hitPer, fontsize=12, color='blue')
# %d部分が変数に置き換えられる, \frac{%d}{100}が分数部分
plt.show()
