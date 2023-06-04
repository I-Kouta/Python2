# 決定木のアルゴリズム,予測分析(cart.py)
# ライブラリの読み込み
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split

iris = datasets.load_iris() # データ読み込み
