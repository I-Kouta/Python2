# 複利計算(python interest_rate.py)
import numpy as np
import matplotlib.pyplot as plt
# 90年12月末:6.08%

def calculate_deposit(deposit, pastRate, years):
    deposit_values = [deposit]
    for _ in range(years):
        deposit_values.append(deposit_values[-1] * (1 + pastRate))
    return deposit_values

deposit = 1000000 # 100万
pastRate = 0.0575 # 70年12月末:5.75%
recentlyRate = 0.00003 # 22年3月末:0.003%
years = 100

yearsRange = np.arange(years + 1)
pastRateValues = calculate_deposit(deposit, pastRate, years) # 過去の利率のグラフ
recentlyValues = calculate_deposit(deposit, recentlyRate, years) # 最近の利率のグラフ

plt.plot(yearsRange, pastRateValues, label=f"interest rate: {pastRate * 100}%")
plt.plot(yearsRange, recentlyValues, label=f"interest rate: {recentlyRate * 100}%")
plt.xlabel("years")
plt.ylabel("deposit amount")
plt.legend()
plt.grid(True)
plt.show()
