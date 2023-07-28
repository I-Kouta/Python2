# 229P, 簡単なデータの可視化
import matplotlib.pyplot as plt

# 折れ線グラフ
ls1 = [1, 4, 9, 16]
ls2 = [8, 7, 6, 16]
plt.plot(ls1, label="1st plot")
plt.plot(ls2, label="2nd plot")
plt.legend()

# 棒グラフ
# x = [1, 2, 3, 4]
# y = {"apple":10, "banana":30, "orange":40, "kiwi":15}
# plt.bar(x, y.values(), tick_label=list(y.keys()))

plt.show()
