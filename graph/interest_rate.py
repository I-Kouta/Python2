# 複利計算(python interest_rate.py)
import numpy as np
import matplotlib.pyplot as plt
# 90年12月末:6.08%

def calculate_deposit(deposit, pastRate, years):
    deposit = [deposit]
    for _ in range(years):
        deposit.append(deposit[-1] * (1 + pastRate))
    return deposit

deposit = 1000000 # 100万
pastRate = 0.0575 # 70年12月末:5.75%
recentlyRate = 0.00003 # 22年3月末:0.003%
years = 10
depositValues = calculate_deposit(deposit, pastRate, years)

yearsRange = np.arange(years + 1)
plt.plot(yearsRange, depositValues)
plt.xlabel("years")
plt.ylabel("deposit amount")
plt.title(f"deposit rate - {pastRate * 100}%")
plt.grid(True)
plt.show()
