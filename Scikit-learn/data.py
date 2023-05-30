# 機械学習ライブラリの使い方(python data.py)
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# データのロード
iris = datasets.load_iris()
X = iris.data
y = iris.target

# データの分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# モデルの作成とトレーニング
model = LogisticRegression()
model.fit(X_train, y_train)

# 予測の実行
y_pred = model.predict(X_test)

# 精度の評価
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
