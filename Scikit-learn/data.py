# 機械学習ライブラリの使い方(python data.py)
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# データのロード
iris = datasets.load_iris() # Irisデータセットをロード,data, target, target_name, feature_namesを含む
x = iris.data # 特微量(説明変数)を保持するNumPy配列,行が花の特徴,列が特徴の種類
y = iris.target # 目的変数(ラベル)を保持するNumPy配列,要素が品種に対応

# データをトレーニングとテストに分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# モデルの作成とトレーニング
model = LogisticRegression()
model.fit(x_train, y_train)

# 予測の実行
y_pred = model.predict(x_test)

# 精度の評価
accuracy = accuracy_score(y_test, y_pred)
print(x)
print(y)
print("Accuracy:", accuracy)
