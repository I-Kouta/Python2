# 機械学習(python basic05.py)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()
X_iris = iris.data # 特徴量データ
y_iris = iris.target # ラベルデータ
# 訓練データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(
    X_iris,
    y_iris,
    test_size = 0.3,
    random_state = 1,
    stratify = y_iris)
# solver引数には最適化手法、multi_classには多クラス分類の方法を指定
model = LogisticRegression(solver = "lbfgs", multi_class = "auto")
model.fit(X_train, y_train) # モデルを訓練データに適合
y_predicted = model.predict(X_test) # テストデータでラベルを予測
print(accuracy_score(y_test, y_predicted))
