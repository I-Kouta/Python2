# 229P, 簡単なデータの可視化
import numpy as np
import matplotlib.pyplot as plt

# 折れ線グラフ
# ls1 = [1, 4, 9, 16]
# ls2 = [8, 7, 6, 16]
# plt.plot(ls1, label="1st plot")
# plt.plot(ls2, label="2nd plot")
# plt.legend()

# 散布図, 要素数は全て同じ数
# x = [1, 4, 9, 8]
# y = [8, 7, 6, 9]
# plt.scatter(x, y)

# 棒グラフ
# x = [1, 2, 3, 4]
# y = {"apple":10, "banana":30, "orange":40, "kiwi":15}
# plt.bar(x, y.values(), tick_label=list(y.keys()))

# ヒートマップ
ary1 = np.random.rand(100)
ary2 = ary1.reshape(10, 10)
im = plt.imshow(ary2)
plt.colorbar(im)

plt.show()
