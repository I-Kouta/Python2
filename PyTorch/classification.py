# 2クラスの色分け(python classification.py)
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

samples = 500
X, Y = datasets.make_circles(n_samples = samples, shuffle = False, factor = 0.3, noise = 0.1)
# 形状
print(X.shape) # データ
print(Y.shape) # ラベル
