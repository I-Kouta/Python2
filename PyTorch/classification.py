# 2クラスの色分け(python classification.py)
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

samples = 500
X, Y = datasets.make_circles(n_samples = samples, shuffle = False, factor = 0.3, noise = 0.1)
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2)
# 形状
print(train_X.shape)
print(test_X.shape)
print(train_Y.shape)
print(test_Y.shape)
