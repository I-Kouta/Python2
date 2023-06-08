# 次元削減アルゴリズム,主成分分析(PCA)(python dimension.py)
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_wine

wine = load_wine() # データセットをロード
x = wine.data[:, :3] # 3次元のデータを読み込む
y = wine.target # 分類ラベル
feature_name = wine.feature_names[:3] # 特微量の名前
target_name = wine.target_names # 目的量の名前
