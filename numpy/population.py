# 多項式回帰(python population.py)
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(1, 31, 1) # 年齢の入力データ
# 年齢に対応する正解データ
Y = np.array([85745, 86140, 86557, 86845, 87023, 87034, 87260, 87161, 87042, 86920,
              86758, 86380, 86139, 85706, 85404, 85077, 84422, 83731, 83015, 82300,
              81493, 81735, 81342, 80175, 79010, 77850, 77282, 76562, 75962, 75451])

def stand(x):
    M = x.mean()
    S = x.std()
    x = (x - M) / S
    return x

X = stand(X)
Y = stand(Y)

plt.scatter(X, Y) #散布図
plt.xlabel('Year')
plt.ylabel('Population(15-64)')
plt.show()
