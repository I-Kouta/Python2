# 機械学習ライブラリの使い方(python data.py)
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# データのロード
iris = datasets.load_iris() # Irisデータセットをロード,data, target, target_name, feature_namesを含む
x = iris.data # 特微量(説明変数)を保持するNumPy配列,行が花の特徴,列が特徴の種類
y = iris.target # 目的変数(ラベル)を保持するNumPy配列,要素が品種に対応

# データをトレーニングとテストに分割, xが特徴料, yが目的変数
x_train, x_test, y_train, y_test = train_test_split(
    x, # 元のデータの特微量配列
    y, # 元のデータの目的変数配列
    test_size=0.2, # テストデータの割合の指定
    random_state=42) # データ分割の際のランダムなシード値

# モデルの作成とトレーニング
model = LogisticRegression() # 会期モデルのインスタンス作成
# 作成したモデルをトレーニングデータで学習,特徴料と目的変数を引数として受け取り関係を学習
model.fit(x_train, y_train)

# 予測の実行
# modelを使用してx_testに対する目的変数の予測値を算出,学習した関数を使用して与えられた特微量からラベルを推定
y_pred = model.predict(x_test)

# 一致度の評価,範囲は0~1
accuracy = accuracy_score(y_test, y_pred)
print(x)
print(y)
print("Accuracy:", accuracy)
