# 期待値算出(python expected.py)
import numpy as np
import matplotlib.pyplot as plt

def calculate_expected_value(rolls):
    return np.mean(rolls)

num_trials = 1000 # 試行回数
numBegin = 1
numEnd = 7 # この値から1引いた値からランダムで値を生成
rolls = np.random.randint(numBegin, numEnd, size=num_trials) # 1から6までの値を生成

expected_values = []
for i in range(1, num_trials + 1):
    expected_value = calculate_expected_value(rolls[:i])
    expected_values.append(expected_value)

expected_value = calculate_expected_value(rolls) # 全体の期待値を計算
# グラフ作成
plt.plot(range(1, num_trials + 1), expected_values)
plt.axhline(y=expected_value, color="r", linestyle="--", label=f"Expected Value: {expected_value}")
plt.xlabel('number of trials')
plt.ylabel('expected value')
plt.ylim(numBegin, numEnd - 1)
plt.legend()
plt.show()
