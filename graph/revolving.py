# リボ払いシミュレーション(python revolving.py)
import numpy as np
import matplotlib.pyplot as plt

def calculate_balance(principal, monthlyInterestRate, monthlyPayment):
    balances = [principal]
    for _ in range(12):
        interest = balances[-1] * monthlyInterestRate
        balance = balances[-1] + interest - monthlyPayment
        balances.append(balance)
    return balances

principal = 100000 # 初期費用10万円
interestRate = 15
monthlyInterestRate = interestRate / 12
monthlyPayment = 20000 # 月の支払い金額

balances = calculate_balance(principal, monthlyInterestRate, monthlyPayment)
months = np.arange(13)

plt.plot(months, balances)
plt.xlabel("months")
plt.ylabel("balances")
plt.grid(True)
plt.show()
