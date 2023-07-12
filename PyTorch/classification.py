# 2クラスの色分け(python classification.py)
import torch
import torch.nn as nn
from torch.nn import functional as F
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

samples = 500
X, Y = datasets.make_circles(n_samples = samples, shuffle = False, factor = 0.3, noise = 0.1)
train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.2) # シャッフルして分割
# 形状
print(train_X.shape)
print(test_X.shape)
print(train_Y.shape)
print(test_Y.shape)
