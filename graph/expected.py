# 期待値算出(expected.py)
import numpy as np
import matplotlib.pyplot as plt

def calculate_expected_value(rolls):
    return np.mean(rolls)

num_trials = 1000 # 試行回数
rolls = np.random.randint(1, 7, size=num_trials) # 1から6までの値を生成

expected_values = []
for i in range(1, num_trials + 1):
    expected_value = calculate_expected_value(rolls[:i])
    expected_values.append(expected_value)
# グラフ作成
plt.plot(range(1, num_trials + 1), expected_values)
plt.axhline(y=3.5, color="r", linestyle="--", label="Expected Value: 3.5")
plt.xlabel('number of trials')
plt.ylabel('expected value')
plt.legend()
plt.show()
