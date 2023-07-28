# 229P, 簡単なデータの可視化
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = {"apple":10, "banana":30, "orange":40, "kiwi":15}

plt.bar(x, y.values(), tick_label=list(y.keys()))
plt.show()
