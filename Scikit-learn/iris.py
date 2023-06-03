# python iris.py
# ランダムフォレストの関数を呼び出し
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split

# irisデータの読み込み
iris = datasets.load_iris() # datasetsにさまざまなデータセットが格納されている

# 特徴量とターゲットの取得
data = iris['data']
target = iris['target']

# 学習データと未知データにデータセットを分類
train_data,test_data,train_target,test_target = train_test_split(data,target,test_size=0.5)

# モデル学習
model = RandomForestClassifier(n_estimators=100) # n_estimators:バギングに用いる決定木の数
model.fit(train_data, train_target)

# 正解率を表示
answer = model.score(test_data, test_target)
print(f"精度:{answer}")
